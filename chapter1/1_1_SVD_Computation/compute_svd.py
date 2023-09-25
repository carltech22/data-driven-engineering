# Compute SVD Full and Economy
# Carlos Zuna Largo 

import numpy as np

# Create random data Matrix
X = np.array([[1,2],[3,4],[5,6],[7,8]])
print("Matrix X = size" + str(X.shape))
print(X)

# Full SVD
print("**** Full SVD ****")

U,S,VT = np.linalg.svd(X,full_matrices=True) 
print("Matrix U = size" + str(U.shape))
print(U)

print("Matrix S = " + str(S.shape))
print(S)

print("Matrix VT = size" + str(VT.shape))
print(VT)

#Economy SVD
print("**** Economy SVD ****")

Uhat, Shat, VThat = np.linalg.svd(X,full_matrices=False) 
print("Matrix U = size" + str(Uhat.shape))
print(Uhat)

print("Matrix S = " + str(Shat.shape))
print(Shat)

print("Matrix VT = size" + str(VThat.shape))
print(VThat)
