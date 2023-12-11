from vectortoolkit.vector import Vector3D
import math

class VectorTools:
    def __init__(self) -> None:
        pass
    
    def add_vectors(vec_a: Vector3D, vec_b: Vector3D) -> Vector3D:
        """Adds two vectors together element-wise

        Args:
            vec_a (Vector3D): A 3D vector
            vec_b (Vector3D): A 3D vector

        Returns:
            Vector3D: The vector resulting from adding the two input vectors together
        """
        i = vec_a.get_i() + vec_b.get_i()
        j = vec_a.get_j() + vec_b.get_j()
        k = vec_a.get_k() + vec_b.get_k()
        return Vector3D(i, j, k)
    
    def subtract_vectors(vec_a: Vector3D, vec_b: Vector3D) -> Vector3D:
        """ subtracts a vector from another vector element-wise

        Args:
            vec_a (Vector3D): A 3D vector
            vec_b (Vector3D): A 3D vector to subtract

        Returns:
            Vector3D: The vector resulting from subtracting a vector from another
        """
        i = vec_a.get_i() - vec_b.get_i()
        j = vec_a.get_j() - vec_b.get_j()
        k = vec_a.get_k() - vec_b.get_k()
        return Vector3D(i, j, k)
    
    def multiply_vectors(vec_a: Vector3D, vec_b: Vector3D) -> Vector3D:
        """Multiplies two vectors together element-wise

        Args:
            vec_a (Vector3D): A 3D vector
            vec_b (Vector3D): A 3D vector

        Returns:
            Vector3D: The vector resulting from multiplying the two input vectors together
        """
        i = vec_a.get_i() * vec_b.get_i()
        j = vec_a.get_j() * vec_b.get_j()
        k = vec_a.get_k() * vec_b.get_k()
        return Vector3D(i, j, k)
    
    def divide_vectors(vec_a: Vector3D, vec_b: Vector3D) -> Vector3D:
        """Divides a vecor by another vector element-wise

        Args:
            vec_a (Vector3D): A 3D vector
            vec_b (Vector3D): A 3D vector that divides the first

        Returns:
            Vector3D: The vector resulting from dividing one vector from another
        """
        i = vec_a.get_i() / vec_b.get_i()
        j = vec_a.get_j() / vec_b.get_j()
        k = vec_a.get_k() / vec_b.get_k()
        return Vector3D(i, j, k)
    
    def dot_product(vec_a: Vector3D, vec_b: Vector3D) -> float:
        """Calculates the dot product of two vectors 

        Args:
            vec_a (Vector3D): A 3D vector
            vec_b (Vector3D): A 3D vector

        Returns:
            float: The dot product of the two input vectors
        """
        i_part = vec_a.get_i() * vec_b.get_i()
        j_part = vec_a.get_j() * vec_b.get_j()
        k_part = vec_a.get_k() * vec_b.get_k()
        return i_part + j_part + k_part
    
    def cross_product(vec_a: Vector3D, vec_b: Vector3D) -> Vector3D:
        """Calculates th cross product of two given vectors and returns the result

        Args:
            vec_a (Vector3D): A 3D vector
            vec_b (Vector3D): A 3D vector

        Returns:
            Vector3D: The cross product of the two input vectors 
        """
        
        i = (vec_a.get_j() * vec_b.get_k()) - (vec_a.get_k() * vec_b.get_j())
        j = (vec_a.get_k() * vec_b.get_i()) - (vec_a.get_i() * vec_b.get_k())
        k = (vec_a.get_i() * vec_b.get_j()) - (vec_a.get_j() * vec_b.get_i())
        
        return Vector3D(i, j, k)
        
        
    def calculate_distance(point_a: [float, float, float], point_b: [float, float, float]) -> float:
        """Calculates the distance between two points in 3D space

        Args:
            point_a (float, float, float]): A point in 3D space described as a list of distances [x, y, z]
            point_b (float, float, float]): A point in 3D space described as a list of distances [x, y, z]

        Returns:
            float: The distance between the given two coordinates
        """
        # calculates the distance in each dimensions between the two points and squares it
        dimenson_distance_squared = list(map(lambda x,y: (x-y)**2, point_a, point_b))
        
        # uses pythagoras to get the distance between two points
        distance = (sum(dimenson_distance_squared))**0.5
        
        return distance
    
    def calculate_angle(vec_a: Vector3D, vec_b: Vector3D) -> float:
        """Calculates the angle (in radians) between any two given vectors 

        Args:
            vec_a (Vector3D): A 3D vector
            vec_b (Vector3D): A 3D vector

        Returns:
            float: The angle in radians between the two vectors
        """
        
        # formula for the angle is: cos(theta) = (A.B)/(|A|*|B|)
        
        vec_a_dot_b = VectorTools.dot_product(vec_a, vec_b)
        
        magnitudes_multiplied = vec_a.get_magnitude() * vec_b.get_magnitude()
        
        angle = math.acos(vec_a_dot_b/magnitudes_multiplied)
        
        return angle
        
        
