class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = None
        self.right = None

    def get(self, key: int) -> int:
        if key in self.cache:
            if self.cache[key] == self.right:
                return self.cache[key].val
            else:
                curr = self.cache[key]
                cPrev = curr.prev
                cNext = curr.next
                if self.left == curr:
                    self.left = cNext
                if cPrev:
                    cPrev.next = cNext
                if cNext:
                    cNext.prev = cPrev
                curr.prev = self.right
                self.right.next = curr
                curr.next = None
                self.right = curr
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            if self.cache[key] == self.right:
                self.cache[key].val = value
            else:
                curr = self.cache[key]
                curr.val = value
                cPrev = curr.prev
                cNext = curr.next
                if self.left == curr:
                    self.left = cNext
                if cPrev:
                    cPrev.next = cNext
                if cNext:
                    cNext.prev = cPrev
                curr.prev = self.right
                self.right.next = curr
                curr.next = None
                self.right = curr
            return
        if len(self.cache) == 0:
            self.cache[key] = Node(key, value)
            self.left = self.cache[key]
            self.right = self.cache[key]
        elif len(self.cache) == self.cap:
            toAdd = Node(key, value)
            self.right.next = toAdd
            toAdd.prev = self.right
            self.right = toAdd
            self.cache[key] = toAdd

            oldLeft = self.left
            self.left = self.left.next
            self.left.prev = None
            del self.cache[oldLeft.key]
            del oldLeft
        else:
            toAdd = Node(key, value)
            self.right.next = toAdd
            toAdd.prev = self.right
            self.right = toAdd
            self.cache[key] = toAdd
