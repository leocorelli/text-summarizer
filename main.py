from transformers import pipeline
import streamlit as st

def load_model():
    '''Loads and returns Facebook BART model trained on CNN Daily Mail for text summarization.'''
    try:
        model = pipeline("summarization", model="./bart")
    except:
        model = pipeline(model="facebook/bart-large-cnn")
    return model


def summarize_text(text: str, model):
    summary_text = model(text)
    return summary_text[0]["summary_text"]

model = load_model()

# Streamlit code begins here
st.title("Text Summarizer")
st.image("./images/ArtificialFictionBrain.png")
st.write("Image source: https://commons.wikimedia.org/wiki/File:ArtificialFictionBrain.png")
st.subheader("Project by Leo Corelli & Rob Baldoni for AIPI 561")
text = st.text_input("Text you want to summarize:")

if text:
    results = summarize_text(text, model)
    
    st.subheader("Text Summary:")
    st.write(results)