#Importing libraries
import streamlit as st
import os
from modules.file_processing import read, pwd_protect
from modules.page_render import basic_render
import time

#Rendering page
basic_render()

#Allowing user to enter directory where word documents are stored for conversion and encryption
directory = st.sidebar.text_input("**Enter path to folder where documents are stored.**")

#Divider
st.sidebar.divider()

#Button to convert to PDFs
button_pdf = st.sidebar.button(label='Convert to PDF',type='primary', use_container_width=True)

#Button to apply password protection to PDFs
button_encrypt = st.sidebar.button(label='Encrypt PDF',type='primary', use_container_width=True)

#Performs the below only if directory provided
if directory:

    #Performs the below only if convert to pdf button is clicked
    if button_pdf:

        try:

            #Creating a list of the word files in the directory
            files = [(f"{directory}\\{file}") for file in os.listdir(directory)]
            files = [file for file in os.listdir(directory) if file.lower().endswith('.docx')]
            files = [directory+"/"+file for file in files]

            for file in files:
                read(file)
            st.success("All documents have been successfully converted to PDF!")

        except:
            st.error("Error occured during conversion to PDF.")
            results=None

    #Performs the below only if encrypt pdf button is clicked
    if button_encrypt:

        try:
            #Filtering for PDFs in directory
            pdf_files = [directory+"/"+file for file in os.listdir(directory) if file.lower().endswith('.pdf')]

            #Applying password protection function
            if len(pdf_files)!=0:
                for file in pdf_files:
                    pwd_protect(file)
                st.success("PDF documents have been successfully encrypted!")
            else:
                st.error("Error occured during file encryption. Ensure that PDF documents are present in the folder.")

        except:
            st.error("Error occured during file encryption. Ensure that PDF documents are present in the folder.")

else:
    st.error("Enter folder path to continue.")

#Horizontal divider
st.divider()

#My branding
st.write("**Created by NivAnalytics - https://www.nivanalytics.com**")
