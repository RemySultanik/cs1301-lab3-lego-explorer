# Lab 3: Chatbot page
# TODO: Rename this file to fit your page. Keep the number at the front.
#
# A chatbot built with Pydantic AI (see the Pydantic AI pages on Canvas).
# It should:
#   - use a Pydantic AI Agent with instructions that fit your project's theme (no tools yet)
#   - use Streamlit's chat elements: st.chat_message and st.chat_input
#   - remember the conversation (message_history, saved in st.session_state)
#   - use try/except so an error shows a message instead of crashing the page
#   - stay on theme, without using any API or external data
#
# Your Gemini API key goes in .streamlit/secrets.toml as GOOGLE_API_KEY.

import streamlit as st
from pydantic_ai import Agent

agent = Agent(
    "google:gemini-3.5-flash-lite",
    instructions=(
        "You are a friendly LEGO companion. "
        "Only talk about LEGO, building, and design inspiration. "
        "Keep replies concise and ask a natural follow up when helpful. "
        "You cannot look up Rebrickable data or exact set details. "
        "If you are unsure, say so instead of guessing."
        "You have the general familiarity of an enthusiastic LEGO fan with themes and building experiences, "
        "but you do not know exact set details unless they are provided in the conversation. "
    ),
)
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! I'm LEGO Bot. Ask me about building ideas, LEGO themes, or design inspiration."}]

if "agent_history" not in st.session_state:
    st.session_state.agent_history = []

st.title("🧱 LEGO Bot")
st.write("Chat with LEGO Bot about building ideas, techniques, or overall love for LEGO. ")

if st.button("Clear chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm LEGO Bot. Ask me about building ideas, LEGO themes, or design inspiration."}
    ]
    st.session_state.agent_history = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask your LEGO companion...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        with st.spinner("Thinking..."):
            result = agent.run_sync(prompt, message_history=st.session_state.agent_history,)

        reply = result.output
        st.session_state.agent_history = result.all_messages()

    except Exception as error:
        reply = (f"Sorry, I couldn't get a response: {error}")

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    