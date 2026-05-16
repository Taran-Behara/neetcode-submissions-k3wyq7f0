class LRUCache:
    class ListNode:
        def __init__(self, key, val, next, prev):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.keyMap = {}
        self.capacity = capacity
        self.LRU = None
        self.MRU = None

    def get(self, key: int) -> int:
        print("Getting", key)
        if key not in self.keyMap:
            return -1
        
        if self.keyMap[key] == self.MRU:
            return self.keyMap[key].val
        
        if self.keyMap[key] == self.LRU:
            print(self.LRU.key)
            print(self.LRU.next.key)
            self.LRU = self.LRU.next
            self.MRU.next = self.keyMap[key]
            self.keyMap[key].prev = self.MRU
            self.MRU = self.keyMap[key]
            self.MRU.next = None
            print(self.LRU.key)
            self.LRU.prev = None
            return self.keyMap[key].val
        
        prev = self.keyMap[key].prev
        nextNode = self.keyMap[key].next

        self.MRU.next = self.keyMap[key]
        self.keyMap[key].prev = self.MRU
        prev.next = nextNode
        nextNode.prev = prev
        self.MRU = self.keyMap[key]
        self.MRU.next = None
        return self.keyMap[key].val

    def put(self, key: int, value: int) -> None:
        print("Putting", key)
        if key in self.keyMap:
            self.keyMap[key].val = value
            if self.keyMap[key] == self.MRU:
                return
            elif self.keyMap[key] == self.LRU:
                self.LRU = self.LRU.next
                self.MRU.next = self.keyMap[key]
                self.keyMap[key].prev = self.MRU
                self.MRU = self.keyMap[key]
                self.MRU.next = None
                self.LRU.prev = None
            else:
                prev = self.keyMap[key].prev
                nextNode = self.keyMap[key].next

                self.MRU.next = self.keyMap[key]
                self.keyMap[key].prev = self.MRU
                self.keyMap[key].next = None
                self.MRU = self.keyMap[key]
                prev.next = nextNode
                nextNode.prev = prev
            
            #prev = self.keyMap[key].prev
            #nextNode = self.keyMap[key].next
        else:
            if len(self.keyMap) == self.capacity:
                lruNext = self.LRU.next
                oldLRU = self.LRU
                self.keyMap.pop(oldLRU.key)
                #print(lruNext.key)
                print(self.MRU.key)
                toAdd = self.ListNode(key = key, val = value, next = None, prev = None)
                toAdd.prev = self.MRU
                self.MRU.next = toAdd
                #print(lruNext.next.key)
                self.MRU = toAdd
                self.LRU.next = None
                print("LRU")
                print(self.LRU.key)
                del self.LRU
                if lruNext:
                    lruNext.prev = None
                self.LRU = lruNext
                #print(self.LRU.key)
                self.keyMap[key] = toAdd
            else:
                toAdd = self.ListNode(key = key, val = value, next = None, prev = None)
                if self.MRU:
                    self.MRU.next = toAdd
                    toAdd.prev = self.MRU
                else:
                    self.LRU = toAdd
                
                self.MRU = toAdd
                self.keyMap[key] = toAdd
        
