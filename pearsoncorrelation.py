from scipy import stats


y=[1,2,3,4,5]

x=[100,101,102,103,104]
pc = stats.pearsonr(x,y)
print(pc)
tau = stats.kendalltau(x,y)
print(tau)
rho = stats.spearmanr(x,y)
print(rho)

x=[100,99,98,97,96]
pc = stats.pearsonr(x,y)
print(pc)
tau = stats.kendalltau(x,y)
print(tau)
rho = stats.spearmanr(x,y)
print(rho)


x=[100,102,103,101,102]
pc = stats.pearsonr(x,y)
print(pc)
tau = stats.kendalltau(x,y)
print(tau)
rho = stats.spearmanr(x,y)
print(rho)
