# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # If either are empty, return the other lsit
        if not list1 or not list2:
            return list1 or list2

        # compare values of the first nodes of both lists
        if list1.val < list2.val:
            # recursively merge the next node of list1 with list2
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1    # return current node as smaller node
        else:
            # recursively merge the next node of list2 with list1
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2    # return current node as smaller node
