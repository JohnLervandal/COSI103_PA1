'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
testing123
'''
import sys
from schedule import Schedule


schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
limit (filter by capacity of a class)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
online(see what classes are online depending on subject)
email(filter by email)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:
        command = input(">> (h for help) ")
        if command == 'quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        elif command in ['l','limit']:
            ''' created by Fritz'''
            limit = int(input("enter a limit: "))
            schedule = schedule.limit(limit)
        elif command in ['d', 'description']:
            '''created by Pedro'''
            phrase = input("enter a phrase: ")
            schedule = schedule.description(phrase)
        elif command in ['i', 'title']:
            '''created by Pedro'''
            phrase = input("enter a phrase: ")
            schedule = schedule.title(phrase)
        elif command in ['in', 'independent']:
            '''created by Pedro'''
            phrase = input("Are you searching for independent studies? <y/n>")
            if phrase == 'y':
                val = True
            elif phrase == 'n':
                val = False
            schedule = schedule.independent(val)
        elif command in ['st', 'status']:
            '''created by Matthew'''
            status = input("Open or Closed?")
            schedule = schedule.state(status)
        elif command in ['o', 'online']:
            '''created by John'''
            major = input("Select A Major: ")
            schedule = schedule.subject(major).description("online")
        elif command in ['e','email']:
            print("hello")
            input1 = input("Enter email")
            schedule = schedule.email(input1)
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''print_course prints a brief description of the course'''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()