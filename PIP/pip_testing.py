import sys

from algorithms.improved_pip import PipImproved
from algorithms.point_in_poly import PointInPoly as pip
import unittest
from shapely.geometry import Polygon, Point
import algorithms.r_tree as rtree


l = [(-122.0045, 40.0335),(-122.0625, 39.60383),(-122.992, 38.90133)]
ply = [[[-123.15532480599389,39.628538026418425],[-119.0541702886981,39.40845421648897],[-122.53717977729988,37.92347617009539],[-123.6189335775142,39.160027074679334],[-123.15532480599389,39.628538026418425]]]
test = pip(l, ply)
class TestRayCasting(unittest.TestCase):

    def test_ray_casting_small_size(self):
       print(test.rayCasting())
    
    def test_ray_casting_large_size(self):
        pass
    
class TestWindNumber(unittest.TestCase):
    
    def test_wind_number_small_size(self):
        print(test.windNumber())
    
    def test_wind_number_large_size(self):
        pass

class TestImproved(unittest.TestCase):
    def test_improved_small_size(self):
        # polys = [Polygon(t) for t in ply]
        # RTree = rtree.build_rtree(polys)
        test =  PipImproved(ply)
        print(test.pip(l))
        pass
    
    def test_improved_large_size(self):
        pass   
unittest.main()