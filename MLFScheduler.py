"""
Author Vinh Truong

Implementation of Multi Level Feedback Scheduling
preemtive scheduling algorithm
"""

from baseScheduler import baseScheduler
from MLFProcess import MLFProcess

class MLFScheduler(baseScheduler):
    def __init__(self):
        self.current = None
        self.processes = [[],[],[],[],[]]
        self.tracker = list()
        self.current_level = None

    def add_job(self, process):
        self.processes[0].append(process)
        self.tracker.append(process)
    
    def create_job(self, arrival, burst):
        self.add_job(MLFProcess(arrival, burst, len(self.tracker)))
    
    def remove_job(self, process):
        for lv in range(5):
            try:
                self.processes[lv].remove(process)
                return True
            except ValueError as e:
                pass
        return False
    
    def get_next(self):
        if not self.isJobFinished() and self.current.time == 2 ** self.current_level:
            self.remove_job(self.current)
            self.current.reset_time()
            self.processes[self._next_level(self.current_level)].append(self.current)
            self.current, self.current_level = None, None

        for level in range(5):
            if len(self.processes[level]) > 0:
                self.current = self.processes[level][0]
                self.current_level = level
                break
        else:
            self.current = None
            self.current_level = None
        return self.current
    
    
    def _next_level(self, cur_lvl):
        if cur_lvl < 4:
            return cur_lvl + 1
        return 4
    
    def __str__(self):
        return "MLFScheduling"
                