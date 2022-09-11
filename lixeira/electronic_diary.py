from lixeira.oab import Oab


class ElectronicDiary:
    def __init__(self, id_diary: int) -> None:
        self.endpoint = f'publicacao/{id_diary}/publicado'

    def get_electronic_diary(self) -> dict:
        oab = Oab()
        return oab.get_oab_data(endpoint=self.endpoint)
