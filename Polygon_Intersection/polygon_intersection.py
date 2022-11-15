from algorithms.polygon_orientation import orientation
import sys
sys.path.insert(0, '../geolocation-poly-intersection')
from PIP.algorithms import wind_number
from ground.base import get_context
from bentley_ottmann.planar import contour_self_intersects
context = get_context()
Point, Segment = context.point_cls, context.segment_cls
# preconditions for Weiler-Atherton algorithm
# 1. Candidate polygons need to be oriented clockwise
# 2. Candidate polygons should not be self-intersecting (i.e., re-entrant).

class baseVertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vertex(baseVertex):
    def __init__(self, x, y, next = None):
        super(Vertex, self).__init__(x, y)
        self.next = next

class Intersection(baseVertex):
    def __init__(self, x, y, nextS = None, nextC = None, crossDi = -1):
        super(Intersection, self).__init__(x, y)
        self.nextS = nextS
        self.nextC = nextC
        self.crossDi = crossDi # -1: undefined, 0: in 1:out
        self.used = False
        
def is_vertex_in_polygon_wind(points, polygon):
    res = []
    for p in points:
       if wind_number.windNumber((p[0], p[1]), polygon)!=0:
           res.append(p)   
    return res
def to_kepler_format(polys):
    res = []
    for poly in polys:
        temp = []
        for vertex in poly:
            temp.append([vertex.x, vertex.y])
        res.append(temp)
    return res
       
def floatEqual(f1, f2):
    prec = 1e-5
    if abs(f1 - f2) < prec:
        return True
    else:
        return False
def floatLarger(f1, f2):
    if floatEqual(f1, f2):
        return False
    elif f1 > f2:
        return True
    else:
        return False 

#using ray casting 
def isVertexInPolygon(v, list):
    judgeIndex = 0
    for i in range(len(list)):
        j = i + 1
        minY = min(list[i % len(list)].y, list[j % len(list)].y)
        maxY = max(list[i % len(list)].y, list[j % len(list)].y)
        if floatLarger(v.y, maxY) or floatLarger(minY, v.y):
            continue
        if floatEqual(maxY, minY):    # on the same horizontal line
            if floatLarger(v.x, max(list[i % len(list)].x, list[j % len(list)].x)): # point is on the right
                judgeIndex += 1
                continue
            elif floatLarger(min(list[i % len(list)].x, list[j % len(list)].x), v.x): # point is on the left, no intersection
                continue
            else:   # point is on the line segment
                return True
        # make rays
        x = (list[i % len(list)].x - list[j % len(list)].x) / (list[i % len(list)].y - list[j % len(list)].y) * (v.y - list[i % len(list)].y) + list[i % len(list)].x
        if(floatEqual(v.x, x)): # point is on the line
            return None
        if floatLarger(v.x, x): # have intersection
            judgeIndex += 1
    if judgeIndex % 2 != 0:
        return True
    return False
# get horizontal / vertical intersection 
def LineCrossH(y, c1, c2):
    return c1.x + (c2.x - c1.x) * (y - c1.y) / (c2.y - c1.y)

def LineCrossV(x, c1, c2):
    return c1.y + (c2.y - c1.y) * (x - c1.x) / (c2.x - c1.x)

