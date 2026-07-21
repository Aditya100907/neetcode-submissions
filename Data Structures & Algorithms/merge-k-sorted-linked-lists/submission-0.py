# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: list[lists]) -> list:
        dummy = ListNode(0)
        current = dummy

        heap = []

        counter = 0

        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, counter, head))
                counter+=1
        
        while heap:
            val,_, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next)
                )
                counter+=1
            
        return dummy.next