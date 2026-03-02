print("Starting hello_ai...")

from dotenv import load_dotenv
from openai import OpenAI
import os
import traceback

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("API key loaded?", "YES" if api_key else "NO")

try:
    client = OpenAI(api_key=api_key)

    print("Calling OpenAI...")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Explain Retrieval Augmented Generation (RAG) in simple terms."}
        ],
    )

    print("Received response:")
    print(response.choices[0].message.content)

except Exception as e:
    print("ERROR occurred:")
    print(str(e))
    print("\nFull traceback:")
    traceback.print_exc()