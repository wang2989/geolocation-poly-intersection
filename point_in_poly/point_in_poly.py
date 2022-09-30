import algorithms.ray_casting as rc
import algorithms.wind_number as wn

class PointInPoly:
    def __init__(self, points: list, v: list) -> None:
        self.points = points
        self.v = v
        
    def rayCasting(self) -> list:
        
        return rc.pip(self.points, self.v)
    
    def windNumber(self) -> list:
        return wn.pip(self.points, self.v )
