# ax^2 + bx + c = 0

a = int(input('value of a: '))
b = int(input('value of b: '))
c = int(input('value of c: '))
d = (b**2 -4*a*c)*0.5
x1 = (-b + d)/(2*a)
x2 = (-b - d)/(2*a)

print("The value of first root x1 is: ",x1)
print("The value of second root x2 is: ",x2)