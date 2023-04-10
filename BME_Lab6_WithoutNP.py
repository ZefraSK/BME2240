import numpy as np
def det_3x3(matrix):
    determinant = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2])-matrix[1][0] * (matrix[0][1] * 
                   matrix[2][2] - matrix[2][1] * matrix[0][2])+ matrix[2][0] * (matrix[0][1] * matrix[1][2] - matrix[1][1] * matrix[0][2]))
    return determinant

def cramer_3x3(A,b):
    
    #Declaring layers of matrix 1
    mat1_top = np.array([b[0],A[0][1],A[0][2]])
    mat1_mid = np.array([b[1],A[1][1],A[1][2]])
    mat1_bot = np.array([b[2],A[2][1],A[2][2]])
    
    #Declaring layers of matrix 2
    mat2_top = np.array([A[0][0],b[0],A[0][2]])
    mat2_mid = np.array([A[1][0],b[1],A[1][2]])
    mat2_bot = np.array([A[2][0],b[2],A[2][2]])
    
    #Declaring layers of matrix 3
    mat3_top = np.array([A[0][0],A[0][1],b[0]])
    mat3_mid = np.array([A[1][0],A[1][1],b[1]])
    mat3_bot = np.array([A[2][0],A[2][1],b[2]])
    
    #making matrix 1,2 and 3
    mat1 = np.array([mat1_top, mat1_mid, mat1_bot])
    mat2 = np.array([mat2_top, mat2_mid, mat2_bot])
    mat3 = np.array([mat3_top, mat3_mid, mat3_bot])  
    
    #debug lines
    #print('Mat1: ' + str(mat1))
    #print('Mat2: ' + str(mat2))
    #print('Mat3: ' + str(mat3))
    
    #finds determinent of original A matrix
    D = det_3x3(A)
    
    #raises an error is determinent of A = 0 becuase would devide by 0
    if D != 0: 
            
        D1 = det_3x3(mat1)
        D2 = det_3x3(mat2)
        D3 = det_3x3(mat3)
        
        X0 = D1/D
        X1 = D2/D
        X2 = D3/D
        
        x = (X0,X1,X2)
    else:
        raise 'error devide by 0'
    return x

# Setting up the data in matrix A and matrix Solution
A = [[1100,-100,-1000],
     [-100,1430,-330],
     [-1000,-330,2330]]
s = [10,0,0]

print('Solving for a Cramer 3x3 without Linalg Commands: ')
print(cramer_3x3(A,s))



