import streamlit as st
from pydantic_ai import Agent

agent = Agent(
    "google:gemini-3.5-flash-lite",
    instructions="You are a friendly assistant. Answer in one sentence.",
)

result = agent.run_sync("Say hello to a CS 1301 student!")
st.write(result.output)