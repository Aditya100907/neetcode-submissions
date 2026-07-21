class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = {}
        for num in nums:
            list[num] = list.get(num, 0) + 1
        for num, count in list.items():
            if count > 1:
                return True
        return False