from __future__ import annotations
from abc import ABC, abstractmethod

class Subject(object):
    m_observers: List[Observer] = []

    def attach(self, a_observer: Observer) -> None:
        self.m_observers.append(a_observer)

    def detach(self, a_observer: Observer) -> None:
        self.m_observers.remove(a_observer)

    def notify(self) -> None:
        for l_observer in self.m_observers:
            l_observer.update(self)

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass            