x = 6
y = 2

# addition
print(x + y)		# 8

# subtraction
print(x - y)		# 4

# multiplication
print(x * y)		# 12

# division
print(x / y)		# 3

print(1/2)          # 0.5
print(4/2)          # 2.0
print(1.5/2)        # 0.75
print(-2/2)         # -1.0

# modulus
print(x % y)		# 0

# exponentiation
print(x ** y)		# 36

# floor division
print(x // y)		# 3



# /	Traditional Division	    x / y
print(1/2)
print(4/2)
print(1.5/2)
print(-2/2)

print("===================")

print(1%2)  # 1/2 = 1 = 2 * 0 + 1
print(13%2) # = 12/2 = 6 * 2 + 1 

# The division rule says:

# 𝑎=𝑏×𝑞+𝑟
# a=b×q+r

# where

# a = dividend
# b = divisor
# q = quotient (how many full times it fits)
# r = remainder (what’s left)
# and

# 0≤𝑟<∣𝑏∣
# 0≤r<∣b∣

print(4/2)
print(1.5/2)
print(-2/2)

# ** Exponentiation	x ** y
# // Floor division	x // y

# Divmod function, gives the floor division and module residue

print(divmod(37, 5))

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool

result = 0

nums = [1,1,1,2,2,2,3,3,3,3]
for n in nums:
    result ^= n
print(result)

# &=	Bitwise AND assignment	x &= 3	x = x & 3
# |=	Bitwise OR assignment	x |= 3	x = x | 3
# ^=	Bitwise XOR assignment	x ^= 3	x = x ^ 3
# >>=	Bitwise right shift assignment	x >>= 3	x = x >> 3
# <<=	Bitwise left shift assignment	x <<= 3	x = x << 3

# XOR operator only gives a 1, if the numbers are different, if it apears again it cancels out

x = 2
y = 3

# not
print(not(x > 0 and y < 0))     # False


x = [1, 2, 3]
y = [1, 2, 3]

print()

# is
print(x is y)		# False

# is not
print(x is not y)	# True

print("=============")


L = ['red', 'green', 'blue']

# in
print('red' in L)           # True

# not in
print('yellow' not in L)    # True



print("=====================")

hash = {1:"uno", 2:"dos", 3:"tres"}

if 1 in hash:
    print("1 is in hash!!")

    

