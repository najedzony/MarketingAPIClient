from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = 'Client for Marketing API'

# Setting up
setup(
    name="marketclient",
    version=VERSION,
    author="Najedzony (Dominik Komla)",
    author_email="<example@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'google-cloud-bigquery', 'cached_property', 'pandas', 'pandas-gbq', 'google-cloud-storage'],
    keywords=['python', 'gcp', 'gbq', 'gcs', 'API'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
