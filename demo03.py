import ollama
import requests
import json
baseUrl = "http://localhost:11434/api/generate"

# response = ollama.generate(model='smollm2', prompt='What is AI?')
# print(response)


#customize the prompt and model
list_item =[
    "banana",
    'orange',
    'grape',
    "watermelon",
    "peach",
    "strawberry",
    "apple"
]

items_str = ", ".join(list_item)


my_prompty= f"""
You are a helpful assistant.
Arrange the following items alphabetically, separate them with commas, and add bullet points:
list of items:{items_str}
"""
myjsondata ={
    "model": "smollm2",
    "prompt": my_prompty,
}


listOfData =[
    ("model", "smollm2"),
    ("prompt", "What is AI?"),
]


#=====THIS FOR CHAT ENDPOINT
# myjsondata = {
#     "model": "smollm2",
#     "messages": [
#         {"role": "user", "content": my_prompty}
#     ]
# }

#=====GET RESPONSE IN CHAT ENDPOINT
# data = response.json()
# print(data["message"]["content"])


response = requests.post(url=baseUrl,json=myjsondata,stream=True)

print(response)

if response.status_code ==200:

    # iterate data
    for line in response.iter_lines():
        if line:
            #decode data
            decoded_line = line.decode('utf-8')
            #load data from decoded to json
            json_data =json.loads(decoded_line)

            #Get data clearly from json
            all_lines = json_data.get('response')

            #clear line  horizontally 
            print(all_lines,end="",flush=True)
            



# resp = ollama.generate(model='smollm2', prompt='What is AI?')