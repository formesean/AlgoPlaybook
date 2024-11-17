import collections

def counter(str):
    count = collections.Counter(str)
    print(count)
    print(count.most_common(1))

def namedtuple(x, y):
    init = collections.namedtuple('Point', 'x,y')
    point = init(x, y)
    print(point.x, point.y)

def ordereddict(nums):
    res = collections.OrderedDict(nums)
    print(res)

def defaultdict(nums):
    res = collections.defaultdict(int, nums)
    print(res)

def deque():
    q = collections.deque()
    q.append(2)
    q.append(1)
    q.append(3)
    print(q)
    q.appendleft(0)
    print(q)
    q.pop()
    print(q)

counter("AaaBBbCCC")
namedtuple(1, -4)
ordereddict({'a': 2, 'b': 1, 'c': 3})
defaultdict({'a': 2, 'b': 1, 'c': 3})
deque()
