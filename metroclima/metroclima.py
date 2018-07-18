"""
Metroclima database dumper

Main module
"""

import os
from pathlib import Path

import requests
from requests_html import HTMLSession

from .options import PostKeys

URL = 'http://www2.portoalegre.rs.gov.br/ceic/default.php?p_secao=52'
SESSION = HTMLSession()
XPATH_ERROR = '/html/body/div[6]/div[1]/div'


class MetroclimaError(Exception):
    """ Domain exception """
    pass


def download_file(url, destination_path=None):
    """Download file from given url and stores it in the given destination_path.

    :type url: str
    :type destination_path: str
    :param url: the string url to get
    :param destination_path: the full path to store the file
    :return: file_name: the full file path
    """
    resp = requests.get(url)

    if resp.ok:
        if not destination_path:
            destination_path = os.path.expanduser('~')
        file_name = '{}/{}'.format(destination_path, Path(url).name)
        with open(file_name, 'w') as file:
            file.write(resp.text)
        return file_name

    raise MetroclimaError('Unable to download file. HTTP Code = {}'.format(resp.status_code))


def retrieve_download_url(post_options):
    """POST to Metroclima site and retrieve the URL to the dump file based on the given post options

    :type post_options: dict
    :param post_options: A dict with the POST call options found in metroclima.options.PostKeys
    :return: download_url: The URL of the generated file
    """
    res = SESSION.post(URL, data=post_options)
    for download_url in res.html.links:
        if '.{}'.format(post_options.get(PostKeys.FILE_TYPE.value)) in download_url:
            return download_url

    elem = res.html.xpath(XPATH_ERROR)

    if elem:
        text = elem[0].text.split('\n')[1:3]
        text = ' '.join(text)
    raise MetroclimaError(text, post_options)


# def dump_full_data(file_type):
#     data = {
#         PostKeys.STATION.value: None,
#         PostKeys.YEAR.value: None,
#         PostKeys.QUARTER.value: None,
#         PostKeys.SENSOR.value: None,
#         PostKeys.FILE_TYPE.value: file_type,
#         PostKeys.SEARCH_STATIONS.value: '',
#     }
#
#     for station in Stations:
#         data[PostKeys.STATION.value] = station.value
#
#         for year in YEARS:
#             data[PostKeys.YEAR.value] = year
#
#             for quarter in QUARTERS:
#                 data[PostKeys.QUARTER.value] = quarter
#
#                 for sensor in Sensors:
#                     data[PostKeys.SENSOR.value] = sensor.value
#
#
#                     retrieve_download_url(data)
