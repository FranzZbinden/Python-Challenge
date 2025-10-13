# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string = ' '.join(('Thirty', 'Days', 'Of', 'Python'))
print(string)
print()

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
tuple_1 = 'Coding', 'For' , 'All'
string_2 = ' '.join(tuple_1)
print(string_2)
print()

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
print(company)
print()

# 4. Print the variable company using print().
print(company)
print()

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
uper_company = company.upper()
print(uper_company)
print()

# 7. Change all the characters to lowercase letters using lower() method.
lower_company = company.lower()
print(lower_company)
print()

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
string_4 = 'coding for all'
string_5 = string_4.title()
print(string_5)
print()




# 10. Cut(slice) out the first word of Coding For All string.
string_4 = 'Codingg For All' 
arr_string_4 = string_4[1:]
print(arr_string_4)
print()

# 11. Check if Coding For All string contains a word Coding using the method index, find or other methods.
string_4 = 'Coding For All'
found_4 = "Coding" in string_4  
print(found_4)
print()

# 12. Replace the word coding in the string 'Coding For All' to Python.
string_4 = 'Coding For All'
repl_string_4 = string_4.replace('Coding', 'Python')
print(repl_string_4)
print()

# 13. Change Python for Everyone to Python for All using the replace method or other methods.
pfe = 'Python for Everyone'
pfa = pfe.replace('Everyone','All')
print(pfa)
print()

# 14. Split the string 'Coding For All' using space as the separator (split()) .
string_4 = 'Coding For All'
string_4_split = string_4.split(' ')
print(string_4_split)
print(string_4_split[2])
print()



# 15. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
stringg = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
stringg_list = stringg.split(', ')
print(stringg_list)


# What is the character at index 0 in the string Coding For All.


# What is the last index of the string Coding For All.


# What character is at index 10 in "Coding For All" string.


# Create an acronym or an abbreviation for the name 'Python For Everyone'.


# Create an acronym or an abbreviation for the name 'Coding For All'.


# Use index to determine the position of the first occurrence of C in Coding For All.


# Use index to determine the position of the first occurrence of F in Coding For All.


# Use rfind to determine the position of the last occurrence of l in Coding For All People.


# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does ''Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.