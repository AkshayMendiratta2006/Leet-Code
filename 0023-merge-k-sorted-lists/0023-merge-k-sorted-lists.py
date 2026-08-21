# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        heap = []
        for index, linked_list in enumerate(lists):
            if linked_list:
                heapq.heappush(heap, (linked_list.val, index, linked_list))
        while heap:
            val, index, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
        return dummy.next