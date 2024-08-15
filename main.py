import os
import requests
import groq
import streamlit as st
from dotenv import load_dotenv
from presets.personas import personas

# Page layout
st.set_page_config(page_title="ITF Chatbot", page_icon="assets/logo-tm.svg", layout="wide")
with open('./assets/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load environment variables
load_dotenv()

# -------------------
# Init session states
# -------------------
default_states = {
    "groq_api_key": os.getenv("GROQ_API_KEY"),
    "preferred_model": os.getenv("PREFERRED_MODEL"),
    "all_models": [],
    "personality": "General Chatbot",
    "temperature": 0.2,
    "messages": [],
}
for key, value in default_states.items():
    if key not in st.session_state:
        st.session_state[key] = value


# -------------------
# Functions
# -------------------
@st.cache_data
def fetch_models():
    os.write(1, b"Fetching models...\n")
    api_key = st.session_state.groq_api_key
    if not api_key:
        return []
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    try:
        response = requests.get("https://api.groq.com/openai/v1/models", headers=headers)
        response.raise_for_status()
        models_data = response.json()
        # Remove models that contains "whisper" or "guard" in their name
        filtered_models = [model["id"] for model in models_data["data"]
                           if "whisper" not in model["id"] and "guard" not in model["id"]]
        return filtered_models
    except requests.RequestException as e:
        st.error(f"Failed to fetch models: {str(e)}")
        return []


def update_session_states():
    sys_prompt = personas[st.session_state.personality]
    if len(st.session_state.messages) > 0:
        st.session_state.messages[0]["content"] = sys_prompt
    else:
        st.session_state.messages = [{"role": "system", "content": sys_prompt}]
        st.session_state.messages.append({"role": "assistant", "content": "How can I help you?"})


def stream_response(completion):
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content


def main():
    # Sidebar
    with st.sidebar:
        st.title("Chat Settings")
        # API Key input
        if st.session_state.groq_api_key is None:
            new_api_key = st.text_input("Enter Groq API Key", type="password")
            if new_api_key:
                st.session_state.groq_api_key = new_api_key
                st.toast("API Key is saved", icon="✅")
                st.rerun()
        else:
            st.session_state.all_models = fetch_models()
            if st.button("Clear API Key"):
                st.session_state.groq_api_key = None
                st.rerun()
            # Add settings to the sidebar
            try:
                pref_model = st.session_state.preferred_model
                index = st.session_state.all_models.index(pref_model)
            except ValueError:
                index = 0
            st.session_state.preferred_model = st.selectbox("Select Preferred Model", st.session_state.all_models,
                                                            index=index)
            st.selectbox("Select Personality", list(personas.keys()), key="personality")
            st.slider("Temperature", 0.0, 2.0, step=0.1, key="temperature")
            # Clear chat history button
            if st.button("Start a new conversation", type="primary"):
                st.session_state.messages = []
            update_session_states()

    # Main chat interface
    with open('assets/logo-tm.svg') as f:
        st.markdown(f'<div id="main_header">{f.read()}<p>ITF Chatbot <span>(v2.0)</span></p></div>',
                    unsafe_allow_html=True)

    # Display a warning if API key is not set
    if st.session_state.groq_api_key is None:
        st.error("""
          Please enter your Groq API key in the sidebar to start chatting.   
          - Login to [Groq](https://groq.com).
          - Go to [API Keys](https://console.groq.com/keys).
          - Create a new API key and enjoy chatting with Groq ;-)
          - And best of all, it's **totally free**! 🎉
          """)
    else:
        # Show chat history
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
        # Set Groq client
        client = groq.Groq(
            api_key=st.session_state.groq_api_key,
        )
        # This runs every time the user submits a prompt
        if prompt := st.chat_input():
            st.session_state.messages.append(
                {"role": "user", "content": prompt}
            )
            st.chat_message("user").write(prompt)
            completion = client.chat.completions.create(
                model=st.session_state.preferred_model,
                temperature=st.session_state.temperature,
                stream=True,
                max_tokens=4096,
                messages=st.session_state.messages
            )
            # Stream completion to the browser
            with st.chat_message("assistant"):
                response = st.write_stream(stream_response(completion))
            # Add finale response to the chat history
            st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
# Debug: Display session state
# st.write(st.session_state)
