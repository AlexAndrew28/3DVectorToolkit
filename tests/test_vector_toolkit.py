from vectortoolkit import vector, vector_tools


def test_add():
    """Tests the element-wise addition of two vectors
    """
    
    vec_a = vector.Vector3D(1, 2, 4)
    vec_b = vector.Vector3D(5, 3, 12)
    
    add_vec_a_b = vector_tools.VectorTools.add_vectors(vec_a, vec_b)
    
    assert add_vec_a_b.get_i() == 6
    assert add_vec_a_b.get_j() == 5
    assert add_vec_a_b.get_k() == 16

    vec_c = vector.Vector3D(-53, 1, 54)
    vec_d = vector.Vector3D(23, -64, 1)
    
    add_vec_c_d = vector_tools.VectorTools.add_vectors(vec_c, vec_d)
    
    assert add_vec_c_d.get_i() == -30
    assert add_vec_c_d.get_j() == -63
    assert add_vec_c_d.get_k() == 55
    
    
def test_subtract():
    """Tests the element-wise subtraction of two vectors
    """
    
    vec_a = vector.Vector3D(1, 2, 4)
    vec_b = vector.Vector3D(5, 3, 12)
    
    subtract_vec_a_b = vector_tools.VectorTools.subtract_vectors(vec_a, vec_b)
    
    assert subtract_vec_a_b.get_i() == -4
    assert subtract_vec_a_b.get_j() == -1
    assert subtract_vec_a_b.get_k() == -8

    vec_c = vector.Vector3D(-53, 1, 54)
    vec_d = vector.Vector3D(23, -64, 1)
    
    subtract_vec_c_d = vector_tools.VectorTools.subtract_vectors(vec_c, vec_d)
    
    assert subtract_vec_c_d.get_i() == -76
    assert subtract_vec_c_d.get_j() == 65
    assert subtract_vec_c_d.get_k() == 53
    
    
def test_multiply():
    """Tests the element-wise multiplication of two vectors
    """
    
    vec_a = vector.Vector3D(1, 2, 4)
    vec_b = vector.Vector3D(5, 3, 12)
    
    multiply_vec_a_b = vector_tools.VectorTools.multiply_vectors(vec_a, vec_b)
    
    assert multiply_vec_a_b.get_i() == 5
    assert multiply_vec_a_b.get_j() == 6
    assert multiply_vec_a_b.get_k() == 48

    vec_c = vector.Vector3D(-53, 1, 54)
    vec_d = vector.Vector3D(23, -64, 1)
    
    multiply_vec_c_d = vector_tools.VectorTools.multiply_vectors(vec_c, vec_d)
    
    assert multiply_vec_c_d.get_i() == -1219
    assert multiply_vec_c_d.get_j() == -64
    assert multiply_vec_c_d.get_k() == 54
    
def test_divide():
    """Tests the element-wise division of two vectors
    """
    
    vec_a = vector.Vector3D(1, 8, 4)
    vec_b = vector.Vector3D(5, 2, 16)
    
    divide_vec_a_b = vector_tools.VectorTools.divide_vectors(vec_a, vec_b)
    
    assert divide_vec_a_b.get_i() == 0.2
    assert divide_vec_a_b.get_j() == 4
    assert divide_vec_a_b.get_k() == 0.25

    vec_c = vector.Vector3D(126, 1, 54)
    vec_d = vector.Vector3D(-3, -64, 1)
    
    divide_vec_c_d = vector_tools.VectorTools.divide_vectors(vec_c, vec_d)
    
    assert divide_vec_c_d.get_i() == -42
    assert divide_vec_c_d.get_j() == -0.015625
    assert divide_vec_c_d.get_k() == 54
    
    
def test_dot_product():
    """Tests the dot product function that calculates the dot product of two vectors
    """
    
    vec_a = vector.Vector3D(1, 8, 4)
    vec_b = vector.Vector3D(5, 2, 16)
    
    vec_a_dot_b = vector_tools.VectorTools.dot_product(vec_a, vec_b)
    
    assert vec_a_dot_b == 85
    
    vec_c = vector.Vector3D(-432, 56, -642)
    vec_d = vector.Vector3D(425, 2, -45)
    
    vec_c_dot_d = vector_tools.VectorTools.dot_product(vec_c, vec_d)
    
    assert vec_c_dot_d == -154598
    
    
