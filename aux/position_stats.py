class StatsByPosition:
    @staticmethod
    def get_stats_by_position():
        dic_stats_by_position = {
                'Atacante': ['playerStats_off_the_ball',
                  'playerStats_received_progressive_pass_success',
                  'playerStats_shot_in_counterattack_success',
                  'playerStats_acceleration_success',
                  'xG/chute',
                  'playerStats_pre_assist_success',
                  'playerStats_under_pressure_success',
                  'playerStats_through_pass_success',
                  'playerStats_pre_pre_assist_success',
                  'playerStats_cross_success',
                  'playerStats_pre_shot_assist_success',
                  'playerStats_smart_pass_success',
                  'playerStats_key_pass_success',
                  'playerStats_pass_success',
                  'xA/assistência',
                  'Passes Progressivos/Passes %',
                  'playerStats_dribble_with_take_on_success',
                  'playerStats_run_success',
                  'playerStats_progressive_run_success',
                  'playerStats_dribble_with_space_success',
                  'playerStats_successful_dribble_leading_to_shot_success',
                  'playerStats_dribble_with_progress',
                  'playerStats_dribble_success',
                  'playerStats_controlled_penalty_area_entry_success',
                  'playerStats_diagonal_to_flank_success',
                  'playerStats_pressed_sequence_recovery_success',
                  'playerStats_recovery_success',
                  'playerStats_defensive_duel_success',
                  'playerStats_interception_success',
                  'playerStats_covering_depth',
                  'playerStats_dangerous_opponent_half_recovery_success',
                  'playerStats_defensive_positioning',
                  'playerStats_pressing_duel',
                  'playerStats_quick_recovery_success',
                  'playerStats_head_shot_success',
                  'playerStats_head_pass_success',
                  'playerStats_linkup_play_success',
                  'playerStats_aerial_duel_success',
                  'playerStats_offensive_shielding_success',
                  'playerStats_shot_from_box_success',
                  'Gol decisivo/gol %',
                  'playerStats_opportunity_success',
                  'playerStats_touch_in_penalty_area_success',
                  'playerStats_touch_in_box',
                  'Toque na área %',
                  'Finalização/Toque na área',
                  'playerStats_non_penalty_goal',
                  'playerStats_action'],
                 'Extremo': ['playerStats_key_pass_success',
                  'playerStats_pass_success',
                  'xA/assistência',
                  'playerStats_smart_pass_success',
                  'Passes Progressivos/Passes %',
                  'playerStats_through_pass_success',
                  'playerStats_long_pass_into_duel_success',
                  'playerStats_pass_to_another_flank_success',
                  'playerStats_pre_assist_success',
                  'playerStats_under_pressure_success',
                  'playerStats_pre_pre_assist_success',
                  'playerStats_cross_success',
                  'playerStats_pre_shot_assist_success',
                  'playerStats_acceleration_success',
                  'playerStats_dribble_with_take_on_success',
                  'playerStats_run_success',
                  'playerStats_cross',
                  'playerStats_progressive_run_success',
                  'playerStats_dribble_with_progress',
                  'playerStats_controlled_penalty_area_entry_success',
                  'playerStats_shot_success',
                  'playerStats_touch_in_box_success',
                  'playerStats_diagonal_to_flank_success',
                  'playerStats_aerial_duel_success',
                  'playerStats_offensive_shielding_success',
                  'playerStats_defensive_duel_success',
                  'playerStats_off_the_ball',
                  'playerStats_received_progressive_pass_success',
                  'playerStats_shot_in_counterattack_success',
                  'playerStats_shot_from_box_success',
                  'Gol decisivo/gol %',
                  'playerStats_opportunity_success',
                  'playerStats_touch_in_penalty_area_success',
                  'playerStats_touch_in_box',
                  'Toque na área %',
                  'xG/chute',
                  'Finalização/Toque na área',
                  'playerStats_non_penalty_goal',
                  'playerStats_pressed_sequence_recovery_success',
                  'playerStats_recovery_success',
                  'playerStats_interception_success',
                  'playerStats_covering_depth',
                  'playerStats_dangerous_opponent_half_recovery_success',
                  'playerStats_defensive_positioning',
                  'playerStats_pressing_duel',
                  'playerStats_quick_recovery_success',
                  'playerStats_action'],
                 'Lateral': ['playerStats_key_pass_success',
                  'playerStats_pass_success',
                  'xA/assistência',
                  'playerStats_smart_pass_success',
                  'Passes Progressivos/Passes %',
                  'playerStats_through_pass_success',
                  'playerStats_long_pass_into_duel_success',
                  'playerStats_pass_to_another_flank_success',
                  'playerStats_pre_assist_success',
                  'playerStats_under_pressure_success',
                  'playerStats_pre_pre_assist_success',
                  'playerStats_cross_success',
                  'playerStats_pre_shot_assist_success',
                  'playerStats_defensive_duel_success',
                  'playerStats_interception_success',
                  'playerStats_covering_depth',
                  'playerStats_defensive_positioning',
                  'playerStats_touch_in_box_success',
                  'playerStats_touch_in_final_third',
                  'playerStats_cross',
                  'playerStats_defensive_duel',
                  'playerStats_pressing_duel',
                  'playerStats_quick_recovery_success',
                  'playerStats_foul',
                  'playerStats_controlled_penalty_area_entry_success',
                  'playerStats_shot_success',
                  'playerStats_diagonal_to_flank_success',
                  'playerStats_acceleration_success',
                  'playerStats_dribble_with_take_on_success',
                  'playerStats_run_success',
                  'playerStats_progressive_run_success',
                  'playerStats_defensive_mistake',
                  'playerStats_ball_loss',
                  'playerStats_assist_success',
                  'playerStats_action'],
                 'Meio Campista': ['xG/chute',
                  'playerStats_pre_assist_success',
                  'playerStats_under_pressure_success',
                  'playerStats_through_pass_success',
                  'playerStats_pre_pre_assist_success',
                  'playerStats_cross_success',
                  'playerStats_pre_shot_assist_success',
                  'playerStats_smart_pass_success',
                  'playerStats_key_pass_success',
                  'playerStats_pass_success',
                  'xA/assistência',
                  'Passes Progressivos/Passes %',
                  'playerStats_acceleration_success',
                  'playerStats_dribble_with_take_on_success',
                  'playerStats_run_success',
                  'playerStats_shot_from_box_success',
                  'Gol decisivo/gol %',
                  'playerStats_opportunity_success',
                  'playerStats_touch_in_penalty_area_success',
                  'playerStats_touch_in_box',
                  'Toque na área %',
                  'Finalização/Toque na área',
                  'playerStats_non_penalty_goal',
                  'playerStats_received_pass',
                  'playerStats_shot_buildup_pass_success',
                  'playerStats_touch',
                  'playerStats_cross',
                  'playerStats_progressive_run_success',
                  'playerStats_dribble_with_progress',
                  'playerStats_controlled_penalty_area_entry_success',
                  'playerStats_off_the_ball',
                  'playerStats_recovery_counterpressing_success',
                  'playerStats_received_long_pass_success',
                  'playerStats_touch_in_box_success',
                  'playerStats_received_dangerous_pass_success',
                  'playerStats_shot_in_counterattack_success',
                  'playerStats_action_in_counterattack',
                  'playerStats_ball_loss',
                  'playerStats_action'],
                 'Volante': ['playerStats_key_pass_success',
                  'playerStats_pass_success',
                  'xA/assistência',
                  'playerStats_smart_pass_success',
                  'Passes Progressivos/Passes %',
                  'playerStats_through_pass_success',
                  'playerStats_long_pass_into_duel_success',
                  'playerStats_pass_to_another_flank_success',
                  'playerStats_pre_assist_success',
                  'playerStats_under_pressure_success',
                  'playerStats_pre_pre_assist_success',
                  'playerStats_cross_success',
                  'playerStats_pre_shot_assist_success',
                  'playerStats_received_pass',
                  'playerStats_shot_buildup_pass_success',
                  'playerStats_touch',
                  'playerStats_aerial_duel_in_own_penalty_area',
                  'playerStats_touch_in_box',
                  'playerStats_opportunity_success',
                  'playerStats_defensive_duel_success',
                  'playerStats_interception_success',
                  'playerStats_covering_depth',
                  'playerStats_defensive_positioning',
                  'playerStats_touch_in_box_success',
                  'playerStats_shot_success',
                  'playerStats_defensive_duel',
                  'playerStats_pressing_duel',
                  'playerStats_quick_recovery_success',
                  'playerStats_foul',
                  'playerStats_off_the_ball',
                  'playerStats_recovery_counterpressing_success',
                  'playerStats_received_long_pass_success',
                  'playerStats_received_dangerous_pass_success',
                  'playerStats_shot_in_counterattack_success',
                  'playerStats_action_in_counterattack',
                  'playerStats_defensive_mistake',
                  'playerStats_ball_loss',
                  'playerStats_action'],
                 'Zagueiro': ['playerStats_received_pass',
                  'playerStats_pass_success',
                  'playerStats_smart_pass_success',
                  'Passes Progressivos/Passes %',
                  'playerStats_through_pass_success',
                  'playerStats_defensive_duel',
                  'playerStats_pressing_duel',
                  'playerStats_quick_recovery_success',
                  'playerStats_interception_success',
                  'playerStats_foul',
                  'playerStats_run',
                  'playerStats_covering_depth',
                  'playerStats_aerial_duel_in_own_penalty_area',
                  'playerStats_aerial_duel_success',
                  'playerStats_recovery_success',
                  'playerStats_defensive_positioning',
                  'playerStats_defensive_mistake',
                  'playerStats_ball_loss',
                  'playerStats_clearance_success',
                  'playerStats_blocked_shot',
                  'playerStats_aerial_duel_in_own_penalty_area_success',
                  'playerStats_progressive_pass_success',
                  'playerStats_pre_pre_assist_success',
                  'playerStats_smart_pass_success',
                  'playerStats_non_penalty_goal',
                  'playerStats_touch',
                  'playerStats_received_pass',
                  'playerStats_action'],
                 'Lateral direito': ['playerStats_key_pass_success',
                  'playerStats_pass_success',
                  'xA/assistência',
                  'playerStats_smart_pass_success',
                  'Passes Progressivos/Passes %',
                  'playerStats_through_pass_success',
                  'playerStats_long_pass_into_duel_success',
                  'playerStats_pass_to_another_flank_success',
                  'playerStats_pre_assist_success',
                  'playerStats_under_pressure_success',
                  'playerStats_pre_pre_assist_success',
                  'playerStats_cross_success',
                  'playerStats_pre_shot_assist_success',
                  'playerStats_defensive_duel_success',
                  'playerStats_interception_success',
                  'playerStats_covering_depth',
                  'playerStats_defensive_positioning',
                  'playerStats_touch_in_box_success',
                  'playerStats_touch_in_final_third',
                  'playerStats_cross',
                  'playerStats_defensive_duel',
                  'playerStats_pressing_duel',
                  'playerStats_quick_recovery_success',
                  'playerStats_foul',
                  'playerStats_controlled_penalty_area_entry_success',
                  'playerStats_shot_success',
                  'playerStats_diagonal_to_flank_success',
                  'playerStats_acceleration_success',
                  'playerStats_dribble_with_take_on_success',
                  'playerStats_run_success',
                  'playerStats_progressive_run_success',
                  'playerStats_defensive_mistake',
                  'playerStats_ball_loss',
                  'playerStats_assist_success',
                  'playerStats_action'],
                 'Lateral Esquerdo': ['playerStats_key_pass_success',
                  'playerStats_pass_success',
                  'xA/assistência',
                  'playerStats_smart_pass_success',
                  'Passes Progressivos/Passes %',
                  'playerStats_through_pass_success',
                  'playerStats_long_pass_into_duel_success',
                  'playerStats_pass_to_another_flank_success',
                  'playerStats_pre_assist_success',
                  'playerStats_under_pressure_success',
                  'playerStats_pre_pre_assist_success',
                  'playerStats_cross_success',
                  'playerStats_pre_shot_assist_success',
                  'playerStats_defensive_duel_success',
                  'playerStats_interception_success',
                  'playerStats_covering_depth',
                  'playerStats_defensive_positioning',
                  'playerStats_touch_in_box_success',
                  'playerStats_touch_in_final_third',
                  'playerStats_cross',
                  'playerStats_defensive_duel',
                  'playerStats_pressing_duel',
                  'playerStats_quick_recovery_success',
                  'playerStats_foul',
                  'playerStats_controlled_penalty_area_entry_success',
                  'playerStats_shot_success',
                  'playerStats_diagonal_to_flank_success',
                  'playerStats_acceleration_success',
                  'playerStats_dribble_with_take_on_success',
                  'playerStats_run_success',
                  'playerStats_progressive_run_success',
                  'playerStats_defensive_mistake',
                  'playerStats_ball_loss',
                  'playerStats_assist_success',
                  'playerStats_action',
                  ]}

        return dic_stats_by_position
stats_by_position = StatsByPosition()