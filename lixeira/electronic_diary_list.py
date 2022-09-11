from datetime import datetime
from xmlrpc.client import DateTime
from lixeira.oab import Oab


class ElectronicDiaryList:
    def __init__(self, page: int = 1, term: str = '', start_date: DateTime = datetime.now(), end_date: DateTime = datetime.now(), id_organization: str = '') -> None:
        start_date = start_date.strftime('%d/%m/%Y')
        end_date = end_date.strftime('%d/%m/%Y')
        self.endpoint = f'diario/pesquisa?pagina={page}&termo={term}&inicio={start_date}&fim={end_date}&idOrganizacao={id_organization}'

    def get_electronic_diary_list(self) -> dict:
        oab = Oab()
        return oab.get_oab_data(endpoint=self.endpoint)
