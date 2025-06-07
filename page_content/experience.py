import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Internship Experiences")
    
    st.markdown("""
    ### Public Relations Intern
    **Burson** | *March 2024 - June 2024*
    
    - Conducted passage writing and layout for ENZ (Education New Zealand)’s Wechat public account, including alumni stories, New Zealand single-sex schools, New Zealand's highly-ranking subjects and other contents, attracting 100+ fans for the account, praised by the client.
    - Wrote the New Zealand education industry weekly report on education field, New Zealand news reported domestically and industry competitors. Recorded consumer interaction and ensured the source authority and data accuracy.
    """)
    
    st.markdown("""
    ### Account Executive Intern
    **Interone China** | *July 2023 - October 2023*
    
    - Revised and integrated the official website content for BMW’s new products, communicated with clients to make required modifications, and collaborated with the Creative Department to modify images and text. Successfully helped update new material onto the website ontime.
    - Conducted consumer interaction analysis on KOC advertising for competitor high-end car brands such as Rolls-Royce and Mercedes-Benz on platforms including Douyin and RedNote. Compiled the findings into reports for the client’s reference.
    """)
    
    st.markdown("""
    ### Segment Marketing Intern
    **Schneider Electric** | *February 2023 - June 2023*
    
    - Supported pre-development marketing research for low-voltage power distribution China (LVC) marketing department, drafting overview on aviation oil, aircraft manufacturing and other industries, and reported individually to partner team.
    - Conducted event support by creating and proofreading slide reports, writing speech drafts and checking the official translation.
    """)

    st.markdown("""
    ### Brand Strategy Consulting Intern(Remote)
    **Singapore Yisin Consulting** | *April 2022 - August 2022*

    - Carried out brand dynamics and consumer interaction analysis of leading brands in plant protein drinks on RedNote and formed weekly reports, and summarized findings into an operation document, on average over 6 items per week.
    - Participated in Lolo’s RedNote and Zhihu official account copywriting, poster creation etc., producing on average over 4 articles per week, over 50% of which were adopted officially by the account.
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Comparative Study of G7 & G20 in the View of New-type Major Country Coordination",
            "description": "As the research assistant to the professor, helped conduct research by developing literature review and providing modification advice for related textbooks.",
            "skills": ["literature research", "business English", "academic writing"],
            "outcome": "Academic results and proposed suggestions on design of the textbooks were praised and adopted."
        },
        {
            "title": "Rural Revitalization Research-Yuanjia Village as an example",
            "description": "Researched online on the revitalization of Yuanjia Village in Shaanxi Province, and made offline interviews with local people.",
            "skills": ["field survey", "real-time interviews", "academic writing", "team work"],
            "outcome": "Co-wrote a final report and of which the case was recommended to be published onto People's Daily and won the school-level scholarship of RMB 4,000."
        },
        {
            "title": "Research on Construction and Application of Value-oriented Quality Standards for Foreign Language Examinations",
            "description": "Conducted factor identification and multi-factor labeling.",
            "skills": ["Semantics", "Pragmatics", "Syntax", "Excel"],
            "outcome": "Completed labeling and annotation of 1000+ corpus extracted sentences within 10 days."
        }
    ]
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R
        - **Data Analysis:** Pandas, NumPy, Matplotlib, Seaborn
        - **Statistical Analysis:** Hypothesis Testing, Regression Analysis
        - **Video Processing:** Capcut, Adobe Premiere
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication of Mandarin and English
        - **Teamwork:** Collaborative team player with experience in agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 
