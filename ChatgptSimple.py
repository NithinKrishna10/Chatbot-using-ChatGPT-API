import openai

openai.api_key = "paste your api key"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "what is data sturctures "}])
print(completion.choices[0].message.content)
