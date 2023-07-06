"""Defines the prompter class for the Formatter."""
import os
from typing import List
from pathlib import Path

class FormatterPrompter:
    def __init__(self):
        _current_dir = os.path.dirname(os.path.abspath(__file__))
        _prompt_dir = os.path.join(_current_dir, "prompts")
        _prompt_path = os.path.join(_prompt_dir, "main.txt")
        self.prompt = self._load_prompt(_prompt_path)

    def _load_prompt(self, prompt_path):
        with open(prompt_path, "r") as f:
            prompt = f.read()
        return prompt

    def get_formatter_prompt(self, idea:str="Hello", desired_formats:List=["[To Dos]", "[LinkedIn Post]"], lang:str="繁體中文", text_engine:str="gpt-3.5-turbo"):
        """Get the prompt for the Formatter."""
        prompt = self.prompt
        # Replace the {idea} placeholder with the idea.
        prompt = prompt.replace("{idea}", idea)
        # Replace the {desired_formats} placeholder with the desired formats.
        desired_formats_prompt = ",".join(desired_formats)
        prompt = prompt.replace("{desired_formats}", desired_formats_prompt)
        # Replace the {lang} placeholder with the language.
        prompt = prompt.replace("{lang:}", f"lang:{lang}")

        if "text" in text_engine:
            return {
                "prompt": prompt,
            }
        elif "gpt-3.5" in text_engine:
            return {
                "messages":[
                {"role": "system", "content": prompt}
                ]
            }
        return prompt