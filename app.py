import streamlit as st
from streamlit_option_menu import option_menu
from book import book_recommendation
from movie import movie_recommendation


# Sidebar with custom subtitle and options
with st.sidebar:
    st.title('Welcome to MoodFlix')
    st.subheader('Pick your poison')
    selected = option_menu(
        "",                 
        ["BookFlix", "MovieFlix"],             
        icons=['book', 'film'],              
        menu_icon="cast",                    
        default_index=0                      
    )

# Show BookPal or MoviePal page based on selection
if selected == "BookFlix":
    book_recommendation()
else:
    movie_recommendation()
