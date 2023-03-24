def to_dict(lst):
    return {i: str(i)*n for i in lst}

n = int(input())
lst = [int(i) for i in input().split()]
print(to_dict(lst))