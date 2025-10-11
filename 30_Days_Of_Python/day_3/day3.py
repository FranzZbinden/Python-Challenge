age = 20
height_franz = 1.80
complex_number = 2 + 3j

base = int(input("Enter the base of a triangle:"))
height = int(input("Enter the height of the triangle:"))
area = int((base * height) / 2)
print("The area of the triangle provided is", area)

print()

side_a = int(input('Enter side a of the triangle: '))
side_b = int(input('Enter side b of the triangle: '))
side_c = int(input('Enter side c of the triangle: '))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter)

print()
print("#6")
length = int(input("Length of the rectangle: "))
width = int(input("Width of the rectangle: "))
area = length * width
print("The area of the provided rectangle is:", area)

print()
print("#7")
rad = int(input("The radius of a circle: "))
circumference = rad * 3.14 * 2
area_of_circle = 3.14 * rad * rad
print("The area: ", area_of_circle, "The circumference: ", circumference)

print()
print("#8")
print("Calculate the slope, x-intercept and y-intercept of y = 2x -2")
x = int(input("Enter a point x in the graph: "))
y = (2*x)-2
print("The point is located in is: (",x,",",y,")")

print()
print("#9")
print("Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean " \
"distance between point (2, 2) and point (6,10)")

first_point_x = int(input("The first point in x: "))
first_point_y = int(input("The first point in y: "))

seccond_point_x = int(input("The seccond point in x: "))
seccond_point_y = int(input("The seccond point in y: "))

slope = (seccond_point_y - first_point_y)/(seccond_point_x-first_point_x)

print("The slope on the provided points is: ", slope)


print()
print("#11")
print("Calculate the value of y (y = x^2 + 6x + 9). Try to use different x " \
"values and figure out at what x value y is going to be 0.")
x = int(input("Enter a value X to determine Y using y = x^2 + 6x + 9: "))
y = (x*x + 6*x + 9)
print("Using the provided x value, the result of y is: ", y)

print()
print("#12")
print("The length of python word is:",len("python"), "and the length of a dragon word is:" \
"", len("dragon"))
print("Are they the same size?:", len("python") == len("dragon"))


print()
print("#13")
sentence = "I hope this course is not full of jargon"
print("Is 'jargon' in: ",sentence,"?")
print("jargon" in sentence)

print()
print("#14")
print("Is there the word 'on' on 'dragon' and 'python'?")
on_on_pyt_and_drg = 'on' in ('dragon' and 'python')
print(on_on_pyt_and_drg)
# print(not(on_on_pyt_and_drg))

print()
print("#16")
print("Find the length of the text python and convert the value to float and convert it to string")
python_len = str(float(len("python")))
print("The length of the word 'python' in floating point as string is:", python_len)

print()
print("#17")
print("Even numbers are divisible by 2 and the remainder is zero. How do you check if a number " \
     "is even or not using python?")
is_div_by_two = int(input("Enter a number to check if is divicible by 2: "))
even = is_div_by_two % 2 == 0
print(even)

print()
print("#18")
print("Check if the floor division of 7 by 3 is equal to the int converted value of 2.7")
flo_to_int = int(2.7)
floor_div = 7 // 3
print("Is int of 2.7 the same as 7 // 3?: ")
print(flo_to_int == floor_div)

print()
print("#19")
print("Check if type of '10' is equal to type of 10")
type1 = type('10')
type2 = type(10)
fact = type1 == type2
print("Is type of 10 the same as '10'?",fact)

print()
print("#20")
print("Check if int('9.8') is equal to 10")
first_int = int(float('9.8'))
second_int = 10
fact = first_int == second_int
print("Is 10 the same type as the integer of '9.8'?", fact)

print()
print("#21")
print("Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?")
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: ")) 
print("Youre weekly earning is:", hours * rate_per_hour)

print()
print("#22")
print("Write a script that prompts the user to enter number of years. Calculate the number of seconds a " \
"person can live. Assume a person can live hundred years")

years_lived = int(input("Enter number of years you have lived: "))
days_lived = years_lived * 365
hours_lived = days_lived * 24
minutes_lived = hours_lived * 60
seccond_lived = minutes_lived * 60

print()
print("You have lived for", seccond_lived, "seconds. (Using method #1)")

seccond_lived2 = years_lived * 31536000

print("You have lived for", seccond_lived2, "seconds. (Using method #2)")

print()
print("#22")

# Write a Python script that displays the following table
# 1 1 1
# 2 1 2
# 3 1 3 
# 4 1 4 
# 5 1 5 

nums = [0,1,0]

for i in range(5):
    indx_0_2 = i + 1
    nums[0] = indx_0_2
    nums[2] = indx_0_2
    print(nums[0], nums[1], nums[2])