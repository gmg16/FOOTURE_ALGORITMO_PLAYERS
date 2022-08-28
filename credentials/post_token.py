import requests
import json
import pandas as pd
from core.config import settings


class Credentials:

    @staticmethod
    def token_wyscout():
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Wy-Route': '0',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://platform.wyscout.com',
            'Connection': 'keep-alive',
            'Referer': 'https://platform.wyscout.com/app/?query={%22obj%22%3A%22network%22%2C%22act%22%3A%22check%22}',
            'TE': 'Trailers',
        }

        data_string = '{"obj":"access","act":"login","params":{"username":settings.WYSCOUT_USERNAME,"password":settings.WYSCOUT_PASSWORD}}'
        data_alterada = eval(data_string)
        data_query = str(data_alterada)
        data_query = data_query.replace("'",'"')
        data_query
        data = {
          'query': data_query
        }

        r = requests.post('https://platform.wyscout.com/app/aengine-service.php', headers=headers,  data=data)



        data = json.loads(r.text)
        df= pd.json_normalize(data,sep='_')
        token = pd.DataFrame(df['status_error'][0])['restrictions'][0]['token']['access_token']

        return token


    @staticmethod
    def cookies_wyscout():

        session = requests.Session()
        headers = {
            'authority': 'platform.wyscout.com',
            'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            'wy-route': '0',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-platform': '"Linux"',
            'origin': 'https://platform.wyscout.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://platform.wyscout.com/app/?',
            'accept-language': 'en-US,en;q=0.9',

        }

        data_string = '{"obj":"access","act":"login","params":{"username":settings.WYSCOUT_USERNAME,"password":settings.WYSCOUT_PASSWORD,"persistent_login":1,"forced":"true","prevPwd":settings.WYSCOUT_PASSWORD}}'
        data_alterada = eval(data_string)
        data_query = str(data_alterada)
        data_query = data_query.replace("'",'"')
        data = {
          'query': data_query
        }


        r = session.post('https://platform.wyscout.com/app/aengine-service.php', headers=headers, data=data)

        string_cookies = ''
        cookies = (session.cookies.get_dict())
        for k,v in cookies.items():
            string = f'{k}={v};'
            string_cookies = string_cookies + string
        return string_cookies

credentials = Credentials()
