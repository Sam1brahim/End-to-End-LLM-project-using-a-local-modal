# End-to-End-LLM-project-using-a-local-modal-with-Ollama-from-Langchain-Community 

## Requirements :

#### ollama
#### langchain
#### streamlit
#### your local LLM 

## Remark : 
Make Sure you run inside your terminal of vscode : 'ollama run yourmodel' so that you can download it ( you can find available models here : https://ollama.com/library ). then write '/bye' to exit the model, then launch the web app with the command : streamlit run main.py
     
# --------------------------------------------------------------

Technology Implementation Guide Generator

This repository hosts the code for a Streamlit-based web application that leverages the langchain_community.llms 'Ollama' module to interact with a custom Local Large Language Model (LLM), specifically "dolphin-mistral". This model is designed to be adept at coding-related tasks, building upon the capabilities of the Mistral model.

The application prompts the LLM to generate detailed, beginner-friendly guides for implementing various technologies on different operating systems. The response is tailored using a prompt template to ensure clarity and thoroughness, making it an ideal starting point for users unfamiliar with the technology they wish to implement.

Key features:

    Custom LLM integration via Ollama from langchain_community.llms
    Dynamic prompt templating for personalized guide generation
    Intuitive Streamlit interface for inputting technology and operating system choices
    Responsive guide output for technology implementation, aimed at beginners

