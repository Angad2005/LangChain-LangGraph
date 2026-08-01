import os #for os functions

# importing functions specific from library to keep track instead of loading full library
from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Loading environment variables
load_dotenv()

# Initializing llm or brain 
llm = ChatOpenAI(model="nvidia/nemotron-3-ultra-550b-a55b:free", api_key=os.getenv("OPENROUTER_API_KEY"),base_url="https://openrouter.ai/api/v1",temperature=0)
# The required functions are built-in

# Pre-defined prompt template to do a fixed task
prompt= ChatPromptTemplate.from_messages([              #using the function to send message template with user input
    ("system", "You are a professional translator. Translate the following text to {language}"),
    ("user", "{text}")
])

parser=StrOutputParser() #using the function to parse the output

# The langChain chain is created with the llm, prompt and output parser
chain=prompt| llm | parser


result=chain.invoke(
    {
        "language": "French",
        "text": "What is the weather like today?"
    }
)

print(result) #printing the result of the chain