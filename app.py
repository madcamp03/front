import requests
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


def reset_session_state():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

    st.session_state['user_data'] = {}


if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {}

    
teams = ["삼성공업고등학교", "SSG상업고등학교", "키움증권고등학교", "두산고등학교"] 


# 로그인 함수
def login(username, password):
    # response = requests.post("http://localhost:3000/api/login", json={'username': username, 'password': password})
    response = requests.post("http://35.209.111.224:3000/api/login", json={'username': username, 'password': password})
    if response.status_code == 200:
        user_data = response.json()
        print(user_data)
        reset_session_state()
        st.session_state['username'] = user_data['user_name']
        st.session_state['role'] = user_data['user_role']
        st.session_state['team'] = user_data['team_id']
        st.session_state['logged_in'] = True
        return True
    else:
        return 

      
# 회원가입 함수
def signup(username, password, role, team):
    if username not in st.session_state['user_data']:
        st.session_state['user_data'][username] = {
            'password': password, 'role': role, 'team': team}
        print(st.session_state['user_data'])
        return True
    return False


# 로그인 페이지
def login_page():
    st.title("로그인")

    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type='password')

    if st.button("로그인"):
        if login(username, password):
            st.success("로그인 성공!")
            st.experimental_rerun()
        else:
            st.error("아이디 또는 비밀번호가 잘못되었습니다.")

    if st.button("회원가입"):
        st.session_state['signup'] = True
  
  
# 회원가입 페이지
def signup_page():
    st.title("회원가입")

    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type='password')
    role = st.selectbox("역할 선택", ["guest", "선수", "관리자"])

    if role == "선수" or role == "관리자":
        if role == "관리자":
            team = st.selectbox("소속 단체 선택", teams + ["새로운 단체 만들기"])
            if team == "새로운 단체 만들기":
                team = st.text_input("새로운 단체 이름")
        else:
            team = st.selectbox("소속 단체 선택", teams)
    else:
        team = ""

    if st.button("가입"):
        if signup(username, password, role, team):
            st.success("회원가입 성공! 로그인 해주세요.")
            st.session_state['signup'] = False
        else:
            st.error("이미 존재하는 아이디입니다.")

    if st.button("로그인 화면으로 돌아가기"):
        st.session_state['signup'] = False


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

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'signup' not in st.session_state:
    st.session_state['signup'] = False

if not st.session_state['logged_in']:
    if st.session_state['signup']:
        signup_page()
    else:
        login_page()
        
else:
    with st.sidebar:
        if st.session_state['role'] == 'manager':
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
        else:
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


    # 각 메뉴에 대한 페이지 내용
    if choose == "메인":
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
            <div class="line-drawing-demo" style="display: flex; justify-content: center; align-items: center; height: 100vh;">
                <svg viewBox="0 0 1000 600" class="lines">
                    <!-- B -->
                    <path d="M10 20 L10 180 Q30 200 50 180 Q30 160 50 140 Q30 120 50 100 Q30 80 50 60 Q30 40 10 20 Z" stroke="white" fill="none" stroke-width="2"></path>
                    <!-- A -->
                    <path d="M70 180 L110 20 L150 180 M85 100 L135 100" stroke="white" fill="none" stroke-width="2"></path>
                    <!-- T -->
                    <path d="M170 20 L230 20 M200 20 L200 180" stroke="white" fill="none" stroke-width="2"></path>
                    <!-- B -->
                    <path d="M250 20 L250 180 Q270 200 290 180 Q270 160 290 140 Q270 120 290 100 Q270 80 290 60 Q270 40 250 20 Z" stroke="white" fill="none" stroke-width="2"></path>
                    <!-- A -->
                    <path d="M310 180 L350 20 L390 180 M325 100 L375 100" stroke="white" fill="none" stroke-width="2"></path>
                    <!-- T (Baseball Bat) -->
                    <path d="M410 180 L430 20 L490 20 L420 180 Z" stroke="white" fill="none" stroke-width="2"></path> <!-- Bat shape -->

                    <!-- Baseball field outline -->
                    <path d="M600 20 L880 300 A260 260 0 0 1 320 300 Z" stroke="white" fill="none" stroke-width="2"></path>
                    <path d="M600 20 L600 300" stroke="white" fill="none" stroke-width="2"></path>
                    <path d="M320 300 L880 300" stroke="white" fill="none" stroke-width="2"></path>
                    <path d="M320 300 L600 580 L880 300" stroke="white" fill="none" stroke-width="2"></path>
                    <path d="M600 580 L600 300" stroke="white" fill="none" stroke-width="2"></path>
                    
                    <!-- Bases -->
                    <circle cx="600" cy="300" r="10" fill="white"></circle> <!-- Pitcher's mound -->
                    <rect x="590" y="10" width="20" height="20" transform="rotate(45 600 20)" fill="white"></rect> <!-- Home plate -->
                    <rect x="790" y="290" width="20" height="20" transform="rotate(45 800 300)" fill="white"></rect> <!-- First base -->
                    <rect x="590" y="490" width="20" height="20" transform="rotate(45 600 500)" fill="white"></rect> <!-- Second base -->
                    <rect x="390" y="290" width="20" height="20" transform="rotate(45 400 300)" fill="white"></rect> <!-- Third base -->
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
