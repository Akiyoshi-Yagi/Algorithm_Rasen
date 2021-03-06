N, W = list(map(int, input().split()))
items = []
for _ in range(N):
    items.append(tuple(map(int, input().split())))


# dpテーブルの作成
# 今回は最大化が目的なのですべてのマスを-1で埋めることにする
dp = [[-1] * (W + 1) for _ in range(N + 1)]

# dpテーブルの初期化
# dp[:][0]が0 ∵大きさ0のナップサックには何も入れられない
# dp[0][:]が0 ∵なにもitemを考慮しないときはナップサックに何も入らない。
for i in range(N + 1):
    dp[i][0] = 0
for w in range(W + 1):
    dp[0][w] = 0

# dpテーブルの更新
# i番目のitemが入らない場合→dp[i+1][w]=dp[i][w] ∵iを考慮しないときと価値は変わらない
# i番目のitemが入る場合→dp[i+1][w]=max(dp[i][w], dp[i][w-item[i]の重さ]+item[i]の価値)
# ∵iを入れる前の最善はdp[i][w-item[i]の重さ]にあり、それにitem[i]の価値を足すことで最善になる可能性がある。
# ただしちゃんと、iを入れないときのほうが良いかもしれないことに注意しなければいけない。
from itertools import product
for i, w in product(range(N), range(W + 1)):
    dp[i + 1][w] = dp[i][w]
    value, weight = items[i]
    if w - weight >= 0:
        dp[i + 1][w] = max(dp[i][w], dp[i][w - weight] + value)

print(dp[-1][-1])
