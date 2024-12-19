from PositionManager.box import Box
from PositionManager.observerPattern import Subject

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

