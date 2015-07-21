# Everyday Operations

# Check working directory:
# import os
# os.getcwd()


# Run file from sublime
# execfile('pytest.py')




# ----------------------------------------------------------------------
# IF/ELSE/ELIF
# find which number is greater


# a = input("Enter a number\n")
# b = input("Enter another number\n")

# if a > b:
# 	print("First number is higher")
# elif b > a:
# 	print("Second number is higher")
# else:
# 	print("Same number")

# ----------------------------------------------------------------------
# FOR LOOPS
# Find all numbers divisible by 3


# for n in range(1, 100):
# 	if n % 3 == 0:
# 		print(n)
# else:
# 	print("The loop is over")
		
# ----------------------------------------------------------------------
# FOR STATEMENTS
# iterate over a dictionary of actors


# actors = {
#     "Kyle MacLachlan": "Dale Cooper",
#     "Sheryl Lee": "Laura Palmer",
#     "Lara Flynn Boyle": "Donna Hayward",
#     "Sherilyn Fenn" : "Audrey Horne"
# }

# keys = actors.keys()
# values = actors.values()

# for n in range(0, len(actors)):
# 	print(keys[n] + " : " + values[n])

# ----------------------------------------------------------------------
# FOR STATEMENTS
# iterate over a dictionary of actors


# miles_run = 0
# running = True

# while running:
# 	if miles_run <= 10:
# 		print("Still running! On mile {}".format(miles_run))
# 		miles_run += 1
# 	else:
# 		running = False
# else:
# 	print("Whew! I'm tired")


# ----------------------------------------------------------------------
# WHILE STATEMENTS
# Finding when two walkers meet


# walker1 = 0
# walker2 = 102

# while walker1 != walker2:
# 	walker1 += 2
# 	walker2 -= 1
# print walker1

# ----------------------------------------------------------------------
# TRY (DEBUGGING)


# phone_book = {
#     "Sarah Hughes": "01234 567890",
#     "Tim Taylor": "02345 678901",
#     "Sam Smith":  "03456 789012"
# }

# try:
# 	phone_book["Jamie Theakston"]
# except KeyError:
# 	print "That person isn't in the dictionary"

# ----------------------------------------------------------------------
# Counts how many of each number in the number list


# import collections

# number_list = [1,1,2,2,2,2,3,3,4,4,5,5,5,5,5,5,6,7,8,8,8,8,9,9,9,9]
# count_dict = collections.defaultdict(int)
# for i in number_list:
#     count_dict[i] += 1

# ----------------------------------------------------------------------
# Function that adds numbers

# def addition(a, b):
# 	return a + b

# addition(2, 2)

# addition("hi ", "there")

# ----------------------------------------------------------------------
# Functions call each other to log addition of numbers


# from datetime import datetime
# import logging

# def log_handler(msg):
#     """Sends msg to the logging platform"""
#     date = str(datetime.now())
#     msg = date + " - " + msg
#     return logging.info(msg)

# def log(msg):
#     """A convenience function. Adds msg to the logs with log_handler"""
#     msg = str(msg)
#     print("Message logged: " + msg)
#     return log_handler(msg)

# def addition(a, b):
#     """Adds two numbers and logs the result"""
#     x = a + b
#     log("Adding {0} and {1} = {2}.".format(a, b, x))
#     return x

# addition(1, 2)
# addition(2, 3)
# addition(5, addition(3, 5))

# ----------------------------------------------------------------------
# L1;P5 - Make cake using tuples


# ingredients = {
#     "butter"  : ("butter", 118.3),
#     "sugar"   : ("sugar", 236.6),
#     "vanilla" : ("vanilla", 4.929),
#     "eggs"    : ("eggs", 2), # whole eggs
#     "cocoa"   : ("cocoa", 118.3),
#     "flour"   : ("flour", 118.3)
# }

# # The butter was refrigerated, so it's not soft yet.
# butter_soft = False

# bowl = []

# # To make the cake, we'll need the following functions
# def melt(this):
#     print("Melting {0}.".format(this))

# def bake(this, temp):
#     print("Baking {0} at {1}.".format(this, temp))

# def mix(this):
#     print("Mixing {0}.".format(this))

# def add_to_bowl(ingredient):
#     print("Adding {0} to the bowl.".format(ingredient))
#     return bowl.append(ingredient)


