import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

class PreRating: 
    
    def __init__(self, df, position: list):
        self.df = df 
        self.position = position


    def filter_minutes_and_position(self):
        df = self.df
        position = self.position
        df_posicao = df[df['primary_position'].isin(position)].reset_index(drop=True)
        competitions = list(df['season_id'].unique())

        # OPERAÇÃO PARA TIRAR OS ATLETAS COM BAIXA MINUTAGEM
        lista_id_ok = []
        for comp in competitions:
            try:
                df_comp = df_posicao[df_posicao['competição'] == comp].reset_index(drop=True)
            except:
                df_comp = df_posicao[df_posicao['season_id'] == comp].reset_index(drop=True)

            media_minutos = df_comp['playerStats_minutes_on_field'].mean()
            id_ok = list(df_comp[df_comp['playerStats_minutes_on_field'] > (media_minutos / 6)]['id'])

            for id in id_ok:
                lista_id_ok.append(id)

        df_position = df_posicao[df_posicao['id'].isin(lista_id_ok)].reset_index(drop=True)
        return df_position

    def get_info(self):
        df_jogador = self.filter_minutes_and_position()
        info = ['id', 'full_name', 'match_id','Nome', 
                      'age', 'birth_date','birth_country_name',
                      'contract_expires', 'market_value', 'on_loan',
                      'primary_position', 'Jogos', 'Minutos em campo',
                      'current_team_name', 'time', 'competição', 'height',
                      'current_team_name_id', 'Time na época', 'season_id',
                      'name', 'time_na_epoca', 'id_time_na_epoca']

        df_info = df_jogador.reindex(info, axis=1).dropna(axis=1,how='all')
        return df_info



    def create_columns(self):
        df = pd.read_csv('csv_aux/colunas jogador por jogador - colunas.csv')

        df_jogador = self.filter_minutes_and_position()
        colunas = list(df['Coluna'])

        colunas_essenciais = []
        wyscout = []
        for coluna in colunas:
            if (coluna.startswith('playerStats')) == True:
                wyscout.append(coluna)
            else:
                colunas_essenciais.append(coluna)

        wyscout_success = []
        wyscout_total = []
        for coluna in wyscout:
            if coluna.endswith('_success') == True:
                wyscout_success.append(coluna)
            else:
                wyscout_total.append(coluna)

        nomes_sem_success = []
        for coluna in wyscout_success:
            nomes_sem_success.append(coluna.split('_success')[0])

        colunas_comum = list(set(nomes_sem_success).intersection(wyscout_total))

        df_comum = df[(df['Coluna'].isin(colunas_comum)) | (df['Coluna'].isin(wyscout_success))].reset_index(drop=True)
        lista_df = []
        colunas_que_porcentagem_deu_errado = []
        for total, sucesso in zip(nomes_sem_success, wyscout_success):
            try:
                tabela_porcentagem = pd.DataFrame((round(df_jogador[sucesso] / df_jogador[total] * 100, 2)))
                tabela_porcentagem = tabela_porcentagem.rename(columns={0: f'{total}_%'})
                lista_df.append(tabela_porcentagem)
            except:
                colunas_que_porcentagem_deu_errado.append(total)

        porcentagens = pd.concat(lista_df, axis=1)
        df_jogador_atualizado = df_jogador.join(porcentagens)


        coluna_geral = list(set(nomes_sem_success) - set(colunas_que_porcentagem_deu_errado))

        lista_frames_algoritmo = []
        for coluna_normal in coluna_geral:
            coluna_pct = f'{coluna_normal}_%'
            tabela_algt = pd.DataFrame(round(df_jogador_atualizado[coluna_pct] * df_jogador_atualizado[coluna_normal], 1))
            tabela_algt = tabela_algt.rename(columns={0: f'{coluna_normal}_algoritmo'})
            lista_frames_algoritmo.append(tabela_algt)

        algoritmo_rascunho = pd.concat(lista_frames_algoritmo, axis=1)

        df_jogador_atualizado = df_jogador_atualizado.rename(columns={'Nome': 'name'})
        df_algoritmo = df_jogador_atualizado.join(algoritmo_rascunho)
        df_algoritmo = df_algoritmo.fillna(0)
        return df_algoritmo


    def data_normalize(self):
        df_algoritmo = self.create_columns()
        df_algoritmo.replace([np.inf, -np.inf], np.nan, inplace=True)
        lista_colunas = list(df_algoritmo.columns)
        index_numero = lista_colunas.index('playerStats_action')
        df = df_algoritmo[list(df_algoritmo.columns[index_numero:])].fillna(0)
        data = df
        colunas_machine = list(df.columns)
        try: 
            colunas_machine.remove('time_na_epoca')
            colunas_machine.remove('id_time_na_epoca')
            colunas_machine.remove('primary_position')
            colunas_machine.remove('name')
            colunas_machine.remove('season_id')
        except:
            pass
        data = df[colunas_machine]

        scaler = MinMaxScaler(feature_range=(1, 2))
        scaler.fit(data)
        scaled_data = scaler.transform(data)
        min_max_df = pd.DataFrame(scaled_data)

        numeros = list(range(0, len(min_max_df.columns)))
        dic = {}
        for nome, numero in zip(colunas_machine, numeros):
            dic.update({numero: nome})
        min_max_df = min_max_df.rename(columns=dic)

        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)
        scaled_data = pd.DataFrame(scaled_data)

        numeros = list(range(0, len(min_max_df.columns)))
        dic = {}
        for nome, numero in zip(colunas_machine, numeros):
            dic.update({numero: nome})
        scaled_data = scaled_data.rename(columns=dic)

        df = min_max_df
        return df


