import sys
import time

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from search.conflict_table import listconflicts
from search.priority_queue import PriorityQueue
from search.ui.big_arrow import BigArrow
from search.ui.button import Button, BUTTON_WIDTH, BUTTON_HEIGHT
from search.ui.figure import FIGURE_WIDTH, FIGURE_HEIGHT, Figure
from search.ui.figure_map import FIFTEEN_FIGURE_HEIGHT

INF = 100000


def find_vacancy(state):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                return (i, j)


def neighbors():
    def generator(state):
        x, y = find_vacancy(state)
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for i, j in moves:
            a, b = x + i, y + j
            if 4 > a > -1 and 4 > b > -1:
                temp = [[num for num in row] for row in state]
                temp[x][y] = temp[a][b]
                temp[a][b] = 0
                yield (((temp[0][0], temp[0][1], temp[0][2], temp[0][3]),
                        (temp[1][0], temp[1][1], temp[1][2], temp[1][3]),
                        (temp[2][0], temp[2][1], temp[2][2], temp[2][3]),
                        (temp[3][0], temp[3][1], temp[3][2], temp[3][3])),
                       i if i else 2 * j)

    return generator


def h(stop):
    stop_map = {}
    for i in range(4):
        for j in range(4):
            stop_map[stop[i][j]] = (i, j)
    row_conflicts = []
    for row in range(4):
        t = stop[row]
        conf_dict = listconflicts([t[0], t[1], t[2], t[3]])
        row_conflicts.append(conf_dict)

    col_conflicts = []
    for col in range(4):
        col_list = []
        for row in range(4):
            col_list.append(stop[row][col])
        conf_dict = listconflicts(col_list)
        col_conflicts.append(conf_dict)

    def conflict(state):
        distance = 0
        rc = row_conflicts
        cc = col_conflicts
        for row in range(4):
            curr_row = tuple(state[row])
            distance += rc[row].get(curr_row, 0)

        for col in range(4):
            col_tuple = (state[0][col], state[1][col],
                         state[2][col], state[3][col])
            distance += cc[col].get(col_tuple, 0)
        return distance

    def manhattan(state):
        h = 0
        # self
        for row in range(4):
            for col in range(4):
                if state[row][col] != 0:
                    v = state[row][col]
                    h += (abs(row - stop_map[v][0]) +
                          abs(col - stop_map[v][1]))
        return h

    def cal(state):
        return conflict(state) + manhattan(state)

    return cal


class A_Star(object):
    def __init__(self, neighbors, h):
        self.neighbors = neighbors
        self.h = h
        self.running = True

    def __call__(self, start, stop):
        stop_map = {}
        for row in range(4):
            for col in range(4):
                v = stop[row][col]
                stop_map[v] = (row, col)
        h = self.h(start)
        f = h
        open_list = PriorityQueue([(f, f, start)])  # f, h, state
        generated = {start: (h, 0, 0, None)}  # h, g, o, parent
        steps = 0
        while open_list.queue_length and self.running:
            steps += 1
            if steps % 100000 == 0:
                print(str(steps) + " positions examined")
            f_n, h_n, n = open_list.pop()
            g_n = f_n - h_n
            if n == stop:
                print("yes! we get it!")
                gen = generated.get(n, None)
                path = [n]
                path_o = []
                while gen:
                    h, g, o, parent = gen
                    path.append(parent)
                    if o != 0:
                        path_o.append(o)
                    gen = generated.get(parent, None)
                path_o.reverse()
                return path, path_o
            else:
                for ex, o_c in self.neighbors(n):
                    s_gen = generated.get(ex, None)
                    if s_gen:
                        h, g, o, parent = s_gen
                        if g > g_n + 1:
                            g = g_n + 1
                            f = g + h
                            generated[ex] = (h, g, o_c, n)
                            open_list.push((f, h, ex))
                    else:
                        h = self.h(ex)
                        g = g_n + 1
                        f = h + g
                        generated[ex] = (h, g, o_c, n)
                        open_list.push((f, h, ex))
        return ([], [])


