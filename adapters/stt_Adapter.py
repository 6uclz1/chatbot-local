from interfaces.stt_interface import SttInterface
import whisper
import numpy as np
import pyaudio
import torch

class WhisperSttAdapter(SttInterface):
    """Whisperを使用したSpeech-to-Text (STT) アダプタ"""

    def __init__(self, model_size="base"):
        """
        Whisperモデルをロードする。
        
        Parameters:
        model_size (str): 使用するモデルサイズ。'tiny', 'base', 'small', 'medium', 'large' から選択。
        """
        self.model = whisper.load_model("base", device="cuda" if torch.cuda.is_available() else "cpu")

    def record_audio(self, duration=5):
        """
        マイクから指定時間の音声を録音し、音声データを返します。

        Args:
            duration (int, optional): 喋っていない空白の秒数。デフォルトは5秒。

        Returns:
            tuple: 録音した音声データ（numpy配列）とサンプルレート。
        """
        chunk = 1024  # フレームサイズ
        sample_format = pyaudio.paInt16  # 音声フォーマット
        channels = 1  # モノラル
        fs = 16000  # サンプリング周波数

        p = pyaudio.PyAudio()
        try:
            print("録音を開始します...")

            stream = p.open(format=sample_format, channels=channels, rate=fs, input=True, frames_per_buffer=chunk)
            frames = [stream.read(chunk) for _ in range(0, int(fs / chunk * duration))]

            stream.stop_stream()
            stream.close()
            
            print("録音を終了します...")
        except Exception as e:
            print(f"Error recording audio: {e}")
            return None, None
        finally:
            p.terminate()

        audio_data = np.frombuffer(b''.join(frames), dtype=np.int16).astype(np.float32) / np.iinfo(np.int16).max
        return audio_data, fs

    def transcribe_audio(self, audio_data, fs):
        """
        録音した音声データをWhisperモデルで文字起こしします。

        Args:
            audio_data (np.ndarray): 録音した音声データ。
            fs (int): サンプリング周波数。16000Hzのみ対応。

        Returns:
            str: 文字起こし結果のテキスト。
        """
        if fs != 16000:
            raise ValueError("サンプリングレートは16000Hzである必要があります。")

        try:
            print("文字起こしを開始します...")

            audio = whisper.pad_or_trim(audio_data)
            mel = whisper.log_mel_spectrogram(audio).to(self.model.device)

            options = whisper.DecodingOptions(language="ja")
            result = self.model.decode(mel, options)
            
            print("文字起こしを終了します...")
            
            return result.text
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return ""