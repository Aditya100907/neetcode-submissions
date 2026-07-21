class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # will need bucket sort for the elements to keep it O(n) rather than nlogn
        # create a freq map of the nums
        #use bucket sort to put the numbers at different indices representing their frequency in an array
        #loop through the array from back forwards to get the k elements
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sort = [[] for _ in range (len(nums)+1)]
        for value in freq:
            sort[freq[value]].append(value)
        result = []
        for i in range(len(sort)-1, -1, -1):
            for j in sort[i]:
                if len(result) != k:
                    result.append(j)
        return result

        
