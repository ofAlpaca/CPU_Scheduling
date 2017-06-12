# CPU_Scheduling
Simulate five types of CPU scheduling
## What is it ?
In this project, I'm going to demostrate the five different scheduling methods including FCFS, RR, PSJF, NPSJF and PP.
## Example
### Input.txt
```
6    2 
ID     CPU Burst  Arrival Time   Priority
 12         6        15           1
  7         4         2           8
  1         4         9          12
 11         6        36          11
  2         1         1          11
  6         7        39           5
  8         7        23           4
  3         1         6           1
  4         3         6          12
 13         9        13           8
  0         7        16           7
  9         5         1           3
  5         4        22           6
 10         2        26           5
```

The integer on the very top-left is the method of scheduling we are going to do.
- 1 means FirstComeFirstServe
- 2 means RoundRobin
- 3 means PreemptiveShortestJobFirst
- 4 means NonPreemptiveShortestJobFirst
- 5 means PreemptivePriority
- 6 means do all of them

The next integer is time slice.

And the following is the process attribures.
### Output.txt
```
==    FCFS==
-299999777734441111DDDDDDDDDCCCCCC000000055558888888AABBBBBB6666666
==      RR==
-297979347914791D4C01DC015D8C0A5D8C0A5D8CB056D8CB06D8B06D8B6D8B6B66
==    PSJF==
-277773444111199999CCCCCC5AA5550000000BBBBBB88888886666666DDDDDDDDD
==Non-PSJF==
-277773444111199999CCCCCC5555AA0000000BBBBBB88888886666666DDDDDDDDD
==Priority==
-999993777724DDCCCCCC058888888AA5550000666666600DDDDDDDBBBBBB111144
===========================================================

Waiting Time
ID      FCFS    RR      PSJF    NPSJF   Priority
===========================================================
0       18      32      15      15      25      
1       6       12      1       1       52      
2       0       0       0       0       10      
3       5       1       0       0       0       
4       6       9       1       1       58      
5       19      18      5       3       9       
6       21      21      12      12      0       
7       5       8       0       0       5       
8       22      32      21      21      0       
9       1       9       13      13      0       
10      26      9       0       3       4       
11      18      23      2       2       19      
12      13      27      4       4       0       
13      6       39      45      45      33      
===========================================================

Turnaround Time
ID      FCFS    RR      PSJF    NPSJF   Priority
===========================================================
0       25      39      22      22      32      
1       10      16      5       5       56      
2       1       1       1       1       11      
3       6       2       1       1       1       
4       9       12      4       4       61      
5       23      22      9       7       13      
6       28      28      19      19      7       
7       9       12      4       4       9       
8       29      39      28      28      7       
9       6       14      18      18      5       
10      28      11      2       5       6       
11      24      29      8       8       25      
12      19      33      10      10      6       
13      15      48      54      54      42      
```
- The first part is gantt chart.
- The second part is waiting time and turnaround time of every processes.
