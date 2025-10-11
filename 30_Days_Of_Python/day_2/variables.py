# Day 2: 30 Days of python programming
import math

first_name = "Carlos"
last_name = "Gonzales"
full_name = "Carlos Gonzales"
country = "Suiza"
city = "Zurich"
age = 19
year = 2025
is_married = True
is_true = True
is_light_on = True
x, y = 1, 2

# Check the data type of all your variables using type() built-in function
print(type(full_name))
print()

# Using the len() built-in function, find the length of your first name
print(len(first_name))
print()

# Compare the length of your first name and your last name and their sum
first_name_len = len(first_name)
last_name_len = len(last_name)

print(f"The length of", first_name, "is: ", first_name_len)
print(f"The length of", last_name, "is: ", last_name_len)
print()

print(f"Their sum is:", first_name_len+last_name_len)
print()

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(num_one,"+", num_two, "=", total)
print()

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(num_one,"-", num_two, "=", diff)
print()

# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(num_one,"*", num_two, "=", product)
print()

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(num_one,"/", num_two, "=", division)
print()

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
reminder = num_one % num_two
print(num_one,"%", num_two, "=", reminder)
print()

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(num_one,"**", num_two, "=", exp)
print()

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(num_one,"//", num_two, "=", floor_division)


# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

rad = int(input("whats the redius of the circle?"))
area_of_circle = (rad*rad) * math.pi
circum_of_circle = (rad*2) * math.pi
print("With radius:", rad, "You get area:", area_of_circle, "and circumference: ", circum_of_circle)



