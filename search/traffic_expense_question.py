import copy
import sys

from PyQt5.QtWidgets import *

cities = ['西安', '北京', '上海', '广州', '昆明']
expenses = [[0, 80, 120, 150, 95],
            [80, 0, 75, 160, 170],
            [120, 75, 0, 70, 130],
            [150, 160, 70, 0, 90],
            [95, 170, 130, 90, 0]]


class State(object):
    def __init__(self, route):
        super(State, self).__init__()
        self.route = route
        self.expense = 0
        for i in range(len(self.route) - 1):
            self.expense += expenses[self.route[i]][self.route[i + 1]]
        if len(self.route) == 4:
            self.operators = [3]
        else:
            self.operators = {0, 1, 2, 4}.difference(self.route)
        self.f = self.expense + 70 * (5 - len(self.route))

    def do_operator(self, operator):
        route = copy.copy(self.route)
        route.append(operator)
        state = State(route)
        return state

    def __eq__(self, other):
        return self.route == other.route

    def __gt__(self, other):
        return self.f > other.f

    def __hash__(self):
        h = 0
        for i in range(len(self.route)):
            h += self.route[i] * 10 ** i
        return h

    def __str__(self):
        return ''.join([str(i) for i in self.route])
        # s = ''
        # for i in self.route:
        #     s += cities[i] + '->'
        # s = s.rstrip('->')
        # return 'route:' + s + ' f:' + str(self.f)


def print_list(l):
    for i in l:
        print(i, end=' ')
    print()


def list_str(l):
    s = ''
    for i in l:
        s += str(i) + '  '
    return s


def breadth_first_search_A_star(w):
    start = State([0])
    open_list = [start]
    close_list = []
    item = QTableWidgetItem(list_str(open_list))
    w.setItem(0, 0, item)
    item = QTableWidgetItem(list_str(close_list))
    w.setItem(0, 1, item)
    row = 0
    while len(open_list):
        row += 1
        n = open_list.pop(0)
        close_list.append(n)
        if n.route[-1] == 3:
            return n
        elif len(n.operators):
            for o in n.operators:
                ex = n.do_operator(o)
                open_list.append(ex)
            open_list.sort()
            print_list(open_list)
        item = QTableWidgetItem(list_str(open_list))
        w.setItem(row, 0, item)
        item = QTableWidgetItem(list_str(close_list))
        w.setItem(row, 1, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QTableWidget()
    w.setColumnCount(2)
    w.setRowCount(10)
    w.setHorizontalHeaderLabels(['open', 'closed'])
    w.setItem(1, 1, QTableWidgetItem('dsfa'))
    w.show()
    n = breadth_first_search_A_star(w)
    app.exec_()
