"""
Author: Vinh Truong

Tests and runs the schedulers. Main file
"""

from FIFOScheduler import FIFOScheduler
from process import process

def main():
    pass
    
if __name__ == "__main__":
    procs = list()
    procs.append(process(0, 4))
    procs.append(process(0, 2))
    procs.append(process(3, 1))
    sched = FIFOScheduler()
    for i in range(30):
        # Add any processes
        for proc in procs:
            if proc.arrival == i:
                sched.add_job(proc)
                sched.get_next()

        if sched.isJobFinished():
            if sched.current != None:
                sched.current.set_finish(i)
                sched.remove_job(sched.current)
            sched.get_next()

        if sched.current != None:
            if sched.current.start == None:
                sched.current.set_start(i)
            sched.current.run(1)
    
    for proc in procs:
        print("Arrival: {}, Burst: {}, Start: {}, Finish: {}, Turnaround: {}".format(proc.arrival, proc.burst, proc.start, proc.finish, proc.finish-proc.arrival))