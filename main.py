from langchain.prompts import PromptTemplate
import streamlit as st
from langchain_community.llms import Ollama

# Initialising my local LLM model ( dolphin-mistral : Good at coding. Based on Mistral)
llm = Ollama(model="dolphin-mistral")

def getllmresponse(technology_name,operating_systems):
    # Template
    template="""
    Give me the best way to implement {technology_name} technology on of these operating systems {operating_systems}. Do not forget that i am a complete beginner. So please be detailed.
"""
    # Creating the prompt
    prompt = PromptTemplate(input_variables = ['technology_name','operating_systems'], template=template)

    #Providing the prompt and invoking the Response from the model
    response = llm.invoke(prompt.format(technology_name=technology_name,operating_systems=operating_systems))
    # Return the response to the page
    return response
    
# Page configurations    
st.set_page_config(page_title="Generate Blogs",
                   layout='centered',
                   initial_sidebar_state='collapsed')

# Simple Page Title    
st.header('Technology Implementation')


## Create two more columns for additional 2 fields

col1,col2 = st.columns([5,5])

with col1:
    technology_name=st.text_input('Technology you want to implement')

with col2:
     operating_systems=st.selectbox('Operating Systems',('Windows','Kali Linux','Ubuntu','MacOS Sierra'),index=0)

# Submission field
submit=st.button('Generate')

# Launching the model on submission following the template given
if submit:
     st.write(getllmresponse(technology_name,operating_systems))