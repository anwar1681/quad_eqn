from matplotlib import pyplot as plt
import numpy as np
import os

# ax^2 + bx + c = 0

a = int(input('value of a: '))
b = int(input('value of b: '))
c = int(input('value of c: '))
d = (b**2 -4*a*c)*0.5
x1 = (-b + d)/(2*a)
x2 = (-b - d)/(2*a)

print("The value of first root x1 is: ",x1)
print("The value of second root x2 is: ",x2)

plt.plot(x1,x2,color='r',linestyle ='dashed',linewidth = 2,marker = '*',markersize =9,label ='red line\n marker at 1 ft interval')
plt.axis([-30,30,-30,30])
plt.title("Roots of a Quadratic Equation")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend(loc = 'lower right')
plt.show()