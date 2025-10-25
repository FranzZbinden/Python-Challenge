# (https://www.learnbyexample.org/python-numbers/)
# Integers in binary, octal and hexadecimal formats

# binary
print(0b10111011)
# Prints 187

# octal
print(0o10)
# Prints 8

# hex
print(0xFF)
# Prints 255

#-----------------------------------------------------

# From int to Bin, hex, Oct

# Converts int to octal
val = 4
print(oct(val))

# Converts int to octal
val = 4
print(hex(val))

# Converts int to octal
val = 4
print(bin(val))

#======================================================

# Booleans are internally integers from (0-1)
# Proof:

print("True + 1:", True + 1)

print("false -1:", False - 1)

#======================================================

# For Scientific Notations in Python:
# using e or E

print("1234 to 1234e3:", 1234e3)

print("1234 to 1234e3:", 1234e-3)

#-----------------------------------------------------

# Using variables
a = 1234
print("1234e2:", a * 10**2) 

print("1234e-2:",a* 10**-2)

#======================================================

# Maximum value of a float
print(1.79e308)
# Prints 1.79e+308

print(1.8e308)
# Prints inf

infiniteNum = 1.8e308

print(type(infiniteNum))

#------------------------------------------------------

# However, the minimum value a float can have is approximately 5.0×10-324 . Any number, less than that is considered zero.

# Minimum value of a float
print(5e-324)
# Prints 4.94065645841e-324

print(5e-325)
# Prints 0.0

#=====================================================

# I consider this not as important but here is complex and imaginary numebrs 

# Following numbers are complex numbers
x = 2j
y = 3+4j
# To extract real and imaginary parts from a complex number x, use x.real and x.imag

x = 3+4j

# real part
print(x.real)
# Prints 3.0

# imaginary part
print(x.imag)
# Prints 4.0