import unittest
import time
import polygon_intersection
from shapely.geometry import Polygon, mapping
import math
# inner case
inside_case_first_poly = [[0,0], [0, 2], [4,2], [4, 0]]
inside_case_second_poly  = [[0,0], [0, 2], [2,2], [2, 0]]
#normal case
convex_case_first_poly =[[-121.33657701203961,39.4644608274132],[-118.41696410320476,39.808810675932236],[-118.28545000821218,38.14242026589671],[-121.33657701203961,38.11138378652503]]
convex_case_second_poly = [[-119.32264241961325,37.64915634673547],[-119.08782961664949,38.78121751212849],[-116.92114784384725,39.146370415097934],[-116.92114784384725,37.90224616382728]]
# no intersection case
no_intersection_first_poly = [[0,0], [0, 2], [4,2], [4, 0]]
no_intersection_second_poly = [[0,10], [0, 20], [10,2], [2, 10]]

# concave case:
concave_case_first_poly=[[-121.3078779355798,39.501403604067164],[-120.52872636210914,37.19991728187789],[-118.87436343213689,37.60689051788002]]
concave_case_second_poly= [[-121.54269073854354,39.36125706946052],[-121.26518469867732,37.44606129152354],[-119.98438759160202,37.361275129880035],[-121.07306513261604,37.75893497289224],[-120.30458686837093,37.817979172820664],[-121.158451606421,37.910667563329284],[-119.97371428237646,38.25511425646991],[-121.10508506029296,38.17125252642114],[-120.00573421005336,39.08011900767557],[-121.04104520493911,38.41418515977385],[-120.96633204035972,39.63304859796313],[-121.29720462635424,38.54786858899416]]

# self-intersecting case:
self_intersecting_case_first = [[-118.32347033354482,37.915823646315715],[-118.62364619048267,39.6987057115261],[-117.81940144170606,39.14305825955042]]
self_intersecting_case_second = [[-118.14789577571362,39.25717331572768],[-117.85904730960365,37.96942215223693],[-118.88417617952292,39.059549302006474],[-117.29267776821159,38.37460362441775]]

