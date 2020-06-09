'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. 
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Function Description:
Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):
  s: a string representing time in 12 hour format

Input Format:
A single string s containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM), where 1<=hh<=12 and 0<=mm,ss<=59.

Constraints:
All input times are valid

Output Format:
Convert and print the given time in 24-hour format, where 0<=hh<=23.
'''


import os
import sys

def timeConversion(str1):
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2]     
    elif str1[-2:] == "AM": 
        return str1[:-2]    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2]        
    else:  
        return str(int(str1[:2]) + 12) + str1[2:8] 

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
