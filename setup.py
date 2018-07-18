# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from metroclima.__version__ import __version__, __description__, __title__, __author__, __author_email__, __copyright__, __license__, __url__

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

REQUIRED = ['click', 'requests', 'requests-html']

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
