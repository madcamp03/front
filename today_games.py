import requests
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta


team = "두산고등학교"

team_list = {
    0: "미정",
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


def get_team_id(team_name):
    for id, name in team_list.items():
        if name == team_name:
            return id
    return None


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
            "승팀": {"팀명": "두산고등학교","점수": 8, "안타": 10, "홈런": 1, "도루": 0, "삼진": 7, "병살": 1, "실책": 0},
            "패팀": {"팀명": "SSG상업고등학교", "점수": 5, "안타": 5, "홈런": 0, "도루": 0, "삼진": 7, "병살": 0, "실책": 2}
        },
        "경기 기록": {
            "승": "곽빈",
            "패": "김광현",
            "홀": "이병헌, 최지강, 이영하",
            "세": "김택연",
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
    "game_id", "날짜 및 시간", "Date", "Time", "장소", "team_away_id", "team_home_id", "memo"
]
game_info_mock_data = [
    (1, "2024-06-26 13:00", "6월 26일 (수)", "오후 13:00", "기아고등학교", 3, 1, "-"),
    (2, "2024-06-27 18:00", "6월 27일 (목)", "오후 18:00", "기아고등학교", 3, 1, "기아고등학교 2차전"),
    (3, "2024-07-17 8:00", "7월 17일 (수)", "오후 8:00", "두산고등학교", 2, 3, "-"),
    (4, "2024-07-17 11:00", "7월 17일 (수)", "오후 11:00", "두산고등학교", 5, 3, "-"),
    (5, "2024-07-19 13:00", "7월 19일 (금)", "오후 13:00", "목동야구장", 3, 10, "-"),
    (6, "2024-07-20 14:00", "7월 20일 (토)", "오후 14:00", "목동야구장", 3, 10, "키움증권고등학교 2차전"),
    (7, "2024-07-25 15:00", "7월 25일 (목)", "오후 15:00", "롯데고등학교", 3, 8, "-"),
    (8, "2024-07-29 15:00", "7월 29일 (월)", "오후 15:00", "두산고등학교", 4, 3, "-"),
]


def map_team(id):
    return team_list[id]

def transform_game_result_to_mock_data(game_result):
    game_id = game_result['game_id']
    game_record = {
        game_id: {
            "팀 기록": {
                "승팀": {
                    "팀명": team_list[game_result['winner_team_id']],  # 팀명을 데이터베이스에서 추가로 가져와야 합니다.
                    "점수": game_result['winner_team_total_score'],
                    "안타": game_result['winner_team_total_hits'],
                    "홈런": game_result['winner_team_total_home_runs'],
                    "도루": game_result['winner_team_total_stolen_bases'],
                    "삼진": game_result['winner_team_total_strikeouts'],
                    "병살": game_result['winner_team_total_double_plays'],
                    "실책": game_result['winner_team_total_errors'],
                },
                "패팀": {
                    "팀명": team_list[game_result['loser_team_id']],  # 팀명을 데이터베이스에서 추가로 가져와야 합니다.
                    "점수": game_result['loser_team_total_score'],
                    "안타": game_result['loser_team_total_hits'],
                    "홈런": game_result['loser_team_total_home_runs'],
                    "도루": game_result['loser_team_total_stolen_bases'],
                    "삼진": game_result['loser_team_total_strikeouts'],
                    "병살": game_result['loser_team_total_double_plays'],
                    "실책": game_result['loser_team_total_errors'],
                }
            },
            "경기 기록": {
                "승": game_result['winning_pitcher_id'],  # 선수 이름을 데이터베이스에서 추가로 가져와야 합니다.
                "패": game_result['losing_pitcher_id'],  # 선수 이름을 데이터베이스에서 추가로 가져와야 합니다.
                "홀": game_result['hold_pitcher_ids'],  # 선수 이름을 데이터베이스에서 추가로 가져와야 합니다.
                "세": game_result['save_pitcher_id'],  # 선수 이름을 데이터베이스에서 추가로 가져와야 합니다.
                "결승타": game_result['deciding_hit'],
                "홈런": game_result['home_run'],
                "2루타": game_result['hit_base2'],
                "3루타": game_result['hit_base3'],
                "실책": game_result['game_error'],
                "주루사": game_result['base_running_out'],
                "병살타": game_result['double_play_hit'],
            }
        }
    }
    return game_record

