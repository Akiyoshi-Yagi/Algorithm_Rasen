n = int(input())
price = []
for k in range(n):
    price.append(int(input()))

min_price = 1000000001
max_pro = -200000

for i in range(n):
    max_pro = max(max_pro, price[i]-min_price)
    min_price = min(price[i], min_price)

print(max_pro)
