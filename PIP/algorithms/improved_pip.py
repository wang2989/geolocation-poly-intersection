from shapely.geometry import Polygon, Point
from algorithms import r_tree as rtree

# using r tree to store spatial data
class PipImproved():
    def __init__(self, ply):
        self.Rtree = rtree.build_rtree(ply)
        
    def pip(self, points: list) -> list :
        res = {}
        func =rtree.get_intersection_func(self.Rtree)
        for point in points:
           intersections = func(point)
           res[point] = intersections
        #    if Polygon(v) in intersections:
        #        res.append(point)
        return res   

        
#  ----------------------------Test---------------------- 
# p1 = (-122.0045, 40.0335)
# p2 = (-122.0625, 39.60383)
# p3 = (-122.992, 38.90133)
# l = [(-122.0045, 40.0335),(-122.0625, 39.60383),(-122.992, 38.90133)]
# v=[[-123.15532480599389,39.628538026418425],[-119.0541702886981,39.40845421648897],[-122.53717977729988,37.92347617009539],[-123.6189335775142,39.160027074679334],[-123.15532480599389,39.628538026418425]]
# ply = [[[-123.15532480599389,39.628538026418425],[-119.0541702886981,39.40845421648897],[-122.53717977729988,37.92347617009539],[-123.6189335775142,39.160027074679334],[-123.15532480599389,39.628538026418425]]]
#v = [[-123.26039217084163,39.53042492619664],[-118.31546219912128,39.540567692544926],[-123.01051539035592,38.147591729521345],[-117.9998283711392,36.906482297387285],[-121.01150114646877,40.086073672949816],[-121.95840263041526,37.21083867441126],[-118.30231078962211,38.3438355532667],[-120.66956449948808,38.85773081562929],[-123.26039217084163,39.53042492619664]]         
# polys = [Polygon(t) for t in ply]
# RTree = rtree.build_rtree(polys)
# test = PipImproved(RTree)

# print(test.pip(l, v))
# print(is_inside_polygon(p2, v))
# print(is_inside_polygon(p3, v))
            

        
        
        