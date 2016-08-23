# Python Scheduler 5000 (Python 2.7)

Reads in a file containing courses and their times and then creates every possible valid schedule
At the bottom of the courses.txt file, an integer should be on the last line to indicate the number of classes necessary in the schedule

The file format should resemble the following:

```
CAP5512 T12:00-13:15 R12:00-13:15  
COP4331 T18:00-19:15 R18:00-19:15  
COP4331L F14:30-15:20  
COP4331L F15:30-16:20  
COP4600 M18:00-19:15 W18:00-19:15  
STA3032 M16:30-17:45 W16:30-17:45  
STA3032 T18:00-19:15 R18:00-19:15  
STA3032 T9:00-10:15 R9:00-10:15  
5  
```
Where in this example, there are 5 courses, 4 lectures and a lab section denoted by the "L" at the end of the course number

Use military time and the weekday prefixes of M, T, W, R, F
