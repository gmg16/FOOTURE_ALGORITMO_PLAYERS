from db.mongo import  QueryMongo
from services.player_algoritmo import Algoritmo
import pandas as pd

class SearchPlayers:

    @staticmethod
    def get_players_by_season_and_positions(list_season: list, list_position: list):

        db = 'footure_stats'
        collection = 'general_stats'
        filter = {'season_id':{"$in":list_season}, 'primary_position':{"$in":list_position}}
        query = QueryMongo().general_query(db=db, collection=collection, search_filter=filter)
        return query

    @staticmethod
    def algoritmo_endpoint_search(list_season: list, main_position: str, positions_selected: list):
        algoritmo_filter=Algoritmo(list_season, main_position, positions_selected)
        df_query = algoritmo_filter.df
        df_info = algoritmo_filter.df_info
        df_algo = algoritmo_filter.df_output_algoritmo
        df_radar = algoritmo_filter.df_output_radar
        df = df_info.join(df_algo)
        df = df_info.join(df_radar)
        df_return = pd.merge(left=df, right=df_query, how='outer')
        return df_return



