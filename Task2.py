data_file = open("sort.in")
output_file = open('sort.out', 'w')

n = data_file.readline()
n = int(n)
data = [int(s) for s in data_file.readline().split()]


def heapify(nums, heap_size, root):
    max_el = root
    l_child = (2 * root) + 1
    r_child = (2 * root) + 2

    if l_child < heap_size and nums[l_child] > nums[max_el]:
        max_el = l_child

    if r_child < heap_size and nums[r_child] > nums[max_el]:
        max_el = r_child

    if max_el != root:
        nums[root], nums[max_el] = nums[max_el], nums[root]
        heapify(nums, heap_size, max_el)


def heap_sort(nums):
    len_nums = len(nums)
    for i in range(len_nums, -1, -1):
        heapify(nums, len_nums, i)

    for i in range(len_nums - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


heap_sort(data)
print(*data, file=output_file)
