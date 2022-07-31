FROM --platform=linux/amd64 python:3.8

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt


COPY . /app
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["main.py"]