import streamlit as st
import nba_api_game_stats as nba_game
import nba_api_indiviual_stats as nba_individual

st.title('Estatísticas NBA')
st.sidebar.title('Filtros')

# Sidebar - Tipo Pesquisa
unique_search = ['Time', 'Posição', 'Jogador', 'Season']
selected_pos = st.sidebar.selectbox('Pesquisa Por', unique_search)

if selected_pos == 'Time':
    # Sidebar - Times
    sorted_unique_team = sorted(nba_game.get_teams())
    selected_team = st.sidebar.multiselect('Times', sorted_unique_team, sorted_unique_team)

if selected_pos == 'Posição':
    # Sidebar - Posição
    unique_pos = ['Center (C)','Power Forward (PF)','Small Forward (SF)','Point Guard (PG)','Shooting Guard (SG)']
    selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

#To Do:
# nba_api disponibiliza uma function SeasonAll, 
# tentar adicionar ela como dataframe, usar no range na lista de season ao invez de fixo.
if selected_pos == 'Season':
    list_season =  list(reversed(range(1950, 2022)))
    selected_year = st.sidebar.selectbox('Ano', list_season)

if selected_pos == 'Jogador':
    add_edit = st.sidebar.text_input('Nome Jogador')
    if add_edit != '':

        table_result = nba_game.get_player_stats_detail(add_edit)
        st.write('All career games from ' + add_edit)
        st.dataframe(table_result)
        
        st.write('Career individual stats')
        st.write(nba_individual.get_player_stats_detail_all(add_edit))

        st.write('Current season individual stats')
        st.write(nba_individual.get_player_stats_detail(add_edit))

        st.write('3Pts attempted vs 3Pts made')
        st.pyplot(nba_game.show_graph(add_edit))