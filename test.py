from PositionManager.cameraScanner import CameraScanner
from PositionManager.tag import Tag
from BoardGameUI.mainWindow import MainWindow

def main():
    '''
    '''
    l_main_window= MainWindow(640,480)


    l_tag_one = Tag(1)
    l_main_window.addTag(l_tag_one, 'first')

    l_tag_two = Tag(42)
    l_main_window.addTag(l_tag_two, 'bob')

    l_scanner_thread = CameraScanner(0, l_main_window.tagDetectionPositionChangeCallback)

    l_scanner_thread.start()
    l_main_window.run()

    l_scanner_thread.join()

if __name__ == '__main__':
    main()