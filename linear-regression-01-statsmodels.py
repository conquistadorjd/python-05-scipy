################################################################################################
#	name:	linear-regression-01-statsmodels.py
#	desc:	linear regression using statsmodels
#	date:	2018-07-14
#	Author:	conquistadorjd
#   reference: http://www.statsmodels.org/dev/examples/notebooks/generated/ols.html
################################################################################################
import numpy as np
import statsmodels.api as sm
from scipy import stats
import matplotlib.pyplot as plt

print('*** Program started ***')

##################################### Testing different patterns
y1=[101,102,103,104,105,106,107]
y2=[101,100,99,98,97,96,95]
y3=[101,102,101,102,101,102,101]
y4=[101,103,105,107,109,111,115]
y5=[101,103,102,105,102,107,105]
y6=[1,2,3,4,5,6,7]
y=y5


x =np.arange(len(y))
x = x +1
# this is to preserve original x values to be used for plotting
x1=x
# This is needed as per statsmodel documentation
x=sm.add_constant(x)
##################################### regression
model = sm.OLS(y,x)
results = model.fit()

# print(results.summary())
# print('Parameters: ', results.params)
print( 'results.params : ',results.params)

# pc = stats.pearsonr(x,y5)
# print(pc)
# tau = stats.kendalltau(x,y5)
# print(tau)
# rho = stats.spearmanr(x,y5)
# print(rho)

# creating regression line
xx= x1
yy = results.params[0] + x1*results.params[1]
plt.scatter(x1,y,s=None, marker='o',color='g',edgecolors='g',alpha=0.9,label="Jagur")
plt.plot(xx,yy)
# plt.xlabel('Sample x Axis')  
# plt.ylabel('Sample y Axis')  
# plt.legend(loc=2)
# plt.grid(color='black', linestyle='-', linewidth=0.5)
# plt.title('PC '+ "{:.3f}".format(pc[0]) + ' tau ' + "{:.3f}".format(tau[0]) + ' rho ' + "{:.3f}".format(rho[0])+ ' gamma ' + "{:.3f}".format(gamma), fontsize=8)


# Saving image
plt.savefig('linear-regression-01-statsmodels.png')

# # In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')