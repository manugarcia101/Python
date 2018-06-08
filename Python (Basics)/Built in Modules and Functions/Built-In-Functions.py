# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 09:27:23 2018

@author: Manu
"""

#! Python 3.6.3
#Author: Manuel Garcia Lopez

#Built-In-Functions
'''
That is making reference to those functions that doesn't belong to any 
external function but to the standard one
'''
exNum1 = -5
exNum2 = 5

print(abs(exNum1)) #absolute function value

if abs(exNum1) == exNum2:
    print('same numbers')
    
#help function
'''
help() #starts like a search bar with everything explained
import time
help(time)
'''

#max, min functions (they search for the max and min of a list)
exList = [2,4,1,6,8,0] 
print(max(exList))
print(min(exList))

#rounding numbers (this rounds floats and doubles to int)
x = 5.662
print(round(x))

#to more precise rounding we need to import math lib
import math

print(math.floor(x))#to up
print(math.ceil(x))#to down

#other math funcs
'''
math.copysign(x, y)
Return x with the sign of y. On a platform that supports 
signed zeros, copysign(1.0, -0.0) returns -1.0.

math.fabs(x)
Return the absolute value of x.

math.factorial(x)
Return x factorial. Raises ValueError if x is not 
integral or is negative.

math.floor(x)
Return the floor of x as a float, the largest
integer value less than or equal to x.

math.fmod(x, y)
Return fmod(x, y), as defined by the platform C library. 

math.frexp(x)
Return the mantissa and exponent of x as the pair (m, e). m is a float and e is 
an integer such that x == m * 2**e exactly. If x is zero, returns (0.0, 0), otherwise 
0.5 <= abs(m) < 1. This is used to “pick apart” the internal representation of a float in a portable way.

math.fsum(iterable)
Return an accurate floating point sum of values in the iterable. Avoids loss of 
precision by tracking multiple intermediate partial sums:

The algorithm’s accuracy depends on IEEE-754 arithmetic guarantees and the typical 
case where the rounding mode is half-even. On some non-Windows builds, the underlying 
C library uses extended precision addition and may occasionally double-round an intermediate 
sum causing it to be off in its least significant bit.

For further discussion and two alternative approaches, see the ASPN cookbook recipes for accurate 
floating point summation.

math.isinf(x)
Check if the float x is positive or negative infinity.

math.isnan(x)
Check if the float x is a NaN (not a number). For more information on NaNs, see the IEEE 754 standards.

math.ldexp(x, i)
Return x * (2**i). This is essentially the inverse of function frexp().

math.modf(x)
Return the fractional and integer parts of x. Both results carry the sign of x and are floats.

math.trunc(x)
Return the Real value x truncated to an Integral (usually a long integer). Uses the __trunc__ method.

Note that frexp() and modf() have a different call/return pattern than their C equivalents: they take a single argument and return a pair of values, rather than returning their second return value through an ‘output parameter’ (there is no such thing in Python).

For the ceil(), floor(), and modf() functions, note that all floating-point numbers of sufficiently large magnitude are exact integers. Python floats typically carry no more than 53 bits of precision (the same as the platform C double type), in which case any float x with abs(x) >= 2**52 necessarily has no fractional bits.

--Power and logarithmic functions
math.exp(x)
Return e**x.

math.expm1(x)
Return e**x - 1. For small floats x, the subtraction in exp(x) - 1 can result in a significant loss of precision; the expm1() function provides a way to compute this quantity to full precision:

math.log(x[, base])
With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).

Changed in version 2.3: base argument added.

math.log1p(x)
Return the natural logarithm of 1+x (base e). The result is calculated in a way which is accurate for x near zero.

math.log10(x)
Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).

math.pow(x, y)
Return x raised to the power y. Exceptional cases follow Annex ‘F’ of the C99 standard as far as possible. In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0, even when x is a zero or a NaN. If both x and y are finite, x is negative, and y is not an integer then pow(x, y) is undefined, and raises ValueError.

Unlike the built-in ** operator, math.pow() converts both its arguments to type float. Use ** or the built-in pow() function for computing exact integer powers.

math.sqrt(x)
Return the square root of x.

9.2.3. Trigonometric functions
math.acos(x)
Return the arc cosine of x, in radians.

math.asin(x)
Return the arc sine of x, in radians.

math.atan(x)
Return the arc tangent of x, in radians.

math.atan2(y, x)
Return atan(y / x), in radians. The result is between -pi and pi. The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.

math.cos(x)
Return the cosine of x radians.

math.hypot(x, y)
Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y).

math.sin(x)
Return the sine of x radians.

math.tan(x)
Return the tangent of x radians.

--Angular conversion
math.degrees(x)
Convert angle x from radians to degrees.

math.radians(x)
Convert angle x from degrees to radians.

--Hyperbolic functions
math.acosh(x)
Return the inverse hyperbolic cosine of x.

math.asinh(x)
Return the inverse hyperbolic sine of x.

math.atanh(x)
Return the inverse hyperbolic tangent of x.

math.cosh(x)
Return the hyperbolic cosine of x.

math.sinh(x)
Return the hyperbolic sine of x.

math.tanh(x)
Return the hyperbolic tangent of x.

--Special functions
math.erf(x)
Return the error function at x.

math.erfc(x)
Return the complementary error function at x.

math.gamma(x)
Return the Gamma function at x.

math.lgamma(x)
Return the natural logarithm of the absolute 
value of the Gamma function at x.

--Constants
math.pi
math.e
'''
#we can also use functions to cast a variable type and transforme it into another
intMe = 55
print(int(intMe))
print(float(intMe))
print(str(intMe))
