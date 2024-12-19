from PyPathUI.gameBoardUI import GameBoardUI
from PyPath.cell import CellMatrix
from PyPath.robot import Robot, RobotNoMoreMoveException

from time import sleep
from tkinter import Tk, Button
from threading import Thread

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

    def resetOccupancy(self):
        self._m_game_board_ui.releaseOccupied()

    def start(self):
        global g_ex, g_cells 
        
        root = Tk()

        root.geometry("800x700+300+300")
        self._m_game_board_ui = GameBoardUI(800, 600, self._m_cells, self._m_robot)

        l_reset_button = Button(root, text="Start/Restart", command=self.resetBotSimulator)

        l_reset_button.pack(side='bottom')

        l_reset_button = Button(root, text="Reset Occupancy", command=self.resetOccupancy)

        l_reset_button.pack(side='bottom')

        # Mouse click tracking
        root.bind('<Button-3>', self._m_game_board_ui.button)

        root.mainloop()

    @property
    def cells(self):
        return self._m_cells
    
    @property
    def gameBoardUI(self):
        return self._m_game_board_ui
