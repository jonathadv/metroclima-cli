import sys

from requests_html import HTMLSession
from .options import QUARTERS, YEARS, PostKeys, Sensors, Stations

URL = 'http://www2.portoalegre.rs.gov.br/ceic/default.php?p_secao=52'
SESSION = HTMLSession()
XPATH_ERROR = '/html/body/div[6]/div[1]/div'


class NotFoundError(Exception):
    pass


def retrieve_download_url(data):
    r = SESSION.post(URL, data=data)
    for download_url in r.html.links:
        if '.{}'.format(data.get(PostKeys.FILE_TYPE.value)) in download_url:
            return download_url

    elem = r.html.xpath(XPATH_ERROR)

    if elem:
        text = elem[0].text.split('\n')[1:3]
        text = ' '.join(text)
    raise NotFoundError(text, data)


def dump_full_data(file_type):
    data = {
        PostKeys.STATION.value: None,
        PostKeys.YEAR.value: None,
        PostKeys.QUARTER.value: None,
        PostKeys.SENSOR.value: None,
        PostKeys.FILE_TYPE.value: file_type,
        PostKeys.SEARCH_STATIONS.value: '',
    }

    for station in Stations:
        data[PostKeys.STATION.value] = station.value

        for year in YEARS:
            data[PostKeys.YEAR.value] = year

            for quarter in QUARTERS:
                data[PostKeys.QUARTER.value] = quarter

                for sensor in Sensors:
                    data[PostKeys.SENSOR.value] = sensor.value

                    try:
                        print(retrieve_download_url(data))
                    except NotFoundError as e:
                        print('ERROR: {}'.format(e), file=sys.stderr)
