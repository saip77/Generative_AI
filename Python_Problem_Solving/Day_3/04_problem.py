#List Reversal 🔄

'''
Take a list of names and print it in reverse order (without using reverse()).
'''

my_list = ["Ronaldo", "Messi", "Neymar", "Kobe", "Ronaldinho"]
reversed_list = []
while len(my_list) > 0:
    reversed_list.append(my_list[-1])
    my_list.pop()
print(reversed_list)