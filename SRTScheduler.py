"""
Author: Vinh Truong

Implementation of Shortest Remaining Time Scheduler
preemptive scheduling algorithm
"""

from baseScheduler import baseScheduler

class SRTScheduler(baseScheduler):
    def __init__(self):
        self.current = None
        self.processes = set()
        self.tracker = list()

    def add_job(self, process):
        self.processes.add(process)
        self.tracker.append(process)
    
    def remove_job(self, process):
        if self.current == process:
            self.current = None
        self.processes.remove(process)

    def get_next(self):
        if len(self.processes) != 0:
            self.current = min(self.processes, key=lambda x: (x.remaining, x.pid))
        else:
            self.current = None
        return self.current
    
    def __str__(self):
        return "SRTScheduler"