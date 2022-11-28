import sys
sys.path.insert(0, '../geolocation-poly-intersection/src/PIP')
from algorithms.improved_pip import PipImproved
from algorithms.point_in_poly import PointInPoly as pip
import unittest
from shapely.geometry import Polygon, Point
import time
import csv
import pandas as pd 
import accuracy
import json
import matplotlib.pyplot as plt
import numpy as np

# Polygon structures used for test cases
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
columbus_poly =[[[-82.94713752299221,40.012085242026195],[-82.98723463591321,39.9740518390705],[-82.98659817380349,39.94478096464229],[-82.946501060882,39.915009398900104],[-82.89749347842276,39.95600294742564],[-82.946501060882,39.96917423012789],[-82.94713752299221,40.012085242026195]]]
#test = pip(l, ply)

# Declaring and initializing additional test variables
small_size =[]
large_size =[]
large_size_cbus = []
large_size_cbus_multiple_polygons =[]
my_csv = pd.read_csv('data/kepler.gl_new_dataset.csv', usecols=['Latitude','Longitude'])
x = my_csv['Latitude']
y = my_csv['Longitude']
points =[]
for i, x in enumerate(x):
    points.append((y[i], x))  

my_csv = pd.read_csv('data/cleaned_crash_stats.csv', usecols=['Latitude','Longitude'])
dataframe = pd.DataFrame(my_csv)
dataframe = dataframe.fillna(0)

x = dataframe['Latitude'].astype(float)
y = dataframe['Longitude'].astype(float)

columbus_points =[]

for i, x in enumerate(x):
    if(x == 0):continue
    columbus_points.append((y[i], x)) 

# Load JSON File
f = open('data/cleaned_polygon_geojson.json')
poly_json =json.load(f)
columbus_polygons = [x['geometry']['coordinates'][0] for x in poly_json['features']]
# poly1 = poly_json['features'][0]['geometry']['coordinates'][0]
#print(len([x['geometry']['coordinates'][0] for x in poly_json['features']]))


