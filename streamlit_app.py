import openai
from loguru import logger
import streamlit as st

from idea_formatter.utils import DESIRED_FORMATS, LANGUAGES
from idea_formatter.prompter import FormatterPrompter
from idea_formatter.config import AppConfig
from idea_formatter.formatter import Formatter
from idea_formatter.utils import LANGUAGES, TO_LANGUAGE_CODE
from idea_formatter.config import text_engine_choices

# Initialize the config class
config = AppConfig()

def main():
    st.title('Ideas Formatter')
    st.write("Polish or extend your ideas to desired formats.")
    
    col1,col2 = st.columns(2)
    openai_key=col1.text_input("OpenAI API Key",type="password")
    text_engine_options = ["gpt-3.5-turbo-16k", "gpt-3.5-turbo","text-davinci-003"]
    default_text_engine_option = "gpt-3.5-turbo-16k"
    text_engine_select=col2.selectbox("Text Engine",options=text_engine_options, index=text_engine_options.index(default_text_engine_option), help='Select the Open AI text engine for the formatted text.')

    col3,col4 = st.columns(2)
    default_lang_option = "traditional chinese"
    languages_options = sorted(LANGUAGES.values())
    lang_select = col3.selectbox("Language",options=languages_options,index=languages_options.index(default_lang_option), help='Select the target language for the formatted text.')
    
    options = col4.multiselect(
    'What formats do you want to generate?',DESIRED_FORMATS, max_selections=5)
    st.write('You selected:', options)
    idea = st.text_area('What is your idea?')
    make_button=st.button("Make Idea Formatted")

    if make_button:
        streamlit_progress_bar = st.progress(0)
        streamlit_progress_message = st.markdown(" ")
        summarizing=st.markdown("Formatting...")
        message = st.markdown(" ")

        text_engine = text_engine_choices.get(text_engine_select, "gpt-3.5-turbo-16k") 
        config.set_text_engine(text_engine)
        config.LANGUAGE = lang_select
        # Initialize the Summarizer class
        openai.api_key = openai_key
        formatter = Formatter(config,FormatterPrompter, streamlit_progress_bar=streamlit_progress_bar, streamlit_progress_message=streamlit_progress_message)
        
        # We generate the formatted text by the desired format one by one
        for i, option in enumerate(options):
            message.write(f"Generating {option}...")
            desired_format = [option]
            logger.info(f"Generating {option}...")
            formatted_result = formatter.format(idea=idea, desired_formats=desired_format, lang=lang_select)
            logger.info(f"Formatted {option} successfully.")
            logger.info(formatted_result)
            # Render a new markdown block for each formatted text
            st.title(f"{option}")
            st.code(formatted_result, language="text")
            st.divider()


if __name__ == "__main__":
    main()