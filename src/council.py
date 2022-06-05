from src.oab import Oab

class Council:
    def __init__(self) -> None:
        self.url = "https://deoab.oab.org.br/api/v1/organizacao/tipo/conselho-e-seccional"

    def get_council_data(self) -> dict:
        oab = Oab()
        return oab.get_oab_data(self.url)
