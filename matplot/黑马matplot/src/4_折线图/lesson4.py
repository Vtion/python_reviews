import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time
# x=np.linspace(-10,10,100) # begin stop 均分100份
# y=x**2
# plt.plot(x,y)
# plt.show()


def date2num(s):
    d = datetime.strptime(s.decode('utf-8'), '%m/%d/%Y')
    strTime = d.strftime("%m/%d/%Y")
    print(strTime,end=" ")
    return strTime


date,open,close=np.loadtxt('../../000001.csv',delimiter=',',
                           converters={0: date2num},skiprows=1,usecols=(0,1,4),unpack=True)


plt.plot_date(date,close,'y-')

plt.show()
#
# plt.plot_date(date,close,'go')
#
# plt.plot_date(date,close,'r--')
#
# plt.show()
#
# plt.plot(date, close, color='green', linestyle='dashed', marker='o',
#      markerfacecolor='blue', markersize=12)
#
# plt.show()


