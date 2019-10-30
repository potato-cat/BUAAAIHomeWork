def min_arg(l):
    m = 0
    m_l = [0]
    for i in range(len(l)):
        if l[m] > l[i]:
            m = i
            m_l = [i]
        elif l[m] == l[i]:
            m_l.append(i)
    return m, m_l


def comp(a, b):
    return a.hash > b.hash


def insertion_sort1(l, e, comp):
    if not len(l):
        l.append(e)
        return
    # 二分法
    start = 0
    stop = len(l)
    index = int((start + stop) / 2)
    while True:
        if comp(l[index], e):
            stop = index
        else:
            start = index
        index = int((start + stop) / 2)
        if start == index or stop == index:
            break
    l.insert(stop, e)


def insertion_sort(l, e):
    if not len(l):
        l.append(e)
        return
    # 二分法
    start = 0
    stop = len(l)
    index = int((start + stop) / 2)
    while True:
        if l[index] < e:
            start = index
        else:
            stop = index
        index = int((start + stop) / 2)
        if start == index or stop == index:
            break
    l.insert(stop, e)


def find(l, e):
    # 二分法
    if not len(l):
        return -1
    start = 0
    stop = len(l)
    index = int((start + stop) / 2)
    while True:
        if l[index] > e:
            stop = index
        elif l[index] == e:
            return index
        else:
            start = index
        index = int((start + stop) / 2)
        if start == index or stop == index:
            break
    return -1


def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size