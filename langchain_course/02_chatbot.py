from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.2,
    max_retries=2,
    timeout=30,
)

from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage(
        content="you are an consultant , suggest me some good masters in ai colleges in india and procedure to get there"
    ),
]

while True:
    userinput = input("you : ")
    if userinput.strip().lower() == "exit":
        break
    messages.append(HumanMessage(content=userinput))
    result = model.invoke(messages)
    print("bot: ", result.text)
    print("[input tokens:", result.usage_metadata["input_tokens"], "]")
    messages.append(result)
