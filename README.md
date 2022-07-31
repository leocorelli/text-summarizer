# Text Summarizer
[![Python application test with Github Actions](https://github.com/leocorelli/AIPI561-finalproj/actions/workflows/main.yml/badge.svg)](https://github.com/leocorelli/AIPI561-finalproj/actions/workflows/main.yml)

A cloud-deployed web microservice by Leo Corelli & Rob Baldoni, made for our Duke AIPI 561 Final Project.

[Microservice Website](https://leocorelli-text-summarizer.azurewebsites.net/)

<p align="center">  <img src="https://github.com/leocorelli/AIPI561-finalproj/blob/main/images/ArtificialFictionBrain.png" width="400" /> </p>

<p align="center">All image credit goes to original author. Image sourced from: https://commons.wikimedia.org/wiki/File:ArtificialFictionBrain.png</p>


## About

For this project we have deployed a machine learning text summarizer to the cloud using Huggingface's Transformers library and Azure App Service. There is a wealth of information on the internet, and we (Rob and Leo) are naturally very curious. We love to read and learn new things. We both frequent wikipedia and other resources to learn more about whatever topics pique our interest on a given day. This can be time consuming. As busy young professionals with degrees in artificial intelligence we set out to find a better way!

Fortunately for us, there is a plethora of pre-trained text summarization models on the [huggingface models hub](https://huggingface.co/models?pipeline_tag=summarization&sort=downloads). We used a pre-trained BART model, which is a transformer architecture particularly well suited to the text summarization task. We built our project around this model, successfully creating a cloud-hosted, continuously delivered text summarization web microservice.

We hope that you enjoy interacting with our microservice and gain some value from it. It is particularly well suited at summarizing medium length articles and wikipedia documents. Hopefully you can learn while saving some time and energy next time you are researching something on the internet. Just find some text, enter it into our web microservice, kick back, grab a drink, and wait for your concise summary. Cheers :)
