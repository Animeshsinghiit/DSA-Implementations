class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linkedlist():
    def __init__(self):
        self.head=None #this will create an empty linkedlist, an after that we will insert node into it.
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    #method to print complete linked list
    def print(self):
        itr=self.head
        llstr=''
        while(itr):
            suffix=''
            if itr.next:
                suffix='-->'
            llstr+=str(itr.data) +suffix
            itr=itr.next
        print(llstr)
    def length(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data)
    def insert_at(self,index,data):
        if index<0 or index>self.length():
            raise Exception('Invalid Index')
        if index==0:
            self.insert_at_begining(data)
            return
        itr=self.head
        count=0
        while itr.next:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    def remove_at(self,index):
        if index<0 or index>self.length():
            raise Exception('Invalid Index')
        if index==0:
            self.head=self.head.next
            return
        itr=self.head
        count=0
        while itr.next:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    def insert_bulk(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)


    

if __name__=='__main__':
    root=Linkedlist()
    # root.insert_at_begining(5)
    # root.insert_at_begining(12)
    # root.insert_at_begining(13)
    # root.insert_at_end(28)
    # root.insert_at(2,24)
    # root.insert_bulk(["animesh","singh"])
    # root.insert_at_end(24)
    # root.insert_at_begining(21)
    # root.insert_at(1,"ani")
    # root.remove_at(2)
    # root.insert_at(-1,23)
    # root.remove_at(3)
    # root.print()
    # print(root.length())


    