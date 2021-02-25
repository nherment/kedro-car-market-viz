from setuptools import setup

setup(
    name='kedro_car_market_viz',
    version='0.0.1',
    description='A library to view analysis of the sales information of cars',
    license='Apache-2',
    packages=['kedro_car_market_viz'],
    author='Nicolas Herment',
    author_email='nicolas.herment@nearform.com',
    keywords=['kedro', 'visualization', 'cars'],
    install_requires=['kedro>=0.17.0,<1', 'plotnine>=0.7.1,<1'],
    url='https://github.com/nherment/kedro-car-market-viz'
)

