from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableMap
from .vectorStore import vector_store
from .llm_service import LLM


prompt_template = """Answer the question based only on the following context:
{context}

Question: {context} 
"""
prompt = ChatPromptTemplate.from_template(template=prompt_template)

retreiver = vector_store.as_retriever()

output_retreiver = StrOutputParser()

llm_instance = LLM(token_limit=3000)
llm = llm_instance.get_llm()


def data_from_rag(query):
    chain = (
        RunnableMap(
            {
                "context": lambda x: retreiver.invoke(x["question"]),
                "question": lambda x: x["question"],
            }
        )
        | prompt
        | llm
        | output_retreiver
    )

    response = chain.invoke({"question": query})
    return response
