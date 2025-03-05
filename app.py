import streamlit as st # type: ignore
import requests

st.title("💡 Deepseek R1")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("Ask for help:")

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("🚀 Deepseek R1 thinking..."):
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "deepseek-r1:latest",
                "prompt": prompt,
                "stream": False
            }
        )

        answer = res.json()["response"]

        st.chat_message("ai").write(answer)    
        st.session_state.messages.append({"role": "ai", "content": answer})