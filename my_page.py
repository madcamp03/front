import streamlit as st
import pandas as pd


def show_my_page():
    st.title("기록실")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image('assets/bears.jpg', width=350)

    with col2:
        st.markdown("### 두산 베어스")
        st.markdown("""
        - **선수명:** 정수빈
        - **생년월일:** 1990년 10월 7일
        - **신장/체중:** 175cm/70kg
        - **등번호:** No.31
        - **포지션:** 외야수(좌투좌타)
        - **경력:** 수원신곡초-수원북중-유신고-두산-경찰
        - **입단년도:** 09두산
        """)

    st.markdown("#### 2024 성적")
    data = {
        '팀명': ['두산'],
        'AVG': [0.282],
        'G': [84],
        'PA': [365],
        'AB': [309],
        'R': [61],
        'H': [87],
        '2B': [12],
        '3B': [3],
        'HR': [3],
        'TB': [114],
        'RBI': [28],
        'SB': [33],
        'CS': [5],
        'SAC': [6],
        'SF': [6],
        'BB': [38],
        'IBB': [1],
        'HBP': [6],
        'SO': [40],
        'GDP': [5],
        'SLG': [0.369],
        'OBP': [0.365],
        'E': [1],
        'SB%': [86.8],
        'MH': [26],
        'OPS': [0.734],
        'RISP': [0.274],
        'PH-BA': [0.000]
    }
    df = pd.DataFrame(data)
    st.table(df)

    st.markdown("#### 최근 10경기")
    recent_games_data = {
        '일자': ['07.12', '07.11'],
        '상대': ['삼성', 'KT'],
        'AVG': [0.000, 0.500],
        'G': [5, 4],
        'PA': [5, 6],
        'AB': [4, 4],
        'R': [0, 1],
        'H': [0, 2],
        '2B': [0, 0],
        '3B': [0, 0],
        'HR': [0, 0],
        'RBI': [0, 0],
        'SB': [0, 0],
        'CS': [0, 0],
        'BB': [0, 1],
        'HBP': [1, 0],
        'SO': [1, 2],
        'GDP': [0, 0]
    }
    recent_df = pd.DataFrame(recent_games_data)
    st.table(recent_df)

    st.markdown("#### 연도별 TOP 10")
    yearly_top10_data = {
        '연도': ['2023', '2022', '2021', '2020', '2019', '2015', '2014', '2013', '2012', '2011'],
        '항목': ['3루타', '3루타', '3루타', '3루타', '3루타', '3루타', '3루타', '3루타', '3루타', '도루'],
        '기록': [11, 4, 4, 8, 5, 7, 7, 8, 7, 39],
        '순위': [1, 7, 9, 1, 10, 1, 6, 1, 2, 1]
    }
    yearly_top10_df = pd.DataFrame(yearly_top10_data)
    st.table(yearly_top10_df)
