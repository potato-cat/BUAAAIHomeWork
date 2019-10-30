import copy
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRectF, QSequentialAnimationGroup, QPropertyAnimation, QPointF

from search.eight_figure_state import State
from search.ui.figure import Figure, FIGURE_WIDTH, FIGURE_HEIGHT

EIGHT_FIGURE_WIDTH = 150
EIGHT_FIGURE_HEIGHT = 150
FIFTEEN_FIGURE_WIDTH = 200
FIFTEEN_FIGURE_HEIGHT = 200


class FigureMap(QGraphicsObject):
    def __init__(self, state):
        super().__init__()
        self.interactive = False
        self.figures = copy.deepcopy(state.state)
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
        self.state = state
        for i, row in enumerate(state):
            for j, col in enumerate(row):
                if state[i][j] != 0:
                    figure = Figure(state[i][j])
                    self.figures[i][j] = figure
                    figure.setPos(j * 50, i * 50)
                    figure.setParentItem(self)

    def move(self, operator, group=True):
        vacancy = self.state.vacancy
        self.state = self.state.operate(operator)
        if operator == 0:  # down
            figure = self.figures[vacancy[0] + 1][vacancy[1]]
            pos = QPointF(FIGURE_HEIGHT * vacancy[1],
                          FIGURE_WIDTH * (vacancy[0] + 1))
            self.figures[vacancy[0] + 1][vacancy[1]] = 0
            mov = QPointF(0, 50)
        if operator == 1:  # up
            figure = self.figures[vacancy[0] - 1][vacancy[1]]
            pos = QPointF(FIGURE_HEIGHT * vacancy[1],
                          FIGURE_WIDTH * (vacancy[0] - 1))
            self.figures[vacancy[0] - 1][vacancy[1]] = 0
            mov = QPointF(0, -50)
        if operator == 2:  # left
            figure = self.figures[vacancy[0]][vacancy[1] - 1]
            pos = QPointF(FIGURE_HEIGHT * (vacancy[1] - 1),
                          FIGURE_WIDTH * vacancy[0])
            self.figures[vacancy[0]][vacancy[1] - 1] = 0
            mov = QPointF(-50, 0)
        if operator == 3:  # right
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
            vacancy = self.state.vacancy
            row_d = vacancy[0] - row
            col_d = vacancy[1] - col
            if row_d == 0 and col_d == 1:
                self.move(2, False)
            if row_d == 0 and col_d == -1:
                self.move(3, False)
            if row_d == 1 and col_d == 0:
                self.move(1, False)
            if row_d == -1 and col_d == 0:
                self.move(0, False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene(0, 0, 500, 500)
    start = State([[11, 9, 4, 15],
                   [1, 3, 0, 12],
                   [7, 5, 8, 6],
                   [13, 2, 10, 14]])
    eightFig = FigureMap(start)
    eightFig.setInteractive(True)
    scene.addItem(eightFig)
    eightFig.move(1)
    eightFig.move(2)
    eightFig.move(2)
    view.setScene(scene)
    view.show()
    eightFig.start()
    app.exec_()
