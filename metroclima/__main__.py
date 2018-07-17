from . import metroclima
from .options import FileTypes

from click import command, option, echo, Abort

FILE_TYPES = [t.value for t in FileTypes]

@command(name='metroclima')
@option('-f', default='json', help='File type to be retrieved {}'.format(FILE_TYPES))
def full_dump(f):
    """Simple program to retrieve Metroclima data"""
    if f not in FILE_TYPES:
        echo('File type "{}" is unknown. Please use one of {}'.format(f, FILE_TYPES))
        raise Abort()
    metroclima.dump_full_data(f)

if __name__ == '__main__':
    try:
        full_dump()
    except KeyboardInterrupt:
        pass
