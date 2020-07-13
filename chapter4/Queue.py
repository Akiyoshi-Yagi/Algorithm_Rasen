from collections import deque

n, q = map(int, input().split())
Queue = deque([])
for i in range(n):
    name, time = input().split()
    Queue.append([name, int(time)])

t = 0
while len(Queue) != 0:
    process = Queue.popleft()
    process[1] = process[1] - q
    if process[1] <= 0:
        t += q + process[1]
        print(process[0]+" "+str(t))
    else:
        t += q
        Queue.append(process)

'''
#入力
5 100
p1 150
p2 80
p3 200
p4 350
p5 20

＃出力
p2 180
p5 400
p1 450
p3 550
p4 800

'''