# ##### Start the algorithm! #####

# if butter_soft != True:
#     melt(ingredients["butter"][0])
#     butter_soft = True

# add_to_bowl(ingredients["butter"][0])
# add_to_bowl(ingredients["sugar"][0])

# mixing_time = 0
# mixture_creamy = False

# # Mix until creamy
# while mixture_creamy == False:
#     mix(bowl)
#     mixing_time += 1
#     if mixing_time == 3:
#         # After 3 minutes, the mixture will be creamy,
#         # and our while loop will stop
#         mixture_creamy = True

# add_to_bowl(ingredients["eggs"][0])
# add_to_bowl(ingredients["vanilla"][0])

# mix(bowl)

# add_to_bowl(ingredients["cocoa"][0])
# add_to_bowl(ingredients["flour"][0])

# mixing_time = 0
# well_blended = False

# # Mix until well-blended
# while well_blended == False:
#     mix(bowl)
#     mixing_time += 1
#     if mixing_time == 4:
#         well_blended = True

# # In cooking terms: pour contents of the bowl into a cake pan
# # In Python terms: redefine the bowl variable as cake_pan
# cake_pan = bowl

# cooking_temp = 350
# cooking_time = 30

# for minute in range(0, cooking_time):
#     bake(cake_pan, cooking_temp)

# print("Cake is done!")


# ----------------------------------------------------------------------
# L1;P5 - Fibonacci


# a = 1
# b = 1
# count = 3
# iterations = int(input("How many iterations should we make?\n"))

# print ("1: {0}".format(a))
# print ("2: {0}".format(b))
# for n in range(0, iterations-2):
# 	c = a + b
# 	print ("{0}: {1}".format(count, c))
# 	count += 1
# 	a = b
# 	b = c

# ----------------------------------------------------------------------
# L1;P5 - Fibonacci (thinkful method)

# def F(n):
# 	if n < 2:
# 		return n
# 	else:
# 		return F(n-2) + F(n-1)

# ----------------------------------------------------------------------
# L1;P5 - FizzBuzz

# Method 1

# count = 0
# while (count < 101):
#     if (count % 5) == 0 and (count % 3) == 0:
#         print "FizzBuzz"
#         count = count +1
#     elif (count % 3) == 0:
#         print "Fizz"
#         count = count + 1
#     elif (count % 5) == 0:
#         print "Buzz"
#         count = count +1
#     else:
#         print count
#         count = count + 1

# # Method 2

# for i in range(1,101): print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i)

# # Method 3

# for i in xrange(1, 101):
#     if i % 15 == 0:
#         print "FizzBuzz"
#     elif i % 3 == 0:
#         print "Fizz"
#     elif i % 5 == 0:
#         print "Buzz"
#     else:
#         print i



# ----------------------------------------------------------------------
# L1;P6 - Reading CSV

# import collections

# # with open('/Users/Takeo/Desktop/Python/gdpData.csv','rU') as inputFile:
# #     header = next(inputFile)
# #     for line in inputFile:
# #             print line

# # Print entire table without headers
# # with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
# #     header = next(inputFile)		#tells program that there is a header
# #     for line in inputFile:			
# #     	line = line.rstrip().split(',')	# splits into separate columns with commas and a space in between
# # 	    print line


# # Prints lines with "Total National Population" in the second column
# population_dict = collections.defaultdict(int)		# creates an empty dictionary
# with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
#     header = next(inputFile)
#     for line in inputFile:
#         line = line.rstrip().split(',')				# splits the lines into columns
#         line[5] = int(line[5])						# converts line 5 from a string to an int
#         if line[1] == 'Total National Population':	
#         	#print line[0], line[5], type(line[5])	# prints the first column, the 6ths column, and the types of the columns
#         	population_dict[line[0]] += line[5]		# creates dictionary using the 6th column


# with open('national_population.csv','w') as outputFile:
#     outputFile.write('continent,2010_population\n')
#     for k,v in population_dict.iteritems():			# iterates through each key-value pair, assigns key to variable k, assigns variable v to values
#         outputFile.write(k + ',' + str(v) + '\n')	# k is key, puts a comma in between, then converts values to strings, '\n' denotes new line


