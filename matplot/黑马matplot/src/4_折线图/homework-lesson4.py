# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



date,open,high,low,close=np.loadtxt('../../000001.csv',delimiter=',', converters={0:mdates.strpdate2num('%m/%d/%Y')},skiprows=1,usecols=(0,1,2,3,4),unpack=True)


plt.plot_date(date,open,'y-')

plt.plot_date(date,high,'g-')

plt.plot_date(date,low,'b-')

plt.plot_date(date,close,'r-')


plt.show()


