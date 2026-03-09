from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature=0
)


prompt = PromptTemplate.from_template(
    """
You are a Databricks SQL expert.

Convert the following question into SQL query.

Tables:
already existed in database

Question:
{question}

SQL Query:
"""
)


def generate_sql(question):

    chain = prompt | llm
    response = chain.invoke({"question": question})

    return response.content