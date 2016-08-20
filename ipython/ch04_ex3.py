# Dicts
d = {
     'Name' : 'Angela Merkel',
     'Country' : 'Germany',
     'Profession' : 'Chancelor',
     'Age' : 60
     }
print type(d)
print d['Name'], d['Age']

print d.keys()
print d.values()
print d.items()

birthday = True
if birthday is True:
	d['Age'] += 1         
print d['Age']

for item in d.iteritems():
	print item
for value in d.itervalues():
	print value

# Sets

s = set(['u', 'd', 'ud', 'du', 'd', 'du'])         
print s

t = set(['d', 'dd', 'uu', 'u'])
print s.union(t) # all of s and t
print s.intersection(t)  # both in s and t
print s.difference(t)  # in s but not in t
print t.difference(s)  # in t but not in s
print s.symmetric_difference(t) # in one but not the other

# Eliminate duplicates
print
from random import randint
l = [randint(0, 10) for i in range(1000)]
print len(l)
print l[:20]
s = set(l)
print s
