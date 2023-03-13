# Класс для хранения узла бинарного дерева.
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Рекурсивная функция для проверки идентичности двух заданных бинарных деревьев.
def isIdentical(x, y):
    # , если оба дерева пусты, вернуть true
    if x is None and y is None:
        return True

    # , если оба дерева непусты и значение их корневого узла совпадает,
    # повторяются для их левого и правого поддерева
    return (x is not None and y is not None) and (x.key == y.key) and \
           isIdentical(x.left, y.left) and isIdentical(x.right, y.right)

def isSymm(x, y):
    if x is None and y is None:
        return True
    return (x is not None and y is not None) and (x.key == y.key) and \
           isSymm(x.left, y.right) and isSymm(x.right, y.left)

def isSelfSymm(x):
    return (isSymm(x.right, x.left))

def NodeSumm(x):
    if x == None:
        return 0
    else:
        return (x.key + NodeSumm(x.left) + NodeSumm(x.right))

def makefakesumm(x):
    y = Node(NodeSumm(x.left)+NodeSumm(x.right))
    if x.left != None:
        y.left = makefakesumm(x.left)
    if x.right != None:
        y.right = makefakesumm(x.right)
    return (y)

def makeSumm(x):
    if (x.right == None and x.left == None):
        y = x
    else:
        y = Node(makeSumm(x.left).key+makeSumm(x.right).key)
        y.left = makeSumm(x.left)
        y.right = makeSumm(x.right)
    return(y)

def isSumm(x):
    if (x.right == None and x.left == None):
        return True
    return (x.key == x.right.key + x.left.key and isSumm(x.left) and isSumm(x.right))

def print3Node(x):
    y = x
    print(y.key)
    print(y.left.key, y.right.key)
    print(y.left.left.key, y.left.right.key, y.right.left.key, y.right.right.key)

def makeSymm(x):
    if x == None:
        return None
    y = Node(x.key)
    y.left = makeSymm(x.right)
    y.right = makeSymm(x.left)
    return(y)

def isin(x, k):
    if x == None: return False
    return(x.key == k or isin(x.right, k) or isin(x.left, k))

def findFamily(x, k):
    if (not isin(x, k)): return []
    return findFamily(x.right, k) + findFamily(x.left, k) + [x.key]
def findPred(x, k):
    if isin(x, k): return findFamily(x, k)[1:]
    else: return []

def sizes(x):
    if x == None: return [-1, 0]
    if (x.right == None and x.left == None): return [0, 0]
    if x.right == None: return [sizes(x.left)[0] + 1, sizes(x.left)[1]]
    if x.left == None: return [sizes(x.right)[0] + 1, sizes(x.right)[1]]
    return [max(sizes(x.left)[0], sizes(x.right)[0])+1, max(sizes(x.left)[1], sizes(x.right)[1], sizes(x.left)[0] + sizes(x.right)[0] + 1)]

def hight(x, k):
    if x == None or not isin(x, k): return -1
    if x.key == k: return 0
    return max(hight(x.left, k), hight(x.right, k))+1

def dist(x, k, l):
    if not isin(x, k) or not isin(x, l): return -1
    if x.key == k or x.key == l: return max(hight(x, k), hight(x, l))-1
    if (isin(x.left, k) and isin(x.right, l)) or (isin(x.left, l) and isin(x.right, k)): return hight(x, k) + hight(x, l) - 1
    return max(dist(x.left, k, l), dist(x.right, k, l))


# построить первое дерево
x = Node(1)
x.left = Node(2)
x.right = Node(3)
x.left.left = Node(4)
x.left.right = Node(5)
x.right.left = Node(6)
x.right.right = Node(7)
''''''
x.left.left.left = Node(10)
x.left.left.right = Node(8)
x.left.left.left.left = Node(11)


# построить второе дерево
y = Node(1)
y.left = Node(2)
y.right = Node(3)
y.left.left = Node(4)
'''
y.left.right = Node(2.3)
y.right.left = Node(2.2)
y.right.right = Node(2.1)
'''
z = Node(1)
z.left = Node(2)
z.left.left = Node(3)
z.left.left.left = Node(4)
z.left.left.right = Node(5)

#print3Node(x)
print(hight(x, 1))
print(dist(x, 5, 4))
'''
x
1
2 3
4 5 6 7
10 8
11
y
1
2 3
4
'''