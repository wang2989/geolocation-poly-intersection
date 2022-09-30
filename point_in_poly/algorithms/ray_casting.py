MAX = 1000
def pip(points: list, v: list) -> list:
    res =[]
    for point in points: 
        if (is_inside_polygon(point, v)):
            res.append(point)
    return res
# p1 = (-122.0045, 40.0335)
# p2 = (-122.0625, 39.60383)
# p3 = (-122.992, 38.90133)
# v=[[-123.15532480599389,39.628538026418425],[-119.0541702886981,39.40845421648897],[-122.53717977729988,37.92347617009539],[-123.6189335775142,39.160027074679334],[-123.15532480599389,39.628538026418425]]
#v = [[-123.26039217084163,39.53042492619664],[-118.31546219912128,39.540567692544926],[-123.01051539035592,38.147591729521345],[-117.9998283711392,36.906482297387285],[-121.01150114646877,40.086073672949816],[-121.95840263041526,37.21083867441126],[-118.30231078962211,38.3438355532667],[-120.66956449948808,38.85773081562929],[-123.26039217084163,39.53042492619664]]
def is_inside_polygon(p: tuple, v: list) -> bool:
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

# print(is_inside_polygon(p1, v))
# print(is_inside_polygon(p2, v))
# print(is_inside_polygon(p3, v))
