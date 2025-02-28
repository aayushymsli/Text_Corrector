import streamlit as st
st.set_page_config(layout="wide")

if 'output_text_content' not in st.session_state:
    st.session_state.output_text_content = ""

def generate_content(text):
    return f"{text}"  # Placeholder for content generation

def content_page():
    st.header("Contextual Content Generation",help="This page will help you extend your text")
    col1 , col2 = st.columns(2)
    with col1:
        input_text = st.text_area("Enter a short text to expand", height=200,max_chars=1000)
        if st.button("Generate Extended Content"):
            st.session_state.output_text_content = generate_content(input_text)
    with col2:
        st.text_area("Extended result:", value=st.session_state.output_text_content, height=200)

content_page()