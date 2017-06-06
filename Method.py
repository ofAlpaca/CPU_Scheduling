#	Operating System - CPU scheduling v1.2
#
#   - main.py
#   - Input.py
#   - myHeap.py
#   -> Method.py
#   - mySchedule.py
#   - myProcess.py
#
#	Created by ShauShian, Chiang on 2017/06/01.
#	Copyright © 2017 ShauShian, Chiang. All rights reserved.

from mySchedule import mySchedule
from myHeap import *
import queue

class FCFS(mySchedule):
    #Override
    def start_scheduling(self, timeslice):
        ready_q = queue.Queue(0)
        running_state = None 

        while not ready_q.empty() or not self.is_every_process_finished():
            self.process_arrival(self.time, ready_q) # At this time, which process is comming

            if running_state != None :
                if running_state.is_finished():
                    self.add_finished_ls(running_state)
                    running_state = None

            if running_state == None :  # First time or running process is finished
                if not ready_q.empty() :
                    running_state = ready_q.get() # Take out the first process

            if running_state != None:
                running_state.after_one_time() # CPU_brust - 1
                self.gantt.append(running_state.pid)

            self.time += 1


class RR(mySchedule):

    #Override
    def start_scheduling(self, timeslice):
        ready_q = queue.Queue(0) # Ready State
        running_state = None # Running State
      
        while not ready_q.empty() or not self.is_every_process_finished() :
            s = 0
            while s <= timeslice:
                self.process_arrival(self.time, ready_q) # Get the arrival process to ready_q

                if running_state != None: # Put running state to ready state
                    if running_state.is_finished(): # Is the process finished ?
                        self.add_finished_ls(running_state) # Yes
                        running_state = None # Empty the running state
              
                if running_state == None or s == 0: # The process in the running state is finished
                    if not ready_q.empty(): # Checks if there is anything in the ready queue 
                        running_state = ready_q.get()
                        s = 0
                elif s == timeslice: # The time slice is used up
                    running_state.update_arrival_time(self.time)
                    ready_q.put(running_state)
                    running_state = ready_q.get()
                    s = 0

                if not running_state == None:
                    running_state.after_one_time() # CPU_brust - 1
                    self.gantt.append(running_state.pid)

                self.time += 1
                s += 1

class NPSJF(mySchedule):
    #Override
    def process_arrival(self, time, ready_q):
        for p in self.process_list:
            if p.arrival_time == time:
                ready_q.push(p)

    #Override
    def start_scheduling(self, timeslice):
        ready_q = NPSJF_Heap()
        running_state = None 

        while not ready_q.empty() or not self.is_every_process_finished():
            self.process_arrival(self.time, ready_q) # At this time, which process is comming

            if running_state != None :
                if running_state.is_finished():
                    self.add_finished_ls(running_state)
                    running_state = None

            if running_state == None:  # First time or running process is finished
                if not ready_q.empty() :
                    running_state = ready_q.pop() # Take out the first process

            if running_state != None:
                running_state.after_one_time() # CPU_brust - 1
                self.gantt.append(running_state.pid)
            self.time += 1

class PSJF(mySchedule):
    #Override
    def process_arrival(self, time, ready_q):
        for p in self.process_list:
            if p.arrival_time == time:
                ready_q.push(p)

    #Override
    def start_scheduling(self, timeslice):
        ready_q = PSJF_Heap() # Heap by remain_brust -> run_times -> arrival_time -> pid
        running_state = None # Running state

        while not ready_q.empty() or not self.is_every_process_finished() :
            s = 0
            while s <= timeslice:
                self.process_arrival(self.time, ready_q) # Get the arrival process to ready_q

                if running_state != None: # Put running state to ready state
                    if running_state.is_finished(): # Is the process finished ?
                        self.add_finished_ls(running_state) # Yes
                        running_state = None

                if running_state == None or s == 0:
                    if not ready_q.empty():
                        running_state = ready_q.pop()
                        s = 0
                elif s == timeslice or ready_q < running_state:
                    running_state.update_arrival_time(self.time)
                    ready_q.push(running_state)
                    running_state = ready_q.pop()
                    s = 0

                if not running_state == None:
                    running_state.after_one_time() # CPU_brust - 1
                    self.gantt.append(running_state.pid)

                self.time += 1
                s += 1

class PP(mySchedule):
    #Override
    def process_arrival(self, time, ready_q):
        for p in self.process_list:
            if p.arrival_time == time:
                ready_q.push(p)

    #Override
    def start_scheduling(self, timeslice):
        ready_q = PP_Heap() # Heap by priority -> run_times -> arrival_time -> pid
        running_state = None # Running state

        while not ready_q.empty() or not self.is_every_process_finished() :
            self.process_arrival(self.time, ready_q) # Get the arrival process to ready_q

            if running_state != None: # Put running state to ready state
                if running_state.is_finished(): # Is the process finished ?
                    self.add_finished_ls(running_state) # Yes
                    running_state = None

            if running_state == None:
                if not ready_q.empty():
                    running_state = ready_q.pop()
            elif ready_q < running_state:
                    running_state.update_arrival_time(self.time)
                    ready_q.push(running_state)
                    running_state = ready_q.pop()

            if not running_state == None:
                running_state.after_one_time() # CPU_brust - 1
                self.gantt.append(running_state.pid)

            self.time += 1
          