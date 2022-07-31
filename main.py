from transformers import pipeline
import streamlit as st
import numpy as np

@st.cache(allow_output_mutation=True)
def load_model():
    '''Loads and returns huggingface BART model.'''
    try:
        model = pipeline("summarization", model="./bart") # load locally
    except:
        model = pipeline("summarization", model="facebook/bart-large-cnn") # if model not found locally, download from huggingface hub
    return model


def summarize_text(text: str, model):
    summary_text = model(text)
    return summary_text[0]["summary_text"]

model = load_model()

# Streamlit code begins here
st.title("Text Summarizer")
st.image("./images/ArtificialFictionBrain.png")
st.write("Image source: https://commons.wikimedia.org/wiki/File:ArtificialFictionBrain.png")
st.subheader("Project by Leo Corelli & Rob Baldoni")
text = st.text_area("Please allow ~30 seconds to run :)", placeholder="Paste text here")

if text:
    try:
        results = summarize_text(text, model)
        input_length = len(text) # get length of original input string
        results_length = len(results) # get length of summary
        percent_change = np.round(((input_length-results_length)/input_length) * 100,2) # get percent reduction in size

        # Display results
        st.subheader("Text Summary:")
        st.write(results)

        st.subheader("Performance Statistics:")
        st.write(f"- Input text length: {input_length} characters")
        st.write(f"- Summary length: {results_length} characters")
        st.write(f"- **Reduction in size: {percent_change}%**")
    except:
        results = '<p style="font-family:serif; color:Red; font-size: 42px;">Input text too long! Please shorten :) Unfortunately, to keep costs down, we have to use a relatively lightweight summarization model that has a limited maximum input length.</p>'
        st.markdown(results, unsafe_allow_html=True)