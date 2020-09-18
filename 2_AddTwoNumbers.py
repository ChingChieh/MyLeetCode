# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1 = l1
        h2 = l2
        result = ListNode()
        head = result
        carrier = 0
        while(h1 != None and h2 != None):
            val = h1.val + h2.val + carrier
            carrier = 0
            if val > 9:
                carrier = 1
                val = val - 10
            result.next = ListNode(val)
            result = result.next
            h1 = h1.next
            h2 = h2.next

        while(h1):
            val = h1.val + carrier
            carrier = 0
            if val > 9:
                carrier = 1
                val = val - 10
            result.next = ListNode(val)
            result = result.next
            h1 = h1.next

        while(h2):
            val = h2.val + carrier
            carrier = 0
            if val > 9:
                carrier = 1
                val = val - 10
            result.next = ListNode(val)
            result = result.next
            h2 = h2.next

        if carrier == 1:
            result.next = ListNode(1)

        return head.next

'''
Be aware the situation that [5] + [5] should output [0,1]
'''
