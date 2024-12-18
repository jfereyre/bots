from PositionManager.cameraScanner import CameraScanner
from PositionManager.box import Box
from PyPathUI.gameBoardUI import GameBoardUI
from PyPath.aStar import AStar
from PyPath.cell import CellMatrix
from PyPath.robot import Robot, RobotNoMoreMoveException

import yaml
from time import sleep
from tkinter import Tk, Button
from threading import Thread

#g_ex = None
#g_cells = None
#
#g_robot_start_position = (0,0)
#g_robot_destination = (39,29)
#
#g_bot = Robot()

class BotPathApp(object):

    def __init__(self):
        self._m_cells = CellMatrix(40,30)
        self._m_robot = Robot()

    def startBotSimulator(self):    
        try:
            while True:
                self._m_robot.move(self._m_cells)
                sleep(0.2)
        except RobotNoMoreMoveException as rnmme:
            print("No more move is possible!")
            
    def resetBotSimulator(self):
        self._m_robot.setStartPosition(0,0)
        self._m_robot.setDestination(39, 29)

        self._m_game_board_ui.reInit()

        l_robot_thread = Thread(target=self.startBotSimulator)
        l_robot_thread.start()

    def start(self):
        global g_ex, g_cells 
        
        root = Tk()

        root.geometry("800x650+300+300")
        self._m_game_board_ui = GameBoardUI(800, 600, self._m_cells, self._m_robot)

        l_reset_button = Button(root, text="Start/Restart", command=self.resetBotSimulator)

        l_reset_button.pack(side='bottom')

        # Mouse click tracking
        root.bind('<Button-3>', self._m_game_board_ui.button)

        root.mainloop()

def tagDetectionPositionChangeCallback(a_tag_id: int, a_box: Box):
    if a_tag_id == 47:
        l_topLeftCell = g_ex.getNearestCell(a_box.topLeft[0], a_box.topLeft[1])
        l_bottomRightCell = g_ex.getNearestCell(a_box.bottomRight[0], a_box.bottomRight[1])

        for l_x in range(l_topLeftCell.col, l_bottomRightCell.col):
            for l_y in range(l_topLeftCell.row, l_bottomRightCell.row):
                g_cells.get(l_x, l_y).occupied()
