Epidemic Python Library
=======================

Introduction
~~~~~~~~~~~~

This Python Library (pip package) is created by Boyuan Liu, with purpose
to help global officials to understand that the danger of epidemic.
Realize that the ultimate ending (assume we have one) for human is more
likely to be a pandemic rather than nuclear warface. Also realize that
we are not prepared for a pandemic, from Ebola to ongoing Coronavirus.

Functions Description/Usage
---------------------------

This python package provide following functions for users: - Linear
Regression - This can help analysts to find a line of best fit based on
provided data. In this package, it’s commonly used as to make
prediction. Example Usage:

.. code:: python

   from epidemic import linear_regression
   """use an input list, output list, and input to predict"""
   linear_regression([1, 2, 3, 4, 5], [282, 314, 581, 846, 1320], 59)
   # return 15273.400

-  Graph, function usage similar to linear regression, it provides a
   graph with all datapoints and a line of best fit. Example usage:

.. code:: python

   from epidemic import graph
   """provide two list represent datapoint"""
   graph([1, 2, 3, 4, 5], [282, 314, 581, 846, 1320])
   # graph shown below

|image0| - Predict, this is a class that contains and predict following
attributes by given year: population, climate_change, democracy_index,
poverty, gdp, life_expectancy, global_health_gdp_average, flights.
Example Usage

.. code:: python

   from epidemic import Predict
   Predict(2020).population()

-  Predict_Epidemic, this is my favorite function to implement, this
   function start with current year (2020), then it based on probability
   gives from each category above, with a special algorithm, to
   calculate the probability of the epidemic happening. Example Usage:

.. code:: python

   from epidemic import Predict_Epidemic
   Predict_Epidemic()
   # try it on your own, don't want to spoil

-  Predict_Virus_Growth, this is another analysis tool that able to
   predict how many people will get infected/death cause by a certain
   virus. Example Usage:

.. code:: python

   from epidemic import Predict_Virus_Growth
   Predict_Virus_Growth([1, 2, 3, 4, 5], [282, 314, 581, 846, 1320], 59)

Installation
~~~~~~~~~~~~

To install, type following command:

.. code:: bash

   pip3 install epidemic

to install this python library.

Disclaimer
==========

This python library shall not guaranteed that it will give correct
output, especially when using ``Predict`` and ``Predict_Epidemic``.
However, this library does created based on a lot of researches done in
the past.

Author
======

This is created by Boyuan Liu, if you have any question or comment want
to make, please `send an email`_ to me.

Video
=====

Coming Soon!

Sources:
========

-  `Climate Change Data`_
-  `Democracy Index Data`_
-  `Poverty Rate`_
-  `GDP`_
-  `Life Expectancy`_
-  `Global Health Spending (GDP Average)`_
-  `Flights`_

Thanks for reading and use this python library.

.. _send an email: mailto:boyuanliu6@yahoo.com?subject=%5BPypi%5D%20epidemic%20comments
.. _Climate Change Data: https://data.giss.nasa.gov/gistemp/graphs/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.txt
.. _Democracy Index Data: https://en.wikipedia.org/wiki/Democracy_Index#Democracy_Index_by_region
.. _Poverty Rate: https://data.worldbank.org/topic/poverty
.. _GDP: https://www.worldometers.info/gdp/
.. _Life Expectancy: https://data.worldbank.org/indicator/SP.DYN.LE00.IN
.. _Global Health Spending (GDP Average): https://www.healthsystemtracker.org/chart-collection/health-spending-u-s-compare-countries/#item-since-1980-the-gap-has-widened-between-u-s-health-spending-and-that-of-other-countries___2018
.. _Flights: https://www.statista.com/statistics/564769/airline-industry-number-of-flights/

.. |image0| image:: https://i.imgur.com/Dg5MYTK.png
