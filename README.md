# Implementation of Question Answers model through `RAG`

This project uses OpenAI's embedding vector for storing data through API call. It required `OPENAI_API_KEY` to be set in
environment variable. It uses `RAG` with the combination of `LangChain` for retrival of embedding vector from vector
database.

> Folder structure

__notebooks__:
- It consists of jupyter notebook 
- Different test been tried w.r.t to Generative AI models (like flan, qa, bert etc)

__resources__:
- It consists of extra resources (like templates; sample questions)
- It also consists of `chromaDB` on-disk files

__configs__:
- configuration files

__main.py__:
- It's a `main` function call



> Technology Stack

- `fastAPI` been used as a microservice
- `Langchain` for building pipeline across sections of generative AI model
- `ChromaDB` for vector database storage
- `OpenAI` for API call
- `RAG` for retrieval
- `FLAN-T5` for fine-tuning model
- `BERT` for fine-tuning model (roberta flavours)