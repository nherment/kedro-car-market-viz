
from plotnine import ggplot, aes, ggsave, geom_point, geom_bar, geom_smooth, labs
from kedro.pipeline import node

import re

d3_d5 = re.compile('(D3|D5)')


def filter(cars):
  cars = cars[(cars.year >= 2015)]
  cars = cars[(cars.km >= 80000)]
  # cars = cars[(cars.model == 'v70')]
  cars = cars[(cars.gas == 'Diesel')]
  # cars = cars[(cars.label.str.contains('Classic'))]
  return cars

def draw(cars):

  cars = filter(cars)

  draw_km_depreciation(cars)
  draw_age_depreciation(cars)
  draw_gas_types(cars)
  draw_transmission_types(cars)

  cars_by_model = cars.groupby('model')
  for model,cars_from_single_model in cars_by_model:
    draw_km_depreciation(cars_from_single_model, '_' + model)
    draw_age_depreciation(cars_from_single_model, '_' + model)
    draw_gas_types(cars_from_single_model, '_' + model)
    draw_transmission_types(cars_from_single_model, '_' + model)

  # print(cars)
  return cars

def draw_km_depreciation(cars, suffix=''):
  scatter_plot = (
    ggplot(cars, aes(x='km', y='price', color='model')) 
    + geom_point()
    + geom_smooth(method='lm')
    + labs(x='Kilometers', y='Price (SEK)')
  )
  ggsave(plot=scatter_plot, filename='data/08_reporting/km_depreciation'+suffix+'.png', dpi=1000)

def draw_age_depreciation(cars, suffix=''):

  year_plot = (
    ggplot(cars, aes(x='year', y='price', color='model')) 
    + geom_point()
    + geom_smooth(method='lm')
    + labs(x='Year', y='Price (SEK)')
  )
  ggsave(plot=year_plot, filename='data/08_reporting/age_depreciation'+suffix+'.png', dpi=1000)


def draw_gas_types(cars, suffix=''):
  gas_types_plot = ggplot(cars) + geom_bar(aes(x='gas'))
  ggsave(plot=gas_types_plot, filename='data/08_reporting/gas_types'+suffix+'.png', dpi=1000)


def draw_transmission_types(cars, suffix=''):
  transmission_types_plot = ggplot(cars) + geom_bar(aes(x='drive'))
  ggsave(plot=transmission_types_plot, filename='data/08_reporting/transmission_types'+suffix+'.png', dpi=1000)

scatter_node = node(func=draw, inputs=['cars'], outputs=None)
filter_node = node(func=filter, inputs=['cars'], outputs='filtered_cars')