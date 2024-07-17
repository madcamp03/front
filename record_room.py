import requests
import streamlit as st
import pandas as pd


hitter_basic_info = {
    1: ('도슨', "1995/05/19", 183, 100, " 미국 Ohio Licking Heights(고)", "외야수", "우투좌타"),
    2: ('에레디아', "1991/01/31", 178, 88, "쿠바 Eide Luis Agusto Tursios Lima", "외야수", "좌투우타"),
    3: ('박건우', "1990/09/08", 184, 80, "역삼초-서울이수중-서울고-두산-경찰-두산", "외야수", "우투우타"),
    4: ('레이예스', "1994/10/05", 196, 87, "베네수엘라 Dr Felipe Guevara(고)", "외야수", "우투양타"),
    5: ('허경민', "1990/08/26", 176, 69, "송정동초-충장중-광주제일고-두산-경찰", "내야수", "우투우타"),
    6: ('송성문', "1996/08/29", 183, 88, "봉천초(용산구리틀)-홍은중-장충고-히어로즈-키움-상무", "내야수", "우투좌타"),
    7: ('양의지', "1987/06/05", 180, 95, "송정동초-무등중-진흥고-두산-경찰-두산-NC", "포수", "우투우타"),
    8: ('김도영', "2003/10/02", 183, 85, "광주대성초-광주동성중-광주동성고", "내야수", "우투우타"),
    9: ('김혜성', "1999/01/27", 179, 80, "문촌초(고양시리틀)-동산중-동산고-히어로즈", "내야수", "우투좌타"),
    10: ('박민우', "1993/02/06", 185, 80, "마포초(용산구리틀)-선린중-휘문고", "내야수", "우투좌타")
}


# hitter_response = requests.get("http://localhost:3000/api/hitter/records").json()
hitter_response = requests.get("http://35.209.111.224:3000/api/hitter/records").json()
hitter_initial_df = pd.DataFrame(hitter_response)
hitter_initial_df.rename(columns={
    'record_id': 'record_id',
    'player_id': 'player_id',
    'player_name': 'Name',
    'team_id': 'team_id',
    'team': 'Team',
    'season': 'Season',
    'game_count': 'Games',
    'bat_avg': 'AVG',
    'slg': 'SLG',
    'obp': 'OBP',
    'ops': 'OPS',
    'pa': 'PA',
    'ab': 'AB',
    'run': 'R',
    'hit': 'H',
    'hit_base2': '2B',
    'hit_base3': '3B',
    'homerun': 'HR',
    'rbi': 'RBI',
    'sac': 'SAC',
    'sf': 'SF',
    'bb': 'BB',
    'so': 'SO',
    'risp': 'RISP',
    'sb': 'SB',
    'sb_percent': 'SB%'
}, inplace=True)


# pitcher_response = requests.get("http://localhost:3000/api/pitcher/records").json()
pitcher_response = requests.get("http://35.209.111.224:3000/api/pitcher/records").json()
pitcher_initial_df = pd.DataFrame(pitcher_response)
pitcher_initial_df.rename(columns={
    'record_id': 'record_id',
    'player_id': 'player_id',
    'player_name': 'Name',
    'team_id': 'team_id',
    'team': 'Team',
    'season': 'Season',
    'era': 'ERA',
    'game_count': 'Games',
    'win': 'Win',
    'lose': 'Lose',
    'sv': 'SV',
    'hld': 'HLD',
    'ip': 'IP',
    'hr': 'HR',
    'bb': 'BB',
    'hbp': 'HBP',
    'so': 'SO',
    'run': 'run',
    'er': 'ER',
    'whip': 'WHIP',
    'wpct': 'WPCT',
    'hit': 'H'
}, inplace=True)


hitter_stats = [
    (2019, 82, 0.345, 0.507, 0.413, 0.92, 329, 284, 41, 98, 13, 3, 9, 58, 0, 7, 37, 33, 0.364, 7, 100),
    (2020, 82, 0.345, 0.507, 0.413, 0.92, 329, 284, 41, 98, 13, 3, 9, 58, 0, 7, 37, 33, 0.364, 7, 100),
    (2021, 82, 0.345, 0.507, 0.413, 0.92, 329, 284, 41, 98, 13, 3, 9, 58, 0, 7, 37, 33, 0.364, 7, 100),
    (2022, 82, 0.345, 0.507, 0.413, 0.92, 329, 284, 41, 98, 13, 3, 9, 58, 0, 7, 37, 33, 0.364, 7, 100),
    (2023, 82, 0.345, 0.507, 0.413, 0.92, 329, 284, 41, 98, 13, 3, 9, 58, 0, 7, 37, 33, 0.364, 7, 100),
]
hitter_stats_columns = [
    "Season", "Games", "AVG", "SLG", "OBP", "OPS", "PA", "AB", "R", "H", "2B", "3B", "HR", "RBI", "SAC", "SF", "BB", "SO", "RISP", "SB", "SB%"
]

