import streamlit as st

# sidebar 영역
# st.sidebar.title('this is sidebar')
# st.logo("logo.jpg")
pages = {
    "Your account": [
        st.Page("create_account.py", title="Create your account"),
        st.Page("manage_account.py", title="Manage your account")
    ],
    "Resources": [
        st.Page("learn.py", title="Learn about us"),
        st.Page("trial.py", title="Try it out")
    ]
}

pg = st.navigation(pages)
pg.run()


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
