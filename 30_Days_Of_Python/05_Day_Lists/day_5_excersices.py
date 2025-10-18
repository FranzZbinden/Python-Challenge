# Declare an empty list
empty_list = []
empty_list2 = list()

print(type(empty_list))
print(type(empty_list2))

# Declare a list with more than 5 items
list_2 = [1,2,3,4,5,6]

# Find the length of your list
leng = len(list_2)
print(leng)

# Get the first item, the middle item and the last item of the list
list_2 = [1,2,3,4,5,6]
first = list_2[0]
last = list_2[-1]
mid_index = len(list_2) // 2
mid_val = list_2[mid_index]
print('The list is: ', list_2)
print("the first val: ", first)
print("the last val: ", last)
print("the mid val: ", mid_val)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Franz", '20', 1.80, 'single', 'Home']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

companies = ['Facebook', 'Google', 'microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print()
# Print the list using print()

print(companies)
print()
# Print the number of companies in the list

print('Number of companies', len(companies))
print()

# Print the first, middle and last company

print('First: {}, Last: {}, Middle: {}'.format(companies[0], companies[-1], companies[len(companies)//2]))

# Print the list after modifying one of the companies

companies[2] = 'Microsoft'

print(companies)
print()

# Add an IT company to it_companies

companies.insert(1, 'Xtillion')
print(companies)
print()

# Insert an IT company in the middle of the companies list
companies.insert(((len(companies)//2)-1), 'HoneyWell')
print(companies)
print()

# Change one of the it_companies names to uppercase (IBM excluded!)

companies[1] = companies[1].upper()
print(companies)
print()

# Join the it_companies with a string '#;  
companies_copy = "#".join(companies)
print(companies_copy)
print()

# Check if a certain company exists in the it_companies list.
print('Apple' in companies)
print()

# Sort the list using sort() method
companies.sort()
print(companies)
print()

# Reverse the list in descending order using reverse() method

companies.reverse()
print(companies)
print()

# Slice out the first 3 companies from the list

slice_companies = companies[:3]
print(slice_companies)

# Slice out the last 3 companies from the list

slice_companies = companies[-3:]
print(slice_companies)

# Slice out the middle IT company or companies from the list

print(companies[len(companies)//2])

# Remove the first IT company from the list

companies.remove(companies[0])
print(companies)
print()

# Remove the middle IT company or companies from the list

companies.remove(companies[len(companies)//2])
print(companies)
print()

# Remove the last IT company from the list

companies.remove(companies[-1])
print(companies)
print()

# Remove all IT companies from the list
companies.clear()
print(companies)
print()

# # Destroy the IT companies list
# del companies
# print(companies)
# print()

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

join_companies = front_end + back_end
print(join_companies)
print()

# After joining the lists in question 26. Copy the joined list and assign it to a 
# variable full_stack, then insert Python and SQL after Redux.

full_stack = join_companies.copy()
print(full_stack)
redux_index = full_stack.index('Redux') + 1
full_stack.insert(redux_index, 'Python')
full_stack.insert(redux_index, 'SQL')
print(full_stack)

# Exercises: Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

min_age = ages[0]
max_age = ages[-1]
median_age = ages[(len(ages)//2)]

print(min_age, max_age, median_age)

avrg_age = sum(ages) / len(ages)
print(avrg_age)


