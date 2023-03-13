class LinkedList():
    def __init__(self):
        self.head = None

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
        if self.head is None:
            self.head = newknot
            return
        lastknot = self.head
        while (lastknot.nextdata):
            lastknot = lastknot.nextdata
        lastknot.nextdata = newknot

    def printstack(self):
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
    def push(self, newdata):
        x = self.head
        self.head = knot(newdata)
        self.head.nextdata = x


class knot:
    def __init__(self, data=None):
        self.data = data
        self.nextdata = None



stack = LinkedList()

for i in range(4):
    LinkedList.addToEnd(stack, int(input()))

stack.printstack()
print(stack.contains(3))

