class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(list(zip(position, speed)), reverse=True)
        for position, speed in cars:
            time = (target-position) / speed
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)