import streamlit as st
from streamlit_option_menu import option_menu
from record_room import show_record_room
from today_games import show_today_games
from team_page import show_team
from my_page import show_my_page
from manager_page import show_manager_page

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
        ["메인", "기록실", "오늘의 경기", "소속 팀", "마이페이지", "관리페이지"],
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#ffffff"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#191848"},
        }
    )

# 각 메뉴에 대한 페이지 내용
if choose == "메인":
    st.write("메인 페이지 내용")
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Anime.js Animations</title>
        <style>
            body {
                background-color: #00205b;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .line-drawing-demo {
                width: 600px;
                height: 200px;
                margin: 20px;
            }
            .line-drawing-demo .lines path {
                fill: transparent;
                stroke: white;
                stroke-width: 2;
            }
        </style>
    </head>
    <body>
        <div class="line-drawing-demo">
            <svg viewBox="0 0 600 200" class="lines">
                <!-- B -->
                <path d="M10 20 L10 180 Q30 200 50 180 Q30 160 50 140 Q30 120 50 100 Q30 80 50 60 Q30 40 10 20 Z"></path>
                <!-- A -->
                <path d="M70 180 L110 20 L150 180 M85 100 L135 100"></path>
                <!-- T -->
                <path d="M170 20 L230 20 M200 20 L200 180"></path>
                <!-- B -->
                <path d="M250 20 L250 180 Q270 200 290 180 Q270 160 290 140 Q270 120 290 100 Q270 80 290 60 Q270 40 250 20 Z"></path>
                <!-- A -->
                <path d="M310 180 L350 20 L390 180 M325 100 L375 100"></path>
                <!-- T (Baseball Bat) -->
                <path d="M410 180 L430 20 L490 20 L420 180 Z"></path> <!-- Bat shape -->
            </svg>
        </div>

        <!-- Anime.js Library -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
        <script>
            anime({
                targets: '.line-drawing-demo .lines path',
                strokeDashoffset: [anime.setDashoffset, 0],
                easing: 'easeInOutSine',
                duration: 1500,
                delay: function(el, i) { return i * 250 },
                direction: 'alternate',
                loop: true
            });
        </script>
    </body>
    </html>
    """

    # Streamlit에서 HTML과 JavaScript 코드 실행
    st.components.v1.html(html_code, height=600, scrolling=False)
elif choose == "기록실":
    show_record_room()
elif choose == "오늘의 경기":
    show_today_games()
elif choose == "소속 팀":
    show_team()
elif choose == "마이페이지":
    show_my_page()
elif choose == "관리페이지":
    show_manager_page()
