from google import genai
from google.genai import errors
from dotenv import load_dotenv
import os
from gtts import gTTS
import io
import streamlit as st


#load environment variable (for local dev)
load_dotenv()

# Try Streamlit secrets first (for deployment), fallback to .env (for local)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = os.getenv("GEMINI_API_KEY")

#api client

client = genai.Client(api_key=api_key)

#note generatior
def hints_generator(images):
    prompt="Look at the piture with code error. Debug the code. Dont give the corrected code ever. Just give proper hints with no answer directly. Some hints with examples. Keep markdowns and Code previewr."
    try:
        response=client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=[images,prompt]
        )
        return response.text

    except errors.ClientError as e:
        if e.code == 429:
            return "⚠️ **Daily limit reached.** You've hit today's Gemini API quota. Please try again later."
        return f"⚠️ **Request error ({e.code}):** {e.message}"

    except errors.ServerError as e:
        if e.code == 503:
            return "⚠️ **Server overloaded.** Gemini is busy right now. Please try again in a moment."
        return f"⚠️ **Server error ({e.code}):** {e.message}"

    except Exception as e:
        return f"⚠️ **Unexpected error:** {str(e)}"


def solution_generator(images):
    prompt="Look at the piture with code error. Debug the code. Give the corrected code fully.Dont Just give proper hints with no answer. Give the full Corrected code. Some hints with examples too. Keep markdowns and Code previewr."
    try:
        response=client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=[images,prompt]
        )
        return response.text

    except errors.ClientError as e:
        if e.code == 429:
            return "⚠️ **Daily limit reached.** You've hit today's Gemini API quota. Please try again later."
        return f"⚠️ **Request error ({e.code}):** {e.message}"

    except errors.ServerError as e:
        if e.code == 503:
            return "⚠️ **Server overloaded.** Gemini is busy right now. Please try again in a moment."
        return f"⚠️ **Server error ({e.code}):** {e.message}"

    except Exception as e:
        return f"⚠️ **Unexpected error:** {str(e)}"