# Prints lines that have "Africa" in the first column
# with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
#     header = next(inputFile)		#tells program that there is a header
#     for line in inputFile:			
#     	line = line.rstrip().split(',')	# splits into separate columns
#     	if line[0] == 'Africa':
# 	        print line


# Print headers
# header = header.rstrip().split(',')


# ----------------------------------------------------------------------
# L1;P7 - Pandas



##### Old Method #####

# Reads file and splits by commas
# with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
#     for line in inputFile:
#         line = line.rstrip().split(',')
#         print line

# Counts the number of elemnts in each row
# with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
#     for line in inputFile:
#         line = line.rstrip().split(',')
#         print len(line)

# Can be used to count the number of characterst in the elements of a list
# for i in range(len(my_list)): 
#     print my_list[i]

##### CSV method #####

# import csv

# Automatically splits lines
# with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','r') as inputFile:
#     inputReader = csv.reader(inputFile)
#     for line in inputReader:
#         print line

# Counts number of characters
# with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','r') as inputFile:
#     inputReader = csv.reader(inputFile)
#     for line in inputReader:
#         print len(line)


##### Pandas #####

# import pandas as pd

# input_dataframe = pd.read_csv('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv')

# # input_dataframe['Continent']
# input_dataframe[0:10]

# ----------------------------------------------------------------------
# L3;P2 - pySQlite fetching


# # The sqlite3 module is used to work with the SQLite database.
# import sqlite3 as lite

# # Here you connect to the database. The `connect()` method returns a connection object.
# con = lite.connect('getting_started.db')

# with con:
#   # From the connection, you get a cursor object. The cursor is what goes over the records that result from a query.
#   cur = con.cursor()    
#   cur.execute('SELECT SQLITE_VERSION()')
#   # You're fetching the data from the cursor object. Because you're only fetching one record, you'll use the `fetchone()` method. If fetching more than one record, use the `fetchall()` method.
#   data = cur.fetchone()
#   # Finally, print the result.
#   print "SQLite version: %s" % data


# execute() can execute any SQLite commands that you want
# fetchone() or fetchall() can fetch results and store as an object


# ----------------------------------------------------------------------
# L3;P2 - pySQlite inserting data


##### in SQLite #####
# CREATE TABLE newWeather AS
# SELECT City, Year, Warm_month, Cold_month FROM weather;



# import sqlite3 as lite

# con = lite.connect('getting_started.db')

# # Inserting rows by passing values directly to `execute()`
# with con:

#     cur = con.cursor()
#     cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
#     cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
#     cur.execute("INSERT INTO newWeather VALUES('Washington', 2013, 'July', 'January')")
#     cur.execute("INSERT INTO newWeather VALUES('Houston', 2013, 'July', 'January')")

# ----------------------------------------------------------------------
# L3;P2 - pySQlite inserting data as tuples


# import sqlite3 as lite

# cities = (('Las Vegas', 'NV'),
#                     ('Atlanta', 'GA'))

# newWeather = (('Las Vegas', 2013, 'July', 'December'),
#                      ('Atlanta', 2013, 'July', 'January'))

# con = lite.connect('getting_started.db')

# # Inserting rows by passing tuples to `execute()`
# with con:

#     cur = con.cursor()
#     cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
#     cur.executemany("INSERT INTO newWeather VALUES(?,?,?,?)", newWeather)


# ----------------------------------------------------------------------
# L3;P2 - pySQlite retrieving data

# import sqlite3 as lite

# con = lite.connect('getting_started.db')

# with con:    

#     cur = con.cursor()    
#     cur.execute("SELECT * FROM cities")

#     rows = cur.fetchall()

#     for row in rows:
#         print row


##### Import as a dataframe using pandas #####

# import sqlite3 as lite
# import pandas as pd

# con = lite.connect('getting_started.db')

# # Select all rows and print the result set one row at a time
# with con:

#   cur = con.cursor()
#   cur.execute("SELECT * FROM cities")

#   rows = cur.fetchall()
#   df = pd.DataFrame(rows)



import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

# Select all rows and print the result set one row at a time
with con:

  cur = con.cursor()
  cur.execute("SELECT * FROM cities")


  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]  # retrieves column names
  df = pd.DataFrame(rows, columns=cols)

# retrieve by calling eh variables df/rows/cols









