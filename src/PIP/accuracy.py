from shapely.geometry import Polygon, Point, LineString
def get_accuracy(points, polygons, y_actual):
    diff = 0
    y_desired = compute_desired(points, polygons)
    for p in y_actual:
        temp1 =y_actual[p]
        temp2 = y_desired[p]
        diff1 = [x for x in temp1 if x not in temp2]
        diff2 = [x for x in temp2 if x not in temp1]
        diff+=(len(diff1)+len(diff2))
    return diff

def compute_desired(points, polygons):
    y = {}
    for point in points:
        curPointInPolys = []
        for poly in polygons:
            line = LineString(poly)
            p = Point(point[0], point[1])
            polygon = Polygon(line)
            if polygon.contains(p):
                curPointInPolys.append(poly)
        y[point]=curPointInPolys
    return y
