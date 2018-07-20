"""
Metroclima database CLI tool

CLI implementation
"""
# pylint: disable=too-many-arguments
# pylint: disable=unexpected-keyword-arg

import sys

from click import Choice, group, option, version_option

from . import metroclima
from .__version__ import __title__, __version__
from .options import QUARTERS, YEARS, FileTypes, PostKeys, Sensors, Stations

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
@option('-f', '--filetype',
        type=Choice(FILE_TYPES),
        default='csv',
        help='The dump file type')
@option('-y', '--year',
        type=Choice([str(i) for i in YEARS]),
        default=YEAR_OPTIONS[-1],
        help='Choose which year')
@option('-q', '--quarter',
        type=Choice([str(q) for q in QUARTERS]),
        default=str(QUARTER_OPTIONS[0]),
        help='Choose which quarter')
@option('-s', '--sensor',
        type=Choice(SENSORS),
        default=SENSORS[0],
        help='Choose the type of sensor')
@option('-l', '--station',
        type=Choice(STATIONS),
        default=STATIONS[0],
        help='Choose which station')
@option('-d', '--download',
        is_flag=True,
        default=False,
        help="Downloads ")
def get_single_dump(filetype, year, quarter, sensor, station, download):
    """Retrieve dump from Metroclima site
    :type download: bool
    :type station: str
    :type sensor: str
    :type quarter: str
    :type year: str
    :type filetype: str
    :param filetype: the file extension.
    :param year: the year of reference for the data do be retrieved.
    :param quarter: the year's quarter of reference for the data do be retrieved.
    :param sensor: the sensor from which the information shoule be retrieved.
    :param station: from which location the information belongs to.
    :param download: determine if the tool should download the file or retreive the URL only.
    """

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
            _stderr('File download at:')
            _stdout(file_name)

    except metroclima.MetroclimaError as err:
        _stderr(err)


def run():
    """ Call cli setting the program title """
    cli(prog_name=__title__)
