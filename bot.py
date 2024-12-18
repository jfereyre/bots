#from PositionManager.cameraScanner import CameraScanner
#from PositionManager.box import Box


from botPathApp import BotPathApp

#import yaml
#from time import sleep
#from tkinter import Tk, Button
#from threading import Thread

#def tagDetectionPositionChangeCallback(a_tag_id: int, a_box: Box):
#    if a_tag_id == 47:
#        l_topLeftCell = g_ex.getNearestCell(a_box.topLeft[0], a_box.topLeft[1])
#        l_bottomRightCell = g_ex.getNearestCell(a_box.bottomRight[0], a_box.bottomRight[1])
#
#        for l_x in range(l_topLeftCell.col, l_bottomRightCell.col):
#            for l_y in range(l_topLeftCell.row, l_bottomRightCell.row):
#                g_cells.get(l_x, l_y).occupied()

def main():
    app = BotPathApp()

    app.start()

#    with open('config.yml', 'r') as l_config_file:
#        l_configuration = yaml.safe_load(l_config_file)
#
#        l_scanner_thread = CameraScanner(l_configuration['camera']['id'], tagDetectionPositionChangeCallback)
#        l_scanner_thread.start()
    

if __name__ == '__main__':
    main()