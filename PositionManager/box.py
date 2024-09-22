from __future__ import annotations
from array import *

class Box(object):
    def __init__(self, a_topRight: tuple=(0,0), a_bottomRight: tuple =(0,0), a_bottomLeft: tuple =(0,0), a_topLeft: tuple = (0,0)):
        '''
        '''
        self.m_topRight = a_topRight
        self.m_bottomRight = a_bottomRight
        self.m_bottomLeft = a_bottomLeft
        self.m_topLeft = a_topLeft

    @property
    def topRight(self) -> array:
        return [int(self.m_topRight[0]), int(self.m_topRight[1])]

    @property
    def topLeft(self) -> array:
        return [int(self.m_topLeft[0]), int(self.m_topLeft[1])]

    @property
    def bottomRight(self) -> array:
        return [int(self.m_bottomRight[0]), int(self.m_bottomRight[1])]

    @property
    def bottomLeft(self) -> array:
        return [int(self.m_bottomLeft[0]), int(self.m_bottomLeft[1])]
    
    def __eq__(self, a_other: Box):
        if not self.m_topRight[0] == a_other.m_topRight[0] or \
        not self.m_topRight[1] == a_other.m_topRight[1] or \
        not self.m_topLeft[0] == a_other.m_topLeft[0] or \
        not self.m_topLeft[1] == a_other.m_topLeft[1] or \
        not self.m_bottomRight[0] == a_other.m_bottomRight[0] or \
        not self.m_bottomRight[1] == a_other.m_bottomRight[1] or \
        not self.m_bottomLeft[0] == a_other.m_bottomLeft[0] or \
        not self.m_bottomLeft[1] == a_other.m_bottomLeft[1]:
            return False
        
        return True


    def center(self) -> tuple:
        return (int((self.m_topLeft[0] + self.m_bottomRight[0]) / 2.0),
                int((self.m_topLeft[1] + self.m_bottomRight[1]) / 2.0))

    def __str__(self):
        return "topRight: {} - topLeft: {} - bottomRight: {} - bottomLeft: {}".format(self.m_topRight, self.m_topLeft, self.m_bottomRight, self.m_bottomLeft)