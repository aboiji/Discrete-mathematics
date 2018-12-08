import numpy as np

def pprint( l):
    for a in l:
        print(a)


A = np.array([[12, 4,-12],

             [2, 8, 3],

             [-13, 4, 4]])

pprint(A)

b = np.array([2, -8, 4])

pprint (b)

x = np.linalg.inv(A).dot(b)
pprint(x)
print("1801127 김민수")