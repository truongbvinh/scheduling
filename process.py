"""
Author: Vinh Truong
Process class for general processes
stores information about remaining
runtime and arrival time
"""

class process():

    def __init__(self, arrival, burst, pid):
        """
        Initializes the process with the attributes of:
            arrival == arrival time
            remaining == remaining burst time
            burst == original burst time
            finish == time of process finish
            start == time of process starting
        """
        self.arrival = arrival
        self.remaining = burst
        self.burst = burst
        self.finish = None
        self.start = None
        self.pid = pid

    def run(self, duration):
        self.remaining -= duration
    
    def is_finished(self):
        return self.remaining == 0
    
    def set_start(self, start_time):
        self.start = start_time
    
    def set_finish(self, finish_time):
        self.finish = finish_time
    
    def __str__(self):
        return "{} {}".format(self.arrival, self.burst)
