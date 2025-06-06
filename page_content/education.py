import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing
    **The Chinese University of Hong Kong** | *August 2024 - October 2025*
    
    - GPA: 3.40/4.0
    - Relevant Coursework: Digital Marketing, Big Data Strategy, Marketing Research, Marketing Analytics, Buyer behavior, Pricing Analytics, Strategic Brand Management, Machine Learning in Marketing, Customer Analytics, Social Media Analytics
    
    ### Bachelor of Arts in Business English
    **University of International Business and Economics** | *September 2020 - June 2024*
    
    - GPA: 3.53/4.0
    - Relevant Coursework: Integrated Business English, Principles of Marketing, Principles of Management, Media Marketing, Global Marketing, Business Data Processing and Analysis, Journalism and Communication Ethics 
    """)
    
    st.markdown("---")
    
    st.markdown("## Student Organization Work Experience")
    
    exp1, exp2, exp3 = st.columns(3)
    
    with exp1:
        st.markdown("""
        ### UIBE Radio and Television Center-English Anchor
        *Sept 2021-Sept 2022*
        
        Conducted weekly lunchtime news broadcasts and monthly special program broadcasts (published on the Wechat public account UIBE Campus Voice), the number of listeners of which exceeded 700.
        """)
        
    with exp2:
        st.markdown("""
        ### SIS-Student Career Development Center-Coordinator
        *Sept 2020-Sept 2021*
        
        Hosted 2 career development lectures, receiving hundreds of listeners.
        """)
        
    with exp3:
        st.markdown("""
        ### SIS-Student Academic Research Development Center-Coordinator
        *Sept 2020-Sept 2021*
        
        Contacted tutors and students for 2 academic courses throughout the whole semester.
        """)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### Comparative Study of G7 & G20 in the View of New-type Major Country Coordination-Research Assistant
    - Wrote a literature review on Argentina and the Belt and Road of over 6600 words
    - Proposed 4 suggestions on the compilation of related textbooks and all were adopted by the professor
    
    ### Rural Revitalization Research - Taking Yuanjia Village's poverty alleviation as example
    - Researched on the revitalization of Yuanjia Village in Shaanxi Province, making interviews with local people and co-wrote a final report
    - Our group's case was recommended to be published onto *People's Daily* and won the school-level scholarship of RMB 4,000
    """)
    
    st.markdown("---") 
