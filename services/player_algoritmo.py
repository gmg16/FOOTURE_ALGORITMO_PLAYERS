from db.mongo import QueryMongo
from data.pre_processing_data import PreRating
from ratings.rating import AlgoritmoRating
from ratings.radar_stats import RadarStats
from plot.funcoes import PlotFuncoes
from plot.plot_radar import Radar
from plot.quadro_dados import PlotStatsQuadro
from aux.translate_positions import translate
from aux.position_stats import stats_by_position




class Algoritmo:

    def __init__(self, season_id: list, position: str, filter_positions: list):
        query = QueryMongo()
        filter = {'season_id':{"$in":season_id}, 'primary_position':{"$in":filter_positions}}
        # self.df = query.general_query(db='footure_stats', collection='general_stats',
                # search_filter={'season_id': season_id, 'primary_position': position})
        self.df = query.general_query(db='footure_stats', collection='general_stats',
                search_filter=filter)
        data_process = PreRating(self.df, filter_positions)
        self.df_algoritmo = data_process.data_normalize()
        self.position = position


        if position == 'Atacante':
            self.df_output_algoritmo = AlgoritmoRating(self.df_algoritmo).algoritmo_atacante()
        if position == 'Volante':
            self.df_output_algoritmo = AlgoritmoRating(self.df_algoritmo).algoritmo_volante()

        if position == 'Extremo':
            self.df_output_algoritmo = AlgoritmoRating(self.df_algoritmo).algoritmo_extremo()

        if position == 'Meio Campista':
            self.df_output_algoritmo = AlgoritmoRating(self.df_algoritmo).algoritmo_meio_campo()

        if position == 'Lateral Esquerdo':
            self.df_output_algoritmo = AlgoritmoRating(self.df_algoritmo).algoritmo_lateral()

        if position == 'Lateral direito':
            self.df_output_algoritmo = AlgoritmoRating(self.df_algoritmo).algoritmo_lateral()

        if position == 'Zagueiro':
            self.df_output_algoritmo = AlgoritmoRating(self.df_algoritmo).algoritmo_zagueiro()

        self.position = position
    
        self.df_info = data_process.get_info()
        self.df_output_radar = RadarStats(self.df_algoritmo).stats()

    
    def get_funcoes(self, player_id: int):
        df_output_algoritmo = self.df_output_algoritmo
        df_cores = self.df_info[['id']].join(df_output_algoritmo, how='outer')
        plot_cores = PlotFuncoes()
        plot_cores.notas_funcoes(df_cores, player_id)

    def get_radar(self, player_id):
        df_radar = self.df_info[['id']].join(self.df_output_radar, how='outer')
        plot_radar = Radar()
        plot_radar.plot_radar(df_radar, player_id)
    
    def get_stats_quadro(self, player_id: int):
        df_colums_position = QueryMongo().general_query(
            db='footure', collection='position_stats',
            search_filter={}
        )
        position_columns = stats_by_position.get_stats_by_position()[self.position]
        df_to_quadro_stats = self.df[['id', 'name','playerStats_minutes_on_field'] + position_columns]
        dic_translate = translate.get_translate()
        df_to_quadro_stats = df_to_quadro_stats.rename(columns=dic_translate)
        player_name = df_to_quadro_stats[df_to_quadro_stats['id'] == player_id].reset_index(drop=True)['name'][0]
        cor_return = PlotStatsQuadro().df_cor(df_to_quadro_stats, player_id)
        df_stats = cor_return[2].drop('id', axis=1)
        df_stats = df_stats.drop('name', axis=1)
        PlotStatsQuadro().arte_quadro( df_stats ,cor_return[0], player_name)



