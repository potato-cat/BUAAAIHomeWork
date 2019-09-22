from PyQt5.QtCore import QPointF, Qt

from search.eight_figure_state import *
import sys

from PyQt5.QtWidgets import *
from search.eight_figure_state import State
from search.ui.big_arrow import BigArrow
from search.ui.button import Button, BUTTON_WIDTH
from search.ui.eight_figure_map import EightFigureMap, EIGHT_FIGURE_WIDTH
from search.ui.small_arrow import SmallArrow


class EightFigureStateTree(QGraphicsView):
    def __init__(self, start, parent=None):
        super(EightFigureStateTree, self).__init__(parent)
        self.setWindowTitle('状态图')
        scene = QGraphicsScene()
        self.setScene(scene)
        self.max_depth = 0  # 最大深度
        self.tree_max_width = 0
        self.width_map = {0: [start]}
        self.ergodic(start, 0)
        for (i, v) in self.width_map.items():
            w = (150 + 50) * 0.75 ** i * len(v)
            if w > self.tree_max_width:
                self.tree_max_width = w
        self.tree_max_depth = (150 + 50) * 4 * (1 - 0.75 ** (self.max_depth + 1))
        figure = EightFigureMap(start)
        figure.setPos((self.tree_max_width - 150) / 2, 0)
        scene.addItem(figure)
        for i in range(self.max_depth + 1):
            self.index = 0
            for j, s in enumerate(self.width_map[i]):
                if s.children:
                    l0 = self.tree_max_width / len(self.width_map[i])
                    l = self.tree_max_width / len(self.width_map[i + 1])
                    for c in s.children:
                        figure = EightFigureMap(c)
                        line = SmallArrow(QPointF(75 * 0.75 ** i + j * l0
                                                  + (l0 - 150 * 0.75 ** i) / 2,
                                                  (150 + 50) * 4 * (1 - 0.75 ** i) + 150 * 0.75 ** i),
                                          QPointF(self.index * l
                                                  + (l - 150 * 0.75 ** (i + 1)) / 2
                                                  + 75 * 0.75 ** (i + 1),
                                                  (150 + 50) * 4 * (1 - 0.75 ** (i + 1))),
                                          Qt.red if c.in_path else Qt.black)
                        figure.setPos(self.index * l
                                      + (l - 150 * 0.75 ** (i + 1)) / 2,
                                      (150 + 50) * 4 * (1 - 0.75 ** (i + 1)))
                        figure.setScale(0.75 ** (i + 1))
                        scene.addItem(figure)
                        scene.addItem(line)
                        self.index += 1

    def ergodic(self, start, currentDepth):
        if start.children:
            currentDepth += 1
            if currentDepth > self.max_depth:
                self.max_depth = currentDepth
            if currentDepth not in self.width_map.keys():
                self.width_map[currentDepth] = copy.deepcopy(start.children)
            else:
                self.width_map[currentDepth].extend(start.children)
            for i in start.children:
                self.ergodic(i, currentDepth)
        else:
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = State([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 0]])
    tree = EightFigureStateTree(start, None)
    tree.setGeometry(0, 0, 1000, 1000)
    tree.showMaximized()
    app.exec_()
