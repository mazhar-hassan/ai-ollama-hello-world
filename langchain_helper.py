from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2:1b")
template = """
You are an expert in answering questions about restaurants in Lahore

Here are some relevant review: {reviews}

Here is the question to answer: {question}
"""

def query_llm(question):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    reviews = retriever.invoke(question)
    response = chain.invoke({"reviews":reviews, "question": question})

    return response

