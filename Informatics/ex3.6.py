class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def contains(self, data):
        lastknot = self.head
        while (lastknot):
            if data == lastknot.data:
                return True
            else:
                lastknot = lastknot.prevdata
        return False

    def addToEnd(self, newdata):
        newknot = knot(newdata)
        if (self.tail == None):
            self.tail = newknot
            self.head = newknot
            return
        firstdata = self.tail
        newknot.nextdata = firstdata
        self.tail.prevdata = newknot
        self.tail = newknot

    def push(self, newdata):
        newknot = knot(newdata)
        if (self.tail == None):
            self.tail = newknot
            self.head = newknot
            return
        lastdata = self.head
        newknot.prevdata = lastdata
        self.head.nextdata = newknot
        self.head = newknot

    def printstackList(self):
        lastknot = self.head
        l = []
        while(lastknot):
            l.append(lastknot.data)
            lastknot = lastknot.nextdata
        print(*l)

    def isEmpty(self):
        lastknot = self.head
        return (lastknot == None)

    def size(self):
        lastknot = self.head
        k = 0
        while (lastknot):
            k+=1
            lastknot = lastknot.prevdata
        return k

    def top(self):
        return(self.head.data)

    def pop(self):
        lastdata = self.head.data
        self.head = self.head.prevdata
        return(lastdata)

    def backprintstack(self):
        lastknot = self.head
        while (lastknot):
            print(lastknot.data)
            lastknot = lastknot.prevdata

    def printstack(self):
        firstknot = self.tail
        while (firstknot):
            print(firstknot.data)
            firstknot = firstknot.nextdata

    def printstack3_3(self):
        lastknot = self.head
        while(lastknot.prevdata):
            lastknot = lastknot.prevdata
        x = lastknot.data
        lastknot = self.head
        while(lastknot):
            print(lastknot.data-x)
            lastknot = lastknot.prevdata

    def printstack3_5(self):
        lastknot = self.head
        firstknot = self.tail
        print(lastknot.data-firstknot.data)
        while (lastknot != firstknot and lastknot.prevdata != firstknot):
            lastknot = lastknot.prevdata
            firstknot = firstknot.nextdata
            print(lastknot.data - firstknot.data)


    def delete(self, data):
        headdata = self.head
        if headdata is not None:
            if headdata.data == data:
                self.head = headdata.prevdata
                headdata = None
                return
        while headdata is not None:
            if headdata.data == data:
                break
            lastdata = headdata
            headdata = headdata.prevdata
        if headdata == None:
            return
        lastdata.prevdata = headdata.prevdata
        headdata = None




class knot:
    def __init__(self, data=None):
        self.data = data
        self.nextdata = None
        self.prevdata = None


stack = LinkedList()

for i in range(4):
    stack.push(int(input()))
for i in range(0):
    stack.addToEnd((int(input())))

stack.printstack()
