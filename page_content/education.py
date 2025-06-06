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
        ### AWS Certified Data Analytics - Specialty
        **Amazon Web Services** | *March 2022*
        
        Demonstrated expertise in designing, building, securing, and maintaining analytics solutions on AWS.
        """)
        
    with exp2:
        st.markdown("""
        ### TensorFlow Developer Certificate
        **Google** | *January 2022*
        
        Validated ability to develop deep learning models using TensorFlow.
        """)
        
    with exp3:
        st.markdown("""
        ### Microsoft Certified: Azure Data Scientist Associate
        **Microsoft** | *November 2021*
        
        Demonstrated expertise in using Azure services to train, evaluate, and deploy machine learning models.
        """)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### Sentiment Analysis of Product Reviews
    - Developed a deep learning model to analyze customer reviews and predict sentiment
    - Achieved 92% accuracy using BERT and fine-tuning techniques
    - Implemented the model as a web application using Flask
    
    ### Image Classification for Medical Diagnosis
    - Created a convolutional neural network to classify medical images
    - Worked with a dataset of X-ray images to detect pneumonia
    - Achieved 88% accuracy and deployed the model on a cloud platform
    """)
    
    st.markdown("---") 
