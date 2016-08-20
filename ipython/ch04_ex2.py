# Tuples
t = (1, 2.5, 'data')
print type(t)
print t[2]
print type(t[2])
print t.count('data')
print t.index(2.5)

# Lists
l = [1, 2.5, 'data']
print l[2]

l = list(t)
print type(l)
print t
print l

l.append([4, 3])
# l.append('append')
print l
l.extend([1.0, 1.5, 2.0])
print l
l.insert(1, 'insert')
print l
l.remove('data')
print l
p = l.pop(3)
print l, p

print l[2:5]

for element in l[2:5]:
	print element ** 2

r = range(0, 8, 1)  # start, end, step width         
print r
print type(r)
for i in range(2,5):
	print l[i] ** 2

for i in range(1, 10):
	if i % 2 == 0:  # % is for modulo
		print "%d is even" % i
	elif i % 3 == 0:
		print "%d is multiple of 3" % i
	else:
		print "%d is odd" % i

total = 0
while total < 100:
	total += 1
print total

# List comprehensions
m = [i ** 2 for i in range(5)]
print m

# Functional programming

def f(x):
	return x ** 2

print f(2)

def even(x):
	return x % 2 == 0         

print even(3)

print map(even, range(10))
print map(lambda x: x ** 2, range(10))

print filter(even, range(15))

print reduce(lambda x, y: x + y, range(10))
print 1+2+3+4+5+6+7+8+9
