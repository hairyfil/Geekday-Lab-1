import os
from flask import Flask



file = open("sessions.txt","r")
Page_Mid = ""

for line in file.readlines():
    print line
    currentline = line.split(",")
    Page_Mid += "<TR>\n"
    Page_Mid += "<TD>" + currentline[0] + "</TD>\n"
    Page_Mid += "<TD>" + currentline[1] + "</TD>\n"
    Page_Mid += "<TD>" + currentline[2] + "</TD>\n"
    Page_Mid += "<TD>" + currentline[3] + "</TD>\n"
    Page_Mid += "<TD>" + currentline[4] + "</TD>\n"

Page_Mid += "</TR></TABLE>\n"

print Page_Mid
file.close()
