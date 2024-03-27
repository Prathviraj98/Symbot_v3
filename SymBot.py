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

def app():
    st.title("SymBot General")
    time.sleep(0.05)
    st.header("Welcome to General AI")
    time.sleep(0.05)
    st.subheader("Our General AI crew is here to help you...")
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = "Please enter your query..."
        message_placeholder.markdown(full_response)
    
    leader=Agent(
        role='AI crew leader',
        goal='Define the Problem,research,Understand the Context,Identify the Root Cause,Brainstorm Solutions,Evaluate Alternatives,Select the Best Solution,Develop an Action Plan,Implement the Solution,Monitor and Evaluate,Information Retrieval,Language Translation,Text Generation,Task Automation,Learning and Education,Creative Writing',
        backstory='you are an AI crew leader capable of solving any problem and answering any query with the help of your crew members and by accessing real-time information and data',
        tools=[search_tool],
        utilities=[stackexchange,wikipedia,python_repl],
        verbose=True,
        llm=llm,
        allow_delegation=True,
    )

    member1=Agent(
        role='AI crew member1',
        goal='Define the Problem,research,Understand the Context,Identify the Root Cause,Brainstorm Solutions,Evaluate Alternatives,Select the Best Solution,Develop an Action Plan,Implement the Solution,Monitor and Evaluate,Information Retrieval,Language Translation,Text Generation,Task Automation,Learning and Education,Creative Writing',
        backstory='you are an AI crew member capable of helping AI crew leader to solve any problem and answering any query with the help of your crew members and by accessing to real-time information and data',
        tools=[search_tool],
        utilities=[stackexchange,wikipedia,python_repl],
        verbose=True,
        llm=llm,
        allow_delegation=True,
    )

    member2=Agent(
        role='AI crew member2',
        goal='Define the Problem,research,Understand the Context,Identify the Root Cause,Brainstorm Solutions,Evaluate Alternatives,Select the Best Solution,Develop an Action Plan,Implement the Solution,Monitor and Evaluate,Information Retrieval,Language Translation,Text Generation,Task Automation,Learning and Education,Creative Writing',
        backstory='you are an AI crew member capable of helping AI crew leader to solve any problem and answering any query with the help of your crew members and by accessing to real-time information and data',
        tools=[search_tool],
        utilities=[stackexchange,wikipedia,python_repl],
        verbose=True,
        llm=llm,
        allow_delegation=True,
    )
    if "messages" not in st.session_state:
        st.session_state.messages = []
    try:
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
