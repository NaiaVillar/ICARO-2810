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

def jacobi_vectorizado(A, b, tol=1e-6, max_iter=100):
    D = diag(A)              #
    R = A - diag(D)          
    x = zeros(len(b))        
    
    for k in range(max_iter):
        x_nuevo = (b - matmul(R, x)) / D
        
        if max(abs(x_nuevo - x)) < tol:
            return x_nuevo
            
        x = x_nuevo
    return x

def mi_svd(A, full_matrices=False):
    # Ejecutamos la descomposición de NumPy
    U, s, Vt = svd(A, full_matrices=full_matrices)
    
    if not full_matrices:
        Sigma = s
    else:
        (N, M) = shape(A)
        Sigma = zeros((N, M))
        for i in range(len(s)):
            Sigma[i, i] = s[i]
            
    return U, Sigma, Vt
#APARTADO 2
q_tunel = np.array([500, 1000, 1500, 2000, 2500, 3000]) 
F_drag_tunel = np.array([12.1, 25.3, 37.8, 51.0, 62.5, 76.2])

def regresion_lineal(A,B):
    V = my_vandermonde(A)
    U, S,VT = mi_svd(V)
    c =  my_transpose(VT) @ diag(1 / S) @ my_transpose(U) @ B
    return c

Resultado = regresion_lineal(q_tunel,F_drag_tunel)
print("la pendiente de la recta", Resultado[1], "y su origen", Resultado[0])


