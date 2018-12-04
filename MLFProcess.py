"""
Author: Vinh Truong

Implementation of a wrapper class for processes
to be used in MLF scheduling algorithm
"""

from process import process

class MLFProcess(process):
    def __init__(self, arrival, burst, pid):
        super().__init__(arrival, burst)
        self.time = 0
        self.pid = pid
    
    def run(self, duration):
        self.remaining -= duration
        self.time += duration
    
    def reset_time(self):
        self.time = 0