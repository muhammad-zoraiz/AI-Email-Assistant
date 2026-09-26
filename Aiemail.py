from dotenv import load_dotenv
import os
from openai import OpenAI
import streamlit as st

# -------- API SETUP --------

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


# -------- GET EMAIL DETAILS --------

def get_email_details():

    email_request = st.text_area("What do you want to write?")
    recipient = st.text_input("Who is this email for?")
    purpose = st.text_input("What is the purpose of the email?")
    details = st.text_area("What details should be included?")

    return email_request, recipient, purpose, details


# -------- CHOOSE TONE --------

def choose_tone():

   tone = st.selectbox(
    "Choose the tone",
    ["Professional", "Friendly", "Formal", "Casual"]
)

   return tone


# -------- CHOOSE LENGTH --------

def choose_length():

   length = st.selectbox(
    "Choose the email length",
    ["Short", "Medium", "Detailed"]
)

   return length

# -------- GENERATE EMAIL --------

def generate_email(prompt):

    try:

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        st.error("Something went wrong while generating the email.")
        st.error(f"Error: {e}")

        return None





# -------- MAIN PROGRAM --------

st.title(" AI Email Assistant")
st.write("Generate professional emails using AI.")


email_request, recipient, purpose, details = get_email_details()

tone = choose_tone()

length = choose_length()


# -------- BUILD PROMPT --------

prompt = f"""
You are an AI email writing assistant.

Write a complete email using the information below.

User request: {email_request}
Recipient: {recipient}
Purpose: {purpose}
Details: {details}
Tone: {tone}
Length: {length}

Return only the finished email.
Do not provide analysis, safety labels, explanations, or notes.
"""


# -------- GENERATE EMAIL --------


if st.button("Generate Email"):

    # VALIDATION
    if (
        not email_request.strip()
        or not recipient.strip()
        or not purpose.strip()
        or not details.strip()
    ):
        st.warning("Please fill in all the fields.") 

    else:

        with st.spinner("Generating your email..."):
            email = generate_email(prompt)

        if email:
            st.subheader("Generated Email")
            st.write(email)  