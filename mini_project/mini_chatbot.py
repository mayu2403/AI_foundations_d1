from ollama import chat
system_msg = "You are a friendly tutor.Answer in one sentence. "
history = [{"role":"system","content":system_msg},]
print("hey,hii! welcome to swetty chatbot😭🤬🤬")
question_counter=0
while True:
    question = input("YOU:")
    if question ==  "":
        print("Laddu🥹2:ask mee something")
        continue
    if question.lower().strip == "/history":
        print("--------- Your conversation so far---------")
        if len(history)<2:
            print("NOthing here so far")
        for msg in history[1:]:
            if msg.role == "user":
                speaker = "You"
            else:
                speaker = "Laddu😎"
            print(f"{speaker}:{msg.content}")
        print("-----------------------------")
        print()
        continue
    if question.lower().strip() == "/clear":
        history = [{"role":"system","content":system_msg}]
        print("Your history is cleared. start a fresh conversation.")
        print()
        continue
    if question.lower().strip()=="/help":
        print("----Available commands---")
        print("/history - displays converstation history")
        print("/clear - clears chat history")
        print("/help - displays this list")
        print("exit - quits the chatbot")
        print("-------------------------")
        print()
        continue
    if question.lower().strip() == "exit":
        print("Anjali:Goodbye user.please come back")
        print(f"you asked{question_counter} question today.Good job!")
        break


    history.append({"role":"user","content":question})
    question_counter+=1
    try:
        response = chat(
                                                                
            model="llama3.2",
            messages=history
        )
        reply = response.message.content
        history.append({"role":"assistant","content":reply})
        print(f"Laddu 🤗:{reply}")3
        print()
        print("-----------------------------------------------------")
    except Exception as e:
        print("Unknown issue. Is Ollama running?")
  
