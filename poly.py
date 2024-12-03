class point:
    def __init__(self, x: float=None, y: float=None):
        # Default is None due to creation of a Head Node for linked lists
        self.__x = x
        self.__y = y
        self.next = None

    def valid(self):
        # A validator is needed mostly for when we go to the end of the file, but
        # also to assure us that the point is properly formatted with either
        # ints or floats.
        val = False # obviously add code here

        return val

    def __str__(self):
        # point (x, y) expressed this way as string
        # as in: (4, 5)
        pass

class Polygon:
    def __init__(self):
        # Set basic properties to default values
        self.__sides = 0
        self.__vertices = 0
        self.__head = point() # a null point with a null Next field

    def add_point(self, x: float, y: float):
        # initialize a point object V
        # if it is the first point, create the object with variable V make head.next point to V
        # if it is any other point, V.next points to it, and V traverses to that point
        # count the vertices as you go
        pass

    def __str__(self):
        # Use a traversal to generate the entire set of points separated by "->" as string
        # You need to use point's __str__ function to help you.
        pass
