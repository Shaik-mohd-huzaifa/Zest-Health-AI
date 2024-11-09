from langchain_core.prompts import ChatPromptTemplate
from .llm_service import LLM
from langchain.schema.output_parser import StrOutputParser

template = """
    You are a HealthCare Assisstant of Zest Health AI. Who help people answer their health related questions & doubts. Do not answer to any other topic.

    Question : {Question}
"""

prompt = ChatPromptTemplate.from_template(template=template)

Output_Retriever = StrOutputParser()


def plain_llm(question):
    llm_instance = LLM(token_limit=2000)
    llm = llm_instance.get_llm()
    chain = prompt | llm | Output_Retriever

    return chain.invoke({"Question": question})
