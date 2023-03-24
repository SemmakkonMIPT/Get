import re
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.mikrocheliks = []

def generate(nodes):
    root_v = nodes.pop(0)
    root = Node(int(root_v))

    queue = [root]
    while queue and nodes:
        node = queue.pop(0)
        mikrocheliks = nodes.pop(0)
        mikrochelik_v = [int(val) if val.isdigit() else val for val in re.split(r'\s|-', mikrocheliks)]

        for val in mikrochelik_v:
            if val is not None:
                mikrochelik = Node(val)
                node.mikrocheliks.append(mikrochelik)
                queue.append(mikrochelik)

    return root

def find_node_level(root, node_val):
    queue = [(root, 1)]
    while queue:
        node, level = queue.pop(0)
        if node.val == node_val:
            return level
        for mikrochelik in node.mikrocheliks:
            queue.append((mikrochelik, level+1))
    return 0

str = input()
list = str.split()

root_v = list[0]
nodes = list[1:]
result = re.split(r"[ -]", str)
node_val = int(result[-1])

tree = generate([root_v] + nodes)
print(find_node_level(tree, node_val))