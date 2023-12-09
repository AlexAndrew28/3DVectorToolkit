from vectortoolkit import vector, vectortools


def test_add():
    """Tests the element-wise addition of two vectors
    """
    
    a = vector.Vector3D(1, 2, 4)
    b = vector.Vector3D(5, 3, 12)
    
    add_a_b = vectortools.VectorTools.add_vectors(a, b)
    
    assert add_a_b.get_i() == 6
    assert add_a_b.get_j() == 5
    assert add_a_b.get_k() == 16

    c = vector.Vector3D(-53, 1, 54)
    d = vector.Vector3D(23, -64, 1)
    
    add_c_d = vectortools.VectorTools.add_vectors(c, d)
    
    assert add_c_d.get_i() == -30
    assert add_c_d.get_j() == -63
    assert add_c_d.get_k() == 55
    
    
def test_subtract():
    """Tests the element-wise subtraction of two vectors
    """
    
    a = vector.Vector3D(1, 2, 4)
    b = vector.Vector3D(5, 3, 12)
    
    subtract_a_b = vectortools.VectorTools.subtract_vectors(a, b)
    
    assert subtract_a_b.get_i() == -4
    assert subtract_a_b.get_j() == -1
    assert subtract_a_b.get_k() == -8

    c = vector.Vector3D(-53, 1, 54)
    d = vector.Vector3D(23, -64, 1)
    
    subtract_c_d = vectortools.VectorTools.subtract_vectors(c, d)
    
    assert subtract_c_d.get_i() == -76
    assert subtract_c_d.get_j() == 65
    assert subtract_c_d.get_k() == 53
    
    
def test_multiply():
    """Tests the element-wise multiplication of two vectors
    """
    
    a = vector.Vector3D(1, 2, 4)
    b = vector.Vector3D(5, 3, 12)
    
    multiply_a_b = vectortools.VectorTools.multiply_vectors(a, b)
    
    assert multiply_a_b.get_i() == 5
    assert multiply_a_b.get_j() == 6
    assert multiply_a_b.get_k() == 48

    c = vector.Vector3D(-53, 1, 54)
    d = vector.Vector3D(23, -64, 1)
    
    multiply_c_d = vectortools.VectorTools.multiply_vectors(c, d)
    
    assert multiply_c_d.get_i() == -1219
    assert multiply_c_d.get_j() == -64
    assert multiply_c_d.get_k() == 54
    
def test_divide():
    """Tests the element-wise multiplication of two vectors
    """
    
    a = vector.Vector3D(1, 8, 4)
    b = vector.Vector3D(5, 2, 16)
    
    divide_a_b = vectortools.VectorTools.divide_vectors(a, b)
    
    assert divide_a_b.get_i() == 0.2
    assert divide_a_b.get_j() == 4
    assert divide_a_b.get_k() == 0.25

    c = vector.Vector3D(126, 1, 54)
    d = vector.Vector3D(-3, -64, 1)
    
    divide_c_d = vectortools.VectorTools.divide_vectors(c, d)
    
    assert divide_c_d.get_i() == -42
    assert divide_c_d.get_j() == -0.015625
    assert divide_c_d.get_k() == 54