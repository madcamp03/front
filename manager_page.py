from PIL import Image
import pandas as pd
import json
import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("API_KEY")

# Initialize the OpenAI client by setting the api_key attribute
client = OpenAI(api_key=api_key)

# 상태 저장을 위한 함수


def initialize_session_state():
    if 'final_lineup_data' not in st.session_state:
        st.session_state['final_lineup_data'] = pd.DataFrame(
            columns=["이름", "포지션", "타율", "출루율", "홈런", "타점"])


def generate_lineup(players_data):
    prompt = f"""
    여기 야구 선수들의 데이터가 있습니다: {json.dumps(players_data, ensure_ascii=False)}.
    다음과 같은 조건으로 라인업을 만들어 주세요:
    1. 4번 타자에는 타점이 제일 높은 사람을 넣어줘.
    2. 1번 타자에는 출루율이 제일 높은 사람을 넣어줘.
    3. 1, 2번에는 출루율이 높은 사람을, 3, 4, 5번에는 타점이 높은 사람들을 넣어줘.
    라인업 형식은 다음과 같이 만들어 주세요:
    {{
        "이름": ["김철수", "이영희", "박민수", "최지현", "홍길동"],
        "포지션": ["투수", "포수", "1루수", "2루수", "3루수"],
        "타율": [0.300, 0.275, 0.320, 0.290, 0.310],
        "출루율": [0.400, 0.375, 0.520, 0.390, 0.360],
        "홈런": [10, 5, 15, 7, 9],
        "타점": [50, 30, 60, 40, 45]
    }}
    """
    pre_prompt = "한국어로 친절하게 대답해줘 :)\n\n"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system",
                "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": pre_prompt + prompt}
        ]
    )
    result = response.choices[0].message.content
    return json.loads(result)


def validate_and_send():
    df = st.session_state['final_lineup_data']
    if df.isnull().values.any() or (df == '').values.any():
        st.toast("모든 칸을 채워주세요!", icon="⚠️")
    else:
        st.toast("모든 칸이 채워졌습니다.\n 데이터를 서버로 전송합니다.", icon="✅")


def show_manager_page():
    initialize_session_state()
    st.title("관리자 페이지")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("선수 정보 변경")
        player_profile_image = st.file_uploader(
            "선수 프로필 사진 업로드", type=["png", "jpg", "jpeg"], key="player_image")
        if player_profile_image:
            st.image(Image.open(player_profile_image), caption="선수 프로필 사진")
        name = st.text_input("이름", key="player_name")
        role = st.selectbox(
            "포지션", ["투수", "포수", "1루수", "2루수", "3루수"], key="player_role")
        if role in ["선수", "관리자"]:
            organization = st.text_input("소속 단체", key="player_organization")

        st.header("팀 정보 변경")
        tab1, tab2 = st.tabs(["기본 정보", "추가 정보"])

        with tab1:
            team_profile_image = st.file_uploader(
                "팀 프로필 사진 업로드", type=["png", "jpg", "jpeg"], key="team_image")
            if team_profile_image:
                st.image(Image.open(team_profile_image), caption="팀 프로필 사진")
            team_name = st.text_input("팀 이름", key="team_name")
            team_creation_year = st.text_input(
                "창단연도", key="team_creation_year")
            team_home_base = st.text_input("연고지", key="team_home_base")
            team_coach = st.text_input("감독", key="team_coach")

        with tab2:
            st.text_area("팀 타임라인", key="team_timeline")
            st.text_area("팀 일정", key="team_schedule")
            st.text_area("소속 선수 프로필", key="team_players_profile")

    # 임의의 야구 데이터 테이블 생성
    players_data = {
        "이름": ["김철수", "이영희", "박민수", "최지현", "홍길동"],
        "포지션": ["투수", "포수", "1루수", "2루수", "3루수"],
        "타율": [0.300, 0.275, 0.320, 0.290, 0.310],
        "출루율": [0.400, 0.375, 0.520, 0.390, 0.360],
        "홈런": [10, 5, 15, 7, 9],
        "타점": [50, 30, 60, 40, 45]
    }
    lineup_df = pd.DataFrame(players_data)

    # 초기화
    if 'recommend_lineup_data' not in st.session_state:
        st.session_state['recommend_lineup_data'] = pd.DataFrame()

    if 'final_lineup_data' not in st.session_state:
        st.session_state['final_lineup_data'] = pd.DataFrame()

    with col2:
        st.header("추천 라인업 테이블")
        if st.button("라인업 생성"):
            final_lineup = generate_lineup(players_data)
            if final_lineup:
                st.session_state['recommend_lineup_data'] = pd.DataFrame(
                    final_lineup)
                st.table(st.session_state['recommend_lineup_data'])
        else:
            st.table(lineup_df)

    # 최종 라인업 데이터
    if 'final_lineup_data' not in st.session_state:
        st.session_state['final_lineup_data'] = pd.DataFrame({
            'Player': ['', '', ''],
            'Position': ['', '', ''],
            'Number': ['', '', '']
        })

    with col3:
        st.header("최종 라인업")
        edited_df = st.data_editor(
            st.session_state['final_lineup_data'])
        st.session_state['final_lineup_data'] = edited_df

        if st.button("저장"):
            validate_and_send()
