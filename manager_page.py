from PIL import Image
import pandas as pd
import json
import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("API_KEY")

# Initialize the OpenAI client by setting the api_key attribute
client = OpenAI(api_key=api_key)

# 팀 소속 선수 데이터(NO)


# def get_player_list(team_id):
#     response = requests.get("http://localhost:3000/api/manager/get/players",
#                             json={"team_id": team_id})
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return False

# # 선수 정보 업데이트 함수(관리자/NO)


# def update_player_info(name, role, team_id):
#     response = requests.patch("http://localhost:3000/api/manager/update/player",
#                              json={"player_name": name, "position": role, "team_id": team_id})
#     if response.status_code == 200:
#         return True
#     else:
#         return False

# # 구단 정보 업데이트 함수(관리자/NO)

def update_team_info(team_profile_image, team_name, team_home_base, team_coach, team_id):
    response = requests.patch("http://localhost:3000/api/manager/update/team",
                              json={"photo": team_profile_image, "team_name": team_name, "region": team_home_base,
                                    "manager": team_coach, "team_id": team_id})
    if response.status_code == 200:
        return True
    else:
        return False

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
        "이름": ["이영희", "박민수", "최지현", "홍길동", "박병호", "이대호", "김현수", "최정", "양의지"],
        "포지션": ["포수", "1루수", "2루수", "3루수", "1루수", "지명타자", "좌익수", "3루수", "포수"],
        "타율": [0.275, 0.320, 0.290, 0.310, 0.285, 0.295, 0.305, 0.280, 0.265],
        "출루율": [0.375, 0.520, 0.390, 0.360, 0.370, 0.380, 0.410, 0.340, 0.320],
        "홈런": [5, 15, 7, 9, 25, 30, 10, 0, 20],
        "타점": [30, 60, 40, 45, 90, 100, 70, 0, 85]
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
    # team_id = st.session_state['team']

    # 임의의 야구 데이터 테이블 생성
    players_data = {
        "이름": ["이영희", "박민수", "최지현", "정수빈", "박병호", "이대호", "김현수", "최정", "양의지"],
        "포지션": ["포수", "1루수", "2루수", "3루수", "1루수", "지명타자", "좌익수", "3루수", "포수"],
        "타율": [0.275, 0.320, 0.290, 0.310, 0.285, 0.295, 0.305, 0.280, 0.265],
        "출루율": [0.375, 0.520, 0.390, 0.360, 0.370, 0.380, 0.410, 0.340, 0.320],
        "홈런": [5, 15, 7, 9, 25, 30, 10, 0, 20],
        "타점": [30, 60, 40, 45, 90, 100, 70, 0, 85]
    }

    with col1:
        st.header("선수 정보 변경")
        players_df = players_data

        # 선수 목록을 select box로 표시
        selected_player_name = st.selectbox(
            "선수를 선택하세요", players_df['이름'])
        selected_player_info = st.selectbox(
            "포지션을 선택하세요", players_df['포지션'])

        # 선택된 선수의 기본 정보를 설정
        name = selected_player_name
        role = selected_player_info

        organization = ""
        if role in ["선수", "관리자"]:
            organization = st.text_input("소속 단체", key="player_organization")

        if st.button("선수 정보 변경"):
            st.toast(":green[선수 정보 수정 성공!]")

        st.header("팀 정보 변경")
        tab1, tab2 = st.tabs(["기본 정보", "추가 정보"])

        with tab1:
            team_profile_image = st.file_uploader(
                "팀 프로필 사진 업로드", type=["png", "jpg", "jpeg"], key="team_image")
            if team_profile_image:
                st.image(Image.open(team_profile_image), caption="팀 프로필 사진")
            team_name = st.text_input("팀 이름", key="team_name")
            team_home_base = st.text_input("연고지", key="team_home_base")
            team_coach = st.text_input("감독", key="team_coach")
            if st.button("팀 정보 변경"):
                st.toast(":green[팀 정보 수정 성공!]")

        with tab2:
            st.text_area("팀 타임라인", key="team_timeline")
            st.text_area("팀 일정", key="team_schedule")
            st.text_area("소속 선수 프로필", key="team_players_profile")

    lineup_df = pd.DataFrame(players_data)

    # index를 1부터 시작하도록 변경
    lineup_df.index = lineup_df.index + 1

    # 초기화
    if 'recommend_lineup_data' not in st.session_state:
        st.session_state['recommend_lineup_data'] = pd.DataFrame()

    if 'final_lineup_data' not in st.session_state:
        st.session_state['final_lineup_data'] = pd.DataFrame()

    if 'lineup_generated' not in st.session_state:
        st.session_state['lineup_generated'] = False

    if 'lineup_saved' not in st.session_state:
        st.session_state['lineup_saved'] = False

    with col2:
        st.header("경기 등록")

        with st.form(key='match_form'):
            match_date = st.date_input("날짜")
            match_time = st.time_input("시간")
            match_place = st.text_input("장소")
            home_team_id = st.text_input("우리팀 ID")
            away_team_id = st.text_input("상대팀 ID")
            match_description = st.text_area("게임 설명")
            submit_button = st.form_submit_button(label='경기 추가')

        if submit_button:
            if match_date and match_time and match_place and home_team_id and away_team_id:
                match_info = {
                    '날짜': match_date.strftime('%Y-%m-%d'),
                    '시간': match_time.strftime('%H:%M'),
                    '장소': match_place,
                    '우리팀 ID': home_team_id,
                    '상대팀 ID': away_team_id,
                    '게임 설명': match_description
                }
                st.session_state['match_info'] = match_info
                st.toast(":green[경기 정보가 추가되었습니다.]")
            else:
                st.toast(":red[모든 필드를 작성해주세요.]")

    with col3:
        st.header("추천 라인업 테이블")

        if 'match_info' in st.session_state and st.session_state['match_info']:
            try:
                match_info = st.session_state['match_info']
                if isinstance(match_info, dict):
                    match_info = [match_info]  # 단일 매치 정보를 리스트로 변환
                match_list = [f"{match['날짜']} {match['시간']
                                               } - {match['장소']}" for match in match_info]

                # Select a specific match from the selectbox
                selected_match = st.selectbox(
                    "등록된 경기 선택",
                    match_list,
                    index=match_list.index(
                        st.session_state['selected_match']) if st.session_state['selected_match'] in match_list else 0
                )
                st.session_state['selected_match'] = selected_match

            except TypeError as e:
                st.error(f"Error processing match information: {e}")
        else:
            st.info("등록된 경기가 없습니다. 먼저 경기를 등록해주세요.")

        if st.session_state['match_info']:

            # Display basic lineup table
            basic_lineup_df = pd.DataFrame(players_data)
            basic_lineup_df.index = basic_lineup_df.index + 1
            st.dataframe(basic_lineup_df)

        if st.button("라인업 생성"):
            final_lineup = generate_lineup(players_data)
            final_lineup_df = pd.DataFrame(final_lineup)
            final_lineup_df.index = final_lineup_df.index + 1
            if not final_lineup_df.empty:
                st.session_state['recommend_lineup_data'] = final_lineup_df
                st.session_state['lineup_generated'] = True

        # Display the lineup if it has been generated
        if 'lineup_generated' in st.session_state and st.session_state['lineup_generated']:
            st.data_editor(
                st.session_state['recommend_lineup_data'], num_rows="dynamic")
            if st.button("라인업 저장"):
                # Save 로직 추가 필요
                st.session_state['lineup_saved'] = True
                st.toast(":green[라인업이 저장되었습니다.]")
                st.write("저장된 라인업:")
                st.dataframe(st.session_state['recommend_lineup_data'])