def test_distance():
    """Tests that the calculate distance function correctly calculates the distance between two points
    """
    
    assert vector_tools.VectorTools.calculate_distance([0, 0, 0], [0, 10, 0]) == 10
    assert round(vector_tools.VectorTools.calculate_distance([-4, 7, 124], [531, -42, 0]), 5) == 551.36376
    assert round(vector_tools.VectorTools.calculate_distance([-0.696, 0.001, 0.643], [17, -2, 3]), 5) == 17.96407
    assert round(vector_tools.VectorTools.calculate_distance([43, -5, 0], [15, 8, 0]), 5) == 30.87070
    
    assert vector_tools.VectorTools.calculate_distance([0, 0, 0], [0, 0, 0]) == 0
    assert vector_tools.VectorTools.calculate_distance([0, 1043, -2], [0, 1043, -2]) == 0
    assert vector_tools.VectorTools.calculate_distance([421.2, 0, 4], [421.2, 0, 4]) == 0
    
    
def test_cross_product():
    """Tests the cross product function that calcualtes the cross product of two vectors
    """
    
    vec_a = vector.Vector3D(5, 2, 16)
    vec_b = vector.Vector3D(2, 5, -4)
    
    vec_a_cross_b = vector_tools.VectorTools.cross_product(vec_a, vec_b)
    
    assert vec_a_cross_b.get_i() == -88
    assert vec_a_cross_b.get_j() == 52
    assert vec_a_cross_b.get_k() == 21
    
    vec_c = vector.Vector3D(32, 19, -64)
    vec_d = vector.Vector3D(-3, 13, 92)
    
    vec_c_cross_d = vector_tools.VectorTools.cross_product(vec_c, vec_d)
    
    assert vec_c_cross_d.get_i() == 2580
    assert vec_c_cross_d.get_j() == -2752
    assert vec_c_cross_d.get_k() == 473
    
    
def test_vector_angle():
    """Tests the function that calculates the angle between two vectors
    """
    
    vec_a = vector.Vector3D(4, 6, -2)
    vec_b = vector.Vector3D(17, -5, 6)
    
    angle_a_b = vector_tools.VectorTools.calculate_angle(vec_a, vec_b)
    
    assert round(angle_a_b, 5) == 1.38400
    
    vec_c = vector.Vector3D(14, 15, 1)
    vec_d = vector.Vector3D(-2, 3, 35)
    
    angle_c_d = vector_tools.VectorTools.calculate_angle(vec_c, vec_d)
    
    assert round(angle_c_d, 5) == 1.49879
    
    
def test_vector_projection():
    """Tests the function that calculates the projection of vector A onto vector B
    """
    
    vec_a = vector.Vector3D(4, 2, 1)
    vec_b = vector.Vector3D(5, -3, 3)
    
    projection_vec_a_on_b = vector_tools.VectorTools.calulate_vector_projection(vec_a, vec_b)
    
    assert round(projection_vec_a_on_b, 5) == 2.59248
    
    vec_c = vector.Vector3D(2, -1, 5)
    vec_d = vector.Vector3D(4, -1, 1)
    
    projection_vec_c_on_d = vector_tools.VectorTools.calulate_vector_projection(vec_c, vec_d)
    
    assert round(projection_vec_c_on_d, 5) == 3.29983
    
    
def test_angle_and_cross():
    """Tests that AxB returns a vector that is perpendicular to both A and B
    """
    vec_a = vector.Vector3D(2, -35, 24)
    vec_b = vector.Vector3D(-53, 32, 0.36)
    
    # calculate AxB
    vec_a_cross_b = vector_tools.VectorTools.cross_product(vec_a, vec_b)
    
    # get the angle between AxB and A
    angle_a = vector_tools.VectorTools.calculate_angle(vec_a_cross_b, vec_a)
    
    # get the angle between AxB and B
    angle_b= vector_tools.VectorTools.calculate_angle(vec_a_cross_b, vec_b)
    
    # both angles should be the same -> pi/2 radians
    assert angle_a == angle_b
    
    assert round(angle_a, 5) == 1.57080 and round(angle_b, 5) == 1.57080