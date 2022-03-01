# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:34:24 2022

@author: Mohab
"""
import streamlit as st
from hotfix_decorator import decorator_result


st.title("Arabic Numbers to Text by Mohab Sameh")
input_val = st.text_input('Insert number here')


if input_val:
    st.text(decorator_result(int(input_val)))
