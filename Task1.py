data_file = open("isheap.in")
output_file = open('isheap.out', 'w')

n = data_file.readline()
n = int(n)
data = [int(s) for s in data_file.readline().split()]


def handle_heap(m):
    flag = True
    for i in range(1, n):
        if m[(i-1)//2] <= m[i]:
            pass
        else:
            flag = False
            print('NO', file=output_file)
            break

    if flag: print('YES', file=output_file)


handle_heap(data)
