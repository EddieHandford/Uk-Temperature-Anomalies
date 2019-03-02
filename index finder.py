# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 00:06:20 2019

@author: Eddie
"""

#index finder program

import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

from netCDF4 import Dataset
nc = Dataset('mega.nc' , 'r')




projection_y_coordinate = nc.variables['projection_y_coordinate'][:]
projection_x_coordinate = nc.variables['projection_x_coordinate'][:]

entered_x = 445856.25
entered_y = 435993.75

index_x = min(projection_x_coordinate , key=lambda x:abs(x-entered_x))
index_y = min(projection_y_coordinate , key=lambda x:abs(x-entered_y))

print(index_x)
print(index_y)