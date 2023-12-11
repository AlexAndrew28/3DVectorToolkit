import random
from vectortoolkit import vector
import pytest


def test_vector_generation():
    """Tests the initalisation of the vector class
    """
    vec_a = vector.Vector3D(5, 7, 2)
    vec_b = vector.Vector3D(-5, 0, 42)
    vec_c = vector.Vector3D(32, 7214235, 2)
    vec_d = vector.Vector3D(0.422, 4, -2423252)
    
    
    assert vec_a.get_i() == 5
    assert vec_b.get_j() == 0
    assert vec_c.get_k() == 2
    assert vec_d.get_k() == -2423252
    
    
def test_vector_magnitude():
    """Tests the function that gets the magnitude of a vector
    """
    
    vec_a = vector.Vector3D(12, -3, -4)
    
    assert vec_a.get_magnitude() == 13
    
    vec_b = vector.Vector3D(15, -5, -224)
    
    assert round(vec_b.get_magnitude(),5) == 224.55734
    

def test_vector_unit():
    """Tests the function that calculates the unit vector of a vector
    """
    
    vec_a = vector.Vector3D(16 ,12 ,6)
    
    vec_a_unit = vec_a.get_unit_vector()
    
    assert round(vec_a_unit.get_i(), 5) == 0.76626
    assert round(vec_a_unit.get_j(), 5) == 0.5747
    assert round(vec_a_unit.get_k(), 5) == 0.28735
    
    vec_b = vector.Vector3D(15, 73, -4)
    
    vec_b_unit = vec_b.get_unit_vector()
    
    assert round(vec_b_unit.get_i(), 5) == 0.20099
    assert round(vec_b_unit.get_j(), 5) == 0.97813
    assert round(vec_b_unit.get_k(), 5) == -0.05360
    
def test_vector_scale():
    """Tests the function that scales a vector by a scalar amount
    """
    
    for i in range(10):
        i = random.randint(0,100)
        j = random.randint(0,100)
        k = random.randint(0,100)
        
        scale = 7
        
        vec_a = vector.Vector3D(i, j, k)
        
        vec_a.scale(scale)
        
        assert vec_a.get_i() == i*7
        assert vec_a.get_j() == j*7
        assert vec_a.get_k() == k*7
        
        
    for i in range(10):
        i = random.randint(0,100)
        j = random.randint(0,100)
        k = random.randint(0,100)
        
        scale = -6
        
        vec_a = vector.Vector3D(i, j, k)
        
        vec_a.scale(scale)
        
        assert vec_a.get_i() == i*-6
        assert vec_a.get_j() == j*-6
        assert vec_a.get_k() == k*-6
    