from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

chatA = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)
chatB = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)

def print_conversation(messages):
    for message in messages:
        if isinstance(message, HumanMessage):
            print(bcolors.OKCYAN +"chatB: " + bcolors.ENDC + message.content)
        elif isinstance(message, AIMessage):
            print(bcolors.OKGREEN + "ChatA: " + bcolors.ENDC + message.content)
        else:
            print("Unknown message type.")

systemA="You are a happy helpful human"
systemB="You are a curious human who is learning a new language and you use english as your primary language. you're also full of questions remember to ask questions to learn more."

messagesA = [
    SystemMessage(content=systemA),
    HumanMessage(
        content="Translate this sentence from English to French: I love programming."
    ),
    AIMessage(content="J'adore la programmation."),
    HumanMessage(content="What did you just say?"),
]

messagesB = [
    SystemMessage(content=systemB),
    AIMessage(
        content="Translate this sentence from English to French: I love programming."
    ),
    HumanMessage(content="J'adore la programmation."),
    AIMessage(content="What did you just say?"),
]

result = chatA.invoke(messagesA).content

messagesA.append(AIMessage(content=result))
messagesB.append(HumanMessage(content=result))
print_conversation(messagesA)



# Continue the conversation
# Try: Can you translate that phrase into Spanish?

while True:
    input(bcolors.WARNING + "press to continue conversation" + bcolors.ENDC)
    prompt = chatB.invoke(messagesB).content
    messagesA.append(HumanMessage(content=prompt))
    messagesB.append(AIMessage(content=prompt))

    result = chatA.invoke(messagesA).content

    messagesA.append(AIMessage(content=result))
    messagesB.append(HumanMessage(content=result))
    print_conversation(messagesA)
