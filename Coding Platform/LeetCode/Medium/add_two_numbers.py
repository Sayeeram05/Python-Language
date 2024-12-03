# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 =r = 0
        Head = Next = None
        while (l1 != None or l2 != None) or (r!=0) :
            try:
                n1 = l1.val
                l1 = l1.next
            except:
                n1 = 0
            try :
                n2 = l2.val
                l2 = l2.next
            except:
                n2 = 0
            v = n1+n2+r
            if(v <= 9):
                NewNode = ListNode(v)
                if(Next == None):
                    Next = NewNode
                    Head = NewNode
                else:
                    Next.next = NewNode
                    Next = NewNode
                r = 0
            else:
                i = v % 10
                NewNode = ListNode(i)
                if(Next == None):
                    Next = NewNode
                    Head = NewNode
                else:
                    Next.next = NewNode
                    Next = NewNode
                r = v // 10
        return Head