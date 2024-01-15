#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:20:28 2024

@author: soham
"""

from numpy import *
from matplotlib.pyplot import*
from scipy.optimize import curve_fit

time,_= loadtxt("muon_1.txt",unpack="True")
sort_time= sort(time)

sort_time_actual=[]
for i in range(1,len(sort_time)):
    if sort_time[i]<10000:
        sort_time_actual.append(sort_time[i])
#print(sort_time_actual)

distinct_time=[sort_time_actual[0]]
for i in range(1,len(sort_time_actual)):
    if (sort_time_actual[i]!=sort_time_actual[i-1]):
        distinct_time.append(sort_time_actual[i])
        
#print(distinct_time)
count=[]
for j in range(len(distinct_time)):
    cnt=0
    for i in range(len(sort_time_actual)):
        if sort_time_actual[i]==distinct_time[j]:
            cnt=cnt+1
    count.append(cnt)
    #print(cnt)

scatter(distinct_time,count,c="k")

fit,err= curve_fit(lambda x,N0,l,B: N0*exp(-l*x)+B, distinct_time, count)
print(1e-3/fit[1])

dist_x= linspace(min(distinct_time), max(distinct_time))
plot(dist_x,fit[0]*exp(-fit[1]*dist_x)+fit[2],"r",linewidth=2)