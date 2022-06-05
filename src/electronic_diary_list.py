from datetime import datetime
from src.oab import Oab


class ElectronicDiaryList:
    def __init__(self, full_page=True, page=1, term='', start_date=datetime.now(), end_date=datetime.now(), id_organization='') -> None:
        start_date = start_date.strftime('%d/%m/%Y')
        end_date = end_date.strftime('%d/%m/%Y')
        self.url = f'https://deoab.oab.org.br/api/v1/diario/pesquisa?pagina={page}&termo={term}&inicio={start_date}&fim={end_date}&idOrganizacao={id_organization}'

    def get_electronic_diary_list(self) -> dict:
        oab = Oab()
        return oab.get_oab_data(self.url)
