#	Operating System - CPU scheduling v1.2
#
#   - main.py
#   - Input.py
#   - myHeap.py
#   - Method.py
#   -> mySchedule.py
#   - myProcess.py
#
#	Created by ShauShian, Chiang on 2017/06/01.
#	Copyright © 2017 ShauShian, Chiang. All rights reserved.
import queue

class mySchedule:

    def __init__(self, p_list):
        self.process_list = p_list
        self.time = 0
        self.finished_ls = []
        self.gantt = []
    
    def add_finished_ls(self, p): # Add process to the finished list for result
        p.finished_time = self.time # Set current time as finished time
        p.finished_flag = True # Raise the finished flag
        self.finished_ls.append(p)

    def is_every_process_finished(self):
        for p in self.process_list:
            if not p.finished_flag: # There is one process is not finished
                return False
        return True

    def process_arrival(self, time, ready_q): # Find the arrival process at that time and store in ready_q
        for p in self.process_list:
            if p.arrival_time == time:
                ready_q.put(p)

    def start_scheduling(self, timeslice): # Just interface
        pass

    @staticmethod
    def sort_by_what(list, method):
        return {
            # sort by the third column in every list element
            1: sorted(sorted(list, key = lambda p : p.pid),
                      key = lambda q : q.arrival_time),             # FCFS
            2: sorted(sorted(list, key = lambda p : p.pid),
                      key = lambda q : q.arrival_time),             # RR
            }[method]
        

        


