import langchain_helper
import streamlit as st

st.title("Restaurant Reviews System")
question = st.chat_input("Enter your question")

if question:
    response = langchain_helper.query_llm(question)
    st.write(response)
