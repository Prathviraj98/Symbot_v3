import streamlit as st
import random
import time
from crewai import Agent, Task, Crew, Process
import os

from langchain_google_genai import ChatGoogleGenerativeAI
api_gemini = os.environ.get("GEMINI-API-KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-pro", verbose=True, temperature=0.1, google_api_key=""
)



from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()

from langchain_community.utilities import StackExchangeAPIWrapper
stackexchange = StackExchangeAPIWrapper()

from langchain.tools import YouTubeSearchTool
youtube_tool = YouTubeSearchTool()

from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL
python_repl = PythonREPL()

ltool=list()
luti=list()
m1tool=list()
m1uti=list()
m2tool=list()
m2uti=list()

def app():
    st.title("SymBot Advanced")
    time.sleep(0.05)
    st.header("Welcome to Advanced AI")
    time.sleep(0.05)
    st.subheader("Our Advanced AI crew provides you the freedom of customization to select the tools and utilities you like to have in your AI crew...")
    st.session_state.clear()
    with st.form("my_form"):
        LeaderRole=st.text_input(label='Leader role : ')
        LeaderRoleDis=st.text_input(label='Leader role discription : ')
        st.text('Select the tools for your crew leader : ')
        lt1 = st.checkbox('Search tool')
        if lt1:
            ltool.append(search_tool)
        lt2 = st.checkbox('Youtube tool')
        if lt2:
            ltool.append(youtube_tool)
        lu1 = st.checkbox('Stack-exchange tool')
        if lu1:
            luti.append(stackexchange)
        lu2 = st.checkbox('Wikipedia tool')
        if lu2:
            luti.append(wikipedia)
        lu3 = st.checkbox('Advanced math tool')
        if lu3:
            luti.append(python_repl)
        Member1Role=st.text_input(label='Member 1 role : ')
        Member1RoleDis=st.text_input(label='Member 1 role discription: ')
        st.text('Select the tools for your crew member 1 : ')
        m1t1 = st.checkbox('Search tool  ')
        if m1t1:
            m1tool.append(search_tool)
        m1t2 = st.checkbox('Youtube tool  ')
        if m1t2:
            m1tool.append(youtube_tool)
        m1u1 = st.checkbox('Stack-exchange tool  ')
        if m1u1:
            m1uti.append(stackexchange)
        m1u2 = st.checkbox('Wikipedia tool  ')
        if m1u2:
            m1uti.append(wikipedia)
        m1u3 = st.checkbox('Advanced math tool  ')
        if m1u3:
            m1uti.append(python_repl)
        Member2Role=st.text_input(label='Member 2 role : ')
        Member2RoleDis=st.text_input(label='Member 2 role discription: ')
        st.text('Select the tools for your crew member 2 : ')
        m2t1 = st.checkbox('Search tool ')
        if m2t1:
            m2tool.append(search_tool)
        m2t2 = st.checkbox('Youtube tool ')
        if m2t2:
            m2tool.append(youtube_tool)
        m2u1 = st.checkbox('Stack-exchange tool ')
        if m2u1:
            m2uti.append(stackexchange)
        m2u2 = st.checkbox('Wikipedia tool ')
        if m2u2:
            m2uti.append(wikipedia)
        m2u3 = st.checkbox('Advanced math tool ')
        if m2u3:
            m2uti.append(python_repl)
        submitted = st.form_submit_button("Submit")
        leader=Agent(
                role=LeaderRole,
                    goal='Define the Problem,research,Understand the Context,Identify the Root Cause,Brainstorm Solutions,Evaluate Alternatives,Select the Best Solution,Develop an Action Plan,Implement the Solution,Monitor and Evaluate,Information Retrieval,Language Translation,Text Generation,Task Automation,Learning and Education,Creative Writing',
                    backstory=LeaderRoleDis,
                    tools=ltool,
                    utilities=luti,
                    llm=llm,
                    allow_delegation=True,
                )

        member1=Agent(
                    role=Member1Role,
                    goal='Define the Problem,research,Understand the Context,Identify the Root Cause,Brainstorm Solutions,Evaluate Alternatives,Select the Best Solution,Develop an Action Plan,Implement the Solution,Monitor and Evaluate,Information Retrieval,Language Translation,Text Generation,Task Automation,Learning and Education,Creative Writing',
                    backstory=Member1RoleDis,
                    tools=m1tool,
                    utilities=m1uti,
                    verbose=True,
                    llm=llm,
                    allow_delegation=True,
                )

        member2=Agent(
                    role=Member2Role,
                    goal='Define the Problem,research,Understand the Context,Identify the Root Cause,Brainstorm Solutions,Evaluate Alternatives,Select the Best Solution,Develop an Action Plan,Implement the Solution,Monitor and Evaluate,Information Retrieval,Language Translation,Text Generation,Task Automation,Learning and Education,Creative Writing',
                    backstory=Member2RoleDis,
                    tools=m2tool,
                    utilities=m2uti,
                    verbose=True,
                    llm=llm,
                    allow_delegation=True,
                )
        
    if "messages" not in st.session_state:
        st.session_state.messages = []
    try:
        if (LeaderRole and LeaderRoleDis and Member1Role and Member1RoleDis and Member2Role and Member2RoleDis):
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = "Please enter your query..."
                message_placeholder.markdown(full_response)
            for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])
            if prompt := st.chat_input("Enter Your Query..."):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)
                    task1 = Task(description=prompt, agent=leader)
                    crew = Crew(
                    agents=[leader,member1,member2],
                    tasks = [task1],
                    verbose=2,
                    process=Process.sequential
                    ) 
                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = " "
                    with st.spinner('We are processing your input. Please wait..'):
                        result = crew.kickoff()
                assistant_response = result
                for chunk in assistant_response:
                    full_response += chunk
                    time.sleep(0.01)
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
    except:
        assistant_response='please enter a valid query which is not included violent, sexual or any other harmful activities...'
        for chunk in assistant_response:
            full_response += chunk
            time.sleep(0.01)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
