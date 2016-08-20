v = [0.5, 0.75, 1.0, 1.5, 2.0]  # vector of numbers
m = [v,v, v]
print m
print m[1][0]

v1 = [0.5, 1.5]
v2 = [1, 2]
m = [v1, v2]
c = [m, m]  # cube of numbers
print c
print c[1][1][0]

v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = [v, v, v]
print m

v[0] = 'Python'
print m

from copy import deepcopy         
v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = 3 * [deepcopy(v), ]
print m

v[0] = 'Python'
print "New m"

print m

# numpy.ndarray
print "numpy"

import numpy as np

a = np.array([0, 0.5, 1.0, 1.5, 2.0])
print type(a)
print a[:2]

print a.sum()
print a.std()
print a.cumsum()
print a * 2
print a ** 2
print np.sqrt(a)

b = np.array([a, a * 2])
print b
print b[0] # first row
print b[0, 2] # first row, thrid element
print b.sum()

print
print b
print b.sum(axis=0) # sum columns
print b.sum(axis=1) # sum rows

c = np.zeros((2, 3, 4), dtype='i', order='C')  # also: np.ones()
print c

d = np.ones_like(c, dtype='f16', order='C')  # also: np.zeros_like()
print d

print np.shape(c)

# Not numpy
import time

import random
I = 5000
start = time.time()
mat = [[random.gauss(0, 1) for j in range(I)]]
end = time.time()
time_interval = end - start
print "Non numpy 1", time_interval

start = time.time()
q = reduce(lambda x, y: x + y,      \
	[reduce(lambda x, y: x + y, row) \
	for row in mat])
end = time.time()
time_interval = end - start
print "Non numpy 2", time_interval
print q
print type(mat)

# numpy approach
start = time.time()
mat2 = np.random.standard_normal((I, I))
end = time.time()
time_interval = end - start
print "numpy 1", time_interval

start = time.time()
q2 = mat2.sum()
end = time.time()
time_interval = end - start
print "numpy 2", time_interval
print q2
print type(mat2)

dt = np.dtype([('Name', 'S10'), ('Age', 'i4'),
		('Height', 'f'), ('Children/Pets', 'i4', 2)])
s = np.array([('Smith', 45, 1.83, (0, 1)),
		('Jones', 53, 1.72, (2, 2))], dtype=dt)
print s
print s['Name']
print s['Height'].mean()
print s[1]['Age']
