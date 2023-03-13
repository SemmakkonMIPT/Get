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


# построить первое дерево
x = Node(1)
x.left = Node(1)
x.right = Node(1)
x.left.left = Node(3)
x.left.right = Node(1)
x.right.left = Node(4)
x.right.right = Node(2)

# построить второе дерево
y = Node(0)
y.left = Node(1.2)
y.right = Node(1.1)
y.left.left = Node(2.4)
y.left.right = Node(2.3)
y.right.left = Node(2.2)
y.right.right = Node(2.1)

z = makeSymm(x)
print3Node(x)
print3Node(z)
print(isSymm(x, z))
