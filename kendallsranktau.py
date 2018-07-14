from scipy import stats


y=[1,2,3,4,5]

x=[100,101,102,103,104]
tau = stats.kendalltau(x,y)
print(tau)

x=[100,99,98,97,96]
tau = stats.kendalltau(x,y)
print(tau)

x=[100,102,103,101,102]
tau = stats.kendalltau(x,y)
print(tau)