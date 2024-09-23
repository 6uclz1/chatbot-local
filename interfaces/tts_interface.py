from abc import ABC, abstractmethod

class TtsInterface(ABC):
    """Text-to-Speech (TTS)のインターフェースを定義"""

    @abstractmethod
    def get_voice(self, text: str) -> tuple:
        """テキストを音声に変換し、音声データとサンプルレートを返す"""
        pass