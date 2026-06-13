class Solution:
        def checkStraightLine(self, coor: list[list[int]]) -> bool:
         
            (x0,y0),(x1,y1) = coor[0],coor[1]

            for x, y in coor:
                if (y1-y0)*(x-x0)-(y-y0)*(x1-x0): return False     # <-- cross product in plane

            return True