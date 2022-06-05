import requests
from config import HOST
class Oab:
    def get_oab_data(self, endpoint:str) -> dict:
        self.url = f'{HOST}/{endpoint}'
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
        else:
            data = None
        return data