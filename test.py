from PositionManager.cameraScanner import CameraScanner
from PositionManager.tag import Tag
from BoardGameUI.mainWindow import MainWindow
import yaml

def main():
    '''
    '''
    l_main_window= MainWindow(640,480)

    with open('config.yml', 'r') as l_config_file:
        l_configuration = yaml.safe_load(l_config_file)

        for l_tag_id in l_configuration['tags']:

            l_main_window.addTag(Tag(l_tag_id), l_configuration['tags'][l_tag_id])

        l_scanner_thread = CameraScanner(l_configuration['camera']['id'], l_main_window.tagDetectionPositionChangeCallback)

        l_scanner_thread.start()

    l_main_window.run()

    exit(0)

if __name__ == '__main__':
    main()