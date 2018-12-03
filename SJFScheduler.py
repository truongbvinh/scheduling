"""
Author: Vinh Truong

Implementation of SJF Scheduling algorithm
Non-preemtive
"""

from baseScheduler import baseScheduler

class SJFScheduler(baseScheduler):
    def __init__(self):
        self.current = None
        self.processes = set()

    def add_job(self, process):
        self.processes.add(process)
    
    def remove_job(self, process):
        if self.current == process:
            self.current = None
        self.processes.remove(process)

    def get_next(self):
        if self.current == None:
            if len(self.processes) != 0:
                self.current = min(self.processes, key=lambda x: x.remaining)
            else:
                self.current = None
        return self.current


"""
dis for SRT
    def get_next(self):
        if len(self.processes) != 0:
            self.current = min(self.processes, key=lambda x: x.remaining)
        else:
            self.current = None
        return self.current
"""