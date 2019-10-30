from PyQt5.QtCore import QPointF

from search.eight_figure_state import *
import sys

from PyQt5.QtWidgets import *
from search.eight_figure_state import State
from search.eight_figure_state_tree import EightFigureStateTree
from search.ui.big_arrow import BigArrow
from search.ui.button import Button, BUTTON_WIDTH
from search.ui.figure_map import FigureMap


class EightFigureView(QGraphicsView):
    def __init__(self, parent=None):
        super(EightFigureView, self).__init__(parent)
        self.start = State([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 0]])
        self.end = State([[1, 2, 3],
                          [4, 5, 6],
                          [7, 0, 8]])
        scene = QGraphicsScene(0, 0, 540, 300)
        self.setScene(scene)
        self.startMap = FigureMap(self.start)
        self.startMap.setPos(10, 10)
        self.startMap.setInteractive(True)
        self.endMap = FigureMap(self.end)
        self.endMap.setPos(250, 10)
        self.arrow = BigArrow(QPointF(10 + 150, 75), QPointF(250, 75))
        self.resetButton = Button('重置')
        self.resetButton.setPos(10, 150 + 30)
        self.resetButton.clicked.connect(self.resetStart)
        self.randomButton = Button('随机')
        self.randomButton.setPos(10 + BUTTON_WIDTH + 10, 150 + 30)
        # self.randomButton.clicked.connect(self.randomStart)
        self.generateButton = Button('状态图')
        self.generateButton.setPos(10 + 2 * (BUTTON_WIDTH + 10) + 10, 150 + 30)
        self.generateButton.clicked.connect(self.generateMap)
        self.breadth_first_button = Button('广度优先')
        self.breadth_first_button.setPos(420, 10)
        self.breadth_first_button.clicked.connect(self.startBreadthFirstSearch)
        scene.addItem(self.startMap)
        scene.addItem(self.endMap)
        scene.addItem(self.arrow)
        scene.addItem(self.resetButton)
        scene.addItem(self.randomButton)
        scene.addItem(self.generateButton)
        scene.addItem(self.breadth_first_button)

    def startBreadthFirstSearch(self):
        self.startMap.clear()
        if self.startMap.state == self.end:
            QMessageBox.warning(self, '结束', '已结束')
            return
        breadth_first_search(self.startMap.state, self.end)
        self.start = self.startMap.state
        n = self.end
        operators = []
        while n.parent:
            operators.append(n.operator)
            n.in_path = True
            n = n.parent
        n.in_path = True
        operators.reverse()
        for o in operators:
            self.startMap.move(o)
        self.startMap.start()

    def generateMap(self):
        self.tree = EightFigureStateTree(self.start)
        self.tree.showMaximized()

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


if __name__ == '__main__':
    main()
