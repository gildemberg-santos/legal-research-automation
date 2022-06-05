from src.oab import Oab

class ElectronicDiary:
    def __init__(self, id_diary) -> None:
        self.url = f'https://deoab.oab.org.br/api/v1/publicacao/{id_diary}/publicado'

    def get_electronic_diary(self) -> dict:
        oab = Oab()
        return oab.get_oab_data(self.url)
