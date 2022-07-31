from transformers import pipeline
import streamlit as st

@st.cache(allow_output_mutation=True)
def load_model():
    '''Loads and returns huggingface BART model.'''
    model = pipeline(model="sshleifer/distilbart-cnn-12-6")
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