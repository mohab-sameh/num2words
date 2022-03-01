# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:34:24 2022

@author: Mohab
"""
import streamlit as st
from hotfix_decorator import decorator_result
import pyperclip as pc
import xclip


hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title("Simple Arabic Numbers to Text by Mohab Sameh")
input_val = st.text_input('Insert number here')


if input_val:
    output_val = decorator_result(int(input_val))
    st.code(decorator_result(int(input_val)))

copy_btn = st.button('Copy Text')
if copy_btn and input_val:
    pc.copy(str(output_val))
    st.success("Text Copied")