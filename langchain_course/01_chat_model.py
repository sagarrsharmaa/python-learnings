from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.2,
    max_retries=2,
    timeout=30,
)
result = model.invoke("what is the capital of india , answer in one word")

print(type(result))
print(result.text)
print(result.usage_metadata)


from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

messages = [
    SystemMessage(content="You are a pirate. Keep answers under 15 words."),
    HumanMessage(content="My name is Sagar."),
    AIMessage(content="Arr, welcome aboard, Sagar!"),
    HumanMessage(content="What's my name?"),
]

reply = model.invoke(messages)
print(reply.text)
