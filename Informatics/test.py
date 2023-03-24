import re

s = "раз, два.три.четыре"
result = re.split(r"[,.]", s)
print(result)