#cut by vertical lines, return the intersection point
def CutByVerticalLine(s1, s2, list):
    assert floatEqual(s1.x, s2.x)
    crossXs = []
    x = s1.x

    shearedList = [Vertex(r.x, r.y) for r in list]

    minY = min(s1.y, s2.y)
    maxY = max(s1.y, s2.y)

    for i in range(len(list)):
        vertex = list[i]
        c1 = shearedList[i % len(list)]
        c2 = shearedList[(i + 1) % len(list)]

        if(floatEqual(c1.x, c2.x) and floatEqual(c1.x, x)):
            continue    # coincide
        if(floatLarger(c1.x, x) and floatLarger(c2.x, x)):
            continue    # not intersect
        if(floatLarger(x, c1.x) and floatLarger(x, c2.x)):
            continue

        y = float('%.9f' % LineCrossV(x, c1, c2))

        intersections = Intersection(x, y)

        next = None
        if((floatLarger(y, minY) and floatLarger(maxY, y))                  # point of intersection is between s1 s2
        # or (c2.y == y and x == s2.x)                # point of intersection is at the end of line segments（ignore when at start）
        # or (c1.y == y and x == s1.x)
            or (floatEqual(c2.x, x) and floatEqual(y, s1.y))                # When the intersection point is at the end point, the beginning of a line segment and the end of another line segment can have an intersection point. The above annotated method will fail in some cases
            or (floatEqual(c1.x, x) and floatEqual(y, s2.y))
            or (floatEqual(y, minY) and (not floatEqual(c1.x, x)) and (not floatEqual(c2.x, x)))  # point of intersection is at one end of line segment
            or (floatEqual(y, maxY) and (not floatEqual(c1.x, x)) and (not floatEqual(c2.x, x)))):
            while not ((isinstance(vertex, Vertex) and isinstance(vertex.next, Vertex)) or (isinstance(vertex, Intersection) and isinstance(vertex.nextS, Vertex))):
                if isinstance(vertex, Vertex):
                    assert isinstance(vertex.next, Intersection)
                    if (floatLarger(c2.x, c1.x) and floatLarger(vertex.next.x, intersections.x)) or (floatLarger(c1.x, c2.x) and floatLarger(intersections.x, vertex.next.x)):    # c1c2的横坐标不可能相同，否则和s1s2重合
                        break
                    vertex = vertex.next
                else:
                    assert isinstance(vertex.nextS, Intersection)
                    if (floatLarger(c2.x, c1.x) and floatLarger(vertex.nextS.x, intersections.x)) or (floatLarger(c1.x, c2.x) and floatLarger(intersections.x, vertex.nextS.x)):
                        break
                    vertex = vertex.nextS
            if isinstance(vertex, Vertex):
                next = vertex.next
            else:
                next = vertex.nextS
            if isinstance(vertex, Vertex):
                vertex.next = intersections
            else:
                assert isinstance(vertex, Intersection)
                vertex.nextS = intersections
            intersections.nextS = next

            # record whether the intersection point is in or out，polygons are CW by default

            if floatEqual(c1.x, x):
                assert not floatEqual(c2.x, x)
                if floatLarger(c2.x, x):
                    intersections.crossDi = 0
                else:
                    intersections.crossDi = 1
            elif floatLarger(c1.x, x):
                intersections.crossDi = 1
            else:
                intersections.crossDi = 0
            if floatLarger(s2.y, s1.y):
                intersections.crossDi = 0 if intersections.crossDi == 1 else 1

            # print("s1:%s, s2:%s, c1:%s, c2:%s, inter:%s, crossDi:%s" % (("%f, %f" % (s1.x, s1.y)), ("%f, %f" % (s2.x, s2.y)), ("%f, %f" % (c1.x, c1.y)), ("%f, %f" % (c2.x, c2.y)), ("%f, %f" % (intersections.x, intersections.y)), ("%s" % ("in" if intersections.crossDi == 0 else "out"))))
            crossXs.append(intersections)
    return crossXs
