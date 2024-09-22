from PositionManager.tag import Tag, TagRegistry
from PositionManager.cameraScanner import CameraScanner
from PositionManager.observerPattern import Observer
import threading

class TagManager(Observer):
    def update(self, a_tag: Tag) -> None:
        print("Tag notification received : {}", a_tag)

def main():
    '''
    '''

    l_tagReg = TagRegistry()
    l_tagManager = TagManager()

    l_scanner_thread = CameraScanner(4, l_tagReg.tagDetectionPositionChangeCallback)

    l_scanner_thread.start()

    l_tag = Tag(1)
    l_tag.attach(l_tagManager)

    l_tagReg.addTag('first', l_tag)

    l_scanner_thread.join()

    l_tag.detach(l_tagManager)

if __name__ == '__main__':
    main()