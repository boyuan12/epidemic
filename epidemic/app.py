from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import os
from datetime import date
import math
import numpy as np
import matplotlib.pyplot as plt

history = [2009, 2013, 2014, 2015, 2016, 2020]

def linear_regression(input_i, output_o, return_val):
    input_i = np.array(input_i, dtype=float)
    output_o = np.array(output_o, dtype=float)
    m, b = np.polyfit(input_i, output_o, 1)
    return m * return_val + b


def graph(input_i, output_o):
    input_i = np.array(input_i, dtype=float)
    output_o = np.array(output_o, dtype=float)
    m, b = np.polyfit(input_i, output_o, 1)
    plt.plot(input_i, output_o, 'o')
    plt.plot(input_i, m*output_o + b)
    plt.show()

class Predict:
    def __init__(self, year):
        self.year = year

    def population(self):
        C = (1.86 + 0.01) * 10**11
        small_t = 42+1
        T_0 = 2007+1
        T = self.year
        estimated_pop_1 = (C / small_t) * math.acos((T_0 - T) / small_t)
        return int(estimated_pop_1) - 200000000

    def climate_change(self):
        # Source: https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt
        return linear_regression([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019], [0.65, 0.66, 0.69, 0.74, 0.78, 0.83, 0.87, 0.91, 0.95, 0.98], self.year)

    def democracy_index(self):
        # Source: https://en.wikipedia.org/wiki/Democracy_Index#Democracy_Index_by_region
        return linear_regression([2006, 2008, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], [5.52, 5.55, 5.46, 5.49, 5.52, 5.53, 5.55, 5.55, 5.52, 5.48, 5.48], self.year)

    def poverty(self):
        # Source: https://data.worldbank.org/topic/poverty
        return linear_regression([1999, 2005, 2008, 2010, 2011, 2012, 2013, 2015], [25.5, 20.7, 18.2, 15.7, 13.7, 12.8, 11.2, 10], self.year)

    def gdp(self):
        # Source: https://www.worldometers.info/gdp/, unit: Trillion
        return linear_regression([2010, 2011, 2012, 2013, 2014, 2015, 2016], [66.04, 73.37, 75.06, 77.22, 73.73, 75.83, 77.80], self.year)

    def life_expectancy(self):
        # Source: https://data.worldbank.org/indicator/SP.DYN.LE00.IN
        return linear_regression([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017], [70.556, 70.884, 71.172, 71.462, 71.742, 71.948, 72.182, 72.383], self.year)

    def global_health_gdp_average(self):
        # Source: https://www.healthsystemtracker.org/chart-collection/health-spending-u-s-compare-countries/#item-since-1980-the-gap-has-widened-between-u-s-health-spending-and-that-of-other-countries___2018
        return linear_regression([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017], [10, 10.11, 10.24, 10.46, 10.52, 10.57, 10.62, 10.54], self.year)

    def flights(self):
        # Source: https://www.statista.com/statistics/564769/airline-industry-number-of-flights/
        return linear_regression([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], [27.8, 30.1, 31.2, 32, 33, 34, 35.2, 36.4, 38.1], self.year)


def Predict_Epidemic():

    year = date.today().year
    probability = {}

    for i in range(10):

        climate_change = Predict(year).climate_change() / Predict(year-1).climate_change() # 20%
        if climate_change < 1:
            climate_change = -climate_change

        democracy_index = Predict(year).democracy_index() / Predict(year).democracy_index() #10%
        if democracy_index > 1:
            democracy_index = -democracy_index

        poverty = Predict(year).poverty() / Predict(year-1).poverty() # 10%
        if poverty < 1:
            poverty = -poverty

        gdp = Predict(year).gdp() / Predict(year-1).gdp() # 10%
        if gdp > 1:
            gdp = -gdp

        life_expectancy = Predict(year).life_expectancy() / Predict(year-1).life_expectancy() # 10%
        if life_expectancy > 1:
            life_expectancy = -life_expectancy

        global_health_gdp_average = Predict(year).global_health_gdp_average() / Predict(year-1).global_health_gdp_average() # 30 %
        if global_health_gdp_average > 1:
            global_health_gdp_average = -global_health_gdp_average

        flights = Predict(year).flights() # 10%
        if poverty > 1:
            poverty = -poverty

        score = climate_change * 0.2 + democracy_index * 0.1 + poverty * 0.1 + gdp * 0.1 + life_expectancy * 0.1 + global_health_gdp_average * 0.3 + flights * 0.1
        try:
            probability[year] = score + probability[year-1]
        except KeyError:
            probability[year] = 50 + score
        year+=1

    for key in probability:
        if probability[key] > 70:
            return key


def Predict_Virus_Growth(day1, day2, day3, day4, day5, predict):
    # expoential
    b = day2 / day1
    a = day1
    x = 4

    expo = a * (b ** x)

    # linear
    line = linear_regression([1, 2, 3], [day1, day2, day3], 5)

    if abs(expo - day5) > abs(line - day5):
        return a * (b ** predict)
    else:
        return linear_regression([1, 2, 3, 4, 5], [day1, day2, day3, day4, day5], predict)
