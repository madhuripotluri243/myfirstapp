from dotenv import load_dotenv
import os
load_dotenv()

print(os.environ["GROQ_API_KEY"])

#1. Take user question

user_question=input("Enter Your Question: ")

#2. Convert to Prompt

from langchain.prompts import PromptTemplate

text="""You are a Career Coach in AI Field. Anser Best Advice to candidate. Don't give cliche answers
Below is user question: 

{question}
"""

prompt=PromptTemplate(
    input_variables=["question"],
    template=text
)

#3. Make LLM call
from langchain_groq import ChatGroq

llm=ChatGroq(model="deepseek-r1-distill-llama-70b")

# Create Chain

chain=prompt | llm


#4. Response

result=chain.invoke({"question":user_question})
print(result.content)