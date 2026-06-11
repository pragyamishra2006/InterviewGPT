import ollama

response = ollama.chat(
    model="qwen2.5:1.5b",
    messages=[
        {
            "role": "user",
            "content": "What is cyber security?"
        }
    ]
)

print(response["message"]["content"])