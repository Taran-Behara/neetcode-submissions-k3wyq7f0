class TimeMap:

    def __init__(self):
        self.keyMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        toAdd = []
        toAdd.append(value)
        toAdd.append(str(timestamp))
        if key in self.keyMap:
            self.keyMap[key].append(toAdd)
        else:
            self.keyMap[key] = []
            self.keyMap[key].append(toAdd)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyMap:
            return ""
    
        arr = self.keyMap[key]
        
        l = 0
        r = len(arr) - 1
        latest = -1
        latestIndex = -1

        while l <= r:
            mid = (l + r)//2
            if int(arr[mid][1]) == timestamp:
                latestIndex = mid
                latest = int(arr[mid][1])
                break
            elif int(arr[mid][1]) > timestamp:
                r = mid - 1
            else:
                if int(arr[mid][1]) > latest:
                    latest = int(arr[mid][1])
                    latestIndex = mid
                l = mid + 1
        
        if latestIndex == -1:
            return ""
        
        return arr[latestIndex][0]