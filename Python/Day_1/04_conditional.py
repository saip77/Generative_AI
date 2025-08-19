# Conditional Statements

x = 10
y = 3

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# Nested Conditional Statements

x = 10
y = 3

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    if x == y:
        print("x is equal to y")
    else:
        print("x is not equal to y")