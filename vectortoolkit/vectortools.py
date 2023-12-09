from vectortoolkit.vector import Vector3D

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
    
