################################################################################################
#	name:	linear-regression-03-scipy.py
#	desc:	linear regression using  scipy
#	date:	2018-07-14
#	Author:	conquistadorjd
#   reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
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
y6=[1,2,3,4,5,6,7]
y=y5

x=np.arange(len(y))
x1=np.arange(len(y))
x = x +1 # to ensure count is starting from 1

##################################### regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print('Coefficients: \n', slope, intercept, r_value, p_value, std_err)

pc = stats.pearsonr(x1,y)
print(pc)
# tau = stats.kendalltau(x,y)
# print(tau)
# rho = stats.spearmanr(x,y)
# print(rho)

# xx= x
# yy = regr.predict(xx)
plt.scatter(x,y,s=None, marker='o',color='g',edgecolors='g',alpha=0.9,label="Jagur")
plt.plot(x, intercept + slope*x, label='fitted line')
# # plt.xlabel('Sample x Axis')  
# # plt.ylabel('Sample y Axis')  
# # plt.legend(loc=2)
# # plt.grid(color='black', linestyle='-', linewidth=0.5)
# # plt.title('PC '+ "{:.3f}".format(pc[0]) + ' tau ' + "{:.3f}".format(tau[0]) + ' rho ' + "{:.3f}".format(rho[0])+ ' gamma ' + "{:.3f}".format(gamma), fontsize=8)

# # Saving image
plt.savefig('linear-regression-03-scipy.png')

# # In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')