import streamlit as st
from streamlit_option_menu import option_menu

# 페이지 설정
st.set_page_config(
    page_title="My Sports App",
    page_icon="⚾",  # 흰 야구공 이모지 사용
    layout="wide",
    initial_sidebar_state="expanded",
)

# 사이드바 로고 설정
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <a href="?page=main">
            <span style="font-size: 48px;">⚾</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    choose = option_menu(
        "Menu",
        ["메인", "기록실", "오늘의 경기", "소속 팀", "마이페이지"],
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#ffffff"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#191848"},
        }
    )

from record_room import show_record_room
from today_games import show_today_games
from team_page import show_team
from my_page import show_my_page

# 선택된 메뉴에 따라 페이지 호출
if choose == "기록실":
    show_record_room()
elif choose == "오늘의 경기":
    show_today_games()
elif choose == "소속 팀":
    show_team()
elif choose == "마이페이지":
    show_my_page()

