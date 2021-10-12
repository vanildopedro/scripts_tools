#!/bin/python3


def nl():
			print('\n')

nl()

courses = ["Cybersecurity Engineer", "Network Engineer", "Help Desk", "Software Engineer"]



print (courses[1]) #this will print the second item,
print (courses[1:3]) #this will not print the last item,
print (courses[0:4])
print (courses[:3])

nl()

print (len(courses))

len_courses = (len(courses))

print (len_courses)


nl()

print (courses)
nl()

courses.append("Vanessa Engineer")
print (courses)

nl()

courses.pop(2)
print (courses)



























