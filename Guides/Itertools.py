import itertools

def counter(start, step):
    counter = itertools.count(start, step)

    for n in counter:
        print(n, end=" ")

        if n == 10:
            break

def repeat(element, max):
    repeater = itertools.repeat(element, max)
    print()

    for s in repeater:
        print(s, end=" ")

def cycle(elements):
    cycler = itertools.cycle(elements)
    i = 0
    print()

    while i < 10:
        print(next(cycler), end=" ")
        i += 1

def accumulate(elements):
    print()
    running_sum = itertools.accumulate(elements)
    print(list(running_sum))

def chain(elements1, elements2):
    chained = itertools.chain(elements1, elements2)
    print(list(chained))

def chain_2d(_2d_chain):
    chained = itertools.chain.from_iterable(_2d_chain)
    print(list(chained))

def compress(data, selectors):
    compressed = itertools.compress(data, selectors)
    print(list(compressed))

def pairwise(nums):
    paired = itertools.pairwise(nums)
    print(list(paired))

def product(nums1, nums2):
    res = itertools.product(nums1, nums2)
    print(list(res))

def permutation(nums):
    res = itertools.permutations(nums, len(nums)//2)
    print(list(res))

def combination(nums):
    res = itertools.combinations(nums, len(nums)//2)
    print(list(res))

counter(2, 2)
repeat("Ss", 5)
cycle("135")
accumulate([2, 4, 6, 8])
chain("Se", "an")
chain_2d([[1, 3], [2, 4]])
compress([[1, 3], [2, 4]], [True, False])
pairwise([2, 4, 6, 8, 10])
product([1, 2, 3], [4, 5, 6])
permutation([1, 2, 3, 4])
combination([2, 4, 6, 8])
