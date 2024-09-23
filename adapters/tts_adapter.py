from interfaces.tts_interface import TtsInterface
import requests
import io
import soundfile

class Sbv2TtsAdapter(TtsInterface):
    """Sbv2エンジンを使用したText-to-Speechの実装"""

    URL = "http://127.0.0.1:5000/voice"

    def _create_audio_query(self, text: str) -> dict:
        """音声生成リクエストのパラメータを作成"""
        params = {
            "text": text,
            "speaker_id": 0,
            "model_id": 0,
            "length": 1,
            "sdp_ratio": 0.2,
            "noise": 0.6,
            "noisew": 0.8,
            "auto_split": True,
            "split_interval": 1,
            "language": "JP",
            "style": "Neutral",
            "style_weight": 5,
        }
        return params

    def _create_request_audio(self, query_data: dict) -> bytes:
        """音声生成APIにリクエストを送信し、音声データを取得"""
        headers = {"accept": "audio/wav"}
        response = requests.post(self.URL, params=query_data, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        return response.content

    def get_voice(self, text: str) -> tuple:
        """テキストを音声に変換し、音声データとサンプルレートを返す"""
        query_data = self._create_audio_query(text)
        audio_bytes = self._create_request_audio(query_data)
        audio_stream = io.BytesIO(audio_bytes)
        data, sample_rate = soundfile.read(audio_stream)
        return data, sample_rate
