row = [0] * 8
col = [0] * 8
dpos = [0] * 15
dneg = [0] * 15

def row_search(a):
    for i in range(8):
        if col[i] == 0 and dpos[a+i] == 0 and dneg[a-i+8-1] == 0:
            #おけるやん！
            row[a] = i
            col[i] = 1
            dpos[a+i] = 1
            dneg[a-i+8-1] = 1
            if a == 7:
                print("==================================")
                for i in row:
                    l = ["-"] * 8
                    l[i] = "*"
                    print(" ".join(l))

            else:
                row_search(a+1)
            #盤面戻すの忘れない
            row[a] = 0
            col[i] = 0
            dpos[a + i] = 0
            dneg[a - i + 8 - 1] = 0
    else:
        #このパターンは行き詰まり
        pass
row_search(0)


