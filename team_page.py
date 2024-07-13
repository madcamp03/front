# team_page
import streamlit as st
import pandas as pd
from streamlit_timeline import timeline


def show_team():
    # Load custom font
    st.markdown(
        """
        <style>
        @font-face {
            font-family: 'KBO_bold';
            src: url('assets/KBO_bold.otf') format('opentype');
        }
        .title {
            font-family: 'KBO_bold', sans-serif;
            font-size: 2em;
            margin-bottom: 10px;
        }
        .card {
            border: 2px solid #6C7A89;
            padding: 10px;
            margin: 10px;
            border-radius: 5px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            text-align: center;
            background-color: #131230;
            color: white;
            cursor: pointer;
        }
        .card-content {
            padding: 10px;
        }
        .card-title {
            font-size: 1.5em;
            margin-bottom: 10px;
            font-weight: bold;
        }
        .timeline-container {
            margin-top: -50px;
            background-color: #f7f7f7;
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Title with custom font
    st.markdown('<p class="title">소속 팀</p>', unsafe_allow_html=True)

    # Define columns for layout
    col1, col2 = st.columns([1, 2])

    # Add image to the first column
    with col1:
        st.image('assets/bears.jpg', caption='DOOSAN BEARS', width=200)

    # Create a DataFrame with the specified rows and set the index
    data = {
        "정보": ["두산 베어스", "1982", "서울", "박정원", "김태형"]
    }
    df = pd.DataFrame(data, index=["팀명", "창단연도", "연고지", "구단주", "감독"])

    # Convert all columns to string to avoid Arrow serialization issues
    df = df.astype(str)

    # Add table to the second column
    with col2:
        st.table(df.style.hide(axis="columns"))

    # Timeline section
    st.markdown('<p class="title">팀 타임라인</p>', unsafe_allow_html=True)

    timeline_data = {
        "events": [
            {
                "start_date": {"year": "1982"},
                "text": {"headline": "창단", "text": "두산 베어스 팀이 창단되었습니다."}
            },
            {
                "start_date": {"year": "1986"},
                "text": {"headline": "첫 번째 우승", "text": "두산 베어스가 첫 번째 우승을 차지했습니다."}
            },
            {
                "start_date": {"year": "1995"},
                "text": {"headline": "두 번째 우승", "text": "두산 베어스가 두 번째 우승을 차지했습니다."}
            },
            {
                "start_date": {"year": "2001"},
                "text": {"headline": "세 번째 우승", "text": "두산 베어스가 세 번째 우승을 차지했습니다."}
            },
            {
                "start_date": {"year": "2005"},
                "text": {"headline": "네 번째 우승", "text": "두산 베어스가 네 번째 우승을 차지했습니다."}
            },
            {
                "start_date": {"year": "2010"},
                "text": {"headline": "다섯 번째 우승", "text": "두산 베어스가 다섯 번째 우승을 차지했습니다."}
            },
            {
                "start_date": {"year": "2015"},
                "text": {"headline": "여섯 번째 우승", "text": "두산 베어스가 여섯 번째 우승을 차지했습니다."}
            },
            {
                "start_date": {"year": "2019"},
                "text": {"headline": "일곱 번째 우승", "text": "두산 베어스가 일곱 번째 우승을 차지했습니다."}
            }
        ]
    }

    timeline(timeline_data, height=600)

    st.markdown('</div>', unsafe_allow_html=True)

    # Tabs section
    st.markdown('<p class="title">팀 일정</p>', unsafe_allow_html=True)
    tabs = st.tabs(["경기 일정", "훈련 일정", "이벤트 일정"])

    with tabs[0]:
        st.markdown("### 경기 일정")
        schedule_data = {
            "날짜": ["2024-07-15", "2024-07-18", "2024-07-20"],
            "상대 팀": ["LG 트윈스", "롯데 자이언츠", "삼성 라이온즈"],
            "장소": ["잠실", "사직", "대구"]
        }
        schedule_df = pd.DataFrame(schedule_data)
        st.table(schedule_df)

    with tabs[1]:
        st.markdown("### 훈련 일정")
        training_data = {
            "날짜": ["2024-07-16", "2024-07-19", "2024-07-21"],
            "훈련 내용": ["수비 훈련", "타격 훈련", "전술 훈련"],
            "장소": ["잠실", "잠실", "잠실"]
        }
        training_df = pd.DataFrame(training_data)
        st.table(training_df)

    with tabs[2]:
        st.markdown("### 이벤트 일정")
        event_data = {
            "날짜": ["2024-07-17", "2024-07-22", "2024-07-25"],
            "이벤트": ["팬 사인회", "사회 공헌 행사", "출정식"],
            "장소": ["잠실", "서울", "잠실"]
        }
        event_df = pd.DataFrame(event_data)
        st.table(event_df)

    st.markdown('<p class="title">소속 선수 프로필</p>', unsafe_allow_html=True)

    # Player profiles data
    players = [
        {"name": "이승엽", "number": 36, "birthdate": "1976-08-18", "position": "1루수"},
        {"name": "박찬호", "number": 61, "birthdate": "1973-07-28", "position": "투수"},
        {"name": "손아섭", "number": 31, "birthdate": "1988-03-18", "position": "외야수"},
        {"name": "김광현", "number": 29, "birthdate": "1988-07-22", "position": "투수"},
        {"name": "강정호", "number": 16, "birthdate": "1987-04-05", "position": "유격수"},
        {"name": "최정", "number": 14, "birthdate": "1987-02-28", "position": "3루수"}
    ]

    # Display player profiles in 3 columns per row
    for i in range(0, len(players), 3):
        cols = st.columns(3)
        for col, player in zip(cols, players[i:i+3]):
            with col:
                st.markdown(
                    f"""
                    <div class="card">
                        <div class="card-content">
                            <p class="card-title">{player['name']}</p>
                            <p><strong>등번호:</strong> {player['number']}</p>
                            <p><strong>생년월일:</strong> {player['birthdate']}</p>
                            <p><strong>포지션:</strong> {player['position']}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                with st.expander(f"{player['name']} 2024 시즌 기록"):

                    if player['position'] == '투수':
                        stats_data = {
                            "평균자책(ERA)": ["3.50"],
                            "승": ["10"],
                            "패": ["5"],
                            "세이브(SV)": ["20"],
                            "홀드(HLD)": ["15"]
                        }
                    else:
                        stats_data = {
                            "타율(AVG)": [".300"],
                            "출루율(OBP)": [".380"],
                            "장타율(SLG)": [".450"],
                            "OPS": [".830"]
                        }
                    stats_df = pd.DataFrame(stats_data)

                    st.table(stats_df)

# Main logic for team_page.py
# if 'selected_player' in st.session_state:
#     show_player(st.session_state['selected_player'])
