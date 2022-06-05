import requests

class Oab:
    def __init__(self) -> None:
        pass

    def get_oab_data(self, url) -> dict:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            data = None
        return data