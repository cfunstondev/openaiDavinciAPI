# Project Name: OpenAI Text-Completion Through Terminal
# File Name: apiRequest.py
# Author: Codey Funston
# Created: 28-04-2023
# Updated: 29-04-2023
# Description: Class for creating objects that can send an API request to an OpenAI model and store the returned data.

# External libraries
import os
import openai

#  Secret API key (saved as an environment variable locally)
openai.api_key = os.getenv("OPENAI_API_KEY")

class APIRequest:
    # Initializes an apiRequest object with openAI request parameters as arguments, and declares the response member variable
    def __init__(self, model: str, prompt: str, token_limit: int, temperature: float, responses_limit: int) -> None:
        self.model = model
        self.prompt = prompt
        self.token_limit = token_limit 
        self.temperature = temperature
        self.response_limit = responses_limit 

        self.response = None
        self.total_tokens = None

    def make_request(self) -> str:
        """
        Creates a completion from selected model.

        Returns: Text part of completion: str
        """

        if (openai.api_key is None):
            raise openai.error.AuthenticationError("Missing API key.")

        self.response = openai.Completion.create(
            model = self.model,
            prompt = self.prompt,
            max_tokens = self.token_limit,
            temperature = self.temperature,
            n = self.response_limit
        )

        response_text = self.response["choices"][0]["text"].replace("\n", "")
        self.total_tokens = self.response["usage"]["total_tokens"]

        return response_text
