from rtree import index
from shapely.geometry import Polygon, Point


def get_containing_box(p):
    xcoords = [x for x, _ in p.exterior.coords]
    ycoords = [y for _, y in p.exterior.coords]
    box = (min(xcoords), min(ycoords), max(xcoords), max(ycoords))   
    return box

def build_rtree( polys):
    def generate_items():
        pindx = 0
        for pol in polys:
            box = get_containing_box(pol)
            yield (pindx, box,  pol)
            pindx += 1
    return index.Index(generate_items())
def insert_index(index, pindx, bounds):
    index.insert(pindx, bounds)
    
def get_intersection_func(rtree_index):
    MIN_SIZE = 0.0001
    def intersection_func(point):
        # Inflate the point, since the RTree expects boxes:
        pbox = (point[0]-MIN_SIZE, point[1]-MIN_SIZE, 
                point[0]+MIN_SIZE, point[1]+MIN_SIZE)
        hits = rtree_index.intersection(pbox, objects='raw')
        #Filter false positives:
        result = [pol for pol in hits if pol.intersects(Point(point)) ]
        return result
    return intersection_func
