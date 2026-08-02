import os
from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

from pydantic import BaseModel, Field

#Defining a structured output model for the joke
class Joke(BaseModel):
    setup : str = Field(..., description="The joke setup")
    punchline : str = Field(..., description="The joke punchline")

llm= ChatOpenAI(model="nvidia/nemotron-3-ultra-550b-a55b:free", api_key=os.getenv("OPENROUTER_API_KEY"),base_url="https://openrouter.ai/api/v1",temperature=1)

structured_llm = llm.with_structured_output(Joke)

prompt= ChatPromptTemplate.from_template(
    "Tell me a funny joke about {topic}. "
    "Easy joke other than dark mode one"
)

chain = prompt | structured_llm

joke= chain.invoke(
    {
        "topic": "programming"    
        }
)

print(f"Setup: {joke.setup}")
print(f"Punchline: {joke.punchline}")