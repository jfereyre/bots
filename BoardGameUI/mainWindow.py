# coding: utf-8
 
from tkinter import * 
from PositionManager.tag import Tag
from PositionManager.box import Box
from BoardGameUI.tagUI import TagUI

class MainWindow(object):
    def __init__(self, a_width: int = 1024, a_height: int = 768):
        '''
        '''
        self.m_width = a_width
        self.m_height = a_height
        self.m_tag_dict = {}
        self.m_window = Tk()
        self.m_canvas = Canvas(self.m_window, width=self.m_width, height=self.m_height, background='yellow')
        self.m_canvas.pack()

    def addTag(self, a_tag: Tag, a_tag_name: str):
        '''
        '''
        self.m_tag_dict[a_tag.id] = TagUI(a_tag, a_tag_name, self)

    def tagDetectionPositionChangeCallback(self, a_tag_id: int, a_box: Box):
        for l_tag_name, l_tag in self.m_tag_dict.items():
            if l_tag.m_tag.id == a_tag_id:
                l_tag.m_tag.location = a_box

    def run(self):
        self.m_window.mainloop()