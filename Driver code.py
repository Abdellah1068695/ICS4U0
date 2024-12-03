# driver for the polygon class
from polygon import *

def getNumeric(S : str):
    # input: S is a point in the format "(x,y)" (type str)
    # output: a tuple or list indicating a point (x, y) where x, y are int or float
    x = None
    y = None # obiviously, change these

    return (x, y)

fh = open("a2.txt", "r") # this is the name of the data file to open

polydata = fh.readline().strip()

# make an array of points (str)
# declare a polygon
# loop through the points array and turn them into numbers for the polynomial object
    # generate an x, y pair (numerical not str) from getNumeric
    # add to the polynomial (call add_point())

print(Poly) # this should print the entire linked list of points as string
