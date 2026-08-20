# import the datetime module and let's see the current time
import datetime # import the built-in module for date and time
x = datetime.datetime.now() # put in variable the function datetime() and now() to display the current time
print(x)

a = dir(datetime)
print(a)

# return the year and the name of the weekday
print(x.year) # print the year from the variable year in the module
print(x.strftime("%A")) # print the week day in full words no abbreviation into string

# creating date object using the datetime() class in the datetime module
# to creat that it need three parameters
y = datetime.datetime(2020, 5, 17)
print(y)
# note: The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

# the strftime() methode
# methode to formating date time into a readable string
# the strftime take one parameter which is the format to specify the returning format of the output
# let's display the name of the month
z = datetime.datetime(2018, 3, 11)
print(z.strftime("%B"))

'''
A reference of all the legal format codes:
Directive 	Description 	Example 	Try it
%a 	Weekday, short version 	Wed 	
%A 	Weekday, full version 	Wednesday 	
%w 	Weekday as a number 0-6, 0 is Sunday 	3 	
%d 	Day of month 01-31 	31 	
%b 	Month name, short version 	Dec 	
%B 	Month name, full version 	December 	
%m 	Month as a number 01-12 	12 	
%y 	Year, short version, without century 	18 	
%Y 	Year, full version 	2018 	
%H 	Hour 00-23 	17 	
%I 	Hour 00-12 	05 	
%p 	AM/PM 	PM 	
%M 	Minute 00-59 	41 	
%S 	Second 00-59 	08 	
%f 	Microsecond 000000-999999 	548513 	
%z 	UTC offset 	+0100 	
%Z 	Timezone 	CST 	
%j 	Day number of year 001-366 	365 	
%U 	Week number of year, Sunday as the first day of week, 00-53 	52 	
%W 	Week number of year, Monday as the first day of week, 00-53 	52 	
%c 	Local version of date and time 	Mon Dec 31 17:41:00 2018 	
%C 	Century 	20 	
%x 	Local version of date 	12/31/18 	
%X 	Local version of time 	17:41:00 	
%% 	A % character 	% 	
%G 	ISO 8601 year 	2018 	
%u 	ISO 8601 weekday (1-7) 	1 	
%V 	ISO 8601 weeknumber (01-53) 	01

'''
