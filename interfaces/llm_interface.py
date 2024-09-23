from abc import ABC, abstractmethod

class LlmInterface(ABC):
    """LLMのインターフェースを定義"""

    @abstractmethod
    def get_response(self, text: str) -> str:
        """テキストに応じたLLMの応答を取得する"""
        pass