from PositionManager.cameraScanner import CameraScanner, DetectionCallback
from PositionManager.box import Box

from PyPath.PyPathUI.gameBoardUI import GameBoardUI
from botPathApp import BotPathApp

import yaml

class MyDetectionCallback(DetectionCallback):
    """
    """

    def __init__(self, a_app: BotPathApp):
        """
        """
        self._m_app = a_app

    def call(self, a_tag_id: int, a_box: Box):
        """
        """
        if a_tag_id == 47:
            l_topLeftCell = self._m_app.gameBoardUI.getNearestCell(a_box.topLeft[0], a_box.topLeft[1])
            l_bottomRightCell = self._m_app.gameBoardUI.getNearestCell(a_box.bottomRight[0], a_box.bottomRight[1])

            for l_x in range(l_topLeftCell.col, l_bottomRightCell.col):
                for l_y in range(l_topLeftCell.row, l_bottomRightCell.row):
                    self._m_app.cells.get(l_x, l_y).occupied()

def main():
    app = BotPathApp()

    with open('config.yml', 'r') as l_config_file:
        l_configuration = yaml.safe_load(l_config_file)

        myCallback = MyDetectionCallback(app)

        l_scanner_thread = CameraScanner(l_configuration['camera']['id'])
        l_scanner_thread.registerCallbackForTag(47, myCallback)
        l_scanner_thread.start()

    app.start()


if __name__ == '__main__':
    main()