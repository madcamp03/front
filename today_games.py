import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

    
team = "두산고등학교"

team_list = {
    1: "기아고등학교",
    2: "삼성공업고등학교",
    3: "두산고등학교",
    4: "엘지디지털고등학교",
    5: "SSG상업고등학교",
    6: "NC특성화고등학교",
    7: "KT인터넷고등학교",
    8: "롯데고등학교",
    9: "한화고등학교",
    10: "키움증권고등학교"
}

lineup_mock_data = {
    3: {
        "삼성공업고등학교": {
            "선발투수": "원태인",
            "1번 타자": {
                "player_id": 21,
                "name": "김지찬",
                "position": "CF"
            },
            "2번 타자": {
                "player_id": 22,
                "name": "이재현",
                "position": "SS"
            },
            "3번 타자": {
                "player_id": 23,
                "name": "구자욱",
                "position": "LF"
            },
            "4번 타자": {
                "player_id": 24,
                "name": "박병호",
                "position": "1B"
            },
            "5번 타자": {
                "player_id": 25,
                "name": "강민호",
                "position": "C"
            },
            "6번 타자": {
                "player_id": 26,
                "name": "이성규",
                "position": "DH"
            },
            "7번 타자": {
                "player_id": 27,
                "name": "윤정빈",
                "position": "RF"
            },
            "8번 타자": {
                "player_id": 28,
                "name": "류지혁",
                "position": "2B"
            },
            "9번 타자": {
                "player_id": 29,
                "name": "전병우",
                "position": "3B"
            },
        },
        "두산고등학교": {
            "선발투수": "곽빈",
            "1번 타자": {
                "player_id": 31,
                "name": "정수빈",
                "position": "CF"
            },
            "2번 타자": {
                "player_id": 32,
                "name": "허경민",
                "position": "3B"
            },
            "3번 타자": {
                "player_id": 33,
                "name": "양의지",
                "position": "C"
            },
            "4번 타자": {
                "player_id": 34,
                "name": "김재환",
                "position": "DH"
            },
            "5번 타자": {
                "player_id": 35,
                "name": "양석환",
                "position": "1B"
            },
            "6번 타자": {
                "player_id": 36,
                "name": "강승호",
                "position": "2B"
            },
            "7번 타자": {
                "player_id": 37,
                "name": "라모스",
                "position": "RF"
            },
            "8번 타자": {
                "player_id": 38,
                "name": "이유찬",
                "position": "SS"
            },
            "9번 타자": {
                "player_id": 39,
                "name": "조수행",
                "position": "LF"
            },
        }
    },
    4: {
        "SSG상업고등학교": {
            "선발투수": "김광현",
            "1번 타자": {
                "player_id": 51,
                "name": "최지훈",
                "position": "CF"
            },
            "2번 타자": {
                "player_id": 52,
                "name": "추신수",
                "position": "DH"
            },
            "3번 타자": {
                "player_id": 53,
                "name": "최정",
                "position": "3B"
            },
            "4번 타자": {
                "player_id": 54,
                "name": "에레디아",
                "position": "LF"
            },
            "5번 타자": {
                "player_id": 55,
                "name": "한유섬",
                "position": "RF"
            },
            "6번 타자": {
                "player_id": 56,
                "name": "박성한",
                "position": "SS"
            },
            "7번 타자": {
                "player_id": 57,
                "name": "박지환",
                "position": "2B"
            },
            "8번 타자": {
                "player_id": 58,
                "name": "이지영",
                "position": "C"
            },
            "9번 타자": {
                "player_id": 59,
                "name": "고명준",
                "position": "1B"
            },
        },
        "두산고등학교": {
            "선발투수": "곽빈",
            "1번 타자": {
                "player_id": 31,
                "name": "정수빈",
                "position": "CF"
            },
            "2번 타자": {
                "player_id": 32,
                "name": "허경민",
                "position": "3B"
            },
            "3번 타자": {
                "player_id": 33,
                "name": "양의지",
                "position": "C"
            },
            "4번 타자": {
                "player_id": 34,
                "name": "김재환",
                "position": "DH"
            },
            "5번 타자": {
                "player_id": 35,
                "name": "양석환",
                "position": "1B"
            },
            "6번 타자": {
                "player_id": 36,
                "name": "강승호",
                "position": "2B"
            },
            "7번 타자": {
                "player_id": 37,
                "name": "라모스",
                "position": "RF"
            },
            "8번 타자": {
                "player_id": 38,
                "name": "이유찬",
                "position": "SS"
            },
            "9번 타자": {
                "player_id": 39,
                "name": "조수행",
                "position": "LF"
            },
        }
    }
}

result_mock_data = {
    4: {
        "팀 기록": {
            "SSG": {"안타": 5, "홈런": 0, "도루": 0, "삼진": 7, "병살": 0, "실책": 2},
            "두산": {"안타": 10, "홈런": 1, "도루": 0, "삼진": 7, "병살": 1, "실책": 0}
        },
        "경기 기록": {
            "결승타": "허경민(1회 무사 1루서 좌월 홈런)",
            "홈런": "허경민 5호(1회 2점 김광현)",
            "2루타": "김재환(4회), 양석환(4회), 양의지(5회), 전다민(8회)",
            "실책": "박성한(5회), 한유섬(8회)",
            "주루사": "추신수(6회)",
            "병살타": "양석환(5회)",
            "포일": "김민식(7회)"
        }
    }
}

