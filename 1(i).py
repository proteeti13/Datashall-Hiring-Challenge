from scipy.optimize import linprog
c = [60, 40, 50]
A = [[-20, -10, -10], [-10, -10, -20]]
b = [-350, -400]

res = linprog(c, A, b)
print('(1)No of packages for -Supplier 1, Supplier 2, Supplier3:',res.x,'\n(2)the minimum cost is:',res.fun)
