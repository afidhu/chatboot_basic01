import ollama

baseUrl = "http://localhost:11434/api/generate"

# response = ollama.generate(model='smollm2', prompt='What is AI?')
# print(response)

resp = ollama.generate(model='smollm2', prompt='What is AI?')