# Test Framework
class Test_1_RayCasting(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        
    def tearDown(self):
        t = time.time()-self.startTime
        print('%s: %.6f' % (self.id(),t))

    def test_ray_casting_1_small_size(self):
        time.sleep(1)
        test = pip(l, ply1)
        y_actual = test.rayCasting()
        diff = accuracy.get_accuracy(l, ply1, y_actual)
        print(f'Difference between expected result: {diff}')
        small_size.append(time.time()-self.startTime)
         
    def test_ray_casting_2_large_size(self):
        time.sleep(1)
        test = pip(points, ply2)
        y_actual = test.rayCasting()
        diff =accuracy.get_accuracy(points, ply2, y_actual)
        print(f'Difference between expected result: {diff}')
        large_size.append(time.time()-self.startTime)
        
    def test_ray_casting_3_large_size_columbus_area(self):
        time.sleep(1)
        test = pip(columbus_points, columbus_poly)
        y_actual =test.rayCasting()  
        diff =accuracy.get_accuracy(columbus_points, columbus_poly, y_actual)  
        print(f'Difference between expected result: {diff}')
        large_size_cbus.append(time.time()-self.startTime)
        
    def test_ray_casting_4_large_size_multiple_polygons(self):
         time.sleep(1)
         test = pip(columbus_points, columbus_polygons)
         y_actual =test.rayCasting() 
         diff =accuracy.get_accuracy(columbus_points, columbus_polygons, y_actual)  
         print(f'Difference between expected result: {diff}')
         large_size_cbus_multiple_polygons.append(time.time()-self.startTime)
    
class Test_2_WindNumber(unittest.TestCase):      
    def setUp(self):
        self.startTime = time.time()
        
    def tearDown(self):
        t = time.time()-self.startTime
        print('%s: %.6f' % (self.id(),t))
    
    def test_wind_number_1_small_size(self):
        time.sleep(1)
        test = pip(l, ply1)
        y_actual = test.windNumber() 
        
        diff = accuracy.get_accuracy(l, ply1, y_actual)
        print(f'Difference between expected result: {diff}')
        small_size.append(time.time()-self.startTime)
        
    def test_wind_number_2_large_size(self):
        time.sleep(1)
        test = pip(points, ply2)
        y_actual = test.windNumber()
        diff =accuracy.get_accuracy(points, ply2, y_actual)
        print(f'Difference between expected result: {diff}')
        large_size.append(time.time()-self.startTime)
        
    def test_wind_number_3_large_size_columbus_area(self):
        time.sleep(1)
        test = pip(columbus_points, columbus_poly)
        y_actual = test.windNumber()
        points = pd.DataFrame([[x[1], x[0]] for x in y_actual], columns=['Latitude','Longitude'])
        points.to_csv('PIP_columbus_area.csv',index = False)
        diff =accuracy.get_accuracy(columbus_points, columbus_poly, y_actual)  
        print(f'Difference between expected result: {diff}')
        large_size_cbus.append(time.time()-self.startTime)
        
    def test_wind_number_4_large_size_columbus_area_multiple_polygons(self):
        time.sleep(1)
        test = pip(columbus_points, columbus_polygons)
        y_actual = test.windNumber()
        # points = pd.DataFrame([[x[0], x[1]] for x in y_actual], columns=['Latitude','Longitude'])
        # points.to_csv('PIP_columbus_area.csv',index = False)
        diff =accuracy.get_accuracy(columbus_points, columbus_polygons, y_actual)  
        print(f'Difference between expected result: {diff}')
        large_size_cbus_multiple_polygons.append(time.time()-self.startTime)

class Test_3_rTree(unittest.TestCase):
    
    def setUp(self):   
        self.startTime = time.time()
        
    def tearDown(self):
        t = time.time()-self.startTime
        print('%s: %.6f' % (self.id(),t))
        
    def test_improved_1_small_size(self):
        # polys = [Polygon(t) for t in ply]
        # RTree = rtree.build_rtree(polys)
        test =  PipImproved(ply1)
        time.sleep(1)
        y_actual = test.pip(l)
        diff = accuracy.get_accuracy(l, ply1, y_actual)
        print(f'Difference between expected result: {diff}')
        small_size.append(time.time()-self.startTime)
        
    def test_improved_2_large_size(self):
        test =  PipImproved(ply2)
        time.sleep(1)
        y_actual = test.pip(points)
        diff =accuracy.get_accuracy(points, ply2, y_actual)
        print(f'Difference between expected result: {diff}')
        large_size.append(time.time()-self.startTime)
    
    def test_improved_3_large_size_columbus_area(self):
        test =  PipImproved(columbus_poly)
        time.sleep(1)
        y_actual = test.pip(columbus_points)
        diff =accuracy.get_accuracy(columbus_points, columbus_poly, y_actual)  
        print(f'Difference between expected result: {diff}')
        large_size_cbus.append(time.time()-self.startTime)
        
    def test_improved_4_large_size_multiple_polygons(self):
        test = PipImproved(columbus_polygons)
        time.sleep(1)
        y_actual = test.pip(columbus_points)
        diff =accuracy.get_accuracy(columbus_points, columbus_polygons, y_actual)  
        print(f'Difference between expected result: {diff}')
        large_size_cbus_multiple_polygons.append(time.time()-self.startTime)
        
class Test_4_draw_chart(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        
    def tearDown(self):
        t = time.time()-self.startTime
    def test_draw(self):
        langs = ['RayCasting', 'WindNumber', 'RTree']
        barWidth = 0.25
        fig = plt.subplots(figsize =(12, 8))
        
        # Set position of bar on X axis
        br1 = np.arange(len(small_size))
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
        br4 = [x + barWidth for x in br3]
        
        
        # Make the plot
        plt.bar(br1, small_size, color ='r', width = barWidth,
                edgecolor ='grey', label ='SmallSize')
        plt.bar(br2, large_size, color ='g', width = barWidth,
                edgecolor ='grey', label ='LargeSize')
        plt.bar(br3, large_size_cbus, color ='y', width = barWidth,
                edgecolor ='grey', label ='LargeSizeColumbus')
        plt.bar(br4, large_size_cbus_multiple_polygons, color ='b', width = barWidth,
        edgecolor ='grey', label ='ColumbusMultiPolys')
        
        # Adding Xticks
        plt.xlabel('Algorithms', fontweight ='bold', fontsize = 15)
        plt.ylabel('Time(s)', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(small_size))],
                langs)
        
        plt.legend()
        plt.show()

        plt.close()


unittest.main()
