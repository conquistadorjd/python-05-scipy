################################################################################################
#	name:	linear-regression-02-scikit-learn.py
#	desc:	linear regression using scikit-learn
#	date:	2018-07-14
#	Author:	conquistadorjd
#   reference: http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
################################################################################################
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats


print('*** Program started ***')

##################################### Testing different patterns
y1=[101,102,103,104,105,106,107]
y2=[101,100,99,98,97,96,95]
y3=[101,102,101,102,101,102,101]
y4=[101,103,105,107,109,111,115]
y5=[101,103,102,105,102,107,105]
y=[1,2,3,4,5,6,7]
y=y5

x=np.arange(len(y))
x1=np.arange(len(y))
x = x +1 # to ensure count is starting from 1
x = np.array(x).reshape(-1, 1)

##################################### regression
regr = linear_model.LinearRegression()
regr.fit(x, y)

print('Coefficients: \n', regr)
m=regr.coef_[0]
b=regr.intercept_
print("slope=",m, "\nintercept=",b)


pc = stats.pearsonr(x1,y)
print(pc)
# tau = stats.kendalltau(x,y)
# print(tau)
# rho = stats.spearmanr(x,y)
# print(rho)

xx= x
yy = regr.predict(xx)
plt.scatter(x,y,s=None, marker='o',color='g',edgecolors='g',alpha=0.9,label="Jagur")
plt.plot(xx,yy)
# plt.xlabel('Sample x Axis')  
# plt.ylabel('Sample y Axis')  
# plt.legend(loc=2)
# plt.grid(color='black', linestyle='-', linewidth=0.5)
# plt.title('PC '+ "{:.3f}".format(pc[0]) + ' tau ' + "{:.3f}".format(tau[0]) + ' rho ' + "{:.3f}".format(rho[0])+ ' gamma ' + "{:.3f}".format(gamma), fontsize=8)

# Saving image
plt.savefig('linear-regression-02-scikit-learn.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')