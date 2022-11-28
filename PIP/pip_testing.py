import sys
from algorithms.improved_pip import PipImproved
from algorithms.point_in_poly import PointInPoly as pip
import unittest
from shapely.geometry import Polygon, Point
import time
import csv
import pandas as pd 
import accuracy

l = [(-122.0045, 40.0335),(-122.0625, 39.60383),(-122.992, 38.90133)]
ply1 = [[[-123.15532480599389,39.628538026418425],[-119.0541702886981,39.40845421648897],[-122.53717977729988,37.92347617009539],[-123.6189335775142,39.160027074679334]]]
ply2 =[[[-120.91522668758174,37.03968992268706],[-121.02735067562631,35.988375676058794],[-119.6725191534244,35.19819855126699],[-119.75661214445758,36.98746397296957],]
       ,[[-118.85027657443348,36.85300395923757],[-118.82224557742211,35.02239699985234],[-117.34594640150613,36.86795566702479],[-118.31768763122297,37.43394875103847]]
       ,[[-117.19934528967242,35.23403173723355],[-118.38409338107398,34.388527082529926],[-118.21093789079211,33.981428254846364],[-118.10157652850896,34.44115513758513],[-117.6459041856621,33.89069540727235],[-117.60033695137771,34.756226929375956],[-116.40647541311947,34.96560973200853],[-116.85303430910918,35.43476744361868]]]
ply3 =[[[-120.91522668758174,37.03968992268706],[-121.02735067562631,35.988375676058794],[-119.6725191534244,35.19819855126699],[-119.75661214445758,36.98746397296957]]
       ,[[-118.85027657443348,36.85300395923757],[-118.82224557742211,35.02239699985234],[-117.34594640150613,36.86795566702479],[-118.31768763122297,37.43394875103847]]
       ,[[-117.19934528967242,35.23403173723355],[-118.38409338107398,34.388527082529926],[-118.21093789079211,33.981428254846364],[-118.10157652850896,34.44115513758513],[-117.6459041856621,33.89069540727235],[-117.60033695137771,34.756226929375956],[-116.40647541311947,34.96560973200853],[-116.85303430910918,35.43476744361868]],
       [[-123.02980205324052,39.24888199618645],[-122.15189129718004,38.19034135855964],[-121.36975262359891,39.31066007301397]]
       , [[-120.23644964759379,39.19942031567585],[-118.11350181930217,38.91433976723213],[-120.28433568883335,38.715344605330465],[-121.70495491227662,37.44640255810604]]
       ,[[-119.52301608426491,38.53004176621298],[-119.38859775116038,37.26976643399039],[-118.15511187090418,36.821689307762114]]]
#test = pip(l, ply)
ray_casting_time =[]
wind_number_time =[]
r_tree_time =[]
my_csv = pd.read_csv('PIP/kepler.gl_new_dataset.csv', usecols=['Latitude','Longitude'])
x = my_csv['Latitude']
y = my_csv['Longitude']
points =[]
for i, x in enumerate(x):
  points.append((y[i], x))  


class TestRayCasting(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        
    def tearDown(self):
        t = time.time()-self.startTime
        print('%s: %.6f' % (self.id(),t))

    def test_ray_casting_small_size(self):
        time.sleep(1)
        test = pip(l, ply1)
        y_actual = test.rayCasting()
        diff = accuracy.get_accuracy(l, ply1, y_actual)
        print(f'Difference between expected result: {diff}')
        
         
    def test_ray_casting_large_size1(self):
        time.sleep(1)
        test = pip(points, ply2)
        y_actual = test.rayCasting()
        diff =accuracy.get_accuracy(points, ply2, y_actual)
        print(f'Difference between expected result: {diff}')
        
    def test_ray_casting_large_size2(self):
        time.sleep(1)
        test = pip(points, ply3)
        y_actual =test.rayCasting()  
        diff =accuracy.get_accuracy(points, ply3, y_actual)  
        print(f'Difference between expected result: {diff}')
    
class TestWindNumber(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        
    def tearDown(self):
        t = time.time()-self.startTime
        print('%s: %.6f' % (self.id(),t))
    
    def test_wind_number_small_size(self):
        time.sleep(1)
        test = pip(l, ply1)
        y_actual = test.windNumber() 
        diff = accuracy.get_accuracy(l, ply1, y_actual)
        print(f'Difference between expected result: {diff}')
        
    def test_wind_number_large_size1(self):
        time.sleep(1)
        test = pip(points, ply2)
        y_actual = test.windNumber()
        diff =accuracy.get_accuracy(points, ply2, y_actual)
        print(f'Difference between expected result: {diff}')
        
    def test_wind_number_large_size2(self):
        time.sleep(1)
        test = pip(points, ply3)
        y_actual = test.windNumber()
        diff =accuracy.get_accuracy(points, ply3, y_actual)  
        print(f'Difference between expected result: {diff}')


class TestImproved(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        
    def tearDown(self):
        t = time.time()-self.startTime
        print('%s: %.6f' % (self.id(),t))
        
    def test_improved_small_size(self):
        # polys = [Polygon(t) for t in ply]
        # RTree = rtree.build_rtree(polys)
        test =  PipImproved(ply1)
        time.sleep(1)
        y_actual = test.pip(l)

        diff = accuracy.get_accuracy(l, ply1, y_actual)
        print(f'Difference between expected result: {diff}')

    
    def test_improved_large_size1(self):
        test =  PipImproved(ply2)
        time.sleep(1)
        y_actual = test.pip(points)
        diff =accuracy.get_accuracy(points, ply2, y_actual)
        print(f'Difference between expected result: {diff}')
    
    def test_improved_large_size2(self):
        test =  PipImproved(ply3)
        time.sleep(1)
        y_actual = test.pip(points)
        diff =accuracy.get_accuracy(points, ply3, y_actual)  
        print(f'Difference between expected result: {diff}')
     
      
  
unittest.main()
