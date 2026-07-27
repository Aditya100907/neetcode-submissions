class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets, slowest = 0, 0
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        for p, s in pair:
            time = (target - p) / s
            if time > slowest:
                slowest = time
                fleets+=1
        return fleets
