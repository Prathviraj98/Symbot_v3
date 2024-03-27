import streamlit as st

from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="SymBot",
    page_icon="icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

import home, SymBot, finance, editor, custom, advanced, about


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='SymBot AI Crews',
                options=['Home','General AI','Finance AI','Editor AI','Custom AI','Advanced AI','About'],
                icons=['house','chat-left-text','bi-currency-rupee','book','plus-circle','terminal-plus','info-circle'],
                menu_icon='robot',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#5ce1e6"},
        "nav-link-selected": {"background-color": "#ee3ec9"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "General AI":
            SymBot.app() 
        if app == "Finance AI":
            finance.app() 
        if app == "Editor AI":
            editor.app()
        if app == "Custom AI":
            custom.app()
        if app == "Advanced AI":
            advanced.app()
        if app == "About":
            about.app() 

    run()            