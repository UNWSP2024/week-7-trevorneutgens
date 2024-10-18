# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

import math

def distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 +
                     (coord2[1] - coord1[1]) ** 2 +
                     (coord2[2] - coord1[2]) ** 2)

def main():
    while True:
        try:
            # first coordinate from the user
            x1, y1, z1 = input("Enter the first 3D coordinate (x1, y1, z1) as comma-separated values: ").split(',')
            coord1 = (float(x1), float(y1), float(z1))
            # second coordinate from the user
            x2, y2, z2 = input("Enter the second 3D coordinate (x2, y2, z2) as comma-separated values: ").split(',')
            coord2 = (float(x2), float(y2), float(z2))
            # calc the distance
            dist = distance(coord1, coord2)
            # display the distance
            print(f"The distance between {coord1} and {coord2} is: {dist:.2f}")
            break
        except ValueError:
            print("Invalid input. Please enter three numeric values separated by commas.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Call the main function
if __name__ == '__main__':
    main()
