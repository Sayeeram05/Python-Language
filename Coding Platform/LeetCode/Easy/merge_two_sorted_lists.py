# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def Function(self,list1,list2):
        Head = list1
        Tamil = None
        while(list1 != None):
            Check = False
            # print("1 : ",list1.val)
            Temp = list1
            while(list2 != None):
                if(list1.val > list2.val):
                    break
                if(Temp != None and Temp.val < list2.val):
                    list1 = Temp
                    Temp = Temp.next
                    continue
                else:
                    Check = True
                    # print("2 : ",list2.val)
                    break
            if(Check):
                Temp = list2.next
                list2.next = list1.next
                list1.next = list2
                list2 = Temp
                # print(list1,"\n",list2)
                list1 = list1.next
            elif(list2 != None):
                list1 = Head
                continue
            Tail = list1
            list1 = list1.next
        print(list1,list2)
        if(list2 != None):
            Tail.next = list2

        return Head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 != None and list2 != None):
            if(list2.val < list1.val):
                list1,list2 = list2,list1
            return(self.Function(list1,list2))
        elif(list2 != None):
            return(self.Function(list2,list1))
        elif(list1 != None):
            return(self.Function(list1,list2))