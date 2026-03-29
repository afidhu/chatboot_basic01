import ollama
from ollama import chat

# user_msg={
#     "mess"
# }


list_item =[
    "banana",
    'orange',
    'grape',
    "watermelon",
    "peach",
    "strawberry",
    "apple",
    'mango',
]

# items_str = ", ".join(list_item)
sorted_items = sorted(list_item)

my_smg= f"""
You are a helpful assistant. And use the politely language to answer the question like human
You must follow these rules strictly:
1. Do NOT add or remove items
2. Do NOT change spelling
3. Sort items alphabetically (A-Z)
4. Output ONLY bullet points
list of items:{sorted_items}
"""


def main():
    response = chat(model='smollm2',messages=[
    {"role": "user", "content": f"{my_smg}"},
    ],
    stream=True
    )
    # print(response['message']['content'])

    if response:
        for line in response:
            print(line.message.content, end="", flush=True)


main()