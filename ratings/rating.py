import pandas as pd 

class AlgoritmoRating:

    def __init__(self,df):
        self.df = df 

    def algoritmo_atacante(self):
        df = self.df
        df['campeonato'] = 1

        raumdeuter = round(((df['playerStats_off_the_ball'] * df[
            'playerStats_received_progressive_pass_algoritmo']) ** 2 * (
                                        df['playerStats_shot_in_counterattack_algoritmo'] + df[
                                    'playerStats_acceleration_algoritmo'])) * df['campeonato'])
        deep_lying_fw = round(((df['xG/chute'] + df['playerStats_pre_assist_algoritmo'] + df[
            'playerStats_under_pressure_algoritmo'] + df['playerStats_through_pass_algoritmo'] + df[
                                    'playerStats_pre_pre_assist_algoritmo'] + df['playerStats_cross_algoritmo'] + df[
                                    'playerStats_pre_shot_assist_algoritmo'] + df['playerStats_smart_pass_algoritmo']) *
                               df['playerStats_key_pass_algoritmo'] * df['playerStats_pass_algoritmo'] * df[
                                   'xA/assistência'] * df['Passes Progressivos/Passes %']) * df['campeonato'])
        velocista = round(((df['playerStats_progressive_run_algoritmo'] + df[
            'playerStats_dribble_with_space_algoritmo'] + df['playerStats_successful_dribble_leading_to_shot_success'] +
                            df['playerStats_dribble_with_progress'] + df['playerStats_dribble_algoritmo'] + df[
                                'playerStats_controlled_penalty_area_entry_algoritmo'] + df[
                                'playerStats_diagonal_to_flank_algoritmo']) * df['playerStats_acceleration_algoritmo'] *
                           df['playerStats_dribble_with_take_on_algoritmo'] * df['playerStats_run_algoritmo']) * df[
                              'campeonato'])
        pressing_fw = round(((df['playerStats_pressed_sequence_recovery_algoritmo'] + df[
            'playerStats_recovery_algoritmo'] + df['playerStats_defensive_duel_algoritmo'] + df[
                                  'playerStats_interception_algoritmo'] + df['playerStats_covering_depth'] + df[
                                  'playerStats_dangerous_opponent_half_recovery_algoritmo'] + df[
                                  'playerStats_defensive_positioning']) * df['playerStats_pressing_duel'] * df[
                                 'playerStats_quick_recovery_algoritmo']) * df['campeonato'])
        aerial = round(((df['playerStats_head_shot_algoritmo'] + df['playerStats_head_pass_algoritmo'] + df[
            'playerStats_linkup_play_algoritmo']) * df['playerStats_aerial_duel_algoritmo'] * df[
                            'playerStats_offensive_shielding_algoritmo']) * df['campeonato'])
        poacher = (round((df['playerStats_shot_from_box_algoritmo'] + df['Gol decisivo/gol %'] + df[
            'playerStats_opportunity_algoritmo'] + df['playerStats_touch_in_penalty_area_algoritmo'] + df[
                              'playerStats_touch_in_box'] + df['Toque na área %']) * (df['xG/chute']) * df[
                             'Finalização/Toque na área'] * df['playerStats_non_penalty_goal']) * df['campeonato'])

        dic_funcoes = {'Raumdeuter': raumdeuter, 'Aéreo': aerial, 'Pressing': pressing_fw, 'Velocista': velocista,
                       'Deep Lying': deep_lying_fw, 'Goleador': poacher}
        df_funcao = pd.DataFrame(dic_funcoes).rank(pct=True)
        return df_funcao

    def algoritmo_volante(self):
        df = self.df
        volante_construtor = round((df['playerStats_key_pass_algoritmo'] * df['playerStats_pass_algoritmo'] * df[
            'xA/assistência'] * df['playerStats_smart_pass_algoritmo'] * df['Passes Progressivos/Passes %'] * df[
                                        'playerStats_through_pass_algoritmo']) * (
                                               df['playerStats_long_pass_into_duel_algoritmo'] + df[
                                           'playerStats_pass_to_another_flank_success'] + df[
                                                   'playerStats_pre_assist_algoritmo'] + df[
                                                   'playerStats_under_pressure_algoritmo'] + df[
                                                   'playerStats_pre_pre_assist_algoritmo'] + df[
                                                   'playerStats_cross_algoritmo'] + df[
                                                   'playerStats_pre_shot_assist_algoritmo']) * df['campeonato'])
        ditador_ritmo = round((((df['playerStats_received_pass'] ** df['playerStats_pass_algoritmo']) + df[
            'playerStats_under_pressure_algoritmo'] * df['playerStats_shot_buildup_pass_algoritmo'] * df[
                                    'playerStats_touch'])) * df['campeonato'])
        box_to_box = round((df['playerStats_aerial_duel_in_own_penalty_area'] ** df['playerStats_touch_in_box'] * (
                    df['playerStats_opportunity_algoritmo'] * (
                        df['playerStats_defensive_duel_algoritmo'] + df['playerStats_interception_algoritmo']))) * df[
                               'campeonato'])
        defensivo = round(((df['playerStats_defensive_duel_algoritmo'] + df['playerStats_interception_algoritmo']) * df[
            'playerStats_covering_depth'] ** 2 * df['playerStats_defensive_positioning'] ** 2) / (
                                      df['playerStats_touch_in_box_algoritmo'] * df[
                                  'playerStats_shot_algoritmo'] ** 2) * df['campeonato'])
        caçador = round(((df['playerStats_defensive_duel'] ** df['playerStats_pressing_duel'] ** df[
            'playerStats_quick_recovery_algoritmo'] * df['playerStats_interception_algoritmo'] * df[
                              'playerStats_foul'])) * df['campeonato'])
        raumdeuter = round((df['playerStats_off_the_ball'] * df['playerStats_recovery_counterpressing_algoritmo'] * (
                    df['playerStats_received_long_pass_algoritmo'] ** 2)) * df['playerStats_touch_in_box_algoritmo'] *
                           df['playerStats_received_dangerous_pass_algoritmo'] * (
                                       df['playerStats_shot_in_counterattack_algoritmo'] * df[
                                   'playerStats_action_in_counterattack']) * df['campeonato'])
        deep_lying = round(((df['playerStats_defensive_duel_algoritmo'] * df['playerStats_interception_algoritmo'] * df[
            'playerStats_pass_to_another_flank_success'] * df['Passes Progressivos/Passes %'] * df[
                                 'playerStats_progressive_pass_algoritmo'] * df['playerStats_long_pass_algoritmo']) /
                            df['playerStats_touch_in_box_algoritmo']) * df['campeonato'])

        dic_funcoes = {'Raumdeuter': raumdeuter, 'Recuperador': caçador, 'Defensivo': defensivo,
                       'Box to box': box_to_box, 'Deep Lying': deep_lying, 'Ritimista': ditador_ritmo,
                       'Construtor': volante_construtor}
        df_funcao = pd.DataFrame(dic_funcoes).rank(pct=True)
        return df_funcao

    def algoritmo_extremo(self):
        df = self.df

        extremo_armador = round((df['playerStats_key_pass_algoritmo'] * df['playerStats_pass_algoritmo'] * df[
            'xA/assistência'] * df['playerStats_smart_pass_algoritmo'] * df['Passes Progressivos/Passes %'] * df[
                                     'playerStats_through_pass_algoritmo']) * (
                                            df['playerStats_long_pass_into_duel_algoritmo'] + df[
                                        'playerStats_pass_to_another_flank_success'] + df[
                                                'playerStats_pre_assist_algoritmo'] + df[
                                                'playerStats_under_pressure_algoritmo'] + df[
                                                'playerStats_pre_pre_assist_algoritmo'] + df[
                                                'playerStats_cross_algoritmo'] + df[
                                                'playerStats_pre_shot_assist_algoritmo']) * df['campeonato'])
        ponta_classico = round(((df['playerStats_acceleration_algoritmo'] ** 2 * (
        df['playerStats_dribble_with_take_on_algoritmo']) * df['playerStats_run_algoritmo'] * df[
                                     'playerStats_cross'] ** 2) * (df['playerStats_progressive_run_algoritmo'] + df[
            'playerStats_dribble_with_progress']) / df['playerStats_controlled_penalty_area_entry_algoritmo'] ** 2) *
                               df['campeonato'])
        ponta_invertido = round((df['playerStats_controlled_penalty_area_entry_algoritmo'] * df[
            'playerStats_shot_algoritmo'] * df['playerStats_touch_in_box_algoritmo'] / (
                                             (df['playerStats_diagonal_to_flank_algoritmo'] ** 2) * df[
                                         'playerStats_cross'] * 2)) * df['campeonato'])
        ponta_força = round((df['playerStats_aerial_duel_algoritmo'] * df['playerStats_offensive_shielding_algoritmo'] *
                             df['playerStats_defensive_duel_algoritmo'] * df['playerStats_acceleration_algoritmo']) *
                            df['campeonato'])
        raumdeuter = round(((df['playerStats_off_the_ball'] * df[
            'playerStats_received_progressive_pass_algoritmo']) ** 2 * (
                                        df['playerStats_shot_in_counterattack_algoritmo'] + df[
                                    'playerStats_acceleration_algoritmo'])) * df['campeonato'])
        ponta_goleador = round(((df['playerStats_shot_from_box_algoritmo'] + df['Gol decisivo/gol %'] + df[
            'playerStats_opportunity_algoritmo'] + df['playerStats_touch_in_penalty_area_algoritmo'] + df[
                                     'playerStats_touch_in_box'] + df['Toque na área %']) * (df['xG/chute']) * df[
                                    'Finalização/Toque na área'] * df['playerStats_non_penalty_goal']) * df[
                                   'campeonato'])
        ponta_pressing = round(((df['playerStats_pressed_sequence_recovery_algoritmo'] + df[
            'playerStats_recovery_algoritmo'] + df['playerStats_defensive_duel_algoritmo'] + df[
                                     'playerStats_interception_algoritmo'] + df['playerStats_covering_depth'] + df[
                                     'playerStats_dangerous_opponent_half_recovery_algoritmo'] + df[
                                     'playerStats_defensive_positioning']) * df['playerStats_pressing_duel'] * df[
                                    'playerStats_quick_recovery_algoritmo']) * df['campeonato'])

        dic_funcoes = {'Raumdeuter': raumdeuter, 'Armador': extremo_armador, 'Ponta Clássico': ponta_classico,
                       'Invertido': ponta_invertido, 'Força': ponta_força, 'Goleador': ponta_goleador,
                       'Pressing': ponta_pressing}
        df_funcao = pd.DataFrame(dic_funcoes).rank(pct=True)
        return df_funcao

    def algoritmo_meio_campo(self):
        df = self.df
        armador = round(((df['xG/chute'] + df['playerStats_pre_assist_algoritmo'] + df[
            'playerStats_under_pressure_algoritmo'] + df['playerStats_through_pass_algoritmo'] + df[
                              'playerStats_pre_pre_assist_algoritmo'] + df['playerStats_cross_algoritmo'] + df[
                              'playerStats_pre_shot_assist_algoritmo'] + df['playerStats_smart_pass_algoritmo']) * df[
                             'playerStats_key_pass_algoritmo'] * df['playerStats_pass_algoritmo'] * df[
                             'xA/assistência'] * df['Passes Progressivos/Passes %']) * df['campeonato'])
        shadow_stricker = (round((df['playerStats_shot_from_box_algoritmo'] + df['Gol decisivo/gol %'] + df[
            'playerStats_opportunity_algoritmo'] + df['playerStats_touch_in_penalty_area_algoritmo'] + df[
                                      'playerStats_touch_in_box'] + df['Toque na área %']) * (df['xG/chute']) * df[
                                     'Finalização/Toque na área'] * df['playerStats_non_penalty_goal']) * df[
                               'campeonato'])
        ditador_ritmo = round((((df['playerStats_received_pass'] ** df['playerStats_pass_algoritmo']) + df[
            'playerStats_under_pressure_algoritmo'] * df['playerStats_shot_buildup_pass_algoritmo'] * df[
                                    'playerStats_touch'])) * df['campeonato'])
        ponta = round(((df['playerStats_acceleration_algoritmo'] ** 2 * (
        df['playerStats_dribble_with_take_on_algoritmo']) * df['playerStats_run_algoritmo'] * df[
                            'playerStats_cross'] ** 2) * (df['playerStats_progressive_run_algoritmo'] + df[
            'playerStats_dribble_with_progress']) / df['playerStats_controlled_penalty_area_entry_algoritmo'] ** 2) *
                      df['campeonato'])
        raumdeuter = round((df['playerStats_off_the_ball'] * df['playerStats_recovery_counterpressing_algoritmo'] * (
                    df['playerStats_received_long_pass_algoritmo'] ** 2)) * df['playerStats_touch_in_box_algoritmo'] *
                           df['playerStats_received_dangerous_pass_algoritmo'] * (
                                       df['playerStats_shot_in_counterattack_algoritmo'] * df[
                                   'playerStats_action_in_counterattack']) * df['campeonato'])

        dic_funcoes = {'Raumdeuter': raumdeuter, 'Armador': armador, 'Ponta': ponta, 'Ritimista': ditador_ritmo,
                       'Goleador': shadow_stricker}
        df_funcao = pd.DataFrame(dic_funcoes).rank(pct=True)
        return df_funcao

    def algoritmo_lateral(self):
        df = self.df
        construtor = round((df['playerStats_key_pass_algoritmo'] * df['playerStats_pass_algoritmo'] * df[
            'xA/assistência'] * df['playerStats_smart_pass_algoritmo'] * df['Passes Progressivos/Passes %'] * df[
                                'playerStats_through_pass_algoritmo']) * (
                                       df['playerStats_long_pass_into_duel_algoritmo'] + df[
                                   'playerStats_pass_to_another_flank_success'] + df[
                                           'playerStats_pre_assist_algoritmo'] + df[
                                           'playerStats_under_pressure_algoritmo'] + df[
                                           'playerStats_pre_pre_assist_algoritmo'] + df['playerStats_cross_algoritmo'] +
                                       df['playerStats_pre_shot_assist_algoritmo']) * df['campeonato'])
        defensivo = round((((df['playerStats_defensive_duel_algoritmo'] + df['playerStats_interception_algoritmo']) *
                            df['playerStats_covering_depth'] * df['playerStats_defensive_positioning']) / (
                                       df['playerStats_touch_in_box_algoritmo'] * df[
                                   'playerStats_touch_in_final_third'] * df['playerStats_cross']) ** 2) * df[
                              'campeonato'])
        caçador = round(((df['playerStats_defensive_duel'] ** 2 * df['playerStats_pressing_duel'] ** 2 * df[
            'playerStats_quick_recovery_algoritmo'] ** 2 * df['playerStats_interception_algoritmo'] * df[
                              'playerStats_foul'])) * df['campeonato'])
        invertido = round((df['playerStats_controlled_penalty_area_entry_algoritmo'] ** 2 * df[
            'playerStats_shot_algoritmo'] ** 2 * df['playerStats_touch_in_box_algoritmo'] / (
                                       (df['playerStats_diagonal_to_flank_algoritmo'] ** 2) * df[
                                   'playerStats_cross'] ** 2)) * df['campeonato'])
        ponta = ((df['playerStats_acceleration_algoritmo'] * df['playerStats_dribble_with_take_on_algoritmo'] * df[
            'playerStats_run_algoritmo'] * df['playerStats_progressive_run_algoritmo']) * (
                             (df['playerStats_cross_algoritmo'] ** 2) * df['playerStats_touch_in_box_algoritmo'] * df[
                         'playerStats_touch_in_final_third']))

        dic_funcoes = {'Defensivo': defensivo, 'Ofensivo': ponta, 'Construtor': construtor, 'Invertido': invertido,
                       'Recuperador': caçador}
        df_funcao = pd.DataFrame(dic_funcoes).rank(pct=True)
        return df_funcao

    def algoritmo_zagueiro(self):
        df = self.df
        construtor = round(((df['playerStats_received_pass'] ** df['playerStats_pass_algoritmo'] ** 2) * df[
            'playerStats_smart_pass_algoritmo'] * df['Passes Progressivos/Passes %'] * df[
                                'playerStats_through_pass_algoritmo']) * (
                                       df['playerStats_long_pass_algoritmo'] ** 2 + df[
                                   'playerStats_under_pressure_algoritmo'] + df[
                                           'playerStats_pre_pre_assist_algoritmo']) * df['campeonato'])
        caçador = round(((df['playerStats_defensive_duel'] ** 2 * df['playerStats_pressing_duel'] ** 2 * df[
            'playerStats_quick_recovery_algoritmo'] ** 2 * df['playerStats_recovery_algoritmo'] * df[
                              'playerStats_foul'] * df['playerStats_covering_depth'] * df['playerStats_run'])) * df[
                            'campeonato'])
        aerial = round((df['playerStats_aerial_duel_in_own_penalty_area'] * df['playerStats_aerial_duel_algoritmo'] *
                        df['playerStats_aerial_duel_%']) * df['campeonato'])
        geral = round(((df['playerStats_recovery_algoritmo'] * df['playerStats_defensive_positioning'] * df[
            'playerStats_covering_depth'] * df['playerStats_aerial_duel_algoritmo'] * df[
                            'playerStats_pass_algoritmo']) / (
                                   df['playerStats_defensive_mistake'] * df['playerStats_ball_loss'])) * df[
                          'campeonato'])
        posicional = round(
            (df['playerStats_interception_algoritmo'] ** 2 * df['playerStats_defensive_positioning'] ** 2) ** 2 * (
                        df['playerStats_clearance_algoritmo'] * df['playerStats_blocked_shot'] * df[
                    'playerStats_aerial_duel_in_own_penalty_area_algoritmo']) / (
                        df['playerStats_pressing_duel'] ** 2 * df['playerStats_defensive_duel'] * df[
                    'playerStats_covering_depth'] * df['playerStats_acceleration_algoritmo'] * df['playerStats_run']) *
            df['campeonato'])

        dic_funcoes = {'Posicional': posicional, 'Aéreo': aerial, 'Construtor': construtor, 'Geral': geral,
                       'Recuperador': caçador}
        df_funcao = pd.DataFrame(dic_funcoes).rank(pct=True)
        return df_funcao

