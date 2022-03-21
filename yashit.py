import streamlit as st

st.header("hello yashi!")

num = st.number_input("enter a num:")

if num:
    for i in range(1, 11):
        st.write(num * i)
