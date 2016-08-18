print "**********************"
print "Monte Carlo Simulation"
print "**********************"

# from bsm_functions import *

from bsm_functions import bsm_call_value
S0 = 100.
K = 105.
T = 1.0
r = 0.05
sigma = 0.2
print bsm_call_value(S0, K, T, r, sigma)

run mcs_pure_python.py

