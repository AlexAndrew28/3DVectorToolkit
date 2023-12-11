.. 3DVectorToolkit documentation master file, created by
   sphinx-quickstart on Mon Dec 11 17:07:22 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to 3DVectorToolkit's documentation!
===========================================

##################
3D Vector Toolkit
##################

By Alex Andrew

3D vector toolkit developed as a technical challenge for Lambda Automata.

==============
Installation:
==============
1. Download the wheel file from the latest release or from the code at the following location 
::

   dist/vectortoolkit-1.0.0-py3-none-any.whl


2. Use pip to install the library and its requirements: 
::

   pip install wheel.whl

3. You are done, everything should be ready to go

==========
Features:
==========

--------
Python:
--------

There are a number of features revolving around 3D vectors.

To create a new 3D vector: ::

   from vectortoolkit import vector
   vec = vector.Vector3D(x, y, z)


You can get the magnitude of the vector with: ::

   magnitude = vec.get_magnitude()


Or you can get the unit vector for the vector with: ::

   unit = vec.get_unit_vector()


You can calculate both dot and cross products using the following commands: ::

   from vectortoolkit import vector, vector_tools

   vec_a = vector.Vector3D(x, y, z)
   vec_b = vector.Vector3D(x, y, z)

   dot_prod = vector_tools.VectorTools.dot_product(vec_a, vec_b)

   cross_prod = vector_tools.VectorTools.cross_product(vec_a, vec_b)


To calculate the angle between two vectors: ::

   from vectortoolkit import vector, vector_tools

   vec_a = vector.Vector3D(x, y, z)
   vec_b = vector.Vector3D(x, y, z)

   angle = vector_tools.VectorTools.calculate_angle(vec_a, vec_b)


To calculate the distance between two points: ::

   from vectortoolkit import vector_tools

   distance = vector_tools.VectorTools.calculate_distance([x, y, z], [x, y, z])


To calculate the projection of one vector onto another: ::

   from vectortoolkit import vector, vector_tools

   vec_a = vector.Vector3D(x, y, z)
   vec_b = vector.Vector3D(x, y, z)

   angle = vector_tools.VectorTools.calulate_vector_projection(vec_a, vec_b)

You can also add, subtract, multiply and divide vectors element-wise: ::

   vec_a = vector.Vector3D(x, y, z)
   vec_b = vector.Vector3D(x, y, z)

   vec_c = vector_tools.VectorTools.add_vectors(vec_a, vec_b)
   vec_d = vector_tools.VectorTools.subtract_vectors(vec_a, vec_b)
   vec_e = vector_tools.VectorTools.multiply_vectors(vec_a, vec_b)
   vec_f = vector_tools.VectorTools.divide_vectors(vec_a, vec_b)


--------------
Command line:
--------------

Usage: ::

   vectortoolkit <command> [arguments]

    
Commands::

    -d          Calculate dot product of two vectors

    -c          Calculate cross product of two vectors

    -di         Calculate distance between two points

    -a          Caclulate the angle between two vectors

    -p          Calculate the projection of one vector onto another

    -n          Calculate the unit vector of a given vector 

    -help       Show help for commands


Example usages:
The first command will calculate the dot product of the two vectors.

The second command will calculate the angle between the two vectors in radians. ::

    python -m vectortoolkit -d [1, 5, 7] [8, -24, 2]
    python -m vectortoolkit -a [0.6, 532, -7] [7, 4, -43]



