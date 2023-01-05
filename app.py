import streamlit as st
from services.player_algoritmo import Algoritmo
from services.query_advanced_search import SearchPlayers
from aux import dic_position, dic_functions, dic_season


tab1, tab2 = st.tabs(['Arte', 'Busca avançada'])

with tab1:
    with st.form('Arte algoritmo'):
        season_id = st.multiselect('Selecione as ligas', list(dic_season.keys()))
        main_position = st.selectbox('Selecione uma posição de referência', dic_position['position'])
        player_id = st.text_input('Jogador')
        button = st.form_submit_button('Gerar arte')
        if button:
            player_id = int(player_id)
            list_season = [dic_season[liga] for liga in season_id]
            algoritmo = Algoritmo(list_season, main_position, [main_position])
            algoritmo.get_funcoes(player_id)
            algoritmo.get_radar(player_id)
            algoritmo.get_stats_quadro(player_id)

with tab2:

    with st.form('First selection'):
        list_season = st.multiselect('Selecione as ligas', list(dic_season.keys()))
        list_season = [dic_season[liga] for liga in list_season]
        positions_selected = st.multiselect('Posições', dic_position['position'])
        search_button = st.form_submit_button('Pesquisar')
        if search_button:
            st.success('Ok')

    with st.form(key='filters'):
        main_position = st.selectbox('Selecione uma posição de referência', positions_selected)
            # list_functions = st.multiselect('Filtre por funções', dic_functions[0][main_position])
        filter_button = st.form_submit_button('Filtrar')
        if filter_button:
            df = SearchPlayers().algoritmo_endpoint_search(list_season, main_position, positions_selected) 
            st.success(f'{len(df)} jogadores encontrados, use os filtros para filtrar aos poucos')
            st.dataframe(df)
