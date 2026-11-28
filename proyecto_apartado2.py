from numpy import array, zeros,shape,diag, matmul, max, abs
import numpy as np
from numpy.linalg import svd
#Creamos una matriz vandermonde para tenerla de 
def my_vandermonde(x):
    m = len(x)
    n = 2
    V = zeros((m, n))
    for i in range(m):
        for j in range(n):
            V[i, j] = x[i] ** j
    return V

def my_transpose(A):
    (N, M) = shape(A)
    T = zeros((M, N))
    for i in range(N):
        for j in range(M):
            T[j, i] = A[i, j]
    return T

def my_matmul(A, B):
    (N, M) = shape(A)
    (M2, P) = shape(B)
    C = zeros((N, P))
    for i in range(N):          
        for j in range(P):      
            for k in range(M):  
                C[i, j] += A[i, k] * B[k, j]     
    return C

def LU_factorization(A,B):
    #we create a method by which we break into two arrays, U (Upper) and  L(lower), the main one to solve the ecuation
    N = len(A)
    L = zeros((N,N))
    U = zeros((N,N))
    #We calculate the U array
    for i in range(N):
        for j in range(i,N):
            suma = 0
            for k in range(i):
                suma += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - suma
    #We fill the diagonal 
        L[i][i]= 1.0
        for j in range(i+1,N):
            suma = 0
            for k in range(i):
                suma += L[j][k] * U[k][i]
            L[j][i] = (A[j][i] - suma) / U[i][i]

    # (L * z = b)
    z = zeros((N))
    for i in range(N):
        suma = 0
        for k in range(i):
            suma += L[i][k] * z[k]
        z[i] = B[i] - suma

    # (U * x = z)
    x = zeros((N))
    for i in range(N - 1, -1, -1):
        suma = 0
        for k in range(i + 1, N):
            suma += U[i][k] * x[k]
        x[i] = (z[i] - suma) / U[i][i]

    return x


#Codigo del main
q_tunel = np.array([500, 1000, 1500, 2000, 2500, 3000]) 
F_drag_tunel = np.array([12.1, 25.3, 37.8, 51.0, 62.5, 76.2])


def minimos_cuadrados(A,B):
    V = my_vandermonde(A)
    VT = my_transpose(V)
    C = my_matmul(VT,V)
    D = my_matmul(VT,B.reshape(-1,1)).flatten()
    return LU_factorization(C,D) 

Resultado = minimos_cuadrados(q_tunel,F_drag_tunel)
print(Resultado)




