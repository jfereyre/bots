from PositionManager.cameraScanner import CameraScanner
from PositionManager.box import Box
from PyPathUI.pathCanvas import PathCanvas
from PyPath.aStar import AStar
from PyPath.cell import CellMatrix

import yaml
from time import sleep
from tkinter import Tk, Button
from threading import Thread

g_ex = None


g_cells = CellMatrix(40,30)
g_robotPosition=g_cells.get(0,0)
g_targetPosition=g_cells.get(39,29)

def BotSimulator():
    global g_ex

    while g_ex is None:
        pass

    l_robot_path = AStar(g_robotPosition, g_targetPosition, g_cells, g_ex.max_col_index, g_ex.max_row_index)

    for l_path_element in l_robot_path:
        g_ex.setRobotPosition((l_path_element.col * 20) + 10, ( l_path_element.row * 20 ) + 10 )
        sleep(0.2)

def UIStart():
    global g_ex 
    
    root = Tk()

    g_ex = PathCanvas(800, 600, g_cells)
    root.geometry("800x650+300+300")

    l_reset_button = Button(root, text="Reset", command=g_ex.reInit)

    l_reset_button.pack(side='bottom')

    # Mouse click tracking
    root.bind('<Button-3>', g_ex.button)

    root.mainloop()

def tagDetectionPositionChangeCallback(a_tag_id: int, a_box: Box):
    if a_tag_id == 47:
        l_topLeftCell = g_ex.getNearestCell(a_box.topLeft[0], a_box.topLeft[1])
        l_bottomRightCell = g_ex.getNearestCell(a_box.bottomRight[0], a_box.bottomRight[1])

        for l_x in range(l_topLeftCell.col, l_bottomRightCell.col):
            for l_y in range(l_topLeftCell.row, l_bottomRightCell.row):
                g_ex.setCellOccupied(l_x, l_y)

def main():
    with open('config.yml', 'r') as l_config_file:
        l_configuration = yaml.safe_load(l_config_file)

        l_scanner_thread = CameraScanner(l_configuration['camera']['id'], tagDetectionPositionChangeCallback)
        l_scanner_thread.start()
    
    l_ui_thread = Thread(target=UIStart)
    l_ui_thread.start()

    l_robot_thread = Thread(target=BotSimulator)
    l_robot_thread.start()




if __name__ == '__main__':
    main()