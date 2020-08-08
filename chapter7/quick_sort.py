L = list(map(int, input().split()))

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    #critの決め方はそれぞれ（今回は左端の数値を無条件でcritとしたがrandを使う場合もある）
    crit = arr[0]
    #critと同じ数値があった場合は、leftにもrightにも入れずに、カウントしてあとで付け加える・
    same_crit = 0

    left = []
    right = []
    for num in arr:
        if num < crit:
            left.append(num)
        elif num > crit:
            right.append(num)
        else:
            same_crit += 1

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [crit] * same_crit + right

print(quick_sort(L))

