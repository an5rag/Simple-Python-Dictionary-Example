__author__ = 'Anurag'

##
# Dictionaries in python are representations of hash maps in Python.
# Using a simple example in which we play with course-offerings at UIUC for Fall and Spring
# semesters, I shall illustrate their application.
##

fall_file = open('fall.txt')
spring_file = open('spring.txt')

fall_dictionary = dict()
spring_dictionary = dict()


# split individual space-separatd-words in the first line of the Fall file into an python list
course = fall_file.readline().split()

# construct fall_dictionary
while(course):
    course_number = course[0]
    course_name = ' '.join(course[1:])
    course = fall_file.readline().split()
    fall_dictionary[course_number] = course_name

# split individual space-separatd-words in the first line of the Spring file into an python list
course = spring_file.readline().split()

# construct spring_dictionary
while(course):
    course_number = course[0]
    course_name = ' '.join(course[1:])
    course = spring_file.readline().split()
    spring_dictionary[course_number] = course_name

both_spring_and_fall = dict()

# make a temporary dictionary to avoid changing size (by popping/adding) in the loop that follows
fall_only = dict()

# loop to remove overlapping courses from both dictionaries and adding the intersecting elements to
# both_spring_and_fall dictionary
for course_number in fall_dictionary:
    if course_number in spring_dictionary:
        both_spring_and_fall[course_number] = fall_dictionary[course_number]
        spring_dictionary.pop(course_number)
    else:
        fall_only[course_number] = fall_dictionary[course_number]

# pointing the unchanged dictionary to the updated fall_only dict
fall_dictionary = fall_only

print("\nCourses offered only in Spring: ")
for key in sorted(spring_dictionary):
    print(key + " " + spring_dictionary[key])

print("\nCourses offered only in Fall: ")
for key in sorted(fall_dictionary):
    print(key + " " + fall_dictionary[key])

print("\nCourses offered both in Spring and Fall: ")
for key in sorted(both_spring_and_fall):
    print(key + " " + both_spring_and_fall[key])