def show_game_results(game_id):
    # result = result_mock_data.get(game_id, {})
    # if not result:
    #     st.write("경기 결과가 없습니다.")
    #     return
    
    response = requests.post("http://localhost:3000/api/game/result", json={'game_id': game_id})
    game_result = response.json()
    result = transform_game_result_to_mock_data(game_result).get(game_id)
    team_record = result.get("팀 기록", {})
    game_record = result.get("경기 기록", {})

    st.subheader("팀 기록")
    team_df = pd.DataFrame.from_dict(
        team_record, orient='index').reset_index().rename(columns={'index': '구분'})


    if st.session_state.get('role') == 'manager':
        edited_team_df = st.data_editor(team_df, use_container_width=True, key=f"{game_id} team_record")
        st.subheader("경기 기록")
        for key, value in game_record.items():
            value = st.text_input(f"{key}", value, key=f'{game_id} {key}')
            game_record[key] = value
            st.write(f"**{key}**: {value}")
        
        if st.button('경기 기록 저장', key=f"save_button_{game_id}"):
            updated_data = {
                "game_id": game_id,
                "winner_team_id": get_team_id(edited_team_df.at[0, '팀명']),
                "loser_team_id": get_team_id(edited_team_df.at[1, '팀명']),
                "winner_team_total_score": int(edited_team_df.at[0, '점수']),
                "winner_team_total_hits": int(edited_team_df.at[0, '안타']),
                "winner_team_total_home_runs": int(edited_team_df.at[0, '홈런']),
                "winner_team_total_stolen_bases": int(edited_team_df.at[0, '도루']),
                "winner_team_total_strikeouts": int(edited_team_df.at[0, '삼진']),
                "winner_team_total_double_plays": int(edited_team_df.at[0, '병살']),
                "winner_team_total_errors": int(edited_team_df.at[0,'실책']),
                "loser_team_total_score": int(edited_team_df.at[1, '점수']),
                "loser_team_total_hits": int(edited_team_df.at[1, '안타']),
                "loser_team_total_home_runs": int(edited_team_df.at[1, '홈런']),
                "loser_team_total_stolen_bases": int(edited_team_df.at[1, '도루']),
                "loser_team_total_strikeouts": int(edited_team_df.at[1, '삼진']),
                "loser_team_total_double_plays": int(edited_team_df.at[1, '병살']),
                "loser_team_total_errors": int(edited_team_df.at[1, '실책']),
                "winning_pitcher_id": game_record['승'],
                "losing_pitcher_id": game_record['패'],
                "hold_pitcher_ids": game_record['홀'],
                "save_pitcher_id": game_record['세'],
                "deciding_hit": game_record['결승타'],
                "home_run": game_record['홈런'],
                "hit_base2": game_record['2루타'],
                "hit_base3": game_record['3루타'],
                "game_error": game_record['실책'],
                "base_running_out": game_record['주루사'],
                "double_play_hit": game_record['병살타']
            }

            # Send the updated data to the backend
            patch_response = requests.patch("http://localhost:3000/api/results/update", json=updated_data)
            if patch_response.status_code == 200:
                st.success("Game result updated successfully!")
            else:
                st.error("Failed to update game result.")
    

    else:
        st.dataframe(team_df)
        st.subheader("경기 기록")
        for key, value in game_record.items():
            st.write(f"**{key}**: {value}")

    # st.subheader("경기 기록")
    # for key, value in game_record.items():
    #     if st.session_state.get('role') == 'manager':
    #         value = st.text_input(f"{game_id} {key}", value)
    #         game_record[key] = value
    #     st.write(f"**{key}**: {value}")


