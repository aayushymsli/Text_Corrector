import streamlit as st
st.set_page_config(layout="wide")

if 'output_text_paraphrase' not in st.session_state:
    st.session_state.output_text_paraphrase = ""

def paraphrase_text(text,tone):
    return f"{tone} : {text}"

def paraphrase_page():
    st.header("Paraphrasing Tool",help="This page will help you to rephrase your content.")
    # Create two columns for organizing the UI components side by side
    col1, col2 = st.columns(2)

    with col1:
        tone = st.selectbox("Select Tone", ['Formal', 'Casual', 'Humanize'])
        input_text = st.text_area("Enter Text Here", height=200,max_chars=4000)
        if st.button("Paraphrase"):
            st.session_state.output_text_paraphrase = paraphrase_text(input_text,tone)

    with col2:
        st.text_area("Paraphrased result:", value=st.session_state.output_text_paraphrase, height=285)

paraphrase_page()