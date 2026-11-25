import streamlit as st

# Title of App
st.title("Web Development Labs 03 & 04")

# Assignment Data
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 58, Web Development")
st.subheader("Remy Sultanik, James Betza")

# TODO (optional): Add a group photo to the images folder and show it here, for example:
# st.image("images/group_photo.jpg")


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description

st.write("""
Welcome to LEGO Set Explorer! Use the sidebar to explore LEGO set data and chat about building ideas. The following pages are:

1. **Home**: An introduction to the project and its pages.
2. **Data Page**: Explore Rebrickable set data, compare average piece counts by year, and view the largest sets from a selected year.
3. **Chatbot**: LEGO Bot, Chat with a LEGO companion about building ideas, techniques, and design inspiration. It does not look up live set details.
4. **Agent**: To come in lab4
""")
