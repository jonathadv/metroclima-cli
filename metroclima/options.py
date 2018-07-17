from enum import Enum

YEARS = (2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018)

QUARTERS = (1, 2, 3, 4)

class Stations(Enum):
    MENINO_DEUS = 1
    MOINHOS_DE_VENTO = 2
    SERRARIA = 3
    SAO_JOAO = 4
    LOMBA_DO_PINHEIRO = 5
    LAMI = 6
    CENTRO_HISTORICO = 7
    SARANDI = 8
    GLORIA = 9
    TRISTEZA = 10

class Months(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

class Sensors(Enum):
    TEMPERATURE = 1
    SENSATION = 2
    HUMIDITY = 3
    RAIN = 4
    PRESSURE = 5
    WIND = 6
    DEW = 7

class PostKeys(Enum):
    STATION = 'f_estacao'
    YEAR = 'f_trimestre_ano'
    QUARTER = 'f_trimestre'
    SENSOR = 'f_campo'
    FILE_TYPE = 'f_tipoArq'
    SEARCH_STATIONS = 'pesquisar_estacoes'

class FileTypes(Enum):
    CSV = 'csv'
    JSON = 'json'
    XLS = 'xls'


