import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()


API_KEY = os.getenv("AQ.Ab8RN6KY_MVZByahKbDzpl6nW2L_qM-iF2x4TN5zhigBmvnpPw")

st.write(API_KEY)

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


st.set_page_config(
    page_title="AI Social Media Creator",
    page_icon="📱"
)


st.title("📱 AI Social Media Content Creator")


business = st.text_input(
    "Enter Business Type"
)


if st.button("Generate Content"):

    if business:

        prompt = f"""

        Create social media marketing content for:

        Business:
        {business}

        Generate:

        1. Instagram Caption
        2. LinkedIn Post
        3. Facebook Post
        4. Hashtags
        5. 7 Days Content Ideas

        Make it creative and professional.

        """

        response = model.generate_content(prompt)


        st.subheader("Generated Content")

        st.write(response.text)


    else:

        st.warning(
            "Please enter business type"
        )