# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        res = None
        ind = 0
        for i in range(0, len(lists)):
            if lists[i] is not None:
                ind = i
                res = lists[i]
                break
        if not res:
            return None
        
        
        for i in range(ind + 1, len(lists)):
            if not lists[i]:
                continue
            currHead = lists[i]
            currRes = res
            prevRes = None
            while currRes and currHead:
                currNext = currHead.next
                if currHead.val <= currRes.val:
                    if res == currRes:
                        res = currHead
                    currHead.next = currRes
                    if prevRes:
                        prevRes.next = currHead
                    currRes = currHead
                    currHead = currNext

                prevRes = currRes
                currRes = currRes.next
            if prevRes.next == None:
                prevRes.next = currHead
        return res