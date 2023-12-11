from vectortoolkit import vector, vector_tools

"""
Task 1 - ensure that the cross product of two vectors is perpendicular to both vectors
"""
print("TASK 1")
vec_a = vector.Vector3D(17, 9, -7)
vec_b = vector.Vector3D(18, 24, -24)

# cross product
vec_a_cross_b = vector_tools.VectorTools.cross_product(vec_a, vec_b)

# calculate the angles between A cross B and A and B
angle_cross_a = vector_tools.VectorTools.calculate_angle(vec_a_cross_b, vec_a)
angle_cross_b = vector_tools.VectorTools.calculate_angle(vec_a_cross_b, vec_b)

# check the angle is equal to pi/2 radians
if round(angle_cross_a, 5) == 1.57080 and round(angle_cross_b, 5) == 1.57080:
    print("A cross B is perpendicular to both A and B")
    
    
"""
Task 2 - A vehicle is traveling along (4, 7, 9) and is at (0, 0, 0). The vehicle wants to change 
its heading to reach point (15, 9, -6). What is the angle of the change in heading and how far 
away is the point?

"""
print("TASK 2")
current_vec_travel = vector.Vector3D(4, 7, 9)

current_location = (0, 0, 0)
point_of_interest = (15, 9, -6)

# get new direction of travel based on current location and point of interest
new_vec_travel = vector.Vector3D(point_of_interest[0]-current_location[0], point_of_interest[1]-current_location[1], point_of_interest[2]-current_location[2])

# get the angle of the change
heading_change = vector_tools.VectorTools.calculate_angle(current_vec_travel, new_vec_travel)

# get the distance to the new point
distance_to_point = vector_tools.VectorTools.calculate_distance(current_location, point_of_interest)

print("Change in heading (radians): ", round(heading_change, 5))
print("Distance to point of interest: ", round(distance_to_point, 5))


"""
Task 3 - Given two input vectors print out the result of the projection of the first vector onto
the second vector

"""
print("TASK 3")
print("Input two vectors to get the result of projecting the first vector onto the second")
print("Input vector A that will be projected onto vector B")
vec_a_input = input("Please enter a vector in the form [x, y, z]: ")

print("Input vector B that will have vector A projected onto it")
vec_b_input = input("Please enter a vector in the form [x, y, z]: ")

# convert the string inputs into lists of floats
vec_a_list = list(map(float, vec_a_input.strip("[]").split(",")))
vec_b_list = list(map(float, vec_b_input.strip("[]").split(",")))

# convert the lists of floats into vectors
vec_a = vector_tools.Vector3D(vec_a_list[0], vec_a_list[1], vec_a_list[2])
vec_b = vector_tools.Vector3D(vec_b_list[0], vec_b_list[1], vec_b_list[2])

projection = vector_tools.VectorTools.calulate_vector_projection(vec_a, vec_b)

print(projection)