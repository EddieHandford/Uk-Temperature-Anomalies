# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:55:22 2019
@author: ED
"""
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

from netCDF4 import Dataset
nc = Dataset('mega.nc' , 'r')



########################### Edit Here ###############################
Title = 'Yorkshire & Humber'
x_cor = 25
y_cor = 21
#####################################################################

for i in nc.variables:
    print(i)
 
tas = nc.variables['tasAnom'][:]
month_number = nc.variables['month_number']
year = nc.variables['year']


temps = []
for i in range (84) :
    temps.extend([np.mean([tas[i , y_cor , x_cor , :]])])

             
output_panda = pd.DataFrame({'year':year , 'month_number':month_number , 'temperature':temps})
output_panda.to_csv(Title)
#                   