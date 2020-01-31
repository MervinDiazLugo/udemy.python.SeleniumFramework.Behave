import os

class Inicializar():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json = basedir + u"/pages"

    Environment = 'Dev'

    # BROWSER DE PRUEBAS
    NAVEGADOR = u'CHROME'

    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/data/capturas'

    # HOJA DE DATOS EXCEL
    Excel = basedir + u'/data/DataTest.xlsx'

    if Environment == 'Dev':
        URL = 'https://www.spotify.com/py/signup/'
        User = 'mdiaz'
        Pass = 'Mm121666'

        #DATABASE CATALOG
        DB_HOST = 'localhost'
        DB_PORT = '5432'
        DB_DATABASE = 'curso_api'
        DB_USER = 'postgres'
        DB_PASS = 'postgres'

        # JsonData
        Json = basedir + u"\pages"
        JsonResponseData = basedir + u"\data\json"

        # API
        API_hostAddressBase = "https://petstore.swagger.io/v2/"
        API_User = "webapi"
        API_Pass = "suipacha"

        API_headers = {
            'version': '1.0-preview.1',
            'content-type': 'application/json',
        }

        API_body = {}


    if Environment == 'Test':
        URL = 'https://www.despegar.com.ar/'
        User = 'mdiaz'
        Pass = 'Mm121666'