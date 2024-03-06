# new_list = [NEW_ITEM for ITEM in LIST]
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

name = "Diego"
letters_list = [letter for letter in name]

range_length = range(1, 5)
print([number*2 for number in range_length])

# new_list = [NEW_ITEM for ITEM in LIST if TEST]
names = ["Angela", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
long_names = [name.upper() for name in names if len(name) > 4]
