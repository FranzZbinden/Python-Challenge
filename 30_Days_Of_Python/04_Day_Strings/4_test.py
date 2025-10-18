
# # For Multiline String, use tripple ''' or """ at the beggining and at the end 
# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)

# # String Concatenation
# first_word = 'Hola'
# space = ' '
# second_word = 'que'
# third_word = 'haces'
# sentence = first_word + space + second_word + space + third_word
# print()
# print(sentence)
# print()
# print(len(sentence))

# # \n: new line
# # \t: Tab means(8 spaces)
# # \\: Back slash
# # \': Single quote (')
# # \": Double quote (")

# print('if i want to write double cuote i write /" ')
# print()
# print('new line -> \nthis is the other line <-')
# print()
# print('For tab use \t and it will do 8 spaces')
# print('single quote \', dubble quote \" ')
# print()
# print()
# print('first tab\t|')
# print('seccond tab\t|')
# print('third tab\t|')
# print('fourth tab\t|')

# # %s                    - String (or any object with a string representation, like numbers)
# # %d                    - Integers
# # %f                    - Floating point numbers
# # "%.number of digitsf" - Floating point numbers with fixed precision
# print() 
# # Example
# firs_name = 'Franz'
# last_name = 'Zbinden'
# third_name = 'Garcia'
# # For formating use the form of variable, '%s or %d and %(variable_1,variable_2)
# formated_name = '%s %s %s' %(firs_name, last_name, third_name) 
# print(type(formated_name))

# print(formated_name)
# print() 

# # Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# circle_info = 'Radius is: %d, pi being %.2f and area %.2f' %(radius, pi, area)

# print(circle_info)
# print()

# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# print('The following is an array of python libraries passed as strings %s'%(python_libraries))

# # New formating for strings
# number = 1
# float_number = 2.4567
# name = "Franz"
# print()
# print("New form of formating int: {}, floats: {:.2f} and strings {}".format(number, float_number, name))
# print()

# #String interpolation a = 4
# a = 2
# b = 3.2
# print(f'Integer:{a}, floating number {b:.2f}')

# a,b,c,d = 'hola'
# print(a)
# print(b)
# print(c)
# print(d)
# print()
# print(name[2])

# python = 'python'
# print("Having the word 'python', using negative indexing, returns the reverse character")
# print(python[0])


# # Slicing in python 

# slice_of_python = python[0:3]
# print(slice_of_python)


# slice_of_python2 = python[::-1]
# print(slice_of_python2)
# print(type(slice_of_python))

# print() 
# print("Para hacer majuscula usar python library 'capitalize'")
# print(python.capitalize())
# print()

# found = python.find('on')
# print(found)
 
# def add(a: int, b: int) -> int:
#     return a + b

# print(add("1"+"2"))

# language = '0123456789'

# # [start:end(exclusive):steps]
# new_langauge = language[0:10:3]

# print(new_langauge)

# challenge = 'thirty days of python'

#                       #(what, start, end(exclusive))
# count = challenge.count('y', 0, 12)
# print(count)

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# age = 250
# job = 'teacher'
# country = 'Finland'

# # given a string with its {} then do .format() for inserting strings into their {} 
# string_formatted = ("name: {}, last name: {}, age: {}, job: {}, country: {}".format(first_name, last_name, str(age), job, country))
# print(string_formatted)


# radius = 10
# pi = 3.14
# area = pi * radius ** 2

# string_of_circle = 'With a radius of {}, the area of the circle is: {}'.format(str(radius), str(area))
# print(string_of_circle)

# string_1 = 'abc'
# string_2 = 'def'

# string_3 = string_1 + string_2
# print(string_3)

# print()
# string_4 = string_2.join(string_1)
# print(string_4)

# # Entre medio pones el caracter que quieras 
# abc_array = ["a", "b", "c"]
# abc = '#'.join(abc_array)
# print(abc)

# print()
# num_array = '123456789'
# even_num_array = num_array.strip('5')
# print(even_num_array)

import requests

isbn = "9780140328721"
url = f"https://openlibrary.org/isbn/{isbn}.json"
data = requests.get(url).json()

print(data["title"])
print(data.get("number_of_pages"))
