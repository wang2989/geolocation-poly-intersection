
def orientation(polygon) -> int:
    """_Determin the orientation of the polygon

    Args:
        polygon (list ): _vetices of a polygon_

    Returns:
        int: _-1 if CCW, 1 if CW_
    """
    i =0
    res = 0
    while(i < len(polygon)):
        if i == len(polygon)-1:
            next = polygon[0]
        else:
            next = polygon[i+1]
        # (x2 − x1)(y2 + y1)
        res = res +  (next[0]- polygon[i][0])*(next[1]+ polygon[i][1])
        i+=1
    return -1 if res<0 else 1