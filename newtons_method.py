"""
Implementation of Newton's method in Python
"""
from complex import Complex
from typing import Callable

EPSILON = 1e-10
MAX_STEPS = 1000

def newton(z0 : Complex, f : Callable, fder : Callable) -> Complex:
	global EPSILON, MAX_STEPS
	if abs(fder(z0)) < EPSILON: return z0 # If the derivative is very small, then we should be close to a root
	values = [z0,z0 - f(z0)/fder(z0)]
	iteration = 0

	while iteration < MAX_STEPS and abs(values[-1] - values[-2]) > EPSILON:
		z = values[-1]
		values.append(z - f(z)/fder(z))
		iteration += 1
	return values[-1]