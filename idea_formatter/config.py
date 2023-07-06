"""Define the app's configuration.
"""


text_engine_choices = {
    "text-davinci-003": "text-davinci-003",
    "gpt-3.5-turbo": "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k": "gpt-3.5-turbo-16k",
}  
class AppConfig:
    MAX_TOKENS = 2000
    OVERLAP_SIZE = int(MAX_TOKENS/5)
    TEXT_ENGINE = text_engine_choices["gpt-3.5-turbo-16k"]
    TEXT_ENGINE_TEMPERATURE = 0.5
    LANGUAGE = "zh-tw"
    IS_TEST = True
    def set_text_engine(self, text_engine):
        self.TEXT_ENGINE = text_engine_choices[text_engine]