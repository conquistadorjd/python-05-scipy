################################################################################################
#	name:	correlationexamples-00.py
#	desc:	Correlations 
#	date:	2018-07-14
#	Author:	conquistadorjd
#   remark : goodman_kruskal_gamma formula taken from https://github.com/shilad/context-sensitive-sr/blob/master/SRSurvey/src/python/correlation.py
################################################################################################
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from itertools import combinations, permutations

def goodman_kruskal_gamma(m, n):
    """ 
    compute the Goodman and Kruskal gamma rank correlation coefficient; 
    this statistic ignores ties is unsuitable when the number of ties in the
    data is high. it's also slow. 
    >>> x = [2, 8, 5, 4, 2, 6, 1, 4, 5, 7, 4]
    >>> y = [3, 9, 4, 3, 1, 7, 2, 5, 6, 8, 3]
    >>> goodman_kruskal_gamma(x, y)
    0.9166666666666666
    """
    num = 0
    den = 0
    for (i, j) in permutations(range(len(m)), 2):
        m_dir = m[i] - m[j]
        n_dir = n[i] - n[j]
        sign = m_dir * n_dir
        if sign > 0:
            num += 1
            den += 1
        elif sign < 0:
            num -= 1
            den += 1
    return num / float(den)

print('*** Program Started ***')

# x=[1,2,3,4,5]

y1=[101,102,103,104,105,106,107]
y2=[101,100,99,98,97,96,95]
y3=[101,102,101,102,101,102,102]
y4=[101,102,101,101,101,102,103]
# y3=y2
# y4=y1
x=np.arange(len(y1))

pc = stats.pearsonr(x,y1)
tau = stats.kendalltau(x,y1)
rho = stats.spearmanr(x,y1)
gamma = goodman_kruskal_gamma(x,y1)
ax1 = plt.subplot(221)
plt.scatter(x,y1,s=None, marker='o',color='g',edgecolors='g',alpha=0.9,label="Jagur")
# plt.xlabel('Sample x Axis')  
# plt.ylabel('Sample y Axis')  
# plt.legend(loc=2)
# plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.title('PC '+ "{:.3f}".format(pc[0]) + ' tau ' + "{:.3f}".format(tau[0]) + ' rho ' + "{:.3f}".format(rho[0])+ ' gamma ' + "{:.3f}".format(gamma))


pc = stats.pearsonr(x,y2)
tau = stats.kendalltau(x,y2)
rho = stats.spearmanr(x,y2)
gamma = goodman_kruskal_gamma(x,y2)
ax2 = plt.subplot(222)
plt.scatter(x,y2,s=None, marker='o',color='g',edgecolors='g',alpha=0.9,label="Jagur")
# plt.xlabel('Sample x Axis')  
# plt.ylabel('Sample y Axis')  
# plt.legend(loc=2)
# plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.title('PC '+ "{:.3f}".format(pc[0]) + ' tau ' + "{:.3f}".format(tau[0]) + ' rho ' + "{:.3f}".format(rho[0])+ ' gamma ' + "{:.3f}".format(gamma))


pc = stats.pearsonr(x,y3)
tau = stats.kendalltau(x,y3)
rho = stats.spearmanr(x,y3)
gamma = goodman_kruskal_gamma(x,y3)
ax2 = plt.subplot(223)
plt.scatter(x,y3,s=None, marker='o',color='g',edgecolors='g',alpha=0.9,label="Jagur")
# plt.xlabel('Sample x Axis')  
# plt.ylabel('Sample y Axis')  
# plt.legend(loc=2)
# plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.title('PC '+ "{:.3f}".format(pc[0]) + ' tau ' + "{:.3f}".format(tau[0]) + ' rho ' + "{:.3f}".format(rho[0])+ ' gamma ' + "{:.3f}".format(gamma))

pc = stats.pearsonr(x,y4)
tau = stats.kendalltau(x,y4)
rho = stats.spearmanr(x,y4)
gamma = goodman_kruskal_gamma(x,y4)
ax2 = plt.subplot(224)
plt.scatter(x,y4,s=None, marker='o',color='g',edgecolors='g',alpha=0.9,label="Jagur")
# plt.xlabel('Sample x Axis')  
# plt.ylabel('Sample y Axis')  
# plt.legend(loc=2)
# plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.title('PC '+ "{:.3f}".format(pc[0]) + ' tau ' + "{:.3f}".format(tau[0]) + ' rho ' + "{:.3f}".format(rho[0])+ ' gamma ' + "{:.3f}".format(gamma))

# Saving image
plt.savefig('correlationexamples-01.png')

# In case you dont want to save image but just displya it
plt.show()

print('*** Program ended ***')