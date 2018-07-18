import sys

from click import option, version_option, group, Choice

from . import metroclima
from .__version__ import __version__, __title__
from .options import FileTypes, Sensors, Stations, YEARS, QUARTERS
from .options import PostKeys

FILE_TYPES = [t.value for t in FileTypes]
SENSORS = [s.name for s in Sensors]
STATIONS = [l.name for l in Stations]
YEAR_OPTIONS = [str(y) for y in YEARS]
QUARTER_OPTIONS = [str(q) for q in QUARTERS]


def _stderr(message, end='\n', flush=False):
    if flush:
        sys.stderr.flush()
    print(message, file=sys.stderr, end=end)


def _stdout(message, end='\n'):
    print(message, end=end)


@group(context_settings={'help_option_names': ['-h', '--help']})
@version_option(version=__version__, prog_name=__title__)
def cli():
    """A simple tool to retrieve information from the Porto Alegre city's Metroclima database."""
    pass


@cli.command('get')
@option('-f', '--filetype', type=Choice(FILE_TYPES), default='csv', help='The dump file type')
@option('-y', '--year', type=Choice([str(i) for i in YEARS]), default=YEAR_OPTIONS[-1],
        help='The year to get information')
@option('-q', '--quarter', type=Choice([str(q) for q in QUARTERS]), default=str(QUARTER_OPTIONS[0]),
        help='The quarter to get information')
@option('-s', '--sensor', type=Choice(SENSORS), default=SENSORS[0], help='The sensor to get information')
@option('-l', '--station', type=Choice(STATIONS), default=STATIONS[0], help='The station to get information')
@option('-d', '--download', is_flag=True, default=False, help="Downloads ")
def get_single_dump(filetype, year, quarter, sensor, station, download):
    """Retrieve dump from Metroclima site"""
    options = {
        PostKeys.FILE_TYPE.value: filetype,
        PostKeys.YEAR.value: int(year),
        PostKeys.QUARTER.value: int(quarter),
        PostKeys.STATION.value: Stations[station].value,
        PostKeys.SENSOR.value: Sensors[sensor].value,
        PostKeys.SEARCH_STATIONS.value: '',
    }

    try:
        _stderr('Retrieving download URL...')
        url = metroclima.retrieve_download_url(options)

        _stdout(url)
        if download:
            _stderr('Downloading file...')

            file_name = metroclima.download_file(url)
            _stderr('File download at ', end='')
            _stdout(file_name)

    except metroclima.MetroclimaError as e:
        _stderr(e)


def run():
    cli(prog_name=__title__)
