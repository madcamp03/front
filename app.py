import streamlit as st

st.sidebar.title('this is sidebar')

st.title('this is title')
st.header('this is header')
st.subheader('this is subheader')

tab1, tab2 = st.tabs(['Tab A', 'Tab B'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write('hello')

with tab2:
    # tab B를 누르면 표시될 내용
    st.write('hi')
