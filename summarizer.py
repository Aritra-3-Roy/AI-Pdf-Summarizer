import google.generativeai as genai
from config.config import GEMINI_API_KEY  # Import Gemini API Key

# Configure Gemini API key
genai.configure(api_key=GEMINI_API_KEY)

def summarize_text(text):
    model = genai.GenerativeModel("gemini-pro")  # Use Gemini model
    response = model.generate_content(f"Summarize this text: {text}")
    return response.text