pitcher_stats = [
    (2020, 16, 3.16, 7, 4, 0, 0, '91', 0.636, 82, 8, 31, 4, 70, 35, 32, 1.24),
    (2021, 16, 3.16, 7, 4, 0, 0, '91', 0.636, 82, 8, 31, 4, 70, 35, 32, 1.24),
    (2022, 16, 3.16, 7, 4, 0, 0, '91', 0.636, 82, 8, 31, 4, 70, 35, 32, 1.24),
    (2023, 16, 3.16, 7, 4, 0, 0, '91', 0.636, 82, 8, 31, 4, 70, 35, 32, 1.24),
]
pitcher_stats_columns = [
    "Season", "Games", "ERA", "Win", "Lose", "SV", "HLD", "IP", "WPCT", "H", "HR", "BB", "HBP", "SO", "run", "ER", "WHIP"
]

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


def show_player_detail(player_type, player_id, player_stats, player_stats_columns):
    if player_type == 'hitter':
        hitter_response = requests.post("http://localhost:3000/api/hitter/details", json={'player_id': player_id})
        # hitter_response = requests.post("http://35.209.111.224:3000/api/hitter/details", json={'player_id': player_id})
        player = hitter_response.json()
    elif player_type == 'pitcher':
        pitcher_response = requests.post("http://localhost:3000/api/pitcher/details", json={'player_id': player_id})
        # pitcher_response = requests.post("http://35.209.111.224:3000/api/pitcher/details", json={'player_id': player_id})
        player = pitcher_response.json()

    player_name = player.get("player_name")
    birth= player.get('birth').split('T')[0]
    player_height= player.get('player_height')
    player_weight= player.get('player_weight')
    career = player.get('career')
    position = player.get('position')
    hand = player.get('hand')
    uni_num = "No. " + str(player.get('uni_num'))

    with st.expander(f"{player_name} 상세 기록 보기"):
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown(f"**{player_name} 기본 정보**")
            basic_info_df = pd.DataFrame([{
                "이름": player_name, "번호": uni_num, "생년월일": birth, "신장": player_height, "체중": player_weight,
                "경력": career, "포지션": position, "투타": hand
            }])
            basic_info_df =basic_info_df.astype('str')
            basic_info_df.index = ["기본 정보"]
            basic_info_df = basic_info_df.T
            st.dataframe(basic_info_df, use_container_width=True)

        with col2:
            st.markdown(f"**{player_name} 통산 기록**")
            stats_df = pd.DataFrame(player_stats, columns=player_stats_columns)
            stats_df['Season'] = stats_df['Season'].astype(int).astype(str)
            st.dataframe(stats_df, hide_index=True)
    

    # record = initial_df.loc[initial_df['player_id']==player_id]
    # st.dataframe(basic_info[player_id])
    # st.dataframe(record)

    # hit_directions = [('left', 0.46),('right', 0.54)]
    # chart_data = pd.DataFrame(hit_directions, ['directions', 'percentage'])
    # st.scatter_chart(chart_data, x='directions', size='percentage')


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

    hitter_df = hitter_initial_df.drop(['record_id', 'player_id', 'team_id'], axis=1)
    hitter_df = hitter_df.sort_values(by='AVG', ascending=False)
    
    hitter_df.index = hitter_df.index + 1
    
    hitter_df['SB%'] = hitter_df['SB%'].astype(str) + '%'
    hitter_df['Season'] = hitter_df['Season'].astype(int).astype(str)
    
    hitter_df['AVG'] = hitter_df['AVG'].round(3)
    hitter_df['SLG'] = hitter_df['SLG'].round(3)
    hitter_df['OBP'] = hitter_df['OBP'].round(3)
    hitter_df['OPS'] = hitter_df['OPS'].round(3)
    hitter_df['RISP'] = hitter_df['RISP'].round(3)

    new_order = ["Name", "Team", "Season", "AVG", "Games", "SLG", "OBP", "OPS", "PA", "AB", "R", "H", 
                 "2B", "3B", "HR", "RBI", "SAC", "SF", "BB", "SO", "RISP", "SB", "SB%"]
    hitter_df = hitter_df[new_order]

    
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
            results = search_df[search_df['match_score'] > 0].sort_values(by=['match_score', 'Name'], ascending=[False, True])
            
            if not results.empty:
                st.dataframe(results, hide_index=True)
                selected_name = st.selectbox('선수를 선택하세요', results['Name'])
                if selected_name:
                    player_id = int(hitter_initial_df.loc[hitter_initial_df['Name'] == selected_name, 'player_id'].values[0])
                    show_player_detail('hitter', player_id, hitter_stats, hitter_stats_columns)
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
            search_df['match_score'] = search_df['Name'].apply(lambda x: get_match_score(x.lower(), search_name))
            results = search_df[search_df['match_score'] > 0].sort_values(by=['match_score', 'Name'], ascending=[False, True])

            if not results.empty:
                st.dataframe(results, hide_index=True)
                selected_name = st.selectbox('선수를 선택하세요', results['Name'])
                if selected_name:
                    # if st.button('선수 상세 기록 보기'):
                    player_id = int(pitcher_initial_df.loc[pitcher_initial_df['Name'] == selected_name, 'player_id'].values[0])
                    show_player_detail('pitcher', player_id, pitcher_stats, pitcher_stats_columns)
            else:
                st.write('일치하는 선수가 없습니다.')
    