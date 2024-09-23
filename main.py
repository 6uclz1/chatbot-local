from adapters.llm_adapter import OllamaLlmAdapter
from adapters.tts_adapter import Sbv2TtsAdapter
from adapters.stt_Adapter import WhisperSttAdapter
from utils.constants import HALLUCINATION_TEXTS
import sounddevice as sd

class App:
    def __init__(self, llm_adapter, tts_adapter, stt_adapter):
        """依存性をコンストラクタで注入"""
        self.llm_adapter = llm_adapter
        self.tts_adapter = tts_adapter
        self.stt_adapter = stt_adapter

    def run(self):
        """アプリのメインロジック"""
        while True:
            try:
                # 音声録音
                audio_data, sample_rate = self.stt_adapter.record_audio(5)
                if audio_data is None or sample_rate is None:
                    print("録音に失敗しました")
                    continue

                # 音声をテキストに変換
                transcription = self.stt_adapter.transcribe_audio(audio_data, sample_rate)
                print("認識結果:", transcription)

                if transcription in HALLUCINATION_TEXTS:
                    print("ハルシネーションの疑いがあるため、スキップします")
                    continue

                # テキストをLLMに送信して応答を取得
                llm_response = self.llm_adapter.get_response(transcription)

                # 応答を音声に変換して再生
                data, sample_rate = self.tts_adapter.get_voice(llm_response)
                sd.play(data, sample_rate)
                sd.wait()

            except KeyboardInterrupt:
                print("\n終了します。")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    # LLMアダプタのインスタンス(Ollamaを使用(引数にはモデル名を入れること))
    ollama = OllamaLlmAdapter('7shi/tanuki-dpo-v1.0:8b-q6_K')
    # TTSアダプタのインスタンス(SBV2を使用)
    sbv2 = Sbv2TtsAdapter()
    # STTアダプタのインスタンス(Whisperを使用)
    whisper = WhisperSttAdapter()

    app = App(llm_adapter=ollama, tts_adapter=sbv2, stt_adapter=whisper)
    app.run()