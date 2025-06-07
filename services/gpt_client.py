from openai import AzureOpenAI
from config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_BASE,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT_NAME
)
from loguru import logger
import os

class GPTClient:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
            azure_endpoint=AZURE_OPENAI_API_BASE
        )
        self.deployment_name = AZURE_OPENAI_DEPLOYMENT_NAME
        
    def generate_response(self, message, context=None):
        try:
            messages = [
                {"role": "system", "content": "You are Dino, a helpful support assistant. "
                 "You provide concise, friendly answers to user questions based on the context provided. "
                 "If you don't know the answer, say you'll escalate to the team."},
            ]
            
            if context:
                messages.append({"role": "system", "content": f"Context: {context}"})
                
            messages.append({"role": "user", "content": message})
            
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            answer = response.choices[0].message.content
            logger.success("Generated response from GPT")
            return answer
            
        except Exception as e:
            logger.error(f"GPT API error: {e}")
            return None