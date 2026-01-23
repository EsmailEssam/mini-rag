from ..LLMInterface import LLMInterface
from ..LLMEnums import GeminiEnums
from google import genai
from google.genai import types
import logging

class GeminiProvider(LLMInterface):
    def __init__(self, api_key: str,
                 default_input_max_characters: int=1000,
                 default_output_max_characters: int=1000,
                 default_generation_temperature: float=0.1):
        
        self.api_key = api_key

        self.default_input_max_characters = default_input_max_characters
        self.default_output_max_characters = default_output_max_characters
        self.default_generation_temperature = default_generation_temperature

        self.generation_model_id = None
        self.embedding_model_id = None
        self.embedding_size = None

        self.client = genai.Client(api_key=self.api_key)

        self.enums = GeminiEnums

        self.logger = logging.getLogger(__name__)

    def set_generation_model(self, model_id: str):
        self.generation_model_id = model_id
    
    def set_embedding_model(self, model_id: str, embedding_size: int):
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size
    
    def process_text(self, text: str):
        return text[:self.default_input_max_characters].strip()
    
    def generate_text(self, prompt: str, chat_history: list, system_prompt: str, max_output_tokens: int=None, temperature: float = None):
        if not self.client:
            self.logger.error("Gemini Client not initialized")
            return None
        
        if not self.generation_model_id:
            self.logger.error("Generation model for Gemini not set")
            return None
        
        max_output_tokens = max_output_tokens if max_output_tokens else self.default_output_max_characters
        temperature = temperature if temperature else self.default_generation_temperature

        chat = self.client.chats.create(
            model=self.generation_model_id,
            history=chat_history,
            config={
                "system_instruction": system_prompt,
                'maxOutputTokens': max_output_tokens,
                'temperature': temperature
            }
        )

        response = chat.send_message(message=self.process_text(prompt))

        if not response or not response.text:
            self.logger.error("Error while generating text with Gemini")
            return None
        
        return response.text
    
    def embed_text(self, text: str, document_type: str = None):
        if not self.client:
            self.logger.error("Gemini Client not initialized")
            return None
        
        if not self.embedding_model_id:
            self.logger.error("Embedding model not set")
            return None
        
        response = self.client.models.embed_content(
            model=self.embedding_model_id,
            contents=text,
            config=types.EmbedContentConfig(output_dimensionality=self.embedding_size)
        )

        if not response or not response.embeddings or len(response.embeddings) == 0 or not response.embeddings[0].values:
            self.logger.error("Error while embedding text with Gemini")
            return None
        
        return response.embeddings[0].values
    
    def construct_prompt(self, prompt: str, role:str):
        return types.Content(role=role, parts=[types.Part(text=prompt)])