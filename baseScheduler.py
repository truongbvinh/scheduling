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
    
    
    def all_finished(self):
        for process in self.tracker:
            if not process.is_finished():
                return False
        return True
    
    def avg_turnaround(self):
        total = 0
        for process in self.tracker:
            total += process.finish - process.arrival
        return total/len(self.tracker)
    
    def create_job(self, arrival, burst):
        self.add_job(process(arrival, burst, len(self.tracker)))
    
    def isJobFinished(self):
        if self.current != None:
            return self.current.is_finished()
        else:
            return True