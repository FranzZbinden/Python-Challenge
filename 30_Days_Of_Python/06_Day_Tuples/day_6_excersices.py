# Exercises: Level 1

# Create an empty tuple
tuple1 = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Helena', 'Sara')
brothers = ('Carlos', 'Juan')

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Pedro", "Zara")
family_members = siblings + parents
print(family_members)

# Exercises: Level 2 =============================================================================
# Unpack siblings and parents from family_members
siblings1 = family_members[0:5]
print(siblings)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'pear', 'strawberry')
vegetables = ('tomatoe', 'salad')
animal = ('cow', ' chicken', 'bird')

food_stuff_tp = fruits + vegetables + animal

# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt1 = food_stuff_lt[len(food_stuff_lt)//2]
print(food_stuff_lt1)

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3])

# Delete the food_staff_tp tuple completely
del food_stuff_lt

# Check if an item exists in tuple:
print('manzana' in food_stuff_tp)
print('apple' in food_stuff_tp)

