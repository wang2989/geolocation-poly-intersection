import sys
sys.path.insert(0, '../geolocation-poly-intersection/src')
from Polygon_Intersection import vertex_in_polygon_intersection as vipi

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

# test cases
print(vipi.vertex_in_polygon(inside_case_first_poly, inside_case_second_poly))
print(vipi.vertex_in_polygon(convex_case_first_poly, convex_case_second_poly))
print(vipi.vertex_in_polygon(no_intersection_first_poly, no_intersection_second_poly))
print(vipi.vertex_in_polygon(concave_case_first_poly, concave_case_second_poly))