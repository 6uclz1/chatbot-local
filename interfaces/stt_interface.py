from abc import ABC, abstractmethod

class SttInterface(ABC):
    """Speech-to-Text (STT) のインターフェースを定義"""

    @abstractmethod
    def record_audio(self, duration: int) -> tuple:
        """
        音声データを取得するメソッド。
        
        Parameters:
        duration (int): 録音する時間（秒）
        
        Returns:
        tuple: 録音された音声データとサンプルレート
        """
        pass

    @abstractmethod
    def transcribe_audio(self, audio_data, sample_rate: int) -> str:
        """
        音声データをテキストに変換するメソッド。
        
        Parameters:
        audio_data: 録音された音声データ
        sample_rate (int): サンプルレート（Whisperでは16kHz）
        
        Returns:
        str: 認識されたテキスト
        """
        pass