import google.generativeai as genai
from dotenv import load_dotenv
import os


def generate_text_g(prompt):
    load_dotenv()

    genai.configure(api_key=os.getenv('gemini_access_token'))

    model = genai.GenerativeModel("gemini-1.5-flash")
    try:
        response = model.generate_content(f"сгенерируй короткую забавную цитату от лица кота в стиле {prompt}, без эмодзи")
        return response.text
    except:
        return "Нужно включить vpn"



if __name__ == "__main__":
    print(generate_text_g('ковбой'))