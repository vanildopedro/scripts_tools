#!/bin/python3


def nl():
			print('\n')

nl()
			
registration = {"courses": "Cybersecurity","price": 13500, "year": 2020}

print (registration)

nl()

course = registration["courses"]


print ("You are registed to ", course, " Welcome")

################################################

nl()


for cour in registration.values():
							print (cour)









