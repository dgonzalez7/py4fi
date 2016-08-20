a = 10
print type(a)
print a.bit_length()

a = 100000
print a.bit_length()

googol = 10 ** 100
print googol
print googol.bit_length()

print 1 + 4
print 1 / 4
print type(1 / 4)

print 1. / 4.
print type(1. / 4.)

b = 0.35
print type(b)
print b + 0.1

c = 0.5
print c.as_integer_ratio()
print b.as_integer_ratio()



import decimal
from decimal import Decimal
print decimal.getcontext()

d = Decimal(1) / Decimal(11)
print d

decimal.getcontext().prec = 4
e = Decimal(1) / Decimal(11)
print e

decimal.getcontext().prec = 50
f = Decimal(1) / Decimal(11)
print f

g = d + e + f
print g 

