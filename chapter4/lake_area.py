ground = input()
idx_stack = []

total_area = 0
for i, s in enumerate(ground):
    if s == "\\":
        idx_stack.append(i)
    elif s == "/" and idx_stack:
        j = idx_stack.pop()
        total_area += i-j

print(total_area)

'''
入力
\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/\

出力
35
'''
