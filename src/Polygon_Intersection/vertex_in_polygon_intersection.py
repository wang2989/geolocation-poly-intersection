from PIP.algorithms import ray_casting as rc

# the order of the polygons being p1 and p2 in the args is not important - same result regardless
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

    # switching p1 and p2 below would also work
    for vertex in p1:
        if rc.is_inside_polygon(vertex,p2):
            return True
    return False