# code for the cse 5242 project -__-

# input = array of tuples of coordinates
# data = [(x,y), (x,y), (x,y)]
# point : tuple()
# Polygon v: list
# (x y)

# IMPORT STATEMENTS
import math

# DOUGLAS-PEUKER ALGORITHM
def distance_from_line(point, line): # point's distance from line, point = (x,y), line = [(x1,y1), (x2,y2), (x3,y3), ...]

    (x1,y1) = line[0]
    (x2,y2) = line[-1]
    (p1,p2) = point

    c_yint = ((((y2-y1)/(x2-x1)) * -1.0 * x1) + y1)
    b = -1
    a_slope = (y2-y1)/(x2-x1)

    distance = abs(a_slope*p1 + b*p2 + c_yint) / math.sqrt(math.pow(a_slope,2) + math.pow(b,2))

    return distance

def point_with_max_distance(line):

    max_dist = 0
    max_point = line[0]
    max_index = 0

    for i in range(len(line)):
        dist = distance_from_line(line[i], line)
        if dist > max_dist:
            max_dist = dist
            max_point = line[i]
            max_index = i
            

    return max_point, max_dist, max_index

def dp_alg_calc(line, tolerance): # line: [(x1,y1), (x2,y2), (x3,y3), ...], epsilon: [0,1]
    max_distance = 0
    max_index = 0
    end = len(line)

    max_point, max_dist, max_index = point_with_max_distance(line)

    result_line = [];

    # If max distance is greater than epsilon, recursively simplify
    if (max_distance > tolerance):
        # Recursive call
        part1_line = dp_alg_calc(line[1, max_index+1], tolerance)
        part2_line = dp_alg_calc(line[max_index, end], tolerance)

        # Build the result list
        result_line = part1_line + part2_line
    else:
        result_line = line
    
    # Return the result
    return result_line

def dp_algorithm(line, epsilon): # finds tolerance for that specific line and
    
    max_point, max_dist, max_index = point_with_max_distance(line)
    tolerance = epsilon * max_dist

    new_line = dp_alg_calc(line, tolerance)

    return new_line

# VISWA-WYATT ALGORITHM
def area_of_triangle(point1, point2, point3): # point1: (x,y), point2: (x,y), point3: (x,y)
    (x1, y1) = point1
    (x2, y2) = point2
    (x3, y3) = point3
    area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    return area

def calculate_triangles_and_smallest(line):
    triangles = []
    index = 1
    smallest_triangle = math.inf
    smallest_point = 0
    for (x,y) in line[1:-1]:
        area = area_of_triangle(line[index-1], (x,y), line[index+1])
        triangles.append(area)
        if area < smallest_triangle:
            smallest_triangle = area
            smallest_point = line[index]
        index+=1
    return triangles, smallest_triangle, smallest_point

def find_tolerance(line, epsilon):
    index = 1
    largest_triangle = -math.inf
    for (x,y) in line[1:-1]:
        area = area_of_triangle(line[index-1], (x,y), line[index+1])
        if area > largest_triangle:
            largest_triangle = area
        index+=1
    return (epsilon * largest_triangle)
    
'''
viswalingam algorithm
line: [(x1,y1), (x2,y2), (x3,y3), ...]
epsilon: [0,1]
'''
def vw_algorithm(line, epsilon): # line: [(x1,y1), (x2,y2), (x3,y3), ...], # epsilon: [0,1]

    tolerance = find_tolerance(line, epsilon)

    while (len(line) >= 3):
        print(line, '\n')
        tris, smallest_tri, smallest_pt = calculate_triangles_and_smallest(line)        

        if smallest_tri < tolerance:
            line.remove(smallest_pt) # check if smallest point is less than tolerance
            print(line)
        else: # else break loop if not
            break

    return line


# READ INPUT
def read_input(line):
    print("chicken")

# GENERATE OUTPUT
def generate_output(line):
    print("{")
    print("\t\"type\": \"FeatureCollection\",")
    print("\t\"features\": [")
    print("\t\t\"{")
    print("\t\t\t\"type\": \"Feature\",")
    print("\t\t\t\"properties\": {")
    print("\t\t\t\t\"vendor\":  \"A\"")
    print("\t\t\t},")
    print("\t\t\t\"geometry\": {")
    print("\t\t\t\t\"type\": \"LineString\",")
    print("\t\t\t\t\"coordinates\": [")

    for (x,y) in line:
        coordinate = "\t\t\t\t\t" + "[" + str(x) + "," + str(y) + ", 0, 0]"
        print(coordinate)

    print("\t\t\t\t]")
    print("\t\t\t}")
    print("\t\t}")
    print("\t]")
    print("}")

# MAIN CODE
test = [(-123.15532480599389,39.628538026418425),(-119.0541702886981,39.40845421648897),(-122.53717977729988,37.92347617009539),(-123.6189335775142,39.160027074679334),(-124.15532480599389,36.628538026418425)]

# GET INPUT FROM CSV


# DOUGLAS-PEUKAR ALGORITHM
out = dp_algorithm(test, 0.5)
print(out)


# TEST DOUGLAS-PEUKAR HELPER METHODS
'''
point_with_max_distance(test)
print(point_with_max_distance(test))
print(point_with_max_distance(test))
'''

# TEST VISWA-WYATT ALGORITHM
#print(len(test))
#out = vw_algorithm(test, 0.5)
#print(out)


# TEST VISWA-WYATT HELPER METHODS
'''
print('triangles: ', calculate_triangles_and_smallest(test))
print('tolerance: ', find_tolerance(test, 0.5))
print('test: ', test)
print('algorithm: ', vw_algorithm(test, 0.5))
'''

generate_output(test)