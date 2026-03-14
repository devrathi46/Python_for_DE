
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val 
        self.next=next

class solution:
    def mergetwolists(self,l1,l2):
        dummy=ListNode(-1)
        temp=dummy
        
        while(l1 and l2):
            if l1.val<=l2.val:
                temp.next=l1
                temp=temp.next
                l1=l1.next
            else:
                temp.next=l2
                temp=temp.next
                l2=l2.next
        if l1:
            temp.next=l1
        if l2:
            temp.next=l2    
        return dummy.next


class LinkedListUtils:
    def create_list(self,arr):
        dummy=ListNode(-1)
        temp=dummy 

        for num in arr:
            temp.next=ListNode(num)
            temp=temp.next

        return dummy.next    
    
    def print_list(self,head):
        temp=head
        while(temp):
            print(temp.val,end=" ->")
            temp=temp.next


class App:
    def run(self):
        util=LinkedListUtils()
        list1=util.create_list([1,2,3,4])
        list2=util.create_list([2,3,4])

        sol=solution()
        merged=sol.mergetwolists(list1,list2)

        util.print_list(merged)

if __name__ == "__main__":
    app = App()
    app.run()