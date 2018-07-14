################################################################################################
#	name:	correlationexamples-00.py
#	desc:	Correlations 
#	date:	2018-07-14
#	Author:	conquistadorjd
################################################################################################
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

print('*** Program Started ***')

# x=[1,2,3,4,5]

y=[101,102,105,105,104]
x=np.arange(len(y))
pc = stats.pearsonr(x,y)
print(pc)
tau = stats.kendalltau(x,y)
print(tau)
rho = stats.spearmanr(x,y)
print(rho)

plt.scatter(x,y,s=None, marker='o',color='g',edgecolors='g',alpha=0.9,label="Jagur")

# labels 
plt.xlabel('Sample x Axis')  
plt.ylabel('Sample y Axis')  
plt.title('PC '+ "{:.3f}".format(pc[0]) + ' tau ' + "{:.3f}".format(tau[0]) + ' rho ' + "{:.3f}".format(rho[0]))
plt.legend(loc=2)

# Saving image
plt.savefig('correlationexamples-00.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')