game_info_columns = [
    "game_id", "날짜 및 시간", "장소", "team_away_id", "team_home_id", "memo"
]
game_info_mock_data = [
    (1, "2024-06-26 13:00", "기아고등학교", 3, 1, "-"),
    (2, "2024-06-27 18:00", "기아고등학교", 3, 1, "기아고등학교 2차전"),
    (3, "2024-07-14 13:00", "두산고등학교", 2, 3, "-"),
    (4, "2024-07-15 1:00", "두산고등학교", 5, 3, "-"),
    (5, "2024-07-19 13:00", "목동야구장", 3, 10, "-"),
    (6, "2024-07-20 14:00", "목동야구장", 3, 10, "키움증권고등학교 2차전"),
    (7, "2024-07-25 15:00", "롯데고등학교", 3, 8, "-"),
    (8, "2024-07-29 15:00", "두산고등학교", 4, 3, "-"),
]

def map_team(id):
    return team_list[id]


def show_game_results(game_id):
    result = result_mock_data.get(game_id, {})
    if not result:
        st.write("경기 결과가 없습니다.")
        return

    team_record = result.get("팀 기록", {})
    game_record = result.get("경기 기록", {})

    st.subheader("팀 기록")
    team_df = pd.DataFrame.from_dict(team_record, orient='index').reset_index().rename(columns={'index': '구분'})
    st.dataframe(team_df)

    st.subheader("경기 기록")
    for key, value in game_record.items():
        st.write(f"**{key}**: {value}")


def show_today_games():
    st.title("오늘의 경기")

    today_games_initial_df = pd.DataFrame(game_info_mock_data, columns=game_info_columns)

    now = pd.Timestamp.now()

    # 오늘 기준 지난 경기 제외, 이번 달 경기만 경기 일정에 포함

    today_games_df = today_games_initial_df.drop(['game_id'], axis=1)

    today_games_df['날짜 및 시간'] = pd.to_datetime(today_games_df['날짜 및 시간'])
    today_games_df = today_games_df[
        (today_games_df['날짜 및 시간'] >= now) & 
        (today_games_df['날짜 및 시간'].dt.month == now.month)
    ]


    today_games_df['team_away_id'] = today_games_df['team_away_id'].map(map_team)
    today_games_df['team_home_id'] = today_games_df['team_home_id'].map(map_team)

    today_games_df.rename(columns={'team_away_id': '원정 팀'}, inplace=True)
    today_games_df.rename(columns={'team_home_id': '홈 팀'}, inplace=True)
    
    st.subheader(team+ " 경기 일정")
    
    column_config = {
        "날짜 및 시간": st.column_config.Column(width=150),
        "장소": st.column_config.Column(width=150),
        "원정 팀": st.column_config.Column(width=150),
        "홈 팀": st.column_config.Column(width=150),
        "memo": st.column_config.Column(width=400)  # memo 열의 너비를 300으로 설정
    }

    st.dataframe(today_games_df, hide_index=True, column_config=column_config, use_container_width=True)

    st.markdown(
        """
        <style>
        div[data-baseweb="tab-border"][role="presentation"] {
            background-color: #131230;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 오늘의 경기 표시

    today = datetime.today().strftime('%Y-%m-%d')
    today_games = today_games_initial_df[today_games_initial_df['날짜 및 시간'].str.startswith(today)]
    

    if not today_games.empty:

        st.subheader(f"오늘의 경기")
        for _, game in today_games.iterrows():
            
            game_time = datetime.strptime(game['날짜 및 시간'], '%Y-%m-%d %H:%M')
            with st.expander(f"vs {team_list[game['team_away_id']]}"):

                tabs = st.tabs(["라인업", "경기 결과"])
                with tabs[0]:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"{team_list[game['team_home_id']]} 라인업")
                        for key, player in lineup_mock_data[game['game_id']][team_list[game['team_home_id']]].items():
                            if isinstance(player, dict):
                                st.write(f"{key}: {player['name']} ({player['position']})")
                            else:
                                st.write(f"{key}: {player}")
                    with col2:
                        st.write(f"{team_list[game['team_away_id']]} 라인업")
                        for key, player in lineup_mock_data[game['game_id']][team_list[game['team_away_id']]].items():
                            if isinstance(player, dict):
                                st.write(f"{key}: {player['name']} ({player['position']})")
                            else:
                                st.write(f"{key}: {player}")
                
                with tabs[1]:
                    if now < game_time:
                        st.write("경기 시작 전입니다")
                    # elif now > game_time + timedelta(hours=4):
                    elif now > game_time + timedelta(minutes=4): # test code
                        show_game_results(game['game_id'])
                    else:
                        st.write("경기 진행 중입니다")
    else:
        st.write("오늘 경기가 없습니다.")