array = list(map(int, input().split()))

def counting_sort(arr):

    max_num = max(arr)
    count = [0] * (max_num+1)
    cum_count = [0] * (max_num+1)
    sorted_arr = [0] * len(arr)

    for i in arr:
        count[i] += 1

    for k in range(max_num+1):
        #kが0の時だけ特別扱い
        if k == 0:
            cum_count[0] = count[0]
            continue
        cum_count[k] = cum_count[k-1] + count[k]

    for t in reversed(arr):
        i = cum_count[t]
        #i-1にすることを忘れない
        sorted_arr[i-1] = t
        cum_count[t] -= 1

    return sorted_arr

if __name__ == "__main__":
    print(counting_sort(array))


