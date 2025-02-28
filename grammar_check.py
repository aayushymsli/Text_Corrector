import streamlit as st
st.set_page_config(layout="wide")

if 'output_text_grammar' not in st.session_state:
    st.session_state.output_text_grammar = ""

def grammar_check(text):
    return f"{text}"  # Placeholder for grammar check

def grammar_page():
    st.header("Grammar Checker",help="This page will help you to correct your grammatical mistakes")
    col1 , col2 = st.columns(2)
    with col1:
        input_text = st.text_area("Enter the text to check grammar", height=200,max_chars=4000)
        if st.button("Check Grammar"):
            st.session_state.output_text_grammar = grammar_check(input_text)
    with col2:
        st.text_area("Processed result:", value=st.session_state.output_text_grammar, height=200)

grammar_page()