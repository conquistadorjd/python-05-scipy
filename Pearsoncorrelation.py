from scipy import stats


y=[1,2,2,3,3]

x=[1,2,2,3,3]
pc = stats.pearsonr(x,y)

print(pc)