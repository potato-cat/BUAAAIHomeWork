import math
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QColor

from search.ui.button import Button, BUTTON_WIDTH
from search.ui.circle_indicator import CircleIndicator
from search.ui.disk import Disk, DISK_HEIGHT
from search.ui.monk_think import MonkThink
from search.ui.tower import Tower, TOWER_HEIGHT, TOWER_BASE_HEIGHT, TOWER_BASE_WIDTH

from PyQt5.QtWidgets import *

towers = set({0, 1, 2})
operators = []
count = 0


class TowerOfHanoiView(QGraphicsView):
    def __init__(self, order=10, parent=None):
        super(TowerOfHanoiView, self).__init__(parent)
        self.setScene(QGraphicsScene())
        self.order = order
        self.disks = [[], [], []]
        self.tower = Tower()
        self.monkThink = MonkThink(100)
        self.orderIndicator = CircleIndicator(150, self.order)
        self.resetBtn = Button('重置')
        self.stopBtn = Button('停止')
        self.playBtn = Button('思考')
        self.resetBtn.setPos(10, 100 + TOWER_BASE_HEIGHT +
                             TOWER_HEIGHT + 10)
        self.stopBtn.setPos(BUTTON_WIDTH + 20, 100 + TOWER_BASE_HEIGHT +
                            TOWER_HEIGHT + 10)
        self.playBtn.setPos(BUTTON_WIDTH * 2 + 30, 100 + TOWER_BASE_HEIGHT +
                            TOWER_HEIGHT + 10)
        self.tower.setPos(0, 100)
        self.orderIndicator.setPos(TOWER_BASE_WIDTH + 80, 170)
        self.monkThink.setPos(TOWER_BASE_WIDTH, 100)
        self.scene().addItem(self.tower)
        self.scene().addItem(self.monkThink)
        self.scene().addItem(self.orderIndicator)
        self.scene().addItem(self.resetBtn)
        self.scene().addItem(self.stopBtn)
        self.scene().addItem(self.playBtn)
        self.scene().setBackgroundBrush(QColor(87, 250, 255))
        self.resetBtn.clicked.connect(self.reset)
        self.stopBtn.clicked.connect(self.stop)
        self.playBtn.clicked.connect(self.play)
        self.orderIndicator.changed.connect(self.changeOrder)
        self.playing = False

        for i in range(self.order):
            disk = Disk(280 - i * 240 / (order - 1))
            self.disks[0].append(disk)
            disk.setPos(150, 100 + TOWER_HEIGHT - i * DISK_HEIGHT)
            self.scene().addItem(disk)
        self.operators = []
        self.animation_group = QSequentialAnimationGroup(self)
        self.animation_group.finished.connect(self.onFinish)

    def changeOrder(self, order):
        self.order = order
        self.reset()

    def onFinish(self):
        print('finish')
        self.playing = False
        self.monkThink.stopThink()

    def reset(self):
        if self.playing:
            QMessageBox.warning(self, '正在进行', '请先停止...')
        else:
            for i in self.disks:
                for j in i:
                    self.scene().removeItem(j)
            self.disks = [[], [], []]
            for i in range(self.order):
                disk = Disk(280 - i * 240 / self.order)
                self.disks[0].append(disk)
                disk.setPos(150, 100 + TOWER_HEIGHT - i * DISK_HEIGHT)
                self.scene().addItem(disk)

    def stop(self):
        if self.playing:
            self.animation_group.stop()
            self.playing = False
            self.monkThink.stopThink()

    def moveDisk(self, before, after, group=True):
        h1 = TOWER_HEIGHT - DISK_HEIGHT * (len(self.disks[before]) - 1)
        h2 = TOWER_HEIGHT - DISK_HEIGHT * (len(self.disks[after]))
        disk = self.disks[before].pop(-1)
        self.disks[after].append(disk)
        animation_up = QPropertyAnimation(disk, bytes('pos', 'utf-8'),
                                          self)
        animation_up.setStartValue(QPointF(
            TOWER_BASE_WIDTH / 6 + before * TOWER_BASE_WIDTH / 3, 100 + h1
        ))
        animation_up.setEndValue(QPointF(
            TOWER_BASE_WIDTH / 6 + before * TOWER_BASE_WIDTH / 3, 100
        ))
        animation_up.setDuration(500 / TOWER_HEIGHT * h1)
        animation_h = QPropertyAnimation(disk, bytes('pos', 'utf-8'),
                                         self)
        animation_h.setStartValue(QPointF(
            TOWER_BASE_WIDTH / 6 + before * TOWER_BASE_WIDTH / 3, 100
        ))
        animation_h.setEndValue(QPointF(TOWER_BASE_WIDTH / 6 +
                                        TOWER_BASE_WIDTH / 3 * after,
                                        100))
        animation_h.setDuration(TOWER_BASE_WIDTH / 3 * math.fabs(after - before)
                                * 500 / TOWER_HEIGHT)
        animation_down = QPropertyAnimation(disk, bytes('pos', 'utf-8'),
                                            self)
        animation_down.setStartValue(QPointF(TOWER_BASE_WIDTH / 6 +
                                             TOWER_BASE_WIDTH / 3 * after,
                                             100))
        animation_down.setEndValue(QPointF(TOWER_BASE_WIDTH / 6 +
                                           TOWER_BASE_WIDTH / 3 * after,
                                           100 + h2))
        animation_down.setDuration(h2 * 500 / TOWER_HEIGHT)
        self.animation_group.addAnimation(animation_up)
        self.animation_group.addAnimation(animation_h)
        self.animation_group.addAnimation(animation_down)

    def play(self):
        global operators
        if self.playing:
            QMessageBox.warning(self, '正在进行', '请先停止...')
            return
        if len(self.disks[0]) != self.order:
            QMessageBox.warning(self, '请先重置', '请先重置...')
            return
        self.animation_group = QSequentialAnimationGroup(self)
        self.animation_group.finished.connect(self.onFinish)
        operators = []
        self.playing = True
        move(self.order, 0, 2)
        for i in operators:
            self.moveDisk(i[0], i[1])
        self.start()
        self.monkThink.startThink()

    def start(self):
        self.animation_group.start(QAnimationGroup.DeleteWhenStopped)


# 递归
def move(num, before, after):
    global operators, count
    if num == 1:
        operators.append([before, after])
    elif num == 2:
        to = towers.difference({before, after}).pop()
        operators.append([before, to])
        operators.append([before, after])
        operators.append([to, after])
    else:
        to = towers.difference({before, after}).pop()
        move(num - 1, before, to)
        move(1, before, after)
        move(num - 1, to, after)


def main():
    app = QApplication(sys.argv)
    view = TowerOfHanoiView(15)
    view.setFixedSize(1500, 600)
    view.show()
    app.exec_()


if __name__ == '__main__':
    main()
