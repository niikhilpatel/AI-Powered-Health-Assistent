import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')


chatbot = pipeline("text-generation", model="distilgpt2")


def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']


# Streamlit web app interface
def main():
    st.title("Healthcare Assistant Chatbot")
    
    user_input = st.text_input("How can I assist you today?", "")
    
    # Display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            # response = healthcare_chatbot(user_input)
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            print("response ",response)
            print("=======================================================")
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")
if __name__ == "__main__":
    main()