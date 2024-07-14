import streamlit as st
import pandas as pd


def get_session_state():
    if 'hitter_search_text' not in st.session_state:
        st.session_state['hitter_search_text'] = ''
    if 'pitcher_search_text' not in st.session_state:
        st.session_state['pitcher_search_text'] = ''


def reset_search_text():
    st.session_state['hitter_search_text'] = ''
    st.session_state['pitcher_search_text'] = ''


def get_match_score(name, query):
    score = 0
    if name.startswith(query):
        score += 3
    elif query in name:
        score += 1
    return score


def show_record_room():
    st.title("기록실")

    get_session_state()

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

    hitter_mock_data = [
        (1, 1, '도슨', 10, '키움증권고등학교', 2024, 80, 0.363, 0.56, 0.427, 0.987, 363, 325, 64, 118, 30, 2, 10, 48, 0, 1, 32, 47, 0.333, 2, 50),
        (2, 2, '에레디아', 5, 'SGG상업고등학교', 2024, 79, 0.36, 0.5, 0.397, 0.897, 343, 314, 43, 113, 15, 1, 9, 62, 0, 6, 15, 42, 0.417, 3, 50),
        (3, 3, '박건우', 6, 'NC특성화고등학교', 2024, 79, 0.354, 0.546, 0.415, 0.961, 325, 291, 52, 103, 21, 1, 11, 46, 0, 2, 30, 49, 0.372, 3, 100),
        (4, 4, '레이예스', 8, '롯데고등학교', 2024, 83, 0.352, 0.498, 0.392, 0.89, 360, 327, 47, 115, 23, 2, 7, 69, 0, 7, 25, 50, 0.411, 4, 100),
        (5, 5, '허경민', 3, '두산고등학교', 2024, 73, 0.348, 0.481, 0.412, 0.893, 301, 264, 49, 92, 17, 0, 6, 42, 0, 5, 21, 17, 0.317, 3, 100),
        (6, 6, '송성문', 10, '키움증권고등학교', 2024, 82, 0.345, 0.507, 0.413, 0.92, 329, 284, 41, 98, 13, 3, 9, 58, 0, 7, 37, 33, 0.364, 7, 100),
        (7, 7, '양의지', 3, '두산고등학교', 2024, 77, 0.342, 0.507, 0.389, 0.896, 324, 292, 38, 100, 12, 0, 12, 73, 0, 6, 21, 32, 0.448, 2, 100),
        (8, 8, '김도영', 1, '기아고등학교', 2024, 84, 0.339, 0.613, 0.407, 1.02, 379, 333, 84, 113, 14, 4, 23, 61, 1, 4, 38, 65, 0.318, 27, 90),
        (9, 9, '김혜성', 10, '키움증권고등학교', 2024, 76, 0.338, 0.518, 0.402, 0.92, 343, 305, 56, 103, 19, 3, 10, 50, 0, 3, 31, 28, 0.392, 20, 83.3),
        (10, 10, '박민우', 6, 'NC특성화고등학교', 2024, 68, 0.326, 0.455, 0.419, 0.874, 311, 264, 43, 86, 15, 2, 5, 23, 3, 1, 35, 46, 0.238, 22, 81.5),
        (11, 11, '문성주', 4, '엘지디지털고등학교', 2024, 81, 0.324, 0.401, 0.427, 0.828, 315, 262, 41, 85, 16, 2, 0, 44, 1, 3, 47, 32, 0.408, 13, 65),
        (12, 12, '로하스', 7, 'KT부설인터넷고등학교', 2024, 87, 0.324, 0.571, 0.426, 0.997, 406, 343, 66, 111, 22, 0, 21, 70, 0, 1, 56, 76, 0.313, 0, 0),
        (13, 13, '이우성', 1, '기아고등학교', 2024, 75, 0.317, 0.45, 0.392, 0.842, 314, 278, 47, 88, 11, 1, 8, 46, 0, 1, 33, 59, 0.321, 6, 85.7),
        (14, 14, '홍창기', 4, '엘지디지털고등학교', 2024, 85, 0.316, 0.389, 0.434, 0.823, 386, 316, 56, 100, 5, 3, 4, 43, 1, 2, 60, 56, 0.357, 8, 47.1),
        (15, 15, '라모스', 3, '두산고등학교', 2024, 73, 0.316, 0.493, 0.37, 0.863, 317, 282, 40, 89, 17, 3, 9, 46, 1, 6, 26, 51, 0.279, 3, 50),
        (16, 16, '구자욱', 2, '삼성공업고등학교', 2024, 84, 0.313, 0.569, 0.377, 0.946, 371, 332, 56, 104, 26, 1, 19, 67, 0, 3, 28, 51, 0.303, 7, 63.6),
        (17, 17, '강백호', 7, 'KT부설인터넷고등학교', 2024, 87, 0.309, 0.546, 0.371, 0.917, 388, 350, 63, 108, 17, 0, 22, 67, 0, 2, 35, 77, 0.25, 5, 71.4),
        (18, 18, '김태연', 9, '한화고등학교', 2024, 71, 0.308, 0.48, 0.393, 0.873, 264, 227, 34, 70, 15, 0, 8, 40, 2, 2, 30, 47, 0.321, 3, 60),
        (19, 19, '페라자', 9, '한화고등학교', 2024, 68, 0.308, 0.574, 0.391, 0.965, 302, 263, 50, 81, 19, 0, 17, 52, 0, 2, 36, 68, 0.359, 7, 63.6),
        (20, 20, '박성한', 5, 'SGG상업고등학교', 2024, 85, 0.301, 0.401, 0.38, 0.781, 366, 319, 53,	96,	17,	0, 5, 41, 3, 2, 41, 49, 0.292, 9, 81.8),
    ]

    hitter_columns = [
        "record_id", "player_id", "Name", "team_id", "Team", "Season", "Games", "AVG", "SLG", "OBP", "OPS", "PA", "AB", "R", "H", 
        "2B", "3B", "HR", "RBI", "SAC", "SF", "BB", "SO", "RISP", "SB", "SB%"
    ]

    hitter_initial_df = pd.DataFrame(hitter_mock_data, columns=hitter_columns)
    hitter_df = hitter_initial_df.drop(['record_id', 'player_id', 'team_id'], axis=1)
    hitter_df = hitter_df.sort_values(by='AVG', ascending=False)
    
    hitter_df['SB%'] = hitter_df['SB%'].astype(str) + '%'
    hitter_df['Season'] = hitter_df['Season'].astype(int)
    
    hitter_df['AVG'] = hitter_df['AVG'].round(3)
    hitter_df['SLG'] = hitter_df['SLG'].round(3)
    hitter_df['OBP'] = hitter_df['OBP'].round(3)
    hitter_df['OPS'] = hitter_df['OPS'].round(3)
    hitter_df['RISP'] = hitter_df['RISP'].round(3)

    new_order = ["Name", "Team", "Season", "AVG", "Games", "SLG", "OBP", "OPS", "PA", "AB", "R", "H", 
                 "2B", "3B", "HR", "RBI", "SAC", "SF", "BB", "SO", "RISP", "SB", "SB%"]
    hitter_df = hitter_df[new_order]

    pitcher_mock_data = [
        (1, 1, '하트', 6, 'NC특성화고등학교', 2024, 2.74, 17, 7, 2, 0, 0, '105', 0.778, 92, 6, 24, 4, 111, 36, 32, 1.1),
        (2, 2, '네일', 1, '기아고등학교', 2024, 2.86, 18, 8, 2, 0, 0, '107', 0.8, 105, 9, 22, 7, 107, 51, 34, 1.19),
        (3, 3, '헤이수스', 10, '키움증권고등학교', 2024, 3.14, 18, 10, 5, 0, 0, '103 1/3', 0.667, 91, 10, 28, 8, 107, 42, 36, 1.15),
        (4, 4, '원태인', 2, '삼성공업고등학교', 2024, 3.16, 16, 7, 4, 0, 0, '91', 0.636, 82, 8, 31, 4, 70, 35, 32, 1.24),
        (5, 5, '후라도', 10, '키움증권고등학교', 2024, 3.36, 18, 8, 4, 0, 0, '112 1/3', 0.667, 116, 11, 21, 4, 97, 44, 42, 1.22),
        (6, 6, '곽빈', 3, '두산고등학교', 2024, 3.59, 17, 7, 6, 0, 0, '97 2/3', 0.538, 83, 4, 38, 3, 92, 40, 39, 1.24),
        (7, 7, '레예스', 2, '삼성공업고등학교', 2024, 3.64, 18, 8, 3, 0, 0, '99', 0.727, 112, 9, 21, 3, 79, 44, 40, 1.34),
        (8, 8, '윌커슨', 8, '롯데고등학교', 2024, 3.64, 19, 8, 7, 0, 0, '118 2/3', 0.533, 127, 15, 12, 2, 102, 52, 48, 1.17),
        (9, 9, '류현진', 9, '한화고등학교', 2024, 3.67, 17, 5, 5, 0, 0, '98', 0.5, 107, 5, 21, 1, 83, 48, 40, 1.31),
        (10, 10, '양현종', 1, '기아고등학교', 2024, 3.81, 17, 6, 3, 0, 0, '101 2/3', 0.667, 102, 12, 22, 4, 72, 45, 43, 1.22),
        (11, 11, '코너', 2, '삼성공업고등학교', 2024, 3.97, 19, 7, 5, 0, 0, '106 2/3', 0.583, 96, 17, 29, 15, 110, 52, 47, 1.17),
        (12, 12, '카스타노', 6, 'NC특성화고등학교', 2024, 4.26, 17, 7, 5, 0, 0, '99 1/3', 0.583, 102, 10, 21, 7, 84, 58, 47, 1.24),
        (13, 13, '엔스', 4, '엘지디지털고등학교', 2024, 4.3, 19, 8, 3, 0, 0, '104 2/3', 0.727, 107, 8, 32, 2, 104, 55, 50, 1.33),
        (14, 14, '쿠에바스', 7, 'kt인터넷고등학교', 2024, 4.32, 18, 4, 8, 0, 0, '106 1/3', 0.333, 95, 12, 35, 3, 101, 53, 51, 1.22),
        (15, 15, '김광현', 5, 'ssg상업고등학교', 2024, 4.66, 18, 6, 6, 0, 0, '96 2/3', 0.5, 90, 14, 37, 2, 93, 52, 50, 1.31),
        (16, 16, '켈리', 4, '엘지디지털고등학교', 2024, 4.68, 18, 4, 8, 0, 0, '107 2/3', 0.333, 123, 13, 24, 5, 63, 63, 56, 1.37),
        (17, 17, '신민혁', 6, 'NC특성화고등학교', 2024, 5.06, 18, 6, 7, 0, 0, '85 1/3', 0.462, 107, 16, 9, 4, 52, 52, 48, 1.36),
        (18, 18, '엄상백', 7, 'kt인터넷고등학교', 2024, 5.18, 17, 7, 7, 0, 0, '88 2/3', 0.5, 95, 16, 25, 1, 100, 53, 51, 1.35),
        (19, 19, '박세웅', 8, '롯데고등학교', 2024, 5.36, 17, 6, 6, 0, 0, '94', 0.5, 113, 6, 33, 5, 67, 63, 56, 1.55),
    ]

    pitcher_columns = [
        "record_id", "player_id", "Name", "team_id", "Team", "Season", "ERA", "Games", "Win", "Lose", "SV", "HLD", "IP", "WPCT", "H", "HR", 
        "BB", "HBP", "SO", "run", "ER", "WHIP"
    ]
    
    pitcher_initial_df = pd.DataFrame(pitcher_mock_data, columns=pitcher_columns)
    pitcher_df = pitcher_initial_df.drop(['record_id', 'player_id', 'team_id'], axis=1)
    pitcher_df = pitcher_df.sort_values(by='ERA', ascending=True)
    
    pitcher_df.index = pitcher_df.index + 1

    pitcher_df['Season'] = pitcher_df['Season'].astype('string')
    pitcher_df['ERA'] = pitcher_df['ERA'].round(2)
    pitcher_df['WHIP'] = pitcher_df['WHIP'].round(2)
    pitcher_df['WPCT'] = pitcher_df['WPCT'].round(3)


    tabs = st.tabs(['**타자**', '**투수**'])

    with tabs[0]:
        reset_search_text()
        st.subheader("타자 기록")
        st.dataframe(hitter_df)

        search_name = st.text_input('타자 이름 검색', '')

        if search_name:
            st.session_state['hitter_search_text'] = search_name
            search_name = search_name.lower()
            search_df = hitter_df.copy()
            search_df['match_score'] = search_df['Name'].apply(lambda x: get_match_score(x.lower(), search_name))
            results_all = search_df[search_df['match_score'] > 0].sort_values(by=['match_score', 'Name'], ascending=[False, True])
            results = results_all
            
            if not results.empty:
                st.dataframe(results)
                selected_name = st.selectbox('선수를 선택하세요', results['Name'])
                if selected_name:
                    if st.button('선수 상세 기록 보기'):
                        st.title("hi")
                        st.write("hello")
                        show_player_detail(hitter_initial_df, 5)
                        
                        hit_directions = [('left', 46),('right', 54)]
                        chart_data = pd.DataFrame(hit_directions, columns=['directions', 'percentage'])
                        st.scatter_chart(chart_data, x='directions', size='percentage')
            else:
                st.write('일치하는 선수가 없습니다.')

    with tabs[1]:
        reset_search_text()
        st.subheader("투수 기록")
        st.dataframe(pitcher_df)

        search_name = st.text_input('투수 이름 검색', '')

        if search_name:
            st.session_state['pitcher_search_text'] = search_name
            search_name = search_name.lower()
            search_df = pitcher_df.copy()
            search_df['match_score'] = search_df['player_name'].apply(lambda x: get_match_score(x.lower(), search_name))
            results = search_df[search_df['match_score'] > 0].sort_values(by=['match_score', 'player_name'], ascending=[False, True])
            results['Name'] = results_all['Name']

            if not results.empty:
                st.dataframe(results)
                selected_name = st.selectbox('선수를 선택하세요', results['Name'])
                if selected_name:
                    if st.button('선수 상세 기록 보기'):
                        st.title("hi")
                        st.write("hello")
            else:
                st.write('일치하는 선수가 없습니다.')
    
def show_player_detail(initial_df, player_id):
    basic_info = [
        (5, '허경민', "1990/08/26", 176, 69, "송정동초-충장중-광주제일고-두산-경찰", "내야수", "우투우타")
    ]
    record = initial_df.loc[initial_df['player_id']==player_id]
    st.dataframe(basic_info)
    st.dataframe(record)
    hit_directions = [('left', 0.46),('right', 0.54)]
    chart_data = pd.DataFrame(hit_directions, ['directions', 'percentage'])
    # st.scatter_chart(chart_data, x='directions', size='percentage')
    
    
