from PositionManager.box import Box
from PositionManager.observerPattern import Subject
from threading import Lock

class Tag(Box, Subject):
    def __init__(self, a_id:int = -1):
        '''
        '''
        super(Tag, self).__init__()
        self.m_id = a_id;

    @property
    def location(self):
        return Box(self)
    
    @location.setter
    def location(self, a_location: Box):
        l_modified = False
        if not self == a_location:
            self.m_bottomLeft = a_location.m_bottomLeft
            self.m_bottomRight = a_location.m_bottomRight
            self.m_topLeft = a_location.m_topLeft
            self.m_topRight = a_location.m_topRight

            self.notify()

    @property
    def id(self):
        return self.m_id
    
    @id.setter
    def id(self, a_id: int):
        self.m_id = a_id

    def __str__(self):
        return "id:{} - {}".format(self.m_id, super(Tag, self).__str__())


class TagRegistry():
    def __init__(self):
        self.m_tag_dict = dict()
        self.m_lock = Lock()

    def addTag(self, a_name: str, a_tag: Tag):
        self.m_lock.acquire()

        self.m_tag_dict[a_name] = a_tag

        self.m_lock.release()

    def getTag(self, a_name: str):
        self.m_lock.acquire()

        l_tag = self.m_tag_dict[a_name]

        self.m_lock.release()

        return l_tag

    def tagDetectionPositionChangeCallback(self, a_tag_id: int, a_box: Box):
        self.m_lock.acquire()

        for l_tag in self.m_tag_dict.values():
            if l_tag.id == a_tag_id:
                l_tag.location = a_box

        self.m_lock.release()
