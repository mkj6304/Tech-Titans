import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ ERROR: OPENAI_API_KEY is missing. Please check your .env file.")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

def generate_answer(question):
    """
    Generate an answer using OpenAI API.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    
    except openai.OpenAIError as e:
        return f"❌ OpenAI API Error: {str(e)}"

# Example test
if __name__ == "__main__":
    print(generate_answer("What is AI?"))
