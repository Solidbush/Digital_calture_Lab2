def SiftUp(a, i):
    while a[i] < a[(i - 1) // 2] and i > 0:
        a[i], a[(i - 1) // 2] = a[(i - 1) // 2], a[i]
        i = (i - 1) // 2


def SiftDown(a, i, Heapsize):
    while 2 * i + 1 < Heapsize:
        l = 2 * i + 1
        r = 2 * i + 2
        j = l
        if r <= Heapsize and a[r] < a[l]:
            j = r
        if a[i] <= a[j]:
            break
        a[i], a[j] = a[j], a[i]
        i = j


def findByKey(queue, key, HeapSize):
    for i in range(HeapSize):
        if queue[i] == key:
            return i
    return -1


def push(a, x, HeapSize):
    a[HeapSize] = x
    SiftUp(a, HeapSize)


def extract_min(a, Heapsize):
    if Heapsize <= 0:
        print('*', file=fout)
    else:
        print(a[0], file=fout)
        a[0] = a[Heapsize-1]
        SiftDown(a, 0, Heapsize-1)


def descrease_key(a, x, y, Heapsize):
    i = findByKey(a,x,Heapsize)
    a[i] = y
    SiftUp(a, i)


fin = open('priorityqueue.in')
fout = open('priorityqueue.out', 'w')
overall = fin.readlines()
n = len(overall)
a = [0] * 1000000
count = 0
Heapsize = 0
keys = [0] * 1000000
for i in range(n):
    s = overall[i]
    if 'push' in s:
        com, num = s.split()
        num = int(num)
        push(a, num, Heapsize)
        Heapsize += 1
        keys[count] = num
    elif 'extract-min' in s:
        extract_min(a, Heapsize)
        if Heapsize > 0:
            Heapsize -= 1
    elif 'decrease-key' in s:
        com, pos, num = s.split()
        pos, num = int(pos), int(num)
        descrease_key(a, keys[pos - 1], num, Heapsize)
        keys[pos-1] = num
    count += 1
fout.close()
