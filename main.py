from transformers import pipeline

def load_model():
    '''Loads and returns Facebook BART model trained on CNN Daily Mail for text summarization.'''
    model = pipeline("summarization", model="./bart")
    return model


if __name__ == "__main__":
    model = load_model()
    print(model)