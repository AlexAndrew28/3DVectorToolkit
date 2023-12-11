"""
The following file contains benchmarking information that compairs the efficiency of my library
vectortoolkit with a pre-existing library vectormath. For fairness these tests should be run in a 
fresh environment with only vectormath and vectortoolkit installed (and with both installed through
pip). 

In this environment I gained the following results:

Calculate angle between two vectors	
vectormath:	    5.011 seconds
vectortools:	0.408 seconds

Calculate cross product of two vectors	
vectormath:	    8.577 seconds
vectortools:	0.267 seconds

Calculate dot product of two two vectors	
vectormath:	    2.123 seconds
vectortools:	0.166 seconds

Find the unit vector	
vectormath:	    3.884 seconds
vectortools:	0.05 seconds

Each test was run 100000 times

    
"""


def vectormath_library_test_angle():
    """Find the angle between two vectors using vectormath
    """
    vec_a = vectormath.Vector3(5, 10, 4)
    vec_b = vectormath.Vector3(16, -2, 100)

    angle = vec_a.angle(vec_b)
    
def vectormath_library_test_cross():
    """Find the cross product of two vectors using vectormath
    """
    vec_a = vectormath.Vector3(5, 10, 4)
    vec_b = vectormath.Vector3(16, -2, 100)

    cross = vec_a.cross(vec_b)
    
def vectormath_library_test_dot():
    """Find the dot product of two vectors using vectormath
    """
    vec_a = vectormath.Vector3(5, 10, 4)
    vec_b = vectormath.Vector3(16, -2, 100)

    dot = vec_a.dot(vec_b)
    
def vectormath_library_test_unit():
    """Find the unit vector of a vector using vectormath
    """
    vec_a = vectormath.Vector3(5, 10, 4)

    unit = vec_a.as_unit()

def vectortoolkit_library_test_angle():
    """Find the angle between two vectors using my library vectortoolkit
    """
    vec_a = vector.Vector3D(5, 10, 4)
    vec_b = vector.Vector3D(16, -2, 100)

    angle = vectortools.VectorTools.calculate_angle(vec_a, vec_b)
    
def vectortoolkit_library_test_cross():
    """Find the cross product of two vectors using my library vectortoolkit
    """
    vec_a = vector.Vector3D(5, 10, 4)
    vec_b = vector.Vector3D(16, -2, 100)
    
    cross = vectortools.VectorTools.cross_product(vec_a, vec_b)
    
def vectortoolkit_library_test_dot():
    """Find the dot product of two vectors using my library vectortoolkit
    """
    vec_a = vector.Vector3D(5, 10, 4)
    vec_b = vector.Vector3D(16, -2, 100)
    
    dot = vectortools.VectorTools.dot_product(vec_a, vec_b)
    
    
def vectortoolkit_library_test_unit():
    """Find the unit vector of a vector using my library vectortoolkit
    """
    vec_a = vector.Vector3D(5, 10, 4)

    unit = vec_a.get_unit_vector


if __name__ == '__main__':
    from vectortoolkit import vector, vectortools
    import timeit
    import vectormath
    
    timeit_number = 100000
    
    # find angle between vectors
    vectormath_angle_time = timeit.timeit("vectormath_library_test_angle()", setup="from __main__ import vectormath_library_test_angle", number=timeit_number)
    vectortools_angle_time = timeit.timeit("vectortoolkit_library_test_angle()", setup="from __main__ import vectortoolkit_library_test_angle", number=timeit_number)
    
    # find cross product
    vectormath_cross_time = timeit.timeit("vectormath_library_test_cross()", setup="from __main__ import vectormath_library_test_cross", number=timeit_number)
    vectortools_cross_time = timeit.timeit("vectortoolkit_library_test_cross()", setup="from __main__ import vectortoolkit_library_test_cross", number=timeit_number)

    # find dot product
    vectormath_dot_time = timeit.timeit("vectormath_library_test_dot()", setup="from __main__ import vectormath_library_test_dot", number=timeit_number)
    vectortools_dot_time = timeit.timeit("vectortoolkit_library_test_dot()", setup="from __main__ import vectortoolkit_library_test_dot", number=timeit_number)
 
    # find unit vector 
    vectormath_unit_time = timeit.timeit("vectormath_library_test_unit()", setup="from __main__ import vectormath_library_test_unit", number=timeit_number)
    vectortools_unit_time = timeit.timeit("vectortoolkit_library_test_unit()", setup="from __main__ import vectortoolkit_library_test_unit", number=timeit_number)
    
    print("angle between two vectors")
    print("vectormath: ", round(vectormath_angle_time,3))
    print("vectortools: ", round(vectortools_angle_time,3))
    
    print("cross product of two vectors")
    print("vectormath: ", round(vectormath_cross_time,3))
    print("vectortools: ", round(vectortools_cross_time,3))
    
    print("dot product of two two vectors")
    print("vectormath: ", round(vectormath_dot_time,3))
    print("vectortools: ", round(vectortools_dot_time,3))
    
    print("finding the unit vector")
    print("vectormath: ", round(vectormath_unit_time,3))
    print("vectortools: ", round(vectortools_unit_time,3))