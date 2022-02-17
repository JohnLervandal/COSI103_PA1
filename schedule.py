'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def sort(self,field):
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        else:
            print("can't sort by "+str(field)+" yet")
            return self

    def limit(self, limit):
        ''' limit filters the courses by limit of class (created by Fritz)'''
        return Schedule(tuple([course for course in self.courses if course['limit'] == limit]))

    def title(self, phrase):
        '''search the course list to find phrase in title(created by Pedro)'''
        return Schedule([c for c in self.courses if phrase in c['name']])
        
    def description(self, phrase):
        '''search the course list to find phrase in description(created by Pedro)'''
        return Schedule([c for c in self.courses if phrase in c['description']])

    def independent(self, phrase):
        '''search the course list to find phrase in description(created by Pedro)'''
        return Schedule([c for c in self.courses if phrase == c['independent_study']])
