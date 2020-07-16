n = int(input())
num = list(map(int, input().split()))
q = int(input())
q_num = list(map(int, input().split()))

'''
solve(i,j)はj番目までの数値でiを構成できるかどうかをTrueかFalseで返す関数
'''
'''
i, jの値を用いて再帰関数のループ終了条件を考える。
'''
def solve(i, j):
    if i == 0:
        return True
    if j < -1:
        return False
    return solve(i-num[j], j-1) or solve(i, j-1)


for k in q_num:
    if solve(k, n-1):
        print("Yes")
    else:
        print("No")
