MAX = 1000
def pip(points: list, polys: list) -> list:
    res ={}
    for point in points: 
        curPointInPolys = []
        for v in polys:
            if (is_inside_polygon(point, v)):
                curPointInPolys.append(v)
        res[point] = curPointInPolys
    return res

def is_inside_polygon(p: tuple, v: list) -> bool:
    """_determin if a point is in the given polygon_

    Args:
        p (tuple): _x, y coordinated of the point_
        v (list): _vetices of the polygon_

    Returns:
        bool: _true if in or on the edge of polygon, false otherwise_
    """
    extreme = [MAX, p[1]]
    n = len(v)
    count = i =0
    decrease =0
    
    while True:
        next = (i+1) %n
        if(v[i][1] == p[1]):
            decrease+=1
        if intersect( v[i], v[next], p, extreme):
            if( direction(v[i], p, v[next])==0):
                return onSegment(v[i], p, v[next] )
            count+=1
        i = next
        if( i==0 ):
            break
    count-=decrease
    return (count%2==1)

def intersect(p1: tuple, p2: tuple, q1: tuple, q2: tuple)-> bool:
    """_check the relative position of two line segments_

    Args:
        p1 (tuple): _first end of line segement 1_
        p2 (tuple): _second end of line segement 1_
        q1 (tuple): _first end of line segement 2_
        q2 (tuple): _second end of line segement 1_

    Returns:
        bool: _if two segements intersect, return true, otherwise return false_
    """
    d1 = direction(p1,p2, q1)
    d2 = direction(p1, p2, q2)
    d3 = direction(q1, q2, p1)
    d4 = direction(q1, q2, p2)
    
    if( d1 != d2) and (d3 != d4):
        return True
    if(d1 == 0) and (onSegment(p1, q1, p2)):
        return True
    if(d2 == 0) and (onSegment(p1, q2, p2)):
        return True
    if(d3 == 0) and (onSegment(q1, p1, q2)):
        return True
    if(d4 == 0) and (onSegment(q1, p2, q2)):
        return True
    
    return False
    
def direction(p1: tuple, p2:tuple, p3:tuple)-> int:
    """_get the direction of a point related to a line segment_

    Args:
        p1 (tuple): _first end of line segement _
        p2 (tuple): _the point_
        p3 (tuple): _second end of line segement_

    Returns:
        int: _if val =0, they are collinear, if val =1, the orientation is CW, 2 if the orientation is CCW_
    """
    val =((p2[1]-p1[1])*(p3[0]-p2[0])-(p2[0]-p1[0])*(p3[1]-p2[1]))
    if val == 0:
        return 0
    if val >0:
        return 1
    return 2

def onSegment(p1: tuple, p2:tuple, p3:tuple)-> bool:
    if( (p2[0] >= min( p1[0], p3[0])) & (p2[0]<= max(p1[0], p3[0]))
       & (p2[1] >= min( p1[1], p3[1])) & (p2[1]<= max(p1[1], p3[1]))):
        return True
    return False

{"type":"Polygon","coordinates":[[[-120.736409337, 39.41874317513134], [-119.2886665020654, 40.111223658386244], [-119.93308556752898, 39.291643527666345], [-118.56533897960645, 37.3834614326313], [-120.39338490000303, 37.58174796964045], [-120.74429421, 38.3673494729134], [-122.39239914388999, 37.758715805127366], [-122.86584988586324, 39.36285540394297], [-122.85269847636407, 40.292029037228566], [-121.02465255596745, 40.40228374716855]]]}