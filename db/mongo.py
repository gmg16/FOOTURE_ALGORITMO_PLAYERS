import pymongo
from core.config import Settings
import pandas as pd 

settings = Settings()

class QueryMongo:

    def __init__(self):
        self.conn_str = settings.MONGO_CONN_STR 
        self.client = pymongo.MongoClient(self.conn_str, serverSelectionTimeoutMS=5000)

    def general_query(self, db: str, collection: str, search_filter: dict):
        db = self.client[db]
        mycollection = db[collection]
        cursor = list(mycollection.find(search_filter))
        df_final = pd.DataFrame(cursor)
        return df_final


    def get_translated_metrics(self):
        result = list(self.client['footure']['translated_metrics'].find({}, { '_id':0}))
        new_dict = {}
        for coluna_dict in result:
            new_dict.update({coluna_dict['Coluna']: coluna_dict['Tradução']})
        return new_dict 

    def metricas_por_rodada(self, lista_jogadores, season_id):
        db = self.client['footure_stats']
        mycollection = db['stats_per_round']
        cursor = list(mycollection.find({'id': {"$in":lista_jogadores}, 'match_seasonId':season_id}))
        df_final = pd.DataFrame(cursor)
        return df_final

    def metricas_comp_posicao(self, season_id, nome_posicao):
        db = self.client['footure']
        mycollection=db['player_info']
        list_cursors=list(mycollection.find({ 'season_id': season_id , 'primary_position': nome_posicao }))
        df_final = pd.DataFrame(list_cursors)
        return df_final

    def get_players_id(self, season_id):
        filter= {'seasonId': season_id}
        result = list(self.client['footure_stats']['footure_stats_per_round']. find(filter, {'id':1, '_id':0}))
        if result:
            list_players = [int(row['id']) for row in result]
            return list_players 
        else: 
            return None
    
    def metricas_jogador(self, season_id):
        # Instanciar a db e acessar a db
        db = self.client['footure_stats']
        mycollection = db['general_stats']
        list_cursors = list(mycollection.find({'season_id': season_id}))
        return list_cursors

    def get_players_by_team_id(self, team_id):
        filter= {'current_team_id': team_id}
        result = list(self.client['footure']['player_info'].find(filter, {'id':1, '_id':0}))
        list_players = [int(row['id']) for row in result]
        return list_players 
    
    
    def get_players_by_team_id_and_season(self, team_id, season_id):
        filter= {'id_time_na_epoca': team_id, 'season_id': season_id}
        result = list(self.client['footure_stats']['general_stats'].find(filter, {'id':1, '_id':0}))
        list_players = [int(row['id']) for row in result]
        return list_players 
    

class IngestionMongo:

    def __init__(self):
        self.conn_str = settings.MONGO_CONN_STR 
        self.client = pymongo.MongoClient(self.conn_str, serverSelectionTimeoutMS=5000)

