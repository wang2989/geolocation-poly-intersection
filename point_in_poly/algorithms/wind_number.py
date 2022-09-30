# p1 = (-122.0045, 40.0335)
# p2 = (-122.0625, 39.60383)
# p3 = (-122.992, 38.90133)
# v=[[-123.15532480599389,39.628538026418425],[-119.0541702886981,39.40845421648897],[-122.53717977729988,37.92347617009539],[-123.6189335775142,39.160027074679334],[-123.15532480599389,39.628538026418425]]
def pip(points: list, v: list) -> list:
    res =[]
    for point in points: 
        if (windNumber(point, v)!= 0):
            res.append(point)
    return res
def windNumber(p: tuple, v: list) -> int:
    wn =0
    #V[] = vertex points of a polygon V[n+1] with V[n]=V[0]
    v = tuple(v[:])+(v[0],)
 
    for i in range(len(v)-1):
        if (v[i][1] <= p[1]): 
            if v[i+1][1] > p[1]:
                if (isLeft(v[i], v[i+1], p)>0):
                    wn+=1
                    print(f'current wn:{wn}')
        else:
            if (v[i+1][1] <= p[1]):
                if (isLeft(v[i], v[i+1], p)) <0:
                    wn-=1
                    print(f'current wn:{wn}')
  
    return wn
def isLeft(p0, p1, p2) -> int:
    return ((p1[0]-p0[0])*(p2[1]-p0[1])-(p2[0]-p0[0])*(p1[1]-p0[1]))

# print(windNumber(p1, v))
# print(windNumber(p2, v))
# print(windNumber(p3, v))