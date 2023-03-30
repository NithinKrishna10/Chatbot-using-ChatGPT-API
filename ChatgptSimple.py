import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "what is data sturctures "}])
print(completion.choices[0].message.content)