#!/usr/bin/python
import os,operator
import datetime,time
from os import walk

print ''' Choose the relevant number to proceed with 
      the action required.
      
      1. Sort all files in descending order based on their size
      2. Sort all files in ascending  order based on their size
      3. Sort files based on last modified date (Earliest as Last)
      4. Sort files based on last modified date (Latest as Last)'''


is_valid=0

while not is_valid :
        try :
                choice = int ( raw_input('Enter your choice [1-4] : ') )
                if choice == 1:
                 print ("Choice 1...")
                 is_valid = 1
                elif choice == 2:
                 print ("Choice 2...")
                 is_valid = 1
                elif choice == 3:
                 print ("Choice 3...")
                 is_valid = 1
                elif choice == 4:
                 print ("Choice 4...")
                 is_valid = 1
                else:
                 print ("Invalid Choice. Try again...")
        except ValueError, e :
                print ("Invalid Choice. Try again...")


is_valid1 = 0
print ''' Choose 1 to run the program on Current Working Directory 
       else enter any other directory
      (Please note the program searched all the specified
      directory and corresponding sub-directories)'''
while not is_valid1 :
    try :
        choicedir = raw_input('Enter your choice : ')

        if choicedir == "1":
         print ("Choice 1...")
         is_valid1 = 1
         choicedir= os.getcwd()
        else:
         print choicedir               
         if os.path.isdir("%s"%choicedir):
          print "Valid Directory",choicedir
          is_valid1 = 1
         else:
          print ("Invalid Directory. Try again...")
    except ValueError, e :
    	print ("Invalid Directory. Try again...") 


def byte_converter(size):
   if size >= 1024*1024*1024:
    unit = "Gb"
    size /= 1024*1024*1024
   elif size >= 1024*1024:
    unit = "Mb"
    size /= 1024*1024
   elif size >= 1024:
    unit = "Kb"
    size /= 1024
   else:
    unit = "b"
   return ("%.2f"%size +" "+ unit)

def formatTime(modified):
	return time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(modified))
	
	
	  
MyDict = {}
MyDict2 = {}
for path, subdirs, files in os.walk(choicedir):
    for name in files:
    	f = os.path.join(path, name)
        if not os.path.islink(f):
            modified = os.path.getmtime(f)
            size = float(os.path.getsize(f))
            MyDict[f] = size
            MyDict2[f] = modified


if choice == 1: 
	sorted_data = sorted(MyDict.iteritems(), key=operator.itemgetter(1), reverse=False)

if choice == 2:
	sorted_data = sorted(MyDict.iteritems(), key=operator.itemgetter(1), reverse=True) 

if choice == 3:
	sorted_data = sorted(MyDict2.iteritems(), key=operator.itemgetter(1), reverse=True)

if choice == 4:
	sorted_data = sorted(MyDict2.iteritems(), key=operator.itemgetter(1), reverse=False)
	

if (choice == 1 or choice == 2):
    for f, size in sorted_data:
    	print f,byte_converter(size)

if (choice == 3 or choice == 4):
    for f, modified in sorted_data:
     print f,formatTime(modified)
