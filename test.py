from PositionManager.cameraScanner import CameraScanner
from PositionManager.box import Box
import yaml
from PyPathUI.mainWindow import build, setOccupied

def tagDetectionPositionChangeCallback(a_tag_id: int, a_box: Box):
    if a_tag_id == 47:
        setOccupied(a_box.topLeft, a_box.bottomRight)

def main():
    with open('config.yml', 'r') as l_config_file:
        l_configuration = yaml.safe_load(l_config_file)

        l_scanner_thread = CameraScanner(l_configuration['camera']['id'], tagDetectionPositionChangeCallback)
        l_scanner_thread.start()

    l_root = build()
    l_root.mainloop()

if __name__ == '__main__':
    main()