import streamlit as st
import nba_api_game_stats as nba_game
import nba_api_indiviual_stats as nba_individual

#col1, col2= st.beta_columns(2)
st.sidebar.title('Menu')
add_edit = st.sidebar.text_input('Procure por')
if add_edit != '':
    st.title('Estatísticas NBA - ' + add_edit)
    table_result = nba_game.get_player_stats_detail(add_edit)
    st.write('All career games from ' + add_edit)
    st.dataframe(table_result)
    
    st.write('Career individual stats')
    st.write(nba_individual.get_player_stats_detail_all(add_edit))

    st.write('Current season individual stats')
    st.write(nba_individual.get_player_stats_detail(add_edit))

    # st.write('3Pts attempted vs 3Pts made')
    # st.pyplot(nba.show_graph(add_edit))
else:
    st.title('Estatísticas NBA')
    expander = st.beta_expander("FAQ")
    expander.write("Here you could put in some really, really long explanations...")