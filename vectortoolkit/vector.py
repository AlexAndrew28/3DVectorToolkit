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
        
    def get_magnitude(self) -> float:
        """Gets the magnitude of the vector

        Returns:
            float: The magnitude of the vector
        """
        # Uses pythagoras to calculate the magnitude
        return (self.i**2 + self.j**2 + self.k**2)**0.5
    
    def scale(self, factor: float) -> None:
        """Scales the vector by a scalar amount

        Args:
            factor (float): The amout to scale the vector by
        """
        self.i *= factor
        self.j *= factor
        self.k *= factor
    
    def get_unit_vector(self) -> Self:
        """ Returns the unit vector of the vector

        Returns:
            Self: A vector with the same direction but a magnitude of 1
        """
        
        magnitude = self.get_magnitude()
        
        i = self.i / magnitude
        j = self.j / magnitude
        k = self.k / magnitude
        
        return Vector3D(i, j, k)
    

    