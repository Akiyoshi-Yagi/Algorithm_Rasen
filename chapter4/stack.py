from collections import deque

Input = list(input().split())
stack = deque([])

for k in Input:
    if k not in ("+", "-", "*"):
        stack.append(int(k))
    elif k == "+":
        stack.append(stack.pop()+ stack.pop())
    elif k == "-":
        stack.append(-(stack.pop()- stack.pop()))
    elif k == "*":
        stack.append(stack.pop()*stack.pop())

print(stack.pop())

