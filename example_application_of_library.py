from vectortoolkit import vector, vectortools

"""
Task 1 - ensure that the cross product of two vectors is perpendicular to both vectors
"""

vec_a = vector.Vector3D(17, 9, -7)
vec_b = vector.Vector3D(18, 24, -24)

vec_a_cross_b = vectortools.VectorTools.cross_product(vec_a, vec_b)

angle_cross_a = vectortools.VectorTools.calculate_angle(vec_a_cross_b, vec_a)
angle_cross_b = vectortools.VectorTools.calculate_angle(vec_a_cross_b, vec_b)

# check the angle is equal to pi/2 radians
if round(angle_cross_a, 5) == 1.57080 and round(angle_cross_b, 5) == 1.57080:
    print("A cross B is perpendicular to both A and B")
    
    
"""
Task 2 - A veihcle is traveling along (4, 7, 9) and is at (0, 0, 0). The veihcle wants to change 
its heading to reach point (15, 9, -6). What is the angle of the change in heading and how far 
away is the point?

"""

current_vec_travel = vector.Vector3D(4, 7, 9)

current_location = (0, 0, 0)
point_of_interest = (15, 9, -6)

# get new direction of travel based on current location and point of interest
new_vec_travel = vector.Vector3D(point_of_interest[0]-current_location[0], point_of_interest[1]-current_location[1], point_of_interest[2]-current_location[2])

# get the angle of the change
heading_change = vectortools.VectorTools.calculate_angle(current_vec_travel, new_vec_travel)

# get the distance to the new point
distance_to_point = vectortools.VectorTools.calculate_distance(current_location, point_of_interest)

print("Change in heading (radians): ", round(heading_change, 5))
print("Distance to point of interest: ", round(distance_to_point, 5))