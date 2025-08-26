#Fibonacci Sequence Generator

'''Input n, print first n Fibonacci numbers.
Example: n=7 → 0 1 1 2 3 5 8.
'''

input_n = int(input("Enter n: "))

fib = [0, 1]

for i in range (2, input_n):
    fib.append(fib[i-1] + fib[i-2])

print(fib)