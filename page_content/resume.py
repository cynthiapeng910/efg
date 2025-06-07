import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "Siyan Peng-cv.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Siyan_Peng_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Siyan Peng")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** cynthiapeng910@gmail.com
    - **Phone:** +852 46368146
    - **LinkedIn:** [linkedin.com/in/siyan-cynthia-p](https://www.linkedin.com/in/siyan-cynthia-p-148b04241/)
    - **GitHub:** [github.com/cynthiapeng910](https://github.com/cynthiapeng910)
    - **Address:** 2-18 Lok King St., Sha Tin, N.T., Hong Kong
    """)

    st.header("Professional Summary")
    st.markdown("""
    Fresh graduate with rich internship experiences in marketing, public relations and advertising. Proven ability to work in teams, manage projects, and improve performance. Currently seeking a role to utilize my marketing expertise and problem-solving skills.
    """)

    st.header("Internship Experience")
    st.markdown("""
    **Public Relations Intern, Burson**
    - *March 2024 – June 2024*
    - Conducted passage writing and layout for ENZ (Education New Zealand)’s Wechat public account, including alumni stories, single-sex schools, New Zealand 's highly-ranking subjects and other contents, attracting 100+ fans for the account, praised by the client.
    - Wrote the New Zealand education industry weekly report on education field, New Zealand news reported domestically and industry competitors. Recorded consumer interaction and ensured the source authority and data accuracy.

    **Account Executive Intern, Interone China**
    - *July 2023 – October 2023*
    - Revised and integrated official website content for BMW’s new products, communicated with clients to make required modifications, and collaborated with the Creative Department to modify images and text. Successfully helped update new material onto the website.
    - Conducted consumer interaction analysis on KOC advertising for competitor high-end car brands such as Rolls-Royce and Mercedes-Benz on platforms including Douyin and RedNote. Compiled the findings into reports for the client’s reference.
    

    **Segment Marketing Intern, Schneider Electric**
    - *February 2023 - June 2023*
    - Supported pre-development marketing research for low-voltage power distribution China (LVC) marketing department, drafting overview on aviation oil, aircraft manufacturing and other industries, and reported individually to partner team.
    - Conducted event support by creating and proofreading slide reports, writing speech drafts and checking the official translation.
    
    **Brand Strategy Consulting Intern, Singapore Yisin Consulting**
    - *April 2022- August 2022*
    - Carried out brand dynamics and consumer interaction analysis of leading brands in plant protein drinks on RedNote and formed weekly reports, and summarized findings into an operation document, on average over 6 items per week.
    - Participated in Lolo’s RedNote and Zhihu official account copywriting, poster creation and other activities, producing with an average of over 4 articles per week, over 50% of which are adopted officially by the account.
    """)
    
    st.header("Education")
    st.markdown("""
    **Bachelor of Arts in Business English**
    - University of International Business and Economics
    - *Graduated: July 2024*
    - GPA: 3.53/4.0
    
    **Master of Science in Marketing**
    - The Chinese University of Hong Kong
    - *Graduating in: October 2025*
    - GPA: 3.40/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, R
    - **Data Analysis:** Pandas, Numpy, Matplotlib, Seaborn
    - **Statistical Analysis:** Hypothesis Testing, Regression Analysis
    - **Video Processing:** Capcut, Adobe Premiere
    - **Soft Skills:** Team Leadership, Problem-Solving, Communication, Copywriting
    """)

    st.header("Campus Experiences")
    st.markdown("""
    - UIBE Radio and Television Center-English Anchor
    - SIS-Student Career Development Center-Coordinator
    - SIS-Student Academic Research Development Center-Coordinator
    """)

    st.header("Academic Projects")
    st.markdown("""
    **Comparative Study of G7 & G20 in the View of New-type Major Country Coordination**
    - As the research assistant, wrote a literature review on Argentina and the Belt and Road of over 6600 words.
    - Proposed 4 suggestions on the compilation of related textbooks and all were adopted by the professor.

    **Rural Revitalization Research - Taking Yuanjia Village's poverty alleviation as example**
    - Researched on the revitalization of Yuanjia Village in Shaanxi Province, making interviews with local people and co-wrote a final report.
    - Our group's case was recommended to be published onto People's Daily and won the school-level scholarship of RMB 4,000.
    """)

    st.header("Languages")
    st.markdown("""
    - **Mandarin:** Native
    - **English:** Fluent
    - **Cantonese:** Intermediate
    """)

    st.header("Interests")
    st.markdown("""
    - Sports: Swimming, playing badminton and table tennis
    - Music: Playing the piano, singing
    - Volunteering: Animal protection volunteering activities
    """)

    st.markdown("---") 
