from enum import Enum

class LLMEnums(Enum):
    OPENAI = "openai"
    GEMINI = "gemini"

class OpenAIEnums(Enum):
    SYSTEM = "developer"
    USER = "user"
    ASSISTANT = "assistant"

class GeminiEnums(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "model"