class IDA_Star:
    def __init__(self, neighbors, h):
        self.neighbors = neighbors
        self.h = h
        self.running = True

    def search(self, g, bound):
        if not self.running:
            return INF
        self.node_generated += 1
        state = self.path[-1]
        f = g + self.h(state)
        if f > bound:
            return f
        if state == self.stop: return -1

        m = None  # Lower bound on cost.
        for ex, o in self.neighbors(state):
            if ex in self.path_gen: continue
            self.path.append(ex)
            self.path_o.append(o)
            self.path_gen.add(ex)
            t = self.search(g + 1, bound)

            if t == -1: return -1
            if m is None or (t is not None and t < m):
                m = t

            self.path.pop()
            self.path_o.pop()
            self.path_gen.remove(ex)
        return m

    def __call__(self, start, stop):
        self.stop = stop
        h = self.h(start)
        bound = h
        self.path = [start]
        self.path_gen = {start}
        self.path_o = []
        self.node_generated = 0
        while self.running:
            print('stop by bound!' + str(self.path) + str(bound), self.node_generated)
            t = self.search(0, bound)
            if t == -1:
                print('yes!We find it!')
                return self.path, self.path_o, bound
            if t is None: return None
            bound = t
        return [], [], INF


class FigureMap(QGraphicsObject):
    def __init__(self, state):
        super().__init__()
        self.interactive = False
        self.figures = [[0 for j in range(len(state))] for i in range(len(state))]
        self.rows = len(self.figures)
        self.animationGroup = QSequentialAnimationGroup(self)
        self.initState(state)

    def paint(self, painter, option, widget):
        painter.setBrush(Qt.blue)
        painter.drawRoundedRect(0, 0, self.rows * FIGURE_WIDTH,
                                self.rows * FIGURE_HEIGHT, 10, 10)
        pass

    def boundingRect(self):
        return QRectF(0, 0, self.rows * FIGURE_WIDTH,
                      self.rows * FIGURE_HEIGHT)

    def initState(self, state):
        self.__state = [[e for e in row] for row in state]
        for i, row in enumerate(state):
            for j, col in enumerate(row):
                if state[i][j] != 0:
                    figure = Figure(state[i][j])
                    self.figures[i][j] = figure
                    figure.setPos(j * 50, i * 50)
                    figure.setParentItem(self)

    def move(self, operator, group=True):
        if operator == 0:
            return
        vacancy = find_vacancy(self.__state)
        if operator == 1:  # down
            temp = self.__state[vacancy[0] + 1][vacancy[1]]
            self.__state[vacancy[0]][vacancy[1]] = temp
            self.__state[vacancy[0] + 1][vacancy[1]] = 0
            figure = self.figures[vacancy[0] + 1][vacancy[1]]
            pos = QPointF(FIGURE_HEIGHT * vacancy[1],
                          FIGURE_WIDTH * (vacancy[0] + 1))
            self.figures[vacancy[0] + 1][vacancy[1]] = 0
            mov = QPointF(0, 50)
        if operator == -1:  # up
            temp = self.__state[vacancy[0] - 1][vacancy[1]]
            self.__state[vacancy[0]][vacancy[1]] = temp
            self.__state[vacancy[0] - 1][vacancy[1]] = 0
            figure = self.figures[vacancy[0] - 1][vacancy[1]]
            pos = QPointF(FIGURE_HEIGHT * vacancy[1],
                          FIGURE_WIDTH * (vacancy[0] - 1))
            self.figures[vacancy[0] - 1][vacancy[1]] = 0
            mov = QPointF(0, -50)
        if operator == -2:  # left
            temp = self.__state[vacancy[0]][vacancy[1] - 1]
            self.__state[vacancy[0]][vacancy[1]] = temp
            self.__state[vacancy[0]][vacancy[1] - 1] = 0
            figure = self.figures[vacancy[0]][vacancy[1] - 1]
            pos = QPointF(FIGURE_HEIGHT * (vacancy[1] - 1),
                          FIGURE_WIDTH * vacancy[0])
            self.figures[vacancy[0]][vacancy[1] - 1] = 0
            mov = QPointF(-50, 0)
        if operator == 2:  # right
            temp = self.__state[vacancy[0]][vacancy[1] + 1]
            self.__state[vacancy[0]][vacancy[1]] = temp
            self.__state[vacancy[0]][vacancy[1] + 1] = 0
            figure = self.figures[vacancy[0]][vacancy[1] + 1]
            pos = QPointF(FIGURE_HEIGHT * (vacancy[1] + 1),
                          FIGURE_WIDTH * vacancy[0])
            self.figures[vacancy[0]][vacancy[1] + 1] = 0
            mov = QPointF(50, 0)

        self.figures[vacancy[0]][vacancy[1]] = figure
        animation = QPropertyAnimation(figure, bytes('pos', 'utf-8'), self)
        animation.setDuration(500)
        animation.setStartValue(pos)
        animation.setEndValue(pos - mov)
        if group:
            self.animationGroup.addAnimation(animation)
        else:
            animation.start()

    def state(self):
        return ((self.__state[0][0], self.__state[0][1], self.__state[0][2], self.__state[0][3]),
                (self.__state[1][0], self.__state[1][1], self.__state[1][2], self.__state[1][3]),
                (self.__state[2][0], self.__state[2][1], self.__state[2][2], self.__state[2][3]),
                (self.__state[3][0], self.__state[3][1], self.__state[3][2], self.__state[3][3]))

    def start(self):
        self.animationGroup.start(QSequentialAnimationGroup.KeepWhenStopped)

    def clear(self):
        self.animationGroup.clear()

    def setInteractive(self, interactive=False):
        self.interactive = interactive

    def mousePressEvent(self, event):
        if self.interactive:
            pos = event.pos()
            col = int(pos.x() / FIGURE_WIDTH)
            row = int(pos.y() / FIGURE_HEIGHT)
            vacancy = find_vacancy(self.__state)
            row_d = vacancy[0] - row
            col_d = vacancy[1] - col
            if row_d == 0 and col_d == 1:
                self.move(-2, False)
            if row_d == 0 and col_d == -1:
                self.move(2, False)
            if row_d == 1 and col_d == 0:
                self.move(-1, False)
            if row_d == -1 and col_d == 0:
                self.move(1, False)


