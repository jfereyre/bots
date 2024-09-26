from PositionManager.observerPattern import Observer, Subject
from PositionManager.tag import Tag
from BoardGameUI import mainWindow

class TagUI(Observer):
    '''
    '''

    def __init__(self, a_tag: Tag, a_name: str, a_parent: mainWindow):
        '''
        '''
        self.m_name = a_name
        
        self.m_tag = a_tag
        a_tag.attach(self)

        self.m_parent = a_parent

    def draw(self):
        '''
        '''
        if self.m_parent.m_canvas:
            ligne1 = self.m_parent.m_canvas.create_line(self.m_tag.m_topLeft[0],        self.m_tag.m_topLeft[1],        self.m_tag.m_topRight[0],       self.m_tag.m_topRight[1])
            ligne2 = self.m_parent.m_canvas.create_line(self.m_tag.m_topRight[0],       self.m_tag.m_topRight[1],       self.m_tag.m_bottomRight[0],    self.m_tag.m_bottomRight[1])
            ligne3 = self.m_parent.m_canvas.create_line(self.m_tag.m_bottomRight[0],    self.m_tag.m_bottomRight[1],    self.m_tag.m_bottomLeft[0],     self.m_tag.m_bottomLeft[1])
            ligne3 = self.m_parent.m_canvas.create_line(self.m_tag.m_bottomLeft[0],     self.m_tag.m_bottomLeft[1],     self.m_tag.m_topLeft[0],        self.m_tag.m_topLeft[1])

    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        self.draw()