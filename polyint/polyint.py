import polyintinput as p

# only checks true/false if there is intersection - if there is one, does not get the intersection
def vertex_in_polygon(p1,p2):
    for x in p1.vertices:
        if point_in_poly(p2,x):
            return True
    return False
def point_in_poly(polygon,x): #use point-in-polygon method
    pass

# requires polygon to be convex
def vector_intersect(p1,p2):
    # starting edge for polygons
    e1 = p1.edges[0]
    e2 = p2.edges[0]
    
    # check intersections
    t1 = t2 = 0
    v1 = e1
    v2 = e2

    if edges_intersect(v1, v2): return True
    t1, t2 = advance_vector(v1, t1, v2, t2)
    v1 = p1.edges[t1]
    v2 = p2.edges[t2]

    while (e1!=v1 or e2!=v2):
        if edges_intersect(v1, v2): return True
        t1, t2 = advance_vector(v1, t1, v2, t2)
        t1 %= len(p1.edges) # avoid index out of bounds error after vector loops back to start
        t2 %= len(p1.edges) # avoid index out of bounds error after vector loops back to start
        v1 = p1.edges[t1]
        v2 = p2.edges[t2]
    
    return False
def edges_intersect(polygon,x): #use point-in-polygon method
    pass
def advance_vector(e1, t1, e2, t2):
    if(True):pass #if v1 and v2 point to each other
        # move the outer vector to the next
        # vertex on its polygon
    elif(True): t2 += 1 #if v2 points to v1
    elif(True): t1 += 1 #if v1 points to v2
    else: pass
        #move the outer vector to the
        #next vertex on its polygon
    return t1, t2


p1 = p.polygon([[0,0],[1,0],[1,1]])
p2 = p.polygon([[2,2],[9,2],[5,6]])
vertex_in_polygon(p1,p2)
vector_intersect(p1,p2)