from openai import OpenAI

# Replace with your API key



client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

# print(completion.choices[0].message)

# # Function to generate a response from the OpenAI model
# def generate_response(prompt, model="gpt-3.5-turbo", temperature=0.7, max_tokens=100):
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=temperature,
#         max_tokens=max_tokens
#     )

#     # Extract the message content from the API response
#     return response['choices'][0]['message']['content'].strip()

# # Example usage
# user_prompt = "Explain quantum computing in simple terms."
# response = generate_response(user_prompt)

# print("User:", user_prompt)
# print("Assistant:", response)

# # Maintaining conversation history
# conversation_history = [
#     {"role": "system", "content": "You are a helpful assistant."}
# ]
