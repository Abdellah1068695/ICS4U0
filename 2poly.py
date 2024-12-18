import math
import turtle

class Point:
    def __init__(self, x: float = None, y: float = None):
        # Default is None due to creation of a Head Node for linked lists
        self.__x = x
        self.__y = y
        self.next = None

    def valid(self):
        # A validator to check that x and y are either int or float
        return isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float))
    
    def get_coordinates(self):
        return self.__x, self.__y

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
        # Create a new Point object
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

    def _distance(self, p1: Point, p2: Point):
        return math.sqrt((p1._Point__x - p2._Point__x) ** 2 + (p1._Point__y - p2._Point__y) ** 2)

    def perimeter(self):
        if self.__vertices < 2:
            return 0.0  # No perimeter for less than 2 points

        current = self.__head.next
        prev = None
        perimeter = 0.0
        first_point = None

        while current is not None:
            if prev is not None:
                x1, y1 = prev.get_coordinates()
                x2, y2 = current.get_coordinates()
                perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            else:
                first_point = current
            prev = current
            current = current.next

        # Close the loop if there are at least 3 points
        if first_point and prev:
            x1, y1 = prev.get_coordinates()
            x2, y2 = first_point.get_coordinates()
            perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return perimeter

    def area(self):
        if self.__vertices < 3:
            return 0  # A polygon must have at least 3 vertices

        current = self.__head.next
        x_coords, y_coords = [], []

        while current is not None:
            x_coords.append(current._Point__x)
            y_coords.append(current._Point__y)
            current = current.next

        x_coords.append(x_coords[0])  # Closing the polygon
        y_coords.append(y_coords[0])

        # Shoelace formula
        n = len(x_coords)
        area = 0
        for i in range(n - 1):
            area += x_coords[i] * y_coords[i + 1] - y_coords[i] * x_coords[i + 1]

        return abs(area) / 2
    
    def is_regular(self):
        if self.__vertices < 3:
            return False

        # Check side lengths
        current = self.__head.next
        lengths = []
        first_point = current
        prev = None

        while current is not None:
            if prev:
                lengths.append(self._distance(prev, current))
            prev = current
            current = current.next

        # Close the loop for side length
        lengths.append(self._distance(prev, first_point))

        # Check if all side lengths are equal
        if not all(math.isclose(length, lengths[0], rel_tol=1e-9) for length in lengths):
            return False

        # Check angles (if necessary, can be added)
        return True

    def draw(self):
        if self.__vertices < 2:
            print("Polygon cannot be plotted. Not enough vertices.")
            return

        plotter = turtle.Turtle()
        plotter.penup()

        current = self.__head.next
        points = []
        while current is not None:
            points.append(current.get_coordinates())
            current = current.next

        # Dynamic scaling
        x_coords, y_coords = zip(*points)
        max_val = max(max(map(abs, x_coords)), max(map(abs, y_coords)))
        scale = 1 if max_val > 10 else 20 if max_val <= 5 else 10

        start_x, start_y = points[0]
        plotter.goto(start_x * scale, start_y * scale)
        plotter.pendown()

        for x, y in points[1:]:
            plotter.goto(x * scale, y * scale)

        plotter.goto(start_x * scale, start_y * scale)  # Close the polygon
