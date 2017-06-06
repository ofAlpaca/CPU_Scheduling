#	Operating System - CPU scheduling v1.2
#
#   - main.py
#   - Input.py
#   - myHeap.py
#   - Method.py
#   - mySchedule.py
#   -> myProcess.py
#
#	Created by ShauShian, Chiang on 2017/06/01.
#	Copyright © 2017 ShauShian, Chiang. All rights reserved.

class myProcess:
    """This is a process object"""
    def __init__(self, pid, brust, arrival_time, priority):
        self.pid = pid
        self.CPU_brust = brust
        self.arrival_time = arrival_time
        self.priority = priority
        self.remain_brust = brust
        self.init_arrival_time = arrival_time
        self.finished_time = 0
        self.finished_flag = False
        self.run_times = 0

    @property
    def turnaround_time(self):
        return self.finished_time - self.init_arrival_time

    @property
    def waitting_time(self):
        return (self.finished_time - self.init_arrival_time) - self.CPU_brust

    def update_arrival_time(self, time):
        self.arrival_time = time

    def after_one_time(self):
        self.remain_brust -= 1
        self.run_times = 1

    def is_finished(self):
        if self.remain_brust <= 0 :
            return True
        else:
            return False




