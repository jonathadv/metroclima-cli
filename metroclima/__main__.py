"""
Metroclima database CLI tool

CLI caller
"""
from .cli import run

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        pass
