# Name: Younghak Yoo
# SBUID: 115935752
##################### SCORE ######################
#######  Score:  8.5/10
#################################################
#your output
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/Younghak1/Homework_1.py"
# Enter the Fahrenheit : 44
# You'd better to wear Sweater.

# The area of triangle = 11.5 --> wrong
# First distance is = 5.83 units
# Second distance is = 6.08 units
# Third distance is = 11.18 units
# Perimeter of triangle is : 23.09405431264247 units--> wrong

# Enter the number of sides of your polygon: 5
# Enter the length of sides of your polygon: 4
# The area of the polygon is : 27.527638409423474
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def mult(x,y):
    return(x*y)
def div(x,y):
    return(x/y)

fahrenheit = float(input("Enter the Fahrenheit : "))
def fahrenheit2celsius(fahrenheit):
    celcius = mult(div(5,9),(fahrenheit - 32))
    return celcius

celcius = fahrenheit2celsius(fahrenheit)

def what_to_wear(celcius):
    if celcius < -10:
        print("You should wear Puffy Jacket.")
    elif celcius < 0:
        print("You should put your scarf on.")
    elif celcius < 10:
        print("You'd better to wear Sweater.")
    elif celcius < 20:
        print("You need a Light jacket.")
    else:
        print("You can wear T-shirts only.")

what_to_wear(celcius)
print("")
#First of all, I created the function fahrenheit to celcius.
#In this case, the temperature can be the float number, so I put float on my code
#Then, I followed the table by using 'if else' code, What should I wear on what temperature.

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    result = abs((((x1*y2)+(x2*y3)+(x3*y1))-((x1*y3)+(x2*y1)+(x3*y2)))/2)
    return result

x1 = 1           #These are the coordinates
x2 = 4
x3 = 3
y1 = 1
y2 = 6
y3 = 12
print("The area of triangle =", shoelace_triangle_area(1,1,4,6,3,12)) #use the defined function to get area.

def euclidean_distance(x1, y1, x2, y2):
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return distance

dist1 = euclidean_distance(1, 1, 4, 6)
dist2 = euclidean_distance(4, 6, 3, 12)
dist3 = euclidean_distance(1, 1, 3, 12)

print("First distance is =",str("{:.2f}".format(dist1)),"units")
print("Second distance is =",str("{:.2f}".format(dist2)),"units")
print("Third distance is =",str("{:.2f}".format(dist3)),"units")


def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    perimeter = dist1 + dist2 + dist3
    return perimeter

print("Perimeter of triangle is :", compute_triangle_perimeter(1,1,4,6,3,12),"units")
print("")
#To compute the area and the perimeter, the length of side is needed information.
#create the given formula to get the area of the triangle and perimeter.
#I was trying to make this task simple, but it was tough. I tried my best...

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

from math import *

def div(x,y):
    return(x/y)
number_sides = float(input("Enter the number of sides of your polygon: "))  #number of the sides of polygon
length_sides = float(input("Enter the length of sides of your polygon: "))
deg = (div(180,number_sides))

def deg2rad(deg):
    import math
    radian = deg*(math.pi/180)      #converts to radian of polygon's one of interior angle
    return radian

radian = deg2rad(deg)

def apothem(length_sides):
    import math
    var = (math.tan(radian))
    apothem = (div(length_sides,(2*var)))      #formula to get apothem
    return apothem

apothem = apothem(length_sides)

def polygon_area(number_sides, length_sides):
    polygon_area = (div((number_sides*length_sides*apothem),2))
    return polygon_area

print ("The area of the polygon is : " + str(polygon_area(number_sides, length_sides)))
#It was hard to create the function degree to radian.
#Even though I know the formual, I did not realize how to apply it.