# completely inside case
completely_inside_case_first = [[-113.96516328673505,37.97388222420227],[-114.86248742561979,37.69454255373925],[-114.61359459877593,36.77153806493362],[-113.44772819934865,36.47716675906124],[-112.94339273442792,36.96018241617512],[-113.07438895908288,37.606383533581784],[-113.76866894975281,38.00485464243119]]
completely_inside_case_second = [[-114.4956979965866,37.63751043138527],[-114.35160214946644,37.080461177813085],[-113.38223008702141,37.22141486120871],[-113.72937008235637,37.715270640525134]]
class TestPolygonIntersectionWindNumber(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        
    def tearDown(self):
        t = time.time()-self.startTime
        print('%s: %.6f' % (self.id(),t))

    def test_polygon_intersection_wind_number_inside_case(self):
        time.sleep(1)
        test_res = polygon_intersection.process_weiler_atherton(inside_case_first_poly, inside_case_second_poly, 0 )
        expected = getExpected(Polygon(inside_case_first_poly), Polygon(inside_case_second_poly))
        self.assertTrue(isSame(test_res, expected))
         
    def test_polygon_intersection_wind_number_convex(self):
        time.sleep(1)
        test_res = polygon_intersection.process_weiler_atherton(convex_case_first_poly, convex_case_second_poly, 0 )
        expected = getExpected(Polygon(convex_case_first_poly), Polygon(convex_case_second_poly))
        self.assertTrue(isSame(test_res, expected))

        
    def test_polygon_intersection_wind_number_concave(self):
        time.sleep(1)
        test_res = polygon_intersection.process_weiler_atherton(concave_case_first_poly, concave_case_second_poly, 0 )
        expected = []

        for l in mapping(Polygon(concave_case_first_poly).intersection(Polygon(concave_case_second_poly)))['coordinates']:
            expected= expected + [list((round(x[0], 5),round(x[1], 5))) for x in l[0][:-1]]
        self.assertTrue(isSame(test_res, expected))
    
    def test_polygon_intersection_wind_number_self_intersecting(self):
        time.sleep(1)
        #test_res = polygon_intersection.process_weiler_atherton(no_intersection_first_poly, no_intersection_second_poly)
        self.assertRaises(TypeError, polygon_intersection.process_weiler_atherton(no_intersection_first_poly, no_intersection_second_poly, 0))
    
    def test_polygon_intersection_wind_number_completely_inside(self):
        time.sleep(1)
        test_res = polygon_intersection.process_weiler_atherton(completely_inside_case_first, completely_inside_case_first,0 )
        expected = getExpected(Polygon(completely_inside_case_first), Polygon(completely_inside_case_first))
        self.assertTrue(isSame(test_res, expected))
class TestPolygonIntersectionRayCasting(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        
    def tearDown(self):
        t = time.time()-self.startTime
        print('%s: %.6f' % (self.id(),t))

    def test_polygon_intersection_ray_casting_inside_case(self):
        time.sleep(1)
        test_res = polygon_intersection.process_weiler_atherton(inside_case_first_poly, inside_case_second_poly, 1 )
        expected = getExpected(Polygon(inside_case_first_poly), Polygon(inside_case_second_poly))
        self.assertTrue(isSame(test_res, expected))
         
    def test_polygon_intersection_ray_casting_convex(self):
        time.sleep(1)
        test_res = polygon_intersection.process_weiler_atherton(convex_case_first_poly, convex_case_second_poly, 1 )
        expected = getExpected(Polygon(convex_case_first_poly), Polygon(convex_case_second_poly))
        self.assertTrue(isSame(test_res, expected))

        
    def test_polygon_intersection_ray_casting_concave(self):
        time.sleep(1)
        test_res = polygon_intersection.process_weiler_atherton(concave_case_first_poly, concave_case_second_poly, 1 )
        expected = []

        for l in mapping(Polygon(concave_case_first_poly).intersection(Polygon(concave_case_second_poly)))['coordinates']:
            expected= expected + [list((round(x[0], 5),round(x[1], 5))) for x in l[0][:-1]]
        self.assertTrue(isSame(test_res, expected))
    
    def test_polygon_intersection_ray_casting_self_intersecting(self):
        time.sleep(1)
        #test_res = polygon_intersection.process_weiler_atherton(no_intersection_first_poly, no_intersection_second_poly)
        self.assertRaises(TypeError, polygon_intersection.process_weiler_atherton(no_intersection_first_poly, no_intersection_second_poly, 1))
    
    def test_polygon_intersection_ray_casting_completely_inside(self):
        time.sleep(1)
        test_res = polygon_intersection.process_weiler_atherton(completely_inside_case_first, completely_inside_case_first, 1 )
        expected = getExpected(Polygon(completely_inside_case_first), Polygon(completely_inside_case_first))
        self.assertTrue(isSame(test_res, expected))

def isSame(actual, expected)-> bool:
        actual = [[round(x[0], 5), round(x[1], 5)]for x in actual]
        diff =0
        diff1 = [x for x in actual if x not in expected]
        diff2 = [x for x in expected if x not in actual]
        diff+=(len(diff1)+len(diff2))
        return diff==0
    
def getExpected(p1, p2)->list:
    p1= Polygon(p1)
    p2 = Polygon(p2)
    res = [list((round(x[0], 5),round(x[1], 5)))for x in list(mapping(p1.intersection(p2))['coordinates'][0])[:-1]]
    return res

def floatEqual(f1, f2):
    prec = 1e-5
    if abs(f1 - f2) < prec:
        return True
    else:
        return False

unittest.main()
#expected = [list((round(x[0], 5),round(x[1], 5)))for x in list(mapping(Polygon(concave_case_first_poly).intersection(Polygon(concave_case_second_poly)))[0])[:-1]]
# expected = []
# for l in mapping(Polygon(concave_case_first_poly).intersection(Polygon(concave_case_second_poly))['coordinates']):
#     expected = expected+l[:-1]     
# print(expected)
# expected = []
# for l in mapping(Polygon(concave_case_first_poly).intersection(Polygon(concave_case_second_poly)))['coordinates']:
#     expected= expected + [list((round(x[0], 5),round(x[1], 5))) for x in l[0][:-1]]
# print(len(expected))

    

