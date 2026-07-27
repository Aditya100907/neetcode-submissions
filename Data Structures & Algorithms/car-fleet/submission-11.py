class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p, s in sorted(zip(position, speed), reverse = True):
            t = (target - p) / s
            if not stack or stack[-1] < t:
                stack.append(t)
        return len(stack)
        
