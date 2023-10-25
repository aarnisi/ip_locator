from setuptools import setup, find_packages

setup(
    name='iptracking',
    version='1.0.2',
    url = 'https://github.com/aarnisi/ip_locator/',
    packages=find_packages(),
    install_requires=[
        'geopy'
       ,'ipinfo'
    ],
)
