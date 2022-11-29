#!/bin/sh

# Run performance tests for polygon-polygon intersection
python3 test/test_poly_intersection.py

# Run performance tests for point-in-polygon
python3 test/test_pip.py

# Run performance tests for line-simplification

# Run kepler visualization for output data
python3 src/concat_graphs.py
python3 src/kepler_visualize.py