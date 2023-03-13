class TwiceLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def contains(self, data):
        lastknot = self.head
        while (lastknot):
            if data == lastknot.data:
                return True
            else:
                lastknot = lastknot.nextdata
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
            lastknot = lastknot.nextdata
        return k

    def top(self):
        return(self.head.data)

    def pop(self):
        x = self.head.data
        self.head = self.head.nextdata
        return(x)


    def printstack(self):
        lastknot = self.head
        while (lastknot):
            print(lastknot.data)
            lastknot = lastknot.prevdata

    def backprintlist(self):
        firstknot = self.tail
        while (firstknot):
            print(firstknot.data)
            firstknot = firstknot.nextdata


class knot:
    def __init__(self, data=None):
        self.data = data
        self.nextdata = None
        self.prevdata = None




stack = TwiceLinkedList()

for i in range(4):
    stack.push(int(input()))
for i in range(0):
    stack.addToEnd((int(input())))

stack.backprintlist()
stack.printstack()
