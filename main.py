#!/usr/bin/env python3
import csv
from datetime import date
import time
from datetime import datetime
csvfile = open('tracker.csv', 'a',newline='\n')
c = csv.writer(csvfile)
data=[]
today_date=date.today()
data.append(today_date)
activity=input("Enter the activity you are going to do \n")
data.append(activity)
start_time=time.strftime("%H:%M:%S", time.localtime())
a=input("Press enter after completing the work")
end_time=time.strftime("%H:%M:%S", time.localtime())
start = datetime.strptime(start_time, "%H:%M:%S") 
end = datetime.strptime(end_time, "%H:%M:%S") 
difference = end - start 
data.append(start_time)
data.append(end_time)
data.append(difference)
seconds = difference.total_seconds() 
minutes = round(seconds / 60,2)
data.append(minutes)
print(f'Start time is {start_time} \n')
print(f'Your stop time is {end_time} \n')
print(f'You had worked for \n{minutes} minutes')
# write a column headings row - do this only once -
desc=input("Do you want to add this data ? [Y/n]\n")
if(desc=='Y' or desc=='y'):
    c.writerow(data)
    print("Data is added to the sheet")
# save and close the file
    csvfile.close()
else:
    print("Data is not added")
    csvfile.close()


