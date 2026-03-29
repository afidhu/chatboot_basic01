from ollama import chat

list_item =[
    "banana",
    'orange',
    'grape',
    "watermelon",
    "peach",
    "strawberry",
    "apple"
]
sorted_items = sorted(list_item)
item = ", ".join(sorted_items)


def main(text,question):


    my_text = {
        "role": "user",
        "content": f"""
    You are a helpful assistant.

    Follow these rules strictly:
    - Answer the user's question
    - Use ONLY the provided list of items
    - Do NOT add or remove items
    - Do NOT repeat items
    - If sorting is requested, sort them alphabetically (A-Z)
    - Do NOT repeat items
    - Can  include emojis
    -Include closing statements or extra comments

    Answer in a polite and natural way.

    Question:
    {question}

    List of items:
    {text}
    """
    }
    
    response = chat(
        model="smollm2",
        messages=[
            my_text,
        ],
        stream=True,
    )

    if response:
        print(f"User:\n{question}\n")
        print(f"Bot:")
        for line in response:

            print(line.message.content, end="", flush=True)
        
user_qn =input("Please enter your question: ")
main(item,user_qn)