def show_today_games():
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("오늘의 경기")

        today_games_initial_df = pd.DataFrame(
            game_info_mock_data, columns=game_info_columns)

        now = pd.Timestamp.now()

        # 오늘 기준 지난 경기 제외, 이번 달 경기만 경기 일정에 포함

        today_games_df = today_games_initial_df.drop(['game_id'], axis=1)

        today_games_df['날짜 및 시간'] = pd.to_datetime(today_games_df['날짜 및 시간'])
        today_games_df = today_games_df[
            (today_games_df['날짜 및 시간'] >= now) &
            (today_games_df['날짜 및 시간'].dt.month == now.month)
        ]

        today_games_df['team_away_id'] = today_games_df['team_away_id'].map(
            map_team)
        today_games_df['team_home_id'] = today_games_df['team_home_id'].map(
            map_team)

        today_games_df.rename(columns={'team_away_id': '원정 팀'}, inplace=True)
        today_games_df.rename(columns={'team_home_id': '홈 팀'}, inplace=True)

        today_games_final_df = today_games_df.drop(['Date', 'Time'], axis=1)

        st.subheader(team + " 경기 일정")

        column_config = {
            "날짜 및 시간": st.column_config.Column(width=150),
            "장소": st.column_config.Column(width=150),
            "원정 팀": st.column_config.Column(width=150),
            "홈 팀": st.column_config.Column(width=150),
            "memo": st.column_config.Column(width=400)  # memo 열의 너비를 300으로 설정
        }

        st.dataframe(today_games_final_df, hide_index=True,
                     column_config=column_config, use_container_width=True)

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
        today_games = today_games_initial_df[today_games_initial_df['날짜 및 시간'].str.startswith(
            today)]

        if not today_games.empty:

            st.subheader(f"오늘의 경기")
            for _, game in today_games.iterrows():

                game_time = datetime.strptime(
                    game['날짜 및 시간'], '%Y-%m-%d %H:%M')
                with st.expander(f"vs {team_list[game['team_away_id']]}"):

                    tabs = st.tabs(["라인업", "경기 결과"])
                    with tabs[0]:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"{team_list[game['team_home_id']]} 라인업")
                            for key, player in lineup_mock_data[game['game_id']][team_list[game['team_home_id']]].items():
                                if isinstance(player, dict):
                                    st.write(
                                        f"{key}: {player['name']} ({player['position']})")
                                else:
                                    st.write(f"{key}: {player}")
                        with col2:
                            st.write(f"{team_list[game['team_away_id']]} 라인업")
                            for key, player in lineup_mock_data[game['game_id']][team_list[game['team_away_id']]].items():
                                if isinstance(player, dict):
                                    st.write(
                                        f"{key}: {player['name']} ({player['position']})")
                                else:
                                    st.write(f"{key}: {player}")

                    with tabs[1]:
                        if now < game_time:
                            st.write("경기 시작 전입니다")
                        elif now > game_time + timedelta(hours=4):
                            show_game_results(game['game_id'])
                        else:
                            st.write("경기 진행 중입니다")
        else:
            st.write("오늘 경기가 없습니다.")

        # Load image
        image_path = "assets/bears.jpg"

        games_df = today_games_df.drop(['날짜 및 시간', '장소', 'memo'], axis=1)

        st.markdown("<br>", unsafe_allow_html=True)
        # Layout the games in a table-like format
        st.subheader("다음 경기 일정")
        for date in games_df["Date"].unique():
            st.markdown(f"---\n### {date}")

            day_games = games_df[games_df["Date"] == date]

            for idx, game in day_games.iterrows():
                col1, col2, col3 = st.columns([1, 1, 1])

                with col1:
                    st.image(image_path, width=50)
                    st.markdown(f"**{game['원정 팀']}**")

                with col2:
                    st.markdown(f"{game['Time']}")

                with col3:
                    st.image(image_path, width=50)
                    st.markdown(f"**{game['홈 팀']}**")

    # with col2:
    #     st.subheader("가상의 야구 선수 라인업 데이터")
    #     # 가상의 선수 데이터 생성
    #     fictional_lineup_data = {
    #         "Position": ["P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF"],
    #         "Name": ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8", "Player9"]
    #     }

    #     fictional_lineup_df = pd.DataFrame(fictional_lineup_data)
    #     st.table(fictional_lineup_df)
