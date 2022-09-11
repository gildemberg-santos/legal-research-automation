from lixeira.oab import Oab


class Council:
    def __init__(self) -> None:
        self.endpoint = f'organizacao/tipo/conselho-e-seccional'

    def get_council_data(self) -> dict:
        oab = Oab()
        return oab.get_oab_data(endpoint=self.endpoint)
