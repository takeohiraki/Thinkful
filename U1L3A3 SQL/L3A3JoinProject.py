# Run in terminal by navigating to the directory with getting_started.db, and L3A3JoinProject.
# enter the python and execute the file using:      execfile('L3A3JoinProject')


########## Part 1: Creating the SQL tables using Python/Pandas ##########


import sqlite3 as lite
import pandas as pd

weather = (('Boston', 2013, 'July', 'January', 59),
	('Chicago', 2013, 'July', 'January', 59),
	('Miami', 2013, 'August', 'January', 84),
	('Dallas', 2013, 'July', 'January', 77),
	('Seattle', 2013, 'July', 'January', 61),
	('Portland', 2013, 'July', 'December', 63),
	('San Francisco', 2013, 'July', 'December', 64),
	('Los Angeles', 2013, 'September', 'December', 75))

cities = (('Boston', 'MA'),
	('Chicago', 'IL'),
	('Miami', 'FL'),
	('Dallas', 'TX'),
	('Seattle', 'WA'),
	('Portland', 'OR'),
	('San Francisco', 'CA'),
	('Los Angeles', 'CA'))

# Creates connection to the database called "getting_started.db")
con = lite.connect('getting_started.db')

with con:

# Detects whether "weather" or "cities" tables exist, and deletes them if they exist
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS weather")
	cur.execute("DROP TABLE IF EXISTS cities")

# Creates "weather" and "cities" tables	
	cur.execute("CREATE TABLE weather (City text, Year integer, Warm_month text, Cold_month text, Average_high integer)")
	cur.execute("CREATE TABLE cities (name text, state text)")

# Takes values from "weather" and "cities", as defined above, and inserts values into the tables
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)

# Joins the weather and cities tables on the name of the city
  	cur.execute("SELECT weather.City, cities.state, weather.Year, weather.Warm_month, weather.Cold_month, weather.Average_high FROM weather LEFT OUTER JOIN cities ON weather.city = cities.name")

# Cretaes data table with Pandas
  	rows = cur.fetchall()
  	cols = [desc[0] for desc in cur.description]  # retrieves column names
  	df = pd.DataFrame(rows, columns=cols)

  	df['City'] = df['City'].astype(str)
  	df['state'] = df['state'].astype(str)

########## Part 2: Pulling certain information from the data tables ##########

# Creates empty vectors 
JulyCity, JulyState, AugustCity, AugustState, SeptemberCity, SeptemberState = [], [], [], [], [], []

# Sorts into months
for i in range(0, len(df["City"])):
	if df["Warm_month"][i] == "July":
		JulyCity.append(df["City"][i])
		JulyState.append(df["state"][i])
	elif df["Warm_month"][i] == "August":
		AugustCity.append(df["City"][i])
		AugustState.append(df["state"][i])
	else:
		SeptemberCity.append(df["City"][i])
		SeptemberState.append(df["state"][i])

# Prints the results by providing the cities that are warmest in each month
print("The cities that are warmest in July are:")
for i in range(0, len(JulyCity)):
	print("{0}, {1}".format(JulyCity[i], JulyState[i]))

print("\n The cities that are warmest in August are:")	
for i in range(0, len(AugustCity)):
	print("{0}, {1}".format(AugustCity[i], AugustState[i]))

print("\n The cities that are warmest in September are:")	
for i in range(0, len(SeptemberCity)):
	print("{0}, {1}".format(SeptemberCity[i], SeptemberState[i]))



