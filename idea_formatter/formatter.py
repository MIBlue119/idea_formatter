"""Define formatter class."""
from typing import List
from idea_formatter.utils import get_model_selection, generate_openai_completion, parse_text_response, count_tokens

class Formatter:
    def __init__(self, config, prompter_class,streamlit_progress_bar=None, streamlit_progress_message=None):
        """Initializes the translator class."""
        self.config = config
        self.text_engine = self.config.TEXT_ENGINE
        self.prompter = prompter_class()
        self.streamlit_progress_bar = streamlit_progress_bar
        self.streamlit_progress_message = streamlit_progress_message

    def format(self, idea:str="Hello", desired_formats:List=["[To Dos]", "[LinkedIn Post]"], lang:str="繁體中文"):
        """Translate a line of text."""
        formatter_prompt = self.prompter.get_formatter_prompt(idea=idea, desired_formats=desired_formats, lang=lang, text_engine=self.text_engine)
        api_settings ={
                **get_model_selection(self.text_engine),
                **formatter_prompt,
                "n": 1, 
                "max_tokens" :self.config.MAX_TOKENS,             
                "temperature": self.config.TEXT_ENGINE_TEMPERATURE,
                "presence_penalty" : 2,
                #\n\n###

        }
        response = generate_openai_completion(text_engine=self.text_engine, api_settings=api_settings)
        formatted_text =  parse_text_response(response, text_engine=self.text_engine)                
        return formatted_text