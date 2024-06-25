import streamlit as st
import ollama
from openai import OpenAI
import time
import os
import base64


@st.cache_data 
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("image2.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 100%;
background-position: top left;

}}



[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}


</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

def stream_data(text, delay: float = 0.02):
    for word in text.split():
        yield word + " "
        time.sleep(delay)

def fetch_answer_from_gpt(prompt):
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Use your OpenAI API key here
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": """You are an expert Travel assistant, respond accordingly"""},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Token count function for GPT response
def count_tokens(text):
    return len(text.split())

# Streamlit page for comparing models
def comparison_page():
    st.title("Compare Ollama (Llama3, Gemma:2b) and OpenAI GPT Models")

    st.markdown("""
        <style>
            div.stTextInput > div.stTextInputV2 > div.stTextInputBase > input {
                background-color: transparent !important;
                border: 1px solid rgba(0, 0, 0, 0.1);
                color: black !important;
            }
        </style>
    """, unsafe_allow_html=True)

    prompt = st.text_input("Ask anything")

    if prompt:
        with st.chat_message("user"):
            st.write(prompt)

        # Measure time taken for Ollama Llama3 model
        with st.spinner("Thinking (Ollama Llama3)"):
            start_time = time.time()
            llama3_result = ollama.chat(model="travel", messages=[{
                "role": "user",
                "content": prompt,
            }])
            end_time = time.time()
            llama3_response = llama3_result["message"]["content"]
            llama3_time_taken = end_time - start_time
            llama3_response_length = len(llama3_response)

        # Measure time taken for Ollama Gemma:2b model
        with st.spinner("Thinking (Ollama Gemma:2b)"):
            start_time = time.time()
            gemma2b_result = ollama.chat(model="travel2", messages=[{
                "role": "user",
                "content": prompt,
            }])
            end_time = time.time()
            gemma2b_response = gemma2b_result["message"]["content"]
            gemma2b_time_taken = end_time - start_time
            gemma2b_response_length = len(gemma2b_response)

        # Measure time taken for GPT model
        with st.spinner("Thinking (GPT)"):
            start_time = time.time()
            gpt_response = fetch_answer_from_gpt(prompt)
            end_time = time.time()
            gpt_time_taken = end_time - start_time
            gpt_response_length = len(gpt_response)

        # Count tokens for GPT response
        gpt_token_count = count_tokens(gpt_response)

        # Display results in three columns
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Ollama Llama3 Model")
            st.write_stream(stream_data(llama3_response))
            st.write(f"Time taken: {llama3_time_taken:.2f} seconds")
            st.write(f"Response length: {llama3_response_length} characters")

        with col2:
            st.header("Ollama Gemma:2b Model")
            st.write_stream(stream_data(gemma2b_response))
            st.write(f"Time taken: {gemma2b_time_taken:.2f} seconds")
            st.write(f"Response length: {gemma2b_response_length} characters")

        with col3:
            st.header("OpenAI GPT Model")
            st.write_stream(stream_data(gpt_response))
            st.write(f"Time taken: {gpt_time_taken:.2f} seconds")
            st.write(f"Response length: {gpt_response_length} characters")
            st.write(f"Token count: {gpt_token_count} tokens")

# Streamlit navigation
comparison_page()

