from ollama import chat
code="give me a single one-linetagline for my coffee shop answer in 1 line.only the tagline/"
for t in[0,0,7,1,5]:
    print(f"temp: (t) ")
    for run in range(3):
        response=chat(
            model="llama3.2",
            messages=[
                {
                    "role":"user",
                    "content":promt
                }
            ],
        options ={"temperature":t}
     
        )
    print(f"run{run+1}:{response.message.content}")
print()