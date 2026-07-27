class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets, slowest = 0, 0
        for p, s in sorted(zip(position, speed), reverse = True):
            t = (target - p) / s
            if t > slowest:
                slowest = t
                fleets+=1
        return fleets
        
