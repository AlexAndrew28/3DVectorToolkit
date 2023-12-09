from vectortoolkit import vector


def test_vector_generation():
    """Tests the initalisation of the vector class
    """
    a = vector.Vector3D(5, 7, 2)
    b = vector.Vector3D(-5, 0, 42)
    c = vector.Vector3D(32, 7214235, 2)
    d = vector.Vector3D(0.422, 4, -2423252)
    
    
    assert a.get_i() == 5
    assert b.get_j() == 0
    assert c.get_k() == 2
    assert d.get_k() == -2423252