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

# построить первое дерево
x = Node(0)
x.left = Node(1.1)
x.right = Node(1.1)
x.left.left = Node(2.1)
x.left.right = Node(2.2)
x.right.left = Node(2.2)
x.right.right = Node(2.1)

# построить второе дерево
y = Node(0)
y.left = Node(1.2)
y.right = Node(1.1)
y.left.left = Node(2.4)
y.left.right = Node(2.3)
y.right.left = Node(2.2)
y.right.right = Node(2.1)


print(isSelfSymm(x))
print(isSelfSymm(y))

