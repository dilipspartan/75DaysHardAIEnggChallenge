# Open AI API
import openai
import os

# Set your API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI engineering assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return None

# Use the function
answer = get_ai_response("Explain what an API is in simple terms")
print(answer)