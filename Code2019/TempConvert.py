# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
#celsius = 37.5

# Take Celsius as input (argument)
def temp(value):
    print("Temp in Celsius is:" + value)
    return value
  
# Take input from program
#celsius =  float(input("Enter Temp in Celsius: "))

value = 25.6

#Call function
celsius = float(temp(value))
    
# calculate fahrenheit
if (celsius > 0):
    fahrenheit = (celsius * 1.8) + 32
    print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
else:
    print("Celsius can't be negative")
    
