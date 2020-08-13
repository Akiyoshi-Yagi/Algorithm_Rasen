row = [0] * 8
col = [0] * 8
dpos = [0] * 15
dneg = [0] * 15

def row_search(a):
    for i in range(8):
        if col[i] == 0 and dpos[a+i] == 0 and dneg[a-i+8-1] == 0:
            row[a] = i
            col[i] = 1
            dpos[a+i] = 1
            dneg[a-i+8-1] = 1
            if a == 7:
                return "Success"
            else:
                if row_search(a+1) == "Success":
                    return "Success"
                else:
                    row[a] = 0
                    col[i] = 0
                    dpos[a + i] = 0
                    dneg[a - i + 8 - 1] = 0
    return "解なし"

row_search(0)

for i in row:
    l = ["-"]*8
    l[i] = "*"
    print(" ".join(l))



