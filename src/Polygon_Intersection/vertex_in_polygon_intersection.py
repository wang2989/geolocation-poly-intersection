from PIP.algorithms import ray_casting as rc

# the order of the polygons being p1 and p2 in the args is mostly not important
    # if one polygon is completely inside the other:
        # the larger, outer polygon must be p2
        # the smaller, inner polygon must be p1
    # otherwise, there is no issue
# polygons are considered as intersecting if:
    # the intersection is normal (intersecting polygon has nonzero area)
    # the intersection is on the edge of the polygons (intersection is a line segment or a point)
# NOTE: the inputted polygons MUST be coplanar to return an accurate result
def vertex_in_polygon(p1: list, p2: list) -> bool:
    """
    Args:
        p1 (list): vertices of polygon #1
        p2 (list): vertices of polygon #2
    Returns:
        bool: true if polygons intersect, false if not
    """

    # if p1 is not completely inside p2, then p1 and p2 in the code below can be switched
    for vertex in p1:
        if rc.is_inside_polygon(vertex,p2):
            return True
    return False