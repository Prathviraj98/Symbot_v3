import streamlit as st
import time
import home, SymBot, finance, editor, about
import json
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
anime=load_lottiefile('home_anime.json')
def app():
    st.title("SymBot AI")
    time.sleep(0.05)
    st.header("Welcome to SymBot")
    time.sleep(0.05)
    st.subheader("A crew of AI agents is here to help you solve problems...")
    time.sleep(0.05)
    st_lottie(
    anime,
    speed=1,
    reverse=False,
    loop=True,
    quality="high",  # canvas
    height=500,
    key=None,
    )
    st.markdown('AI crew is a team of artificial intelligence experts who work together to solve problems and answer queries. They have access to real-time information and data, and they can use this information to help them make decisions and solve problems. AI crew members are also able to learn and adapt, so they can continue to improve their skills over time. AI crew members can be used to solve a wide variety of problems, including: * Answering customer questions * Troubleshooting technical problems * Developing new products and services * Conducting research * Making business decisions AI crew members can also be used to help people learn and grow. They can provide personalized instruction, answer questions, and offer feedback. AI crew is a valuable resource for businesses and individuals alike. They can help people solve problems, learn new things, and make better decisions.')