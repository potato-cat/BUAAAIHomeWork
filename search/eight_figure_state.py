import copy


# 定义一个状态


class State(object):
    def __init__(self, s):
        self.rows = 3
        self.cols = 3
        self.state = s
        self.vacancy = (-1, -1)
        self.parent = None  # 用于获取路径
        self.children = []  # 用于画图
        self.operator = -1  # 用于动画
        self.in_path = False # 用于画图
        for i in range(self.rows):
            for j in range(self.cols):
                if self.state[i][j] == 0:
                    self.vacancy = (i, j)
                    break
            if self.vacancy != (-1, -1):
                break
        # 0->down 1->up 2->left 3->right
        self.operations = []
        if self.vacancy[0] == 0:
            self.operations.append(0)
        elif self.vacancy[0] == 1:
            self.operations.append(0)
            self.operations.append(1)
        elif self.vacancy[0] == 2:
            self.operations.append(1)
        if self.vacancy[1] == 0:
            self.operations.append(3)
        elif self.vacancy[1] == 1:
            self.operations.append(2)
            self.operations.append(3)
        elif self.vacancy[1] == 2:
            self.operations.append(2)

    def __eq__(self, other):
        for i in range(self.rows):
            for j in range(self.cols):
                if other.state[i][j] != self[i][j]:
                    return False
        return True

    def __getitem__(self, item):
        return self.state[item]

    def __str__(self):
        return str(self.state)

    def __hash__(self):
        h = 0
        for i in range(self.rows):
            for j in range(self.cols):
                h += self[i][j] * 10 ** (3 * i + j)
        return h

    def do_operation(self, operator):
        vacancy = self.vacancy
        s = copy.deepcopy(self.state)
        if operator == 0:  # down
            temp = self[vacancy[0] + 1][vacancy[1]]
            s[vacancy[0]][vacancy[1]] = temp
            s[vacancy[0] + 1][vacancy[1]] = 0
            return State(s)
        if operator == 1:  # up
            temp = self[vacancy[0] - 1][vacancy[1]]
            s[vacancy[0]][vacancy[1]] = temp
            s[vacancy[0] - 1][vacancy[1]] = 0
            return State(s)
        if operator == 2:  # left
            temp = self[vacancy[0]][vacancy[1] - 1]
            s[vacancy[0]][vacancy[1]] = temp
            s[vacancy[0]][vacancy[1] - 1] = 0
            return State(s)
        if operator == 3:  # right
            temp = self[vacancy[0]][vacancy[1] + 1]
            s[vacancy[0]][vacancy[1]] = temp
            s[vacancy[0]][vacancy[1] + 1] = 0
            return State(s)

    def setParent(self, parent):
        self.parent = parent

    def addChild(self, child):
        self.children.append(child)


def breadth_first_search(start, stop):
    start.parent = None
    start.in_path = False
    start.children = []
    stop.parent = None
    stop.in_path = False
    stop.children = []
    # 去重
    generated = set()
    generated.add(start)
    open_list = [start]
    close_list = []
    while len(open_list):
        n = open_list[0]
        open_list.remove(n)
        close_list.append(n)
        if n == stop:
            stop.setParent(n.parent)
            stop.children = n.children
            stop.operator = n.operator
            n.in_path = True
            print("yes! we get it!")
            break
        elif len(n.operations):
            for o in n.operations:
                ex = n.do_operation(o)
                before = len(generated)
                generated.add(ex)
                after = len(generated)
                if after > before:
                    open_list.append(ex)
                    ex.setParent(n)
                    n.addChild(ex)
                    ex.operator = o
