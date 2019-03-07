# Created by: Adam Linco
# Created on: March 5 2019
# Created for: ICS3U
# Daily Assignment  Unit 3-04
# This code determines if it is a leap year 


from tkinter import *

year=int(input("Enter a year:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("this year is a leap year")
else:
    print("this is not a leap year")   
