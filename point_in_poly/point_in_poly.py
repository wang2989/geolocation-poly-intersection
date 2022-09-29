import algorithms.ray_casting as rc
import algorithms.wind_number as wn

class PointInPoly:
    def __init__(self, points:tuple, v: list) -> None:
        self.points = points
        self.v = v
        
    def rayCasting(self) -> list:
        return rc(self.points, self.v)
    
    def windNumber(self) -> list:
        return wn(self.points, self.v )
