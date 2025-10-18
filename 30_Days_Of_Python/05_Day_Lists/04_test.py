# Empty list with build in function from python list is a function that creates an empty array and assign the aray to the return
emptyLst = list()
print(len(emptyLst))

print()

emptyLst2 = []  # most conventional
print(len(emptyLst2))

print()

# Making non empty list
non_empty1 = ['Arroz', 'Abichuela', 'coco']

print("List length: {}".format(len(non_empty1)))
print(non_empty1)

print()
lst1 = ["hola", 'como', 'estas']
list_mixed = [1,"1", lst1, 2.3]
print(list_mixed)

first_elem = list_mixed[0]
print(first_elem)

print()

#Using negattive indexing for accesing data on a List
list_1 = ["hola", 'como', 'estas', 'hoy', 'yo', 'estoy', 'bien']
print(list_1[-2])

print()

first, seccond, third, *rest = list_1

print(first)
print(seccond)
print(third)
print(rest) 
print('the variable rest is an object type:', type(rest))
print()

# Another use:
arr = [1,2,3,4,5,6,7,8,9,10]
first, secondd, third, fourth, *rest, semi_last, last = arr

print("The list is:", arr)
print('first',first)
print('seccond',secondd)
print('third',third)
print('fourtth',fourth)
print('rest',rest)
print('semi Last',semi_last)
print('Last',last)

# Checking items on a list
fruits = ['banana', 'orange', 'mango', 'lemon']
print('Is lemon on fruits?: ', "lemon" in fruits)
exist_question = 'apple' in fruits
print('thers apples on fruits?:', exist_question)

# appending items to a list, Append añade simepre al final de las listas, appenda al final ( tip, a la izquierda va el List.APPEND append es el item)
listt = list()
listt.append("hola")
print(listt)
listt.append('Aguacate')
print(listt)
listt.append('Toronja')
print(listt)
print()

# Insert is for inserting a value to the list and not replacing them, the left out items move to the right
# First index and then the value to be inserted 
# Inserts with the index and the value at the same time

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(3, "Aguacate")
print(fruits)
fruits.insert(2, 'Manzana verde')
print(fruits)
print()

# Remove does the items with the same concept as the insert
# Removes by the key value, not the index
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('orange')
print(fruits)
print()
print()

# Removing items using a pop
# Using pop thers 2 options, one is by not puting a paramete ron the pop(), this removes the last elem of the list
# Using the parameter to put a index, is the same as remove() but the differenc is that it uses the index instead of the key value 

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)
fruits.insert(3, "manzanaa")
fruits.insert(2, 'Pera')
print(fruits)
fruits.pop(3)
print(fruits)

fruits.clear()
print(fruits)

# Coping lists
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits_copy = fruits.copy()
print("the two lists:", fruits, fruits_copy)

# Joining Lists using the + symbol 
fruits_max = fruits + fruits_copy
print()
print(fruits_max)

# Joining using the Extend function
first_list = [-4,-3,-2,-1]
second_list = [1,2,3,4]
zero = [0]
first_list.extend(zero)
first_list.extend(second_list)
print(first_list)
print()

# counting items on a list 
nums = [1,2,3,4,4,5,6,77,7,7,7,9.99]
count = nums.count(7)
print(count)
print()

# Finding the index of a certain value 

nums = [1,2,3,4,5,6,7,8,9,10]
index = nums.index(6)
print(index)

# reversing the items of a list
nums.reverse()
print(nums)

