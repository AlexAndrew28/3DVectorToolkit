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
    
    add_a_b = vectortools.VectorTools.subtract_vectors(a, b)
    
    assert add_a_b.get_i() == -4
    assert add_a_b.get_j() == -1
    assert add_a_b.get_k() == -8

    c = vector.Vector3D(-53, 1, 54)
    d = vector.Vector3D(23, -64, 1)
    
    add_c_d = vectortools.VectorTools.subtract_vectors(c, d)
    
    assert add_c_d.get_i() == -76
    assert add_c_d.get_j() == 65
    assert add_c_d.get_k() == 53