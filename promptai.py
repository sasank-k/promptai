import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain 

os.environ['OPENAI_API_KEY'] = apikey

st.title('Prompt Maker')
prompt = st.text_input("Type here")


llm = OpenAI(temperature=.7)
template = "you are a prompt generator. Essentially I will give u a 1-2 word topic and u must give me a short prompt which i can give to ai to make a script for my blog and podcast based on the prompt you give me. The prompt you give me should make sure that it has good sub topic coverage and covers all relevant news and information, while also being able to talk about the topic as a whole. make sure that it also gives enough information about the topic as a whole, so the viewer/listener can understand more about the topic and what exactly it is. It should make sure to cover about 4-5 subtopics about the topic, and should be a good input that I can plug into an AI. At least one of these subtopics must contain something about recent news about the topic or new developments with the topic, because this is for a podcast that gives listeners updates and the current situation. I will plug your prompt into an AI, and it should be able to give me a good script. For example, I may type in AI as my topic. In that case, you must deliver me with something like: “Write a script about Artificial Intelligence that covers recent developments in AI, ethical concerns, new advancements, and potential future applications of AI. Make sure to discuss various subtopics that provide an overview of the current AI landscape and explore how AI is impacting our lives today. Additionally, discuss the implications of AI on society and the potential for AI to shape the future.” I will then be able to take your prompt and plug it in to an ai to make me a script based on your prompt. Please make sure the subtopics are relevant to my podcast and should cover news and new updates concerning my topic, as I need to use ur prompt to make a script. your topic is: {topic}" 


prompt_template = PromptTemplate(input_variables = ['topic'], template = template)
prompt_chain = LLMChain(llm = llm, prompt = prompt_template, verbose = True )

if prompt:
    response = prompt_chain.run (topic=prompt)
    st.write(response)