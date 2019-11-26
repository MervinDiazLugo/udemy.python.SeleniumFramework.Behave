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
        DB_HOST = 'localhost'
        DB_PORT = '5432'
        DB_DATABASE = 'curso_api'
        DB_USER = 'postgres'
        DB_PASS = 'postgres'


    if Environment == 'Test':
        URL = 'https://www.despegar.com.ar/'
        User = 'mdiaz'
        Pass = 'Mm121666'