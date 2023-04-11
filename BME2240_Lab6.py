import numpy as np

# Setting up the data in matrix A and matrix Solution
A = [[1100,-100,-1000],
     [-100,1430,-330],
     [-1000,-330,2330]]
s = [10,0,0]

# Solving for I1,I2,I3 using Cramer
A_inv = np.linalg.inv(A)
x = np.dot(A_inv,s)
print('I1, I2, I3 - using Cramer')
print(x,end='\n\n')

print('Inverted Matrix A: ')
print('| {:} {:} {:}  |'.format(A_inv[0][0],A_inv[0][1],A_inv[0][2]))
print('| {:} {:} {:} |'.format(A_inv[1][0],A_inv[1][1],A_inv[1][2]))
print('| {:} {:} {:} |\n'.format(A_inv[2][0],A_inv[2][1],A_inv[2][2]))


# Solving for I1,I2,I3 using linalg.solve()
x = np.linalg.solve(A,s)
print('I1, I2, I3 - using linalg.solve()')
print(x)