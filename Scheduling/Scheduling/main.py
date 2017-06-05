#	Operating System - CPU scheduling v1.2
#
#   -> main.py
#   - Input.py
#   - myHeap.py
#   - Method.py
#   - mySchedule.py
#   - myProcess.py
#
#	Created by ShauShian, Chiang on 2017/06/01.
#	Copyright © 2017 ShauShian, Chiang. All rights reserved.

from mySchedule import mySchedule
from myProcess import myProcess
from Method import *
import copy
from Input import *

filename = input('Enter filename:')
inputFile = InputFile( filename )

p_method, p_slice = inputFile.get_method_timeslice()
process_list = inputFile.get_processes()

p_list = []
for p in range(int(len(process_list)/4)):
    s = p*4
    myprocess = myProcess(process_list[s],
                          process_list[s+1],
                          process_list[s+2],
                          process_list[s+3]
                          )

    p_list.append(myprocess)

p_list = sorted(p_list, key = lambda p: p.pid)

if p_method == 1 or p_method == 6:
    fcfs_ls = copy.deepcopy(mySchedule.sort_by_what(p_list, 1))
    fcfs = FCFS(fcfs_ls)
    fcfs.start_scheduling(p_slice)
    fcfs.finished_ls = sorted(fcfs.finished_ls, key = lambda p: p.pid)

if p_method == 2 or p_method == 6:
    rr_ls = copy.deepcopy(p_list)
    rr = RR(rr_ls)
    rr.start_scheduling(p_slice)
    rr.finished_ls = sorted(rr.finished_ls, key = lambda p: p.pid)

if p_method == 4 or p_method == 6:
    npsjf_ls = copy.deepcopy(p_list)
    npsjf = NPSJF(npsjf_ls)
    npsjf.start_scheduling(p_slice)
    npsjf.finished_ls = sorted(npsjf.finished_ls, key = lambda p: p.pid)

if p_method == 3 or p_method == 6:
    psjf_ls = copy.deepcopy(p_list)
    psjf = PSJF(psjf_ls)
    psjf.start_scheduling(p_slice)
    psjf.finished_ls = sorted(psjf.finished_ls, key = lambda p: p.pid)

if p_method == 5 or p_method == 6:
    pp_ls = copy.deepcopy(p_list)
    pp = PP(pp_ls)
    pp.start_scheduling(p_slice)
    pp.finished_ls = sorted(pp.finished_ls, key = lambda p: p.pid)




method = {1:'FCFS', 2:'RR', 3:'PSJF', 4:'Non-PSJF', 5:'Priority'}
gantt = {}
if p_method == 1 or p_method == 6:
    gantt[1] = fcfs.gantt
if p_method == 2 or p_method == 6:
    gantt[2] = rr.gantt
if p_method == 3 or p_method == 6:
    gantt[3] = psjf.gantt
if p_method == 4 or p_method == 6:
    gantt[4] = npsjf.gantt
if p_method == 5 or p_method == 6:
    gantt[5] = pp.gantt

g_plot = ''
for m in range(1, 6):
    if m == p_method or p_method == 6 :
        g_plot += '=={0:>8}==\n'.format(method[m])
        g_plot += '-'
        Hex2Dec = '0123456789ABCDEFGHIJKLMNOPQRSTUVWKYZ'
        for g in gantt[m]:
            g_plot += Hex2Dec[g]
        g_plot += '\n'
print(g_plot)

waiting_time = '='*59 + '\n'
waiting_time += '\nWaiting Time\n{0:<8}{1:<8}{2:<8}{3:<8}{4:<8}{5:<8}\n'.format('ID', 'FCFS', 'RR', 'PSJF', 'NPSJF', 'Priority' )
waiting_time += '='*59 + '\n'

for p in range(len(p_list)):
    waiting_time += '{0:<8}'.format(p_list[p].pid)
    if p_method == 1 or p_method == 6:
        waiting_time += '{0:<8}'.format(fcfs.finished_ls[p].waitting_time)
    else:
        waiting_time += ' '*8
    if p_method == 2 or p_method == 6:
        waiting_time += '{0:<8}'.format(rr.finished_ls[p].waitting_time)
    else:
        waiting_time += ' '*8
    if p_method == 3 or p_method == 6:
        waiting_time += '{0:<8}'.format(psjf.finished_ls[p].waitting_time)
    else:
        waiting_time += ' '*8
    if p_method == 4 or p_method == 6:
        waiting_time += '{0:<8}'.format(npsjf.finished_ls[p].waitting_time)
    else:
        waiting_time += ' '*8
    if p_method == 5 or p_method == 6:
        waiting_time += '{0:<8}'.format(pp.finished_ls[p].waitting_time)
    else:
        waiting_time += ' '*8
    waiting_time += '\n'

print(waiting_time)

turnaround_time = '='*59 + '\n'
turnaround_time += '\nTurnaround Time\n{0:<8}{1:<8}{2:<8}{3:<8}{4:<8}{5:<8}\n'.format('ID', 'FCFS', 'RR', 'PSJF', 'NPSJF', 'Priority' )
turnaround_time += '='*59 + '\n'

for p in range(len(p_list)):
    turnaround_time += '{0:<8}'.format(p_list[p].pid)
    if p_method == 1 or p_method == 6:
        turnaround_time += '{0:<8}'.format(fcfs.finished_ls[p].turnaround_time)
    else:
        turnaround_time += ' '*8
    if p_method == 2 or p_method == 6:
        turnaround_time += '{0:<8}'.format(rr.finished_ls[p].turnaround_time)
    else:
        turnaround_time += ' '*8
    if p_method == 3 or p_method == 6:
        turnaround_time += '{0:<8}'.format(psjf.finished_ls[p].turnaround_time)
    else:
        turnaround_time += ' '*8
    if p_method == 4 or p_method == 6:
        turnaround_time += '{0:<8}'.format(npsjf.finished_ls[p].turnaround_time)
    else:
        turnaround_time += ' '*8
    if p_method == 5 or p_method == 6:
        turnaround_time += '{0:<8}'.format(pp.finished_ls[p].turnaround_time)
    else:
        turnaround_time += ' '*8
    turnaround_time += '\n'

print(turnaround_time)

try:
    filename_num = str(list(filter(str.isdigit, filename))[0])
except:
    filename_num = ''

with open("output" + filename_num + ".txt", "w") as f:
    f.write(g_plot)
    f.write(waiting_time)
    f.write(turnaround_time)

input("Press Enter to continue...")