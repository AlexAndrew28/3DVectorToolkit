## 3D Vector Toolkit
### By Alex Andrew

3D vector toolkit developed as a technical challenge for Lambda Automata.

### Installation:
1. Download the wheel file found at:
```
dist/vectortoolkit-1.0.0-py3-none-any.whl
```

2. Use pip to install the library and its requirements:
```
pip install wheel.whl
```
3. You are done, everything should be ready to go

### Features:

#### Python:
There are a number of features revolving around 3D vectors.

To create a new 3D vector:
```python
from vectortoolkit import vector
vec = vector.Vector3D(x, y, z)
```

You can get the magnitude of the vector with:
```python
magnitude = vec.get_magnitude()
```

Or you can get the unit vector for the vector with:
```python
unit = vec.get_unit_vector()
```

You can calculate both dot and cross products using the following commands:
```python
from vectortoolkit import vector, vectortools

vec_a = vector.Vector3D(x, y, z)
vec_b = vector.Vector3D(x, y, z)

dot_prod = vectortools.VectorTools.dot_product(vec_a, vec_b)

cross_prod = vectortools.VectorTools.cross_product(vec_a, vec_b)
```

To calculate the angle between two vectors:
```python
from vectortoolkit import vector, vectortools

vec_a = vector.Vector3D(x, y, z)
vec_b = vector.Vector3D(x, y, z)

angle = vectortools.VectorTools.calculate_angle(vec_a, vec_b)
```

To calculate the distance between two points:
```python
from vectortoolkit import vectortools

distance = vectortools.VectorTools.calculate_distance([x, y, z], [x, y, z])
```

To calculate the projection of one vector onto another:
```python
from vectortoolkit import vector, vectortools

vec_a = vector.Vector3D(x, y, z)
vec_b = vector.Vector3D(x, y, z)

angle = vectortools.VectorTools.calulate_vector_projection(vec_a, vec_b)
```

To see more example code please see the following file:
```
example_application_of_library.py
```

#### Command line:

Usage:
```
vectortoolkit <command> [arguments]
```
    
Commands:
    -d          Calculate dot product of two vectors

    -c          Calculate cross product of two vectors

    -di         Calculate distance between two points

    -a          Caclulate the angle between two vectors

    -p          Calculate the projection of one vector onto another

    -n          Calculate the unit vector of a given vector 

    -help       Show help for commands


Example usages:
The first command will calculate the dot product of the two vectors.

The second command will calculate the angle between the two vectors in radians.
```
    python -m vectortoolkit -d [1, 5, 7] [8, -24, 2]
    python -m vectortoolkit -a [0.6, 532, -7] [7, 4, -43]
```

#### Benchmarking

To ensure the effciency of my library I compared it to a published 3D vector python library: vectormath. The code used for this test can be found in: 
```
benchmark.py
```
For fairness these tests should be run in a fresh environment with only vectormath and vectortoolkit installed (and with both installed through pip). 

From these tests I gained the following results:

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

Each test was run 100000 times.

