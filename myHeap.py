#	Operating System - CPU scheduling v1.2
#
#   - main.py
#   - Input.py
#   -> myHeap.py
#   - Method.py
#   - mySchedule.py
#   - myProcess.py
#
#	Created by ShauShian, Chiang on 2017/06/01.
#	Copyright © 2017 ShauShian, Chiang. All rights reserved.

import heapq

class NPSJF_Heap:
    def __init__(self, brust_key = lambda x: x.CPU_brust, arrival_key = lambda x : x.arrival_time, pid_key = lambda x : x.pid):
        self.brust_key = brust_key # CPU_brust key
        self.arrival_key = arrival_key # Arrval_time key
        self.pid_key = pid_key # Pid key
        self._data = [] # Heap for CPU_brust

    def push(self, item):
        heapq.heappush(self._data, (self.brust_key(item),
                                    self.arrival_key(item),
                                    self.pid_key(item),
                                    item))

    def pop(self):
        return heapq.heappop(self._data)[3]

    def empty(self):
        if len(self._data) == 0 :
            return True
        else:
            return False

class PSJF_Heap:
    def __init__(self, remain_key = lambda x:x.remain_brust, arrival_key = lambda x:x.arrival_time, run_times_key = lambda x:x.run_times, pid_key = lambda x:x.pid):
        self.remain_key = remain_key # Remain time key
        self.arrival_key = arrival_key # Arrval_time key
        self.run_times_key = run_times_key # Run_times key
        self.pid_key = pid_key # Pid key
        self._data = [] # Heap for CPU_brust

    def push(self, item):
        heapq.heappush(self._data, (self.remain_key(item),
                                    self.run_times_key(item),
                                    self.arrival_key(item),
                                    self.pid_key(item),
                                    item))

    def pop(self):
        return heapq.heappop(self._data)[4]

    def __lt__(self, running_state):
        if len(self._data) == 0 or running_state == None:
            # if there is anything empty
            return False
        
        if self._data[0][4].remain_brust < running_state.remain_brust:
            return True
        else:
            return False

    def empty(self):
        if len(self._data) == 0 :
            return True
        else:
            return False

class PP_Heap:
    def __init__(self, priority_key = lambda x:x.priority, arrival_key = lambda x:x.arrival_time, run_times_key = lambda x:x.run_times, pid_key = lambda x:x.pid):
        self.priority_key = priority_key # Priority key
        self.arrival_key = arrival_key # Arrval_time key
        self.run_times_key = run_times_key # Run_times key
        self.pid_key = pid_key # Pid key
        self._data = [] # Heap for CPU_brust

    def push(self, item):
        heapq.heappush(self._data, (self.priority_key(item),
                                    self.run_times_key(item),
                                    self.arrival_key(item),
                                    self.pid_key(item),
                                    item))

    def pop(self):
        return heapq.heappop(self._data)[4]

    def __lt__(self, running_state):
        if len(self._data) == 0 or running_state == None:
            # if there is anything empty
            return False
        
        if self._data[0][4].priority < running_state.priority:
            return True
        else:
            return False

    def empty(self):
        if len(self._data) == 0 :
            return True
        else:
            return False