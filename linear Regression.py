# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:12:01 2022

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv ('advertising.csv')
data.head()

fig, axs = plt.subplots(1,3,sharey=True)
data.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(16,8))
data.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1])
data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2])

feautur_col=['TV']
X=data[feautur_col]
Y=data.Sales

from sklearn.linear_model import LinearRegression
lr=LinearRegression()

lr.fit(X,Y)

print(lr.intercept_)
print(lr.coef_)

#y=a+b(X)

result=6.9748214882298925+0.05546477*50
print(result)

mi_mx=pd.DataFrame({'TV':[data.TV.min(),data.TV.max()]})
mi_mx.head()

predt=lr.predict(mi_mx)
predt


data.plot(kind='scatter',x='TV',y='Sales')

plt.plot(mi_mx,predt,c='red',linewidth=2)

import statsmodels.formula.api as smf
lm=smf.ols(formula='Sales ~ TV',data=data).fit()
lm.conf_int()

lm.pvalues

lm.rsquared



feautur_col=['TV','Radio','Newspaper']
X=data[feautur_col]
Y=data.Sales

lr=LinearRegression()
lr.fit(X,Y)

print(lr.intercept_)
print(lr.coef_)

lm.summary()



