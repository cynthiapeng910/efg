import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Internship Experience")
    
    st.markdown("""
    ### Public Relations Intern
    **Burson** | *March 2024 - June 2024*
    
    - Conducted passage writing and layout for ENZ (Education New Zealand)’s Wechat account, including alumni stories, single-sex schools, New Zealand 's highly-ranking subjects and other contents, attracting 100+ fans for the account, praised by the client.
    - Wrote the New Zealand education industry weekly report on education field, New Zealand news reported domestically and industry competitors. Recorded consumer interaction to and ensured the source authority and data accuracy.
    """)
    
    st.markdown("""
    ### Account Executive Intern
    **Interone China** | *July 2023 - October 2023*
    
    - Revised and integrated official website content for BMW’s new products, communicated with clients to make required modifications, and collaborated with the Creative Department to modify images and text. Successfully helped update new material onto the website.
    - Conducted consumer interaction analysis on KOC advertising for competitor high-end car brands such as Rolls-Royce and Mercedes-Benz on platforms like Douyin and RedNote. Compiled the findings into reports for the client’s reference..
    """)
    
    st.markdown("""
    ### Segment Marketing Intern
    **Schneider Electric** | *February 2023 - June 2023*
    
    - Supported pre-development marketing research for low-voltage power distribution China (LVC) marketing department, drafting overview on aviation oil, aircraft manufacturing and other industries, and reported individually to partner team.
    - Conducted event support by creating and proofreading PowerPoint reports, writing speech drafts and checking the official translation.
    """)

    st.markdown("""
    ### Brand Strategy Consulting Intern
    **Singapore Yisin Consulting** | *April 2022 - August 2022*

    - Carried out brand dynamics and consumer interaction analysis of leading brands in plant protein drinks on RedNote and formed weekly reports, and summarized findings into an operation document, on average over 6 items per week.
    - Participated in Lolo’s RedNote and Zhihu official account copywriting, poster creation and other activities, producing with an average of over 4 articles per week, over 50% of which are adopted officially by the account.
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Customer Segmentation Analysis",
            "description": "Used K-means clustering to segment customers based on purchasing behavior.",
            "skills": ["Python", "scikit-learn", "Pandas", "Matplotlib"],
            "outcome": "Identified 5 distinct customer segments that informed targeted marketing campaigns."
        },
        {
            "title": "Predictive Maintenance System",
            "description": "Developed a model to predict equipment failures before they occur.",
            "skills": ["Python", "TensorFlow", "Time Series Analysis", "IoT"],
            "outcome": "Reduced downtime by 23% and maintenance costs by 15%."
        },
        {
            "title": "Natural Language Processing for Customer Support",
            "description": "Created a text classification system to automatically categorize customer support tickets.",
            "skills": ["Python", "NLTK", "spaCy", "BERT"],
            "outcome": "Improved response time by 35% and increased customer satisfaction scores."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # Add the interactive visualization demo
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL, JavaScript
        - **Machine Learning:** scikit-learn, TensorFlow, PyTorch
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        - **Cloud Platforms:** AWS, Azure, Google Cloud
        - **Web Development:** Django, Flask, React
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 
