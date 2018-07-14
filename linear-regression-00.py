################################################################################################
#	name:	linear-regression-01.py
#	desc:	linear-regression-01.py 
#	date:	2018-07-14
#	Author:	conquistadorjd
################################################################################################
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.sandbox.regression.predstd import wls_prediction_std

print('*** Program started ***')

nsample = 100
x = np.linspace(0, 10, 100)
X = np.column_stack((x, x**2))
beta = np.array([1, 0.1, 10])
e = np.random.normal(size=nsample)

X = sm.add_constant(X)
y = np.dot(X, beta) + e

model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

print('y : ', y)
print('X : ', X)

print('*** Program ended ***')