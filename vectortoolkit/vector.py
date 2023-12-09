from typing_extensions import Self

class Vector3D:
    def __init__(self, i: float, j: float ,k: float):
        """Initialises a 3D vector from its i,j and k components

        Args:
            i (float): magnitude of the vector in i direction
            j (float): magnitude of the vector in j direction
            k (float): magnitude of the vector in k direction
        """
        self.i = i
        self.j = j
        self.k = k
        
    def get_i(self) -> float:
        """Gets the i component of the vector

        Returns:
            float: The i component of the vector
        """
        return self.i
    
    def get_j(self) -> float:
        """Gets the j component of the vector

        Returns:
            float: The j component of the vector
        """
        return self.j
    
    def get_k(self) -> float:
        """Gets the k component of the vector

        Returns:
            float: The k component of the vector
        """
        return self.k
        
    def get_magnitude() -> float:
        pass
    
    def get_direction() -> float:
        pass
    
    def get_unit_vector() -> Self:
        pass
    
    def get_normal() -> Self:
        pass

    