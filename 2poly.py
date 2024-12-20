import math
import turtle

class Point:
    def __init__(self, x: float = None, y: float = None):
        """
        Initializes a Point object with optional x and y coordinates.
        If x and y are not provided, they default to None (used for a head node).
        """
        self.__x = x
        self.__y = y
        self.next = None  # Pointer for linked list structure

    def valid(self):
        """
        Validates if the x and y coordinates are of type int or float.
        """
        return isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float))
    
    def get_coordinates(self):
        """
        Returns the x and y coordinates as a tuple.
        """
        return self.__x, self.__y

    def __str__(self):
        """
        Returns the string representation of the point in the format "(x, y)".
        """
        return f"({self.__x}, {self.__y})"


class Polygon:
    def __init__(self):
        """
        Initializes a Polygon object with a default head node and zero sides/vertices.
        """
        self.__sides = 0
        self.__vertices = 0
        self.__head = Point()  # Head node for linked list

    def add_point(self, x: float, y: float):
        """
        Adds a new point to the polygon.
        - Creates a Point object with given coordinates.
        - Links it to the end of the linked list.
        """
        new_point = Point(x, y)
        
        # If the linked list is empty, add the first point
        if self.__head.next is None:
            self.__head.next = new_point
        else:
            # Traverse to the end of the list and add the new point
            current = self.__head.next
            while current.next is not None:
                current = current.next
            current.next = new_point

        # Increment counters for vertices and sides
        self.__vertices += 1
        self.__sides += 1

    def __str__(self):
        """
        Returns a string representation of the polygon, showing all points connected by "->".
        """
        points_str = []
        current = self.__head.next  # Start with the first valid point
        while current is not None:
            points_str.append(str(current))
            current = current.next
        return " -> ".join(points_str)

    def _distance(self, p1: Point, p2: Point):
        """
        Calculates the Euclidean distance between two points.
        """
        return math.sqrt((p1._Point__x - p2._Point__x) ** 2 + (p1._Point__y - p2._Point__y) ** 2)

    def perimeter(self):
        """
        Calculates the perimeter of the polygon by summing the distances between consecutive points.
        """
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

        # Close the loop by connecting the last point to the first
        if first_point and prev:
            x1, y1 = prev.get_coordinates()
            x2, y2 = first_point.get_coordinates()
            perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return perimeter

    def area(self):
        """
        Calculates the area of the polygon using the shoelace formula.
        Automatically checks and prints if the polygon is regular or irregular.
        """
        if self.__vertices < 3:
            return 0  # A polygon must have at least 3 vertices

        current = self.__head.next
        x_coords, y_coords = [], []

        while current is not None:
            x_coords.append(current._Point__x)
            y_coords.append(current._Point__y)
            current = current.next

        x_coords.append(x_coords[0])  # Close the polygon
        y_coords.append(y_coords[0])

        # Shoelace formula
        area = 0
        for i in range(len(x_coords) - 1):
            area += x_coords[i] * y_coords[i + 1] - y_coords[i] * x_coords[i + 1]

        area = abs(area) / 2

        # Check and print regularity
        regularity = self.is_regular()
        print(f"The polygon is {regularity}.")

        return area

    def is_regular(self):
        """
        Determines if the polygon is regular (all sides and angles are equal).
        Returns "regular" or "irregular".
        """
        if self.__vertices < 3:
            return "irregular"  # A regular polygon must have at least 3 vertices

        # Calculate side lengths
        current = self.__head.next
        lengths = []
        first_point = current
        prev = None

        while current is not None:
            if prev:
                lengths.append(self._distance(prev, current))
            prev = current
            current = current.next

        # Close the loop for the last side
        lengths.append(self._distance(prev, first_point))

        # Check if all side lengths are approximately equal
        if not all(math.isclose(length, lengths[0], rel_tol=1e-9) for length in lengths):
            return "irregular"

        return "regular"  # Regular polygon if all sides are equal

    def draw(self):
        """
        Draws the polygon using the turtle module.
        Dynamically scales the polygon based on coordinate values.
        """
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

