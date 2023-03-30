
import openai

openai.api_key = "paste your api key"


messages = []

input_msg= input("What type of chatbot would you like to create?\n")
messages.append({"role":"system","content":input_msg})

print("tan ta dan Your new assistant is ready!")

while input != "quit()":
    message = input()
    messages.append({"role": "system", "content": message})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "system", "content": reply})
    print("\n"+reply+"\n")
