"""
Author: Vinh Truong
"""

from abc import ABC, abstractmethod
from process import process

class baseScheduler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_job(self, proc):
        pass
    
    @abstractmethod
    def remove_job(self, proc):
        pass
    
    @abstractmethod
    def get_next(self):
        pass
    
    def create_job(self, arrival, burst):
        self.add_job(process(arrival, burst))
    
    def isJobFinished(self):
        if self.current != None:
            return self.current.is_finished()
        else:
            return True