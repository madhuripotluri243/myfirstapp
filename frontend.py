import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
load_dotenv()


# Step 1: UI Title

st.set_page_config(page_title="My First Chatbot", layout="centered")
st.title("My First Chatbot")
st.markdown("Ask Any Question and Get Instant Reply")


# Step 2: User Inputs Question

user_question=st.text_input("Ask Your Question")

if st.button("Get Answer") and user_question.strip():
    with st.spinner("Fetching the Most Updated Answer..."):
        text="""You are a Career Coach in AI Field. Anser Best Advice to candidate. Don't give cliche answers
Below is user question: 

{question}
"""
        prompt=PromptTemplate(
    input_variables=["question"],
    template=text
        )

        llm=ChatGroq(model="llama2-70b-chat")
        chain=prompt | llm

        try:
            result=chain.invoke({"question":user_question})
            st.success("Here is Your Answer")
            st.write(result.content)
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")
else:
    st.caption("Powered by DataSense")