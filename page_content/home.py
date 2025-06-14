import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Siyan Peng</h4>
        <p>Recent Master's Graduate in Marketing<br>
        The Chinese University of Hong Kong<br>
        2-18 Lok King St., Sha Tin, N.T., Hong Kong<br>
        <a href="mailto:cynthiapeng910@gmail.com">cynthiapeng910@gmail.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "PENG Siyan profile pic.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
       I am a recent master's graduate in Marketing (big data track) from The Chinese University of Hong Kong. My former Bachelor’s degree in Business English with a focus on intercultural communication has equipped me with a robust understanding of global business practices in diverse cultural contexts. During my academic journey, I developed a strong foundation in business acumen, marketing intricacies, and data analysis.

       As part of my master's program, I completed several projects that involved working with real-world datasets and applying various data science techniques, such as providing advice for sellers on JD.com based on problems discovered from their provided transaction data. These projects allowed me to gain hands-on experience in data preprocessing, data analysis, model building, and evaluation.
       
       I am passionate about leveraging my business expertise and data dealing and analysis capability to drive insights and make informed decisions. At work, I focus on independent learning, team collaboration, and effective and efficient decisions. I am excited to contribute my skills and grow as a digital marketing professional in a dynamic, data-driven and diversified environment.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
        - Statistical Analysis: Hypothesis Testing, Regression Analysis
        - Video Processing: Capcut, Adobe Premiere
        - Language Level：IELTS 7.5, TEM-8 80, TEM-4 82, GRE 320
        - Communication: Presentation Skills, Technical Writing, Copywriting
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 
