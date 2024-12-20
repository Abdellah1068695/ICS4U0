from poly import *

def getNumeric(S: str):
    """
    Converts a string representation of a point (e.g., "(x, y)") into a tuple of numeric values.
    """
    S = S.strip()  # Remove leading/trailing whitespaces
    if S.startswith("(") and S.endswith(")"):
        S = S[1:-1]  # Remove parentheses
    P = S.split(",")  # Split the string by comma
    
    if len(P) != 2:
        raise ValueError(f"Invalid format for point: {S}. Expected format '(x, y)'")

    x, y = P

    # Convert x and y to int or float
    try:
        x = int(x)
    except:
        x = float(x)

    try:
        y = int(y)
    except:
        y = float(y)

    return (x, y)

# Read from file and process each point
fh = open("a2.txt", "r")  # Open the file for reading
polydata = fh.readline().strip()  # Read the first line of the file

# Split the string into individual points
points = polydata.split("),")  # Split by closing parenthesis and comma

# Create a Polygon object
polygon = Polygon()

# Process each point in the file
for point_str in points:
    # Ensure the point string ends with a closing parenthesis if it's the last one
    if not point_str.endswith(")"):
        point_str += ")"
    
    # Get numeric coordinates from the string
    point = getNumeric(point_str)
    x, y = point
    # Add the point to the polygon
    polygon.add_point(x, y)
    
# Print out the polygon
print(polygon)  # Prints the linked list of points
print("Area of the polygon:", polygon.area())  # Calculates and prints the area
print("Perimeter of the polygon:", polygon.perimeter())  # Calculates and prints the perimeter
polygon.draw()  # Draws the polygon using turtle graphics

