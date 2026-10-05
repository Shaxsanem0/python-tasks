#zadaniya s 11 po 15
#11
number=5
if number>0:(
    print (f"this {number} positive")
)
elif number<0:(
    print(f"this number{number} is negative")
)
else:
    print(f" the number is zero")
#12
number=7
if number%2==0:(
    print(f"this number {number }is even")
)
else:
    print(f"this number {number} is odd")
    #13
a=45
b=47
if a>b:(
    print(f"{a}>{b}")
)
elif a<b:(
    print(f" {a}<{b}")
)
else:(
        print(f"{a}={b}")
    )
    #14
a=34
b=25
c=67
if a>b and a>c:
    max_num=a
    print(f" the max number is a: {max_num}")
elif b>a and b>c:
    max_num=b
    print(f" the max number is b: {max_num}")
else:
    max_num=c
    print(f" the max number is c: {max_num}")
#15
number=15
if number%3==0 and number%5==0:(
print(f"this number {number} % 3 and 5")
)
else:(
print(f"this number{number} dont % 3 and 5")
    )