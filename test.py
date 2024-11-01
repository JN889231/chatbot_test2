import streamlit as st
import webbrowser

st.title("간단한 버튼 예제")

# 첫 번째 버튼
if st.button("첫 번째 버튼"):
    webbrowser.open("http://3.35.137.204")

# 두 번째 버튼
if st.button("두 번째 버튼"):
    webbrowser.open("http://3.35.137.204/test")