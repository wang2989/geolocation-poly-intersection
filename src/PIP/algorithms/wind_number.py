import pandas as pd

def pip(points: list, polys: list) -> list:
    res ={}
    for point in points: 
        curPointInPolys = []
        for v in polys:
            if (windNumber(point, v)!= 0):
                curPointInPolys.append(v)
        res[point] = curPointInPolys
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
                    #print(f'current wn:{wn}')
        else:
            if (v[i+1][1] <= p[1]):
                if (isLeft(v[i], v[i+1], p)) <0:
                    wn-=1
                    #print(f'current wn:{wn}')
  
    return wn
def isLeft(p0, p1, p2) -> int:
    return ((p1[0]-p0[0])*(p2[1]-p0[1])-(p2[0]-p0[0])*(p1[1]-p0[1]))

def findOverlappingPoints(points, polys):
    res = []
    for p in points:
        for v in polys:
            if windNumber(p, v)!= 0:
                res.append(p)
    points = pd.DataFrame([[x[1], x[0]] for x in res], columns=['Latitude','Longitude'])
    points.to_csv('PIP_columbus_area.csv',index = False)
    