def CutByLine(s1, s2, list):
    # print("s1 = %s, s2 = %s" % (("%f, %f" % (s1.x, s1.y)), ("%f, %f" % (s2.x, s2.y))))

    if floatEqual(s1.x, s2.x):
        return CutByVerticalLine(s1, s2, list)
    crossXs = []

    # shear mapping transformation
    slope = (s2.y - s1.y) / (s1.x - s2.x)
    y = s1.x * slope + s1.y
    shearedList = [Vertex(r.x, r.x * slope + r.y) for r in list]

    minX = min(s1.x, s2.x)
    maxX = max(s1.x, s2.x)

    for i in range(len(list)):
        vertex = list[i]
        c1 = shearedList[i % len(list)]
        c2 = shearedList[(i + 1) % len(list)]
        # print("c1 = %s, c2 = %s" % (("%f, %f" % (c1.x, c1.y - c1.x * slope)), ("%f, %f" % (c2.x, c2.y - c2.x * slope))))

        if(floatEqual(c1.y, c2.y) and floatEqual(c1.y, y)):
            continue   
        if(floatLarger(c1.y, y) and floatLarger(c2.y, y)):
            continue   
        if(floatLarger(y, c1.y) and floatLarger(y, c2.y)):
            continue

        x = float('%.9f' % LineCrossH(y, c1, c2))
        npy = y - x * slope
        intersections = Intersection(x, npy)

        next = None
        if((floatLarger(x, minX) and floatLarger(maxX, x))                 
        or (floatEqual(c2.y, y) and floatEqual(x, s1.x))              
        or (floatEqual(c1.y, y) and floatEqual(x, s2.x))
        or (floatEqual(x, minX) and (not floatEqual(c1.y, y)) and (not floatEqual(c2.y, y)))  
        or (floatEqual(x, maxX) and (not floatEqual(c1.y, y)) and (not floatEqual(c2.y, y)))):
            # find the insert point
            while not ((isinstance(vertex, Vertex) and isinstance(vertex.next, Vertex)) or (isinstance(vertex, Intersection) and isinstance(vertex.nextS, Vertex))):    # 如果下一个点是交点
                if isinstance(vertex, Vertex):
                    assert isinstance(vertex.next, Intersection)
                    # insert the point to the linked list
                    if (floatLarger(c2.x, c1.x) and floatLarger(vertex.next.x, intersections.x)) \
                            or (floatLarger(c1.x, c2.x) and floatLarger(intersections.x, vertex.next.x))\
                            or (floatLarger(c1.y - c1.x * slope, c2.y - c2.x * slope) and floatLarger(intersections.y, vertex.next.y))\
                            or (floatLarger(c2.y - c2.x * slope, c1.y - c1.x * slope)  and floatLarger(vertex.next.y, intersections.y)): 
                        break
                    vertex = vertex.next
                else:
                    assert isinstance(vertex.nextS, Intersection)
                    if (floatLarger(c2.x, c1.x) and floatLarger(vertex.nextS.x, intersections.x))\
                            or (floatLarger(c1.x, c2.x) and floatLarger(intersections.x, vertex.nextS.x))\
                            or (floatLarger(c2.y - c2.x * slope, c1.y - c1.x * slope) and floatLarger(intersections.y, vertex.nextS.y))\
                            or (floatLarger(c2.y - c2.x * slope, c1.y - c1.x * slope) and floatLarger(vertex.nextS.y, intersections.y)):
                        break
                    vertex = vertex.nextS
            if isinstance(vertex, Vertex):
                next = vertex.next
            else:
                next = vertex.nextS
            if isinstance(vertex, Vertex):
                vertex.next = intersections
            else:
                assert isinstance(vertex, Intersection)
                vertex.nextS = intersections
            intersections.nextS = next

            if floatEqual(c1.y, y):
                assert not floatEqual(c2.y, y)
                if floatLarger(y, c2.y):
                    intersections.crossDi = 0
                else:
                    intersections.crossDi = 1
            elif floatLarger(y, c1.y):
                intersections.crossDi = 1
            else:
                intersections.crossDi = 0

            if floatLarger(s2.x, s1.x): 
                intersections.crossDi = 0 if intersections.crossDi == 1 else 1

            # print("s1:%s, s2:%s, c1:%s, c2:%s, inter:%s, crossDi:%s" % (("%f, %f" % (s1.x, s1.y)), ("%f, %f" % (s2.x, s2.y)), ("%f, %f" % (c1.x, c1.y - c1.x * slope)), ("%f, %f" % (c2.x, c2.y - c2.x * slope)), ("%f, %f" % (intersections.x, intersections.y)), ("%s" % ("in" if intersections.crossDi == 0 else "out"))))
            crossXs.append(intersections)

    return crossXs

def Compose(list):
    res = []
    for intersections in list:
        res.append([intersections.x, intersections.y])
    return res
def deduplicate(list):
    res = []
    for point in list:
        if [float(point[0]), float(point[1])] in res:
            continue
        res.append([float(point[0]), float(point[1])])
    return res

def getX(v):
    return v.x

def getY(v):
    return v.y

def processNoCross(listS, listC):
    sInC = isVertexInPolygon(listS[0], listC)
    if sInC:
        return listS
    cInS = isVertexInPolygon(listC[0], listS)
    if cInS:
        return listC
    return []
def toVertexList(polygon) -> list:
    res = []
    for  vertex in polygon:
        res.append(Vertex(vertex[0], vertex[1]))
    return res
def to_kepler_format(polys):
    res = []
    for poly in polys:
        temp = []
        for vertex in poly:
            temp.append([vertex.x, vertex.y])
        res.append(temp)
    return res
 
def decode(lists):
    results = []
    for list in lists:
        result = ""
        for v in list:
            result += "%f %f " % (v.x, v.y)
        result = result.strip()
        results.append(result)
    return results

def transDirect(list):  # change the orientation
    newList = []
    for i in range(len(list)):
        newList.append(list[len(list) - 1 - i])
    return newList

def toClockwise(list):  # to cw
    crossPr = []
    maxX = -1
    mark_i = -1

    for i in range(len(list)):
        if list[i].x > maxX:
            maxX = list[i].x
            mark_i = i
    v1 = Vertex(list[mark_i].x - list[mark_i - 1].x, list[mark_i].y - list[mark_i - 1].y)
    v2 = Vertex(list[(mark_i + 1) % len(list)].x - list[mark_i].x, list[(mark_i + 1) % len(list)].y - list[mark_i].y)
    crossPr = v1.x * v2.y - v2.x * v1.y
    while floatEqual(crossPr, 0):
        mark_i += 1
        v2 = Vertex(list[(mark_i + 1) % len(list)].x - list[mark_i % len(list)].x,
                    list[(mark_i + 1) % len(list)].y - list[mark_i % len(list)].y)
        crossPr = v1.x * v2.y - v2.x * v1.y
    assert not floatEqual(crossPr, 0)
    if crossPr < 0:
        return transDirect(list)
    else:
        return list

def process_weiler_atherton(s, c):
    Contour = context.contour_cls
    if (contour_self_intersects(Contour([ Point(x[0], x[1]) for x in s])) or
       contour_self_intersects(Contour([ Point(x[0], x[1]) for x in c]))):
        raise TypeError("Self-intersecting polygons are not allowed in weiler_atherton algorithm ")
    # make the orientation of the polygons
    if orientation(s) == -1:
        list.reverse(s)
    if orientation(c) == -1:
        list.reverse(c)
    # store all the intersection points
    listS = toVertexList(s)
    listC = toVertexList(c)
    # listS = toClockwise(listS)
    # listC = toClockwise(listC)
    listI = []  

    #connect the linkedList
    for i in range(len(listS)):
        listS[i-1].next = listS[i]
    for i in range(len(listC)):
        listC[i-1].next = listC[i]   

    for cutIndex in range(len(listC)):
        s1 = listC[cutIndex]
        s2 = listC[(cutIndex+ 1) %len(listC)]
        intersections = CutByLine(s1, s2, listS)
        if(len(intersections) ==0):
            continue
        if floatEqual(s1.x, s2.x):
            assert not floatEqual(s1.y, s2.y)
            if floatLarger(s2.y, s1.y):
                intersections.sort(key=getY)
            else:
                intersections.sort(key=getY, reverse=True)
        elif floatLarger(s2.x, s1.x):
            intersections.sort(key=getX)
        else:
            intersections.sort(key=getX, reverse=True)

        # append intersections into listI
        for v in intersections:
            listI.append(v)

        # insert into C
        s1.next = intersections[0]
        for i in range(len(intersections) - 1):
            intersections[i].nextC = intersections[i + 1]
        intersections[len(intersections) - 1].nextC = s2

    pipOne = is_vertex_in_polygon_wind(s, c)
    pipTwo = is_vertex_in_polygon_wind(c, s)
    res = Compose(listI)
    if(len(pipOne)!=0):
        res = res + pipOne
    if(len(pipTwo)!=0):
        res = res +  pipTwo
    return  deduplicate(res)
# test cases:

#inner case
#p1 = [[0,0], [0, 2], [4,2], [4, 0]]
#p2 = [[0,0], [0, 2], [2,2], [2, 0]]
#
#p1 = [[161, 137], [429, 376], [558, 192], [619, 418], [281, 431]]
#p2 = [[183, 391], [224,240], [610, 107], [657, 361],[429, 376]]
#normal case
#p1 =[[-121.33657701203961,39.4644608274132],[-118.41696410320476,39.808810675932236],[-118.28545000821218,38.14242026589671],[-121.33657701203961,38.11138378652503]]
#p2 = [[-119.32264241961325,37.64915634673547],[-119.08782961664949,38.78121751212849],[-116.92114784384725,39.146370415097934],[-116.92114784384725,37.90224616382728]]
# no intersection case
# p1 = [[0,0], [0, 2], [4,2], [4, 0]]
# p2 = [[0,10], [0, 20], [10,2], [2, 10]]
# concave case:
# p1=[[-121.3078779355798,39.501403604067164],[-120.52872636210914,37.19991728187789],[-118.87436343213689,37.60689051788002]]
# p2 = [[-121.54269073854354,39.36125706946052],[-121.26518469867732,37.44606129152354],[-119.98438759160202,37.361275129880035],[-121.07306513261604,37.75893497289224],[-120.30458686837093,37.817979172820664],[-121.158451606421,37.910667563329284],[-119.97371428237646,38.25511425646991],[-121.10508506029296,38.17125252642114],[-120.00573421005336,39.08011900767557],[-121.04104520493911,38.41418515977385],[-120.96633204035972,39.63304859796313],[-121.29720462635424,38.54786858899416]]
# self-intersecting case:
# p1 = [[-118.32347033354482,37.915823646315715],[-118.62364619048267,39.6987057115261],[-117.81940144170606,39.14305825955042]]
# p2 = [[-118.14789577571362,39.25717331572768],[-117.85904730960365,37.96942215223693],[-118.88417617952292,39.059549302006474],[-117.29267776821159,38.37460362441775]]
# res = process_weiler_atherton(p1, p2)
# print(len(res))
# for r in res:
#      print(r)
