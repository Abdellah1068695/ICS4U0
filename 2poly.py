import math

class Point:
    def __init__(self, x: float = None, y: float = None):
        # Default is None due to creation of a Head Node for linked lists
        self.__x = x
        self.__y = y
        self.next = None

    def valid(self):
        # A validator to check that x and y are either int or float
        return isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float))

    def __str__(self):
        # Point (x, y) expressed this way as a string
        return f"({self.__x}, {self.__y})"

class Polygon:
    def __init__(self):
        # Set basic properties to default values
        self.__sides = 0
        self.__vertices = 0
        self.__head = Point()  # a null point with a null Next field

    def add_point(self, x: float, y: float):
        # Crea*te a new Point object
        new_point = Point(x, y)
        
        # If this is the first point, make it the head node's next
        if self.__head.next is None:
            self.__head.next = new_point
        else:
            # Traverse the linked list to find the last point and add the new point
            current = self.__head.next
            while current.next is not None:
                current = current.next
            current.next = new_point

        # Update the vertices counter and sides counter
        self.__vertices += 1
        self.__sides += 1  # For simplicity, assuming each new point adds a side

    def __str__(self):
        # Use a traversal to generate the entire set of points separated by "->" as a string
        points_str = []
        current = self.__head.next  # Start with the first valid point
        while current is not None:
            points_str.append(str(current))  # Call the __str__ method of Point
            current = current.next

        # Join the list of point strings with " -> "
        return " -> ".join(points_str)

    def _distance(p1: Point, p2: Point):
        return math.sqrt((p1._Point__x - p2._Point__x) ** 2 + (p1._Point__y - p2._Point__y) ** 2)

    def perimeter(self):
        if self.__head.next is None or self.__head.next.next is None:
            return 0  # Not enough points to form a polygon

        total_distance = 0
        current = self.__head.next
        start = current  # Save the starting point to close the polygon at the end

        while current.next is not None:
            total_distance += calculate_distance(current, current.next)
            current = current.next

        # Close the polygon by adding the distance from the last point to the first
        total_distance += calculate_distance(current, start)
        return total_distance

    #def distance(self ; x ,self : y):
        #return math.sqrt((

