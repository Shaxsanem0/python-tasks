#zadaniya s 6 po 10
import math
#6
radius=float(input("raduis:"))
area= math.pi*(radius**2)
print(f"area of the circle is:{area}")
#7
celsius=float(input("enter temperature:"))
fahrenheit=celsius*1.8+32
print(f"temperature in celcios {celsius}, temperature in fahrenheit {fahrenheit}")
#8
seconds=int(input("enter second:"))
hours=seconds//3600
seconds2=seconds%3600
minutes=seconds2//60
second=seconds2%60
print(f"{seconds} seconds is: {hours} hours, {minutes} minutes, and {second} second")
#9
a=3
b=6
a, b=b, a
print({a})
print({b})
#10
user_input=input("enter any value:")
val_int=int(user_input)
val_float=float(user_input)
val_str=str(user_input)
print(f"Type of int : {type(val_int)}")
print(f"Type of float : {type(val_float)}")
print(f"Type of str : {type(val_str)}")