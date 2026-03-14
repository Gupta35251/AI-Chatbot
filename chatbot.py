import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

# load_dotenv()     It is the alternative of os.environ[] = "" because it automatically loads the environment variables from the .env file made

st.set_page_config(
    page_title = "ChatBot",
    page_icon = "🤖",
    layout = "centered"
)

st.title("💬 Generative AI Chatbot")

# Initializing Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
# It is the feature of streamlit that st.chat_input when user gives input the complete code
# in the streamlit will reruns nd it make the chat history empty again and again so if we use st.session_state
# then it will store the history or other things that is stored in it
# And not unfill again and again if reruns



for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

llm = ChatOllama(
    model = "mistral:7b",
    temperature = 0.2,
)


user_input = st.chat_input("Ask ChatBot ...")
if user_input:
    st.chat_message("User").markdown(user_input)
    st.session_state.chat_history.append({"role":"user","content":user_input})
    response = llm.invoke(
        input = [{"role":"system","content":"You are helpful ai assistant"},*st.session_state.chat_history]
    )
    st.session_state.chat_history.append({"role":"assistant","content" : response.content})
#  * unpacks the chat_history it gives the message one by one to llm
    with st.chat_message("Assistant"):
        st.markdown (response.content)