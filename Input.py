#	Operating System - CPU scheduling v1.2
#
#   - main.py
#   -> Input.py
#   - myHeap.py
#   - Method.py
#   - mySchedule.py
#   - myProcess.py
#
#	Created by ShauShian, Chiang on 2017/06/01.
#	Copyright © 2017 ShauShian, Chiang. All rights reserved.
class InputFile:
    def __init__(self, filename):
        self.filename = filename

        f = open(self.filename, "r")
        self.buffer = f.read()
        f.close()

    def get_method_timeslice(self):
        buffer_list = self.buffer.split()
        self.method = buffer_list[0]
        self.timeslice = buffer_list[1]
        return int(self.method), int(self.timeslice)

    def get_processes(self):
        buffer_list = self.buffer.split()
        self.process_list = []
        for p in buffer_list[8:]:
            self.process_list.append(int(p))

        return self.process_list