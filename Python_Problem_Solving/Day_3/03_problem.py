#Remove Duplicates 🚫

'''
Input a list of numbers.
Remove all duplicates and print the unique list.
'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 9, 10]

my_set = set(my_list)
print(my_set)

new_list = list(my_set)
print(new_list)

unique_list = list(dict.fromkeys(my_list))
print(unique_list)