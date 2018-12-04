"""
Author: Vinh Truong

Tests and runs the schedulers. Main file
"""

from FIFOScheduler import FIFOScheduler
from SJFScheduler import SJFScheduler
from SRTScheduler import SRTScheduler
from MLFScheduler import MLFScheduler
from process import process

def main():
    fname = "input.txt"
    with open(fname) as file:
        procs = file.read().split()
    procs = [int(x) for x in procs]
    procs = list(zip(procs[::2], procs[1::2]))
    schedulers = list()
    schedulers.append(FIFOScheduler())
    schedulers.append(SJFScheduler())
    schedulers.append(SRTScheduler())
    schedulers.append(MLFScheduler())
    
    total = 1
    for val in procs:
        total += val[1]
    
    # i = 0
    # while len(schedulers[0].tracker) != len(procs) and len(schedulers[0].processes) != 0:
    for i in range(100):
        for sched in schedulers:
            # Add any processes
            for proc in procs:
                if proc[0] == i:
                    sched.create_job(proc[0], proc[1])

            if sched.isJobFinished():
                if sched.current != None:
                    sched.current.set_finish(i)
                    sched.remove_job(sched.current)
            
            sched.get_next()

            if sched.current != None:
                if sched.current.start == None:
                    sched.current.set_start(i)
                sched.current.run(1)
        # i += 1
    
    for sched in schedulers:
        print(sched)
        for proc in sched.tracker:
            print("Arrival: {}, Burst: {}, Start: {}, Finish: {}, Turnaround: {}".format(proc.arrival, proc.burst, proc.start, proc.finish, proc.finish-proc.arrival))

    
if __name__ == "__main__":
    main()
    # procs = list()
    # procs.append((0, 4))
    # procs.append((0, 2))
    # procs.append((3, 1))
    # schedulers = list()
    # schedulers.append(FIFOScheduler())
    # schedulers.append(SJFScheduler())
    # schedulers.append(SRTScheduler())
    # schedulers.append(MLFScheduler())
    # for i in range(30):
    #     for sched in schedulers:
    #         # Add any processes
    #         for proc in procs:
    #             if proc[0] == i:
    #                 sched.create_job(proc[0], proc[1])

    #         if sched.isJobFinished():
    #             if sched.current != None:
    #                 sched.current.set_finish(i)
    #                 sched.remove_job(sched.current)
            
    #         sched.get_next()

    #         if sched.current != None:
    #             if sched.current.start == None:
    #                 sched.current.set_start(i)
    #             sched.current.run(1)
    
    # for sched in schedulers:
    #     print(sched)
    #     for proc in sched.tracker:
    #         print("Arrival: {}, Burst: {}, Start: {}, Finish: {}, Turnaround: {}".format(proc.arrival, proc.burst, proc.start, proc.finish, proc.finish-proc.arrival))