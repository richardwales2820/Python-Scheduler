import datetime

class Course(object):
    def __init__(self, times, name):
        self.times = times
        self.name = name
        self.numToDay = {1:'M', 2:'T', 3:'W', 4:'R', 5:'F'}

    def printCourse(self):
        print self.name
        for day, time in self.times.items():
            print self.numToDay[day], time
        print

    def valid(self, otherCourse):
        if self.name == otherCourse.name:
            return False

        for day in self.times:
            start = self.times[day][0]
            end = self.times[day][1]
            for otherDay in otherCourse.times:
                oStart = otherCourse.times[otherDay][0]
                oEnd = otherCourse.times[otherDay][1]
                if day == otherDay:
                    if not (start > oEnd or oStart > end):
                        return False
        return True
                    


def importClasses(classes):
    """
    classes[]: list of strings. Course code, then days and times space separated
    ex: COP3502 M9:30-10:20 W9:30-10:20 
    """
    courses = []
    weekdayDict = {'M':1, 'T':2, 'W':3, 'R':4, 'F':5}
    for course in classes:
        splitStr = course.split()
        name = splitStr[0]
        times = {}

        for i in xrange((len(splitStr)-1)/2 + 1):
            courseTime = splitStr[1 + i]
            weekday = weekdayDict[courseTime[0]]

            startTime = int(courseTime[1:courseTime.find(':')]) * 100 \
            + int(courseTime[courseTime.find(':') + 1:courseTime.find('-')])
            endTime = int(courseTime[courseTime.find('-')+1:courseTime.find(':', 5)]) * 100 + \
            int(courseTime[courseTime.find(':', 5) + 1:])
            times[weekday] = (startTime, endTime)
        newCourse = Course(times, name)
        courses.append(newCourse)

    return courses

memo = [[]]
def findMatches(courses, index, chosenCourses, numCourses):
    if len(chosenCourses) == numCourses and chosenCourses not in memo:
        memo.append(list(chosenCourses))
        drawWeek(numCourses, chosenCourses)

    if index == len(courses):
        return
    
    valid = True
    for course in chosenCourses:
        if not course.valid(courses[index]):
            valid = False
    findMatches(courses, index + 1, chosenCourses, numCourses)
    
    if valid:
        chosenCourses.append(courses[index])
        findMatches(courses, index + 1, chosenCourses, numCourses)
        chosenCourses.remove(courses[index])        

def drawWeek(numClasses, courses):
    # Initializes NxN array of empty strings
    table = ["" for x in xrange((numClasses*2)**2)]
    startTimes = sorted([course.times.values()[0][0] for course in courses])
    timeToIndex = {}
    for x in xrange(numClasses):
        timeToIndex[startTimes[x]] = x

    for course in courses:
        days = course.times.keys()
        for day in days:
            listIndex = (day-1) + numClasses * timeToIndex[course.times[day][0]]*2
            table[listIndex] = course.name
            table[listIndex+numClasses] = "%2d:%02d -%2d:%02d" %(course.times[day][0]/100 - \
            12*(0 if course.times[day][0]/100 <= 12 else 1), course.times[day][0]%100, course.times[day][1]/100 - \
            12*(0 if course.times[day][1]/100 <= 12 else 1), course.times[day][1]%100) 
    cal = """#################################################################################################\n"""
    cal += """#{:^18}#{:^18} #{:^18}#{:^18}#{:^18}#\n""".format("Mon", "Tues", "Wed", "Thur", "Fri")
    cal += """#################################################################################################\n""" + \
"""#{:^18}#{:^18} #{:^18}#{:^18}#{:^18}#
#{:^18}#{:^18} #{:^18}#{:^18}#{:^18}#
#################################################################################################
""" * numClasses
    print cal.format(*table)
    print "\n"

if __name__ == '__main__':
    classes = None
    with open('courses.txt') as f:
        classes = f.readlines()
    numClasses = int(classes[-1])
    del classes[-1]
    courses = importClasses(classes)
    findMatches(courses, 0, [], numClasses)