import heapq


class PriorityQueue(object):
    """
    Priority queue using heapq.
    我们使用(f, h, state)作为队列的元素，由于元组的排序规则，h值较小的状态会
    被优先扩展，我们认为这样更接近事情的真相
    """

    def __init__(self, object_list):
        """
        初始化heapq
        """
        self.queue_length = 0
        self.qheap = []
        for e in object_list:
            self.qheap.append(e)
            self.queue_length += 1
        heapq.heapify(self.qheap)

    def push(self, new_object):
        """
        push 长度加一
        """
        heapq.heappush(self.qheap, new_object)
        self.queue_length += 1

    def pop(self):
        """
        pop 长度减一
        """
        if self.queue_length < 1:
            return None
        o = heapq.heappop(self.qheap)
        self.queue_length -= 1
        return o

    def __repr__(self):
        strrep = ""
        for e in self.qheap:
            f, h, state = e
            strrep += str(state) + "\n"

        return strrep
