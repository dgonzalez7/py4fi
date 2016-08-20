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

# Strings

t = 'this is a string object'
print t.capitalize()
print t.split()
print t.find('string')
print t.find('Python')
print t.replace(' ', '|')
print 'http://www.python.org'.strip('htp:/')

import re

series = """
'01/18/2014 13:00:00', 100, '1st';
'01/18/2014 13:30:00', 110, '2nd';
'330, '5th','01/22/2014 13:30:00';
'01/18/2014 14:00:00', 120, '3rd'
"""

dt = re.compile("'[0-9/:\s]+'")  # datetime
result = dt.findall(series)
print result

from datetime import datetime         
pydt = datetime.strptime(result[2].replace("'", ""),
		'%m/%d/%Y %H:%M:%S')
print result[2]
print pydt
print type(pydt)


