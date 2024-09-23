# ハルシネーションと判断されるテキストのリスト
HALLUCINATION_TEXTS = [
    "ご視聴ありがとうございました", "ご視聴ありがとうございました。",
    "ありがとうございました", "ありがとうございました。",
    "どうもありがとうございました", "どうもありがとうございました。",
    "どうも、ありがとうございました", "どうも、ありがとうございました。",
    "おやすみなさい", "おやすみなさい。",
    "Thanks for watching!",
    "終わり", "おわり",
    "お疲れ様でした", "お疲れ様でした。",
    "おはようございます", "おはようございます。",
]

# Whisperのモデルサイズに関する定数
WHISPER_MODEL_SIZES = {
    "tiny": "tiny",
    "base": "base",
    "small": "small",
    "medium": "medium",
    "large": "large",
}

# TTS関連のデフォルト設定
DEFAULT_TTS_PARAMS = {
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

# TTS APIのURL
TTS_API_URL = "http://127.0.0.1:5000/voice"

# 録音に関する定数
AUDIO_RECORDING_CONFIG = {
    "chunk_size": 1024,
    "sample_format": "pyaudio.paInt16",
    "channels": 1,
    "sample_rate": 16000,  # Whisperが推奨するサンプルレート
}
