import pandas as pd 

class RadarStats:
    def __init__(self, df) -> None:
        self.df = df

    def stats(self):
        df = self.df
        ideal_criação = ['playerStats_key_pass_algoritmo', 'playerStats_pass_within_final_third', 'xA/assistência',
                         'playerStats_smart_pass_algoritmo', 'playerStats_through_pass_algoritmo',
                         'playerStats_pre_assist_algoritmo', 'playerStats_pre_pre_assist_algoritmo',
                         'playerStats_cross_algoritmo', 'playerStats_pre_shot_assist_algoritmo']
        criação = df[df.columns[df.columns.isin(ideal_criação)]]
        passe = df[
            ['playerStats_long_pass_into_duel_algoritmo', 'playerStats_pass_algoritmo', 'Passes Progressivos/Passes %',
             'playerStats_pass_to_another_flank_success', 'playerStats_progressive_pass_algoritmo',
             'playerStats_smart_pass_algoritmo']]
        finalizaçao = df[['xG/chute', 'Gol decisivo/gol %', 'playerStats_head_shot_algoritmo', 'playerStats_shot_algoritmo',
                          'playerStats_non_penalty_goal', 'playerStats_shot_on_goal']]
        velocidade = df[
            ['playerStats_progressive_run_algoritmo', 'playerStats_acceleration_algoritmo', 'playerStats_run_algoritmo']]
        drible = df[['playerStats_dribble_with_take_on_algoritmo', 'playerStats_dribble_algoritmo',
                     'playerStats_dribble_with_space_algoritmo']]
        defensivo = df[
            ['playerStats_tackle_algoritmo', 'playerStats_recovery_algoritmo', 'playerStats_defensive_duel_algoritmo',
             'playerStats_interception_algoritmo', 'playerStats_defensive_positioning', 'playerStats_covering_depth']]
        aereo = df[['playerStats_aerial_duel_algoritmo']]
        pressão = df[['playerStats_pressed_sequence_recovery_algoritmo', 'playerStats_quick_recovery_algoritmo',
                      'playerStats_recovery_algoritmo', 'playerStats_dangerous_opponent_half_recovery_algoritmo']]

        dic_atributos = {'Criação': criação, 'Passe': passe, 'Finalização': finalizaçao, 'Velocidade': velocidade,
                         'Drible': drible, 'Defesa': defensivo, 'Bola Aérea': aereo, 'Pressão': pressão}
        lista_frame_caracteristicas = []
        for nome, frame in dic_atributos.items():
            tabela = (pd.DataFrame(frame.sum(axis=1)).rename(columns={0: nome}))
            lista_frame_caracteristicas.append(tabela)

        caracteristicas = pd.concat(lista_frame_caracteristicas, axis=1)
        df_radar = caracteristicas.rank(pct=True)
        return df_radar

