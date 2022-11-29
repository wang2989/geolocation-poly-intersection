import algorithms.ray_casting as rc
import algorithms.wind_number as wn

class PointInPoly:
    def __init__(self, points: list, polys: list) -> None:
        self.points = points
        self.polys = polys
        
    def rayCasting(self) -> list:
        
        return rc.pip(self.points, self.polys)
    
    def windNumber(self) -> list:
        return wn.pip(self.points, self.polys)
    
    def getOverlapping(self)->list:
        return wn.findOverlappingPoints(self.points, self.polys)


