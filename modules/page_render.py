#Below function is to render the page for the word2pdf conversion app
#=================================================================================================

#Importing libraris
import streamlit as st
import os
from PIL import Image

def basic_render():

    #Getting path of images
    cwd_dir = os.path.dirname(__file__)
    rel_path = '../images'
    images_path = os.path.join(cwd_dir,rel_path)
    logo = Image.open(images_path + '/Browser Icon Reverse.png')

    #Configuring Streamlit page
    st.set_page_config(page_title = 'PDF Encryption',
                       page_icon = logo,
                       layout = "wide")
    
    #Creating container with columns for page heading, specific title and logo
    with st.container():
        col1, col2, padding = st.columns([10,1,1])

        #Setting page header and subheader
        with col1:
            st.markdown("### Automation of Document Encryption")
            st.markdown("##### The purpose of this application is to automate the process of converting word documents into password-protected PDF files.")

        #Setting logo
        with col2:
            niv_logo = Image.open(images_path + '/Social Logo.png')
            st.image(niv_logo, width=200, output_format='auto')

    #Horizontal divider
    st.divider()