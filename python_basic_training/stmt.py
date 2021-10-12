#!/bin/python3


def course(money):
				if money >= 1000:
								return " You have registed to your course!"
							
				
				else:
								return " Tou dont have enough amount for this course!"


#print(course(1000))
#print(course(500))


#=================================================

def course(age,money):
						if (age >= 18) and (money >= 13500):
													return " You have registed to your new couse!"
						
						elif	(age >= 18) and (money < 13500):
													return " You dont have enough money for this course!"
						
						elif 	(age < 18) and ( money >= 13500):
													return " You still kid, try next time!"
						else:
						
										return "You dont have enough money and you still young!"


print(course(18,13500))
print(course(18,13000))
print(course(17,13000))



































