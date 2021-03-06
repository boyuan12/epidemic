# Epidemic Python Library

[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/boyuan12/epidemic/?ref=repository-badge)

### Introduction
This Python Library (pip package) is created by Boyuan Liu, with purpose to help global officials to understand that the danger of epidemic. Realize that the ultimate ending (assume we have one) for human is more likely to be a pandemic rather than nuclear warface. Also realize that we are not prepared for a pandemic, from Ebola to ongoing Coronavirus.

### Installation
To install, type following command: 
```bash
pip3 install epidemic
```
to install this python library.

## Functions Description/Usage
This python package provide following functions for users:
- Linear Regression - This can help analysts to find a line of best fit based on provided data. In this package, it's commonly used as to make prediction. Example Usage:
```python
from epidemic import linear_regression
"""use an input list, output list, and input to predict"""
linear_regression([1, 2, 3, 4, 5], [282, 314, 581, 846, 1320], 59)
# return 15273.400
```
- Graph, function usage similar to linear regression, it provides a graph with all datapoints and a line of best fit. Example usage:
```python
from epidemic import graph
"""provide two list represent datapoint"""
graph([1, 2, 3, 4, 5], [282, 314, 581, 846, 1320])
# graph shown below
```
![](https://i.imgur.com/Dg5MYTK.png)
- Predict, this is a class that contains and predict following attributes by given year: population, climate_change, democracy_index, poverty, gdp, life_expectancy, global_health_gdp_average, flights. Example Usage
```python
from epidemic import Predict
Predict(2020).population()
```
- Predict_Epidemic, this is my favorite function to implement, this function start with current year (2020), then it based on probability gives from each category above, with a special algorithm, to calculate the probability of the epidemic happening. Example Usage:
```python
from epidemic import Predict_Epidemic
Predict_Epidemic()
# try it on your own, don't want to spoil
```
- Predict_Virus_Growth, this is another analysis tool that able to predict how many people will get infected/death cause by a certain virus. Example Usage:
```python
from epidemic import Predict_Virus_Growth
Predict_Virus_Growth([1, 2, 3, 4, 5], [282, 314, 581, 846, 1320], 59)
```

# Disclaimer
This python library shall not guaranteed that it will give correct output, especially when using `Predict` and `Predict_Epidemic`. However, this library does created based on a lot of researches done in the past. 

# Author
This is created by Boyuan Liu, if you have any question or comment want to make, please [send an email](mailto:boyuanliu6@yahoo.com?subject=[Pypi]%20epidemic%20comments) to me.

# Video
Coming Soon!

# CLI
There is a CLI available, upon install, this should automatically be availble. Execute like this:
```bash
predict-epidemic [-h] year
```

# Sources:
- [Climate Change Data](https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt)
- [Democracy Index Data](https://en.wikipedia.org/wiki/Democracy_Index#Democracy_Index_by_region)
- [Poverty Rate](https://data.worldbank.org/topic/poverty)
- [GDP](https://www.worldometers.info/gdp/)
- [Life Expectancy](https://data.worldbank.org/indicator/SP.DYN.LE00.IN)
- [Global Health Spending (GDP Average)](https://www.healthsystemtracker.org/chart-collection/health-spending-u-s-compare-countries/#item-since-1980-the-gap-has-widened-between-u-s-health-spending-and-that-of-other-countries___2018)
- [Flights](https://www.statista.com/statistics/564769/airline-industry-number-of-flights/)

Thanks for reading and use this python library.

Version 0.0.8
