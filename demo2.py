import ollama


mytext=ollama.chat(
    model="smollm2",
    messages=[
    {"role": "user", "content": "what is AI?"}
    ],
  stream=True
)

for chunk in mytext:
    msg = chunk.message

    print(msg.content, end="", flush=True)

print(mytext)



