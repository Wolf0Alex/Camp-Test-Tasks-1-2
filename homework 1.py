import numpy as np

A = np.zeros((3,3))
print(A)

for i in range(3):
    for g in range(3):
        A[i][g] = int(input('Enter value for A: '))

B = []
for i in range(3):
    B.append(int(input('Enter value for B: ')))
    
solution = np.linalg.solve(A, np.array(B))

print(solution)

np.allclose(np.dot(A, solution), B)