class Worker(QThread):
    finished = pyqtSignal(list, list)

    def __init__(self):
        super().__init__(None)
        self.idastar = None
        self.astar = None
        self.moveToThread(self)
        self.start()

    def run(self):
        self.exec_()

    def stop(self):
        if self.astar:
            self.astar.running = False
        if self.idastar:
            self.idastar.running = False

    def a_star(self, start, end):
        self.astar = A_Star(neighbors(), h(end))
        path, path_o = self.astar(start, end)
        self.finished.emit(path, path_o)

    def ida_star(self, start, end):
        self.idastar = IDA_Star(neighbors(), h(end))
        path, path_o, bound = self.idastar(start, end)
        self.finished.emit(path, path_o)


class EightFigureView(QGraphicsView):
    a_star_sig = pyqtSignal(tuple, tuple)
    ida_star_sig = pyqtSignal(tuple, tuple)

    def __init__(self, parent=None):
        super(EightFigureView, self).__init__(parent)
        self.start = ((11, 9, 4, 15),
                      (1, 3, 0, 12),
                      (7, 5, 8, 6),
                      (13, 2, 10, 14))
        # self.start = ((5, 10, 12, 14),
        #               (6, 3, 0, 4),
        #               (8, 13, 7, 15),
        #               (2, 1, 9, 11))
        # self.start = ((1, 2, 3, 4),
        #               (5, 6, 7, 8),
        #               (9, 10, 11, 12),
        #               (13, 14, 0, 15))
        self.end = ((1, 2, 3, 4),
                    (5, 6, 7, 8),
                    (9, 10, 11, 12),
                    (13, 14, 15, 0))
        self.worker = Worker()
        self.running = False
        scene = QGraphicsScene(0, 0, 650, 300)
        self.setScene(scene)
        self.startMap = FigureMap(self.start)
        self.startMap.setPos(10, 10)
        self.startMap.setInteractive(True)
        self.endMap = FigureMap(self.end)
        self.endMap.setPos(300, 10)
        self.arrow = BigArrow(QPointF(10 + 200, 110), QPointF(300, 110))
        self.resetButton = Button('重置')
        self.resetButton.setPos(10, FIFTEEN_FIGURE_HEIGHT + 30)
        self.resetButton.clicked.connect(self.resetStart)
        self.randomButton = Button('随机')
        self.randomButton.setPos(10 + BUTTON_WIDTH + 10, FIFTEEN_FIGURE_HEIGHT + 30)
        # self.randomButton.clicked.connect(self.randomStart)
        self.stopButton = Button('停止')
        self.stopButton.setPos(10 + BUTTON_WIDTH * 2 + 20, FIFTEEN_FIGURE_HEIGHT + 30)
        self.stopButton.clicked.connect(self.stop)
        self.timeText = QGraphicsTextItem('运行时间:')
        self.timeText.setDefaultTextColor(Qt.red)
        font = QFont()
        font.setPixelSize(30)
        font.setWeight(QFont.Bold)
        self.timeText.setFont(font)
        self.timeText.setPos(10 + BUTTON_WIDTH * 3 + 30, FIFTEEN_FIGURE_HEIGHT + 30)
        self.a_star_button = Button('A*算法')
        self.a_star_button.setPos(530, 10)
        self.a_star_button.clicked.connect(self.start_a_star)
        self.ida_star_button = Button('IDA*')
        self.ida_star_button.setPos(530, 20 + BUTTON_HEIGHT)
        self.ida_star_button.clicked.connect(self.start_ida_star)
        self.stepText = QGraphicsTextItem('步数:')
        self.stepText.setDefaultTextColor(Qt.red)
        self.stepText.setFont(font)
        self.stepText.setPos(530, 30 + 2 * BUTTON_HEIGHT)
        self.stepCount = QGraphicsTextItem('')
        self.stepCount.setDefaultTextColor(Qt.red)
        self.stepCount.setFont(font)
        self.stepCount.setPos(530, 40 + 2 * BUTTON_HEIGHT + 40)
        self.a_star_sig.connect(self.worker.a_star)
        self.ida_star_sig.connect(self.worker.ida_star)
        self.worker.finished.connect(self.finished)
        scene.addItem(self.startMap)
        scene.addItem(self.endMap)
        scene.addItem(self.arrow)
        scene.addItem(self.resetButton)
        scene.addItem(self.randomButton)
        scene.addItem(self.stopButton)
        scene.addItem(self.timeText)
        scene.addItem(self.a_star_button)
        scene.addItem(self.ida_star_button)
        scene.addItem(self.stepText)
        scene.addItem(self.stepCount)

    def stop(self):
        if self.running:
            self.worker.stop()
            self.running = False
            self.killTimer(self.timer)
            self.time = 0
            self.timeText.setPlainText('运行时间:')

    def finished(self, path, path_o):
        self.stepCount.setPlainText(str(len(path_o)))
        for o in path_o:
            self.startMap.move(o)
        self.startMap.start()
        self.worker.running = False
        self.running = False
        self.killTimer(self.timer)
        self.time = 0

    def start_a_star(self):
        if self.startMap.animationGroup.state() == QAnimationGroup.Running:
            QMessageBox.warning(self, '正在运行', '动画正在运行，请稍后')
            return
        self.startMap.clear()
        if self.startMap.state() == self.end:
            QMessageBox.warning(self, '结束', '已结束')
            return
        if self.running:
            QMessageBox.warning(self, '正在运行', '算法正在运行，请稍后。。。')
            return
        self.running = True
        self.start = self.startMap.state()
        self.a_star_sig.emit(self.start, self.end)
        self.timer = self.startTimer(1000)
        self.time = 0

    def start_ida_star(self):
        if self.startMap.animationGroup.state() == QAnimationGroup.Running:
            QMessageBox.warning(self, '正在运行', '动画正在运行，请稍后')
            return
        self.startMap.clear()
        if self.startMap.state == self.end:
            QMessageBox.warning(self, '结束', '已结束')
            return
        if self.running:
            QMessageBox.warning(self, '正在运行', '算法正在运行，请稍后。。。')
            return
        self.running = True
        self.start = self.startMap.state()
        self.ida_star_sig.emit(self.start, self.end)
        self.timer = self.startTimer(1000)
        self.time = 0

    def timerEvent(self, a0):
        self.time += 1
        self.timeText.setPlainText('运行时间:' + str(self.time) + 's')

    def resetStart(self):
        self.scene().removeItem(self.startMap)
        self.startMap.deleteLater()
        self.startMap = FigureMap(self.start)
        self.startMap.setPos(10, 10)
        self.scene().addItem(self.startMap)
        self.startMap.setInteractive(True)


def main():
    app = QApplication(sys.argv)
    view = EightFigureView()
    view.show()
    app.exec_()
    return 0


if __name__ == '__main__':
    main()
    # start_time = time.time()
    # start = ((2, 13, 7, 1),
    #          (10, 3, 4, 11),
    #          (0, 5, 8, 9),
    #          (14, 6, 12, 15))
    # end = ((1, 2, 3, 4),
    #        (5, 6, 7, 8),
    #        (9, 10, 11, 12),
    #        (13, 14, 15, 0))
    # a_star = A_Star(neighbors(), h(end))
    # path, path_o = a_star(start, end)
    # print(path)
    # print(path_o)
    # stop_time = time.time()
    # print('用时：%ds' % (stop_time - start_time))
