"""
Metroclima database dumper

POST Call options
"""

from enum import Enum

YEARS = (2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018)

QUARTERS = (1, 2, 3, 4)

class Stations(Enum):
    """ Enums for the `f_estacao` POST option """
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
    """ Enums for the `f_mes` POST option """
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
    """ Enums for the `f_campo` POST options """
    TEMPERATURE = 1
    SENSATION = 2
    HUMIDITY = 3
    RAIN = 4
    PRESSURE = 5
    WIND = 6
    DEW = 7

class PostKeys(Enum):
    """ Enums with the POST options """
    STATION = 'f_estacao'
    YEAR = 'f_trimestre_ano'
    QUARTER = 'f_trimestre'
    SENSOR = 'f_campo'
    FILE_TYPE = 'f_tipoArq'
    SEARCH_STATIONS = 'pesquisar_estacoes'

class FileTypes(Enum):
    """ Enums for the the file types """
    CSV = 'csv'
    JSON = 'json'
    XLS = 'xls'
