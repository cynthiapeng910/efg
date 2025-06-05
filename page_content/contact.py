import streamlit as st

def contact_page():
    st.markdown("## Contact Me")
    
    st.markdown("""
    Thank you for your attention! Feel free to reach out to me through any of the following channels:
    
    ### Direct Contact
    - **Email**: [11555218678@link.cuhk.edu.hk](mailto:1155218678@link.cuhk.edu.hk)
    - **Phone**: +852 46368146
    - **LinkedIn**: [linkedin.com/in/siyan-cynthia-p-148b04241](https://www.linkedin.com/in/siyan-cynthia-p-148b04241/)
    - **GitHub**: [github.com/cynthiapeng910](https://github.com/cynthiapeng910)
    """)
    
    st.markdown("### Send Me a Message")
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
            
        with col2:
            subject = st.text_input("Subject")
            
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success("Thank you for your message! I'll get back to you soon.")
            # In a real application, you would process the form data here
            # For example, send an email or store in a database
    
    st.markdown("---")
    
    st.markdown("""
    ### Office Hours
    I'm generally available for virtual meetings Monday through Friday, 9 AM to 5 PM Eastern Time.
    Please email me to schedule a call or video conference.
    """)
