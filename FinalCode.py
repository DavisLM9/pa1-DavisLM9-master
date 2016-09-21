#Programmers: Liam Davis
#Course: CS201.O2, Dr. Olsen
#Date:9/21/16
#Programming Assignment: PA1
#Problem Statement: Calculating the area of a trapezoid
#Data in: The two bases and the height to calculate the area
#Data Out: The area calculated for the dimensions
#Other files needed: NA
#Credits: NA

#Prompt for bases of trapezoid
base1_str= input("Enter base 1 of your trapezoid: ")
base1_int= int(base1_str)
base2_str= input("Enter base 2 of your trapezoid: ")
base2_int= int(base2_str)

#Prompt for height of trapezoid
height_str= input("Enter height of your trapezoid: ")
height_int= int(height_str)

#Apply the area formula to the trapezoid
area= .5*height_int*((base1_int+base2_int))

#Output the area of the trapezoid
print("The area of the trapezoid is: ", area)