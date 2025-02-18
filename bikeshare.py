import openai

openai.api_key = 'your_openai_api_key'

def generate_response(prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=100
    )
    return response['choices'][0]['text']

# Example usage
user_input = "Tell me something about AI."
output = generate_response(user_input)
print(output)
