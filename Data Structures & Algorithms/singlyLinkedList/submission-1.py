class ListNode:
    def __init__(self, value):
        self.nxt = None
        self.val = value

class LinkedList:
    
    def __init__(self):
        self.ll = []
        self.num_nodes = 0
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if self.num_nodes > index:
            curr = self.head
            for _ in range(index):
                curr = curr.nxt
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        t = ListNode(val)
        t.nxt = self.head
        self.head = t
        if self.tail is None:
            self.tail = t
        self.num_nodes += 1

    def insertTail(self, val: int) -> None:
        h = ListNode(val)
        if self.tail is None:
            self.tail = h
            self.head = h
        else:
            prev = self.tail
            prev.nxt = h
            self.tail = h
        self.num_nodes += 1


    def remove(self, index: int) -> bool:
        if self.num_nodes > index:

            self.num_nodes -= 1
            curr = self.head

            if index == 0:
                self.head = self.head.nxt
                if self.head is None:
                    self.tail = None
                return True

            for _ in range(index):
                prev = curr
                curr = curr.nxt
            
            prev.nxt = curr.nxt
            if curr is self.tail:
                self.tail = prev

            return True

        return False

    def getValues(self) -> List[int]:
        curr = self.head
        if curr is None:
            return []
        a = [curr.val]
        while curr.nxt is not None:
            curr = curr.nxt
            a.append(curr.val)
        
        return a

