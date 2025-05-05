import cv2
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
img = st.sidebar.file_uploader('uplode an image',type= ['jpg','jpeg','png'])



selected_option = st.sidebar.selectbox('Select an option',['Pencil Sketch','Gray Scale Image'])
st.title('Image Processing App')

if img is not None:

    image_bytes = img.read()
    np_image = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_image,cv2.IMREAD_COLOR)


    img1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_g = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img_inv = cv2.bitwise_not(img_g)
    img_sm = cv2.GaussianBlur(img_inv, (25,25),sigmaX= 0, sigmaY = 0)
    img_pe = cv2.divide(img_g,255-img_sm,scale=255)


    if selected_option == 'Gray Scale Image':
        st.image(img_g, caption='Gray Scale Image')
    elif selected_option =='Pencil Sketch':
        st.image(img_pe, caption= 'Pencil Sketch')


hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
