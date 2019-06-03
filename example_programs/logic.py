##logic.py
x = int(input("enter the first number "))
y = int(input("enter the second number "))
if(x > 0):
    print("x is greater than 0")

else:
    print("x is less than 0")

if(y > x):
    print("y is greater than x")

elif(x > y):
    print("x is greater than y")
    
else:
    print("x and y are equal")