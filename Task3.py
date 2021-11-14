data_file = open("radixsort.in")
output_file = open('radixsort.out', 'w')
params = [int(s) for s in data_file.readline().split()]
data = [s.replace('\n', '').replace('\r', '').strip() for s in data_file.readlines()]
n, m, k = params[0], params[1], params[2]


def compare(a, b):
    _a = a[-k:]
    _b = b[-k:]

    if _a > _b:
        return 1
    else:
        return -1


def insert_sort(a):
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and compare(a[j], key) == 1:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def digital_sort():
    for el in insert_sort(data):
        print(el, file=output_file)


def new_feature2():
    pass


digital_sort()
