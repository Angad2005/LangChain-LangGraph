import os #for os functions

# importing functions specific from library to keep track instead of loading full library
from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI
from langchain_core import ChatPromptTemplate
from langchain_core import StrOutputparser

# Loading environment variables
load_dotenv()

# Initializing llm or brain 
llm = ChatOpenAI(model="", api_key=os.getenv("OPENROUTER_API_KEY"),base_url="https://openrouter.ai/api/v1",temperature=0)
# The required functions are built-in

# Pre-defined prompt template to do a fixed task
prompt= ChatPromptTemplate.from_messages([              #using the function to send message template with user input
    ("system", "You are a professional translator. Translate the following text to {language}"),
    ("user", "{text}")
])
