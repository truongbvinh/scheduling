"""
Author: Vinh Truong

Implementation of First In First Out Scheduler algorithm
for processes. Also known as First Come First Served (FCFS)
"""

from baseScheduler import baseScheduler

class FIFOScheduler(baseScheduler):
    def __init__(self):
        self.current = None
        self.processes = list()
        self.tracker = list()

    def add_job(self, process):
        self.processes.append(process)
        self.tracker.append(process)
    
    def remove_job(self, process):
        self.processes.remove(process)
    
    def get_next(self):
        if len(self.processes) != 0:
            self.current = self.processes[0]
        else:
            self.current = None
        return self.current
    
    def __str__(self):
        return "FIFOScheduler"