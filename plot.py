# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stock=pd.read_csv('AAPL Historical Data.csv',usecols=[0,1,2,3,4])

avrg=stock[['Price','Open','High','Low']].mean(axis=1)

date=np.arange(1,len(stock)+1,1)

plt.plot(date,avrg,'r',label='myfirst plot')