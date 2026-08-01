# LangChain-LangGraph
This repo is practice repo for Langchain & LangGraph to further develop and understand AI agents.

# Install Dependencies
Install python packages `Langchain`.\
(Optional) add `LangGraph` incase you need more fucntions from library.\
We are using `-openroutuer`for free LLM access
```bash
pip install langchain Deepagents langchain-openrouter
```
Also export your API key to connect to LLM can also be done via `.env`
```bash
OPENROUTER_API_KEY="YOUR_API_KEY"
```

# Terminologies
`Chat Models` The actual LLM\
`Prompt Templates` To be injected into prompt for structured output for tools etc.
`Output Parser` Outputs given in a specific format to be used by LLM or tool or agent.
`Retrievers` Perform RAG and fetch relevent context
`Tool` Functions an LLm can execute

# Methods of Running
`.invoke()` runs it once
`.batch()` Run it on multiple inputs at once
`.stream()` get token by token output (for UI)

# Files & Notes
`FirstChain` is the first simple chain I implemented to learn syntax of langchain