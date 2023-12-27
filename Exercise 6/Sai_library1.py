
#############
The Python Standard Library
By: Sai Mahesh
17OCT2023
################

#functions for trigonometry values
import math
print("Input lengths of the two short triangle sides:")
x = float(input("x: "))
y = float(input("y: "))
c = math.sqrt(x**2 + y**2)
print("The length of the hypotenuse to four places is: {hypo:1.4f}".format(hypo=c))