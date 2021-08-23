# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 17:11:14 2021

@author: admin
"""
import cv2 as cv
import numpy as np
import streamlit as st
st.title("WaterMark Maker")
file1=st.file_uploader("Select the files in  such a way that second file is watermark file",type=["jpg",'png'],accept_multiple_files=True)
k=[]
for uploaded_file in file1:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv.imdecode(file_bytes, 1)
    # Now do something with the image! For example, let's display it:
    k.append(opencv_image)
if len(k)>1:
    for i in range(2):
        st.image(k[i], channels="BGR")
if (file1 is not None) and (len(k)>=2):
    k1=k[0].shape
    k12=k[1].shape
    st.write("shapes are ",str(k1),"and",str(k12))
    if (k1!=k12):
        h,w,c=k[0].shape
        k[1]=cv.resize(k[1],(w,h))
        k13=k[0].shape
        k14=k[1].shape
        st.write("shapes are ",str(k13),"and",str(k14))
        o=st.number_input("Choose a number between 1 and 0")
        dst=cv.addWeighted(k[1],o,k[0],1-o,0)
        st.image(dst,channels='BGR')
        
        