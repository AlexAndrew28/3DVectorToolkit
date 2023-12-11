import os
import sys

project = '3D Vector Toolkit'
copyright = '2023, Alex A'
author = 'Alex A'
release = '1.0.1'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []


html_theme = 'classic'
html_static_path = ['_static']

sys.path.insert(0, os.path.abspath('..'))
