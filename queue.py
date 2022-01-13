class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items)>0:
            a=self.items[0]
            self.items.remove(a)
            return a
        else:
            return "empty queue"


    def size(self):
        return len(self.items)


if __name__=='__main__':

#we will check if it works, here
    # q=Queue()
    # q.enqueue(2)
    # q.enqueue(3)
    # q.enqueue(5)
    # q.enqueue(2.3)
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.isEmpty())
    # print(q.size())
    # q.enqueue(22)
    # print(q.isEmpty())
    # print(q.size())



        


