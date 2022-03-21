import streamlit as st

st.header("HELLO BEAUTIFUL!")

num = st.number_input("enter a num:", 1, 10)

if num:
    for i in range(1, 11):
        st.write(num * i)
st.write("Thank You!")
