import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import requests
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

# Use GPT-2 (lightweight)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)

def get_weather(city: str) -> str:
    try:
        url = f"http://wttr.in/{city}?format=3"
        res = requests.get(url)
        return res.text.strip() if res.ok else "Weather service unavailable."
    except Exception as e:
        return f"Error fetching weather: {e}"

st.set_page_config(page_title="Weather Chatbot")
st.title("☁️ Weather Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask about the weather in any city or chat...")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    if "weather" in user_input.lower():
        city = user_input.split("in")[-1].strip()
        response = get_weather(city)
    else:
        inputs = tokenizer.encode(user_input, return_tensors="pt").to(device)
        outputs = model.generate(inputs, max_length=50, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
