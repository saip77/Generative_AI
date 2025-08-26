#Prime Number Check

'''Input a number.
Check if it’s prime (divisible only by 1 and itself).
'''

number = int(input("Enter a number: "))
factors = []
if(number > 1):
    for i in range(2, number+1):
        if(number % i ==0):
            factors.append(i)
    if(len(factors) == 1):
        print("Prime")
    else:
        print("Not prime")
else:    
    print("Invalid input")