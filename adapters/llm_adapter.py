from interfaces.llm_interface import LlmInterface
import ollama

class OllamaLlmAdapter(LlmInterface):
    """LLMを扱う具体的な実装"""

    def __init__(self, model_name):
        self.messages = []
        self.model_name = model_name

    def get_response(self, text: str) -> str:
        """LLMにテキストを送信し、応答を取得"""
        self.messages.append({'role': 'user', 'content': text})
        try:
            response = ollama.chat(model=self.model_name, messages=[{'role': 'user', 'content': text}])
            bot_response = response.get('message', {}).get('content', "")
            if bot_response:
                self.messages.append({'role': 'assistant', 'content': bot_response})
                print('ボットの回答:' + bot_response)
                return bot_response
            else:
                raise ValueError("Invalid response format")
        except Exception as e:
            print(f"Error getting response from LLM: {e}")
            return ""