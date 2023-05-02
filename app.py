from helper import helper
from datetime import datetime
import mysql.connector
import random

tracks = helper.data_cleaner("circuits.csv")
contructors = helper.data_cleaner("constructors.csv")
races = helper.data_cleaner("races.csv")
#lapTimes = helper.data_cleaner("lapTimes.csv")
drivers = helper.data_cleaner("drivers.csv")
#results = helper.data_cleaner("results.csv")

currentID = 0

# establish the connection 
connection = mysql.connector.connect(host="localhost",
user="root",
password="cpsc408!",
auth_plugin='mysql_native_password',
database = 'Formula1')

# create a cursor object using the connection 
cursor = connection.cursor()

def create_tables():
        tracks = '''
            CREATE TABLE tracks(
                trackID INTEGER NOT NULL PRIMARY KEY,
                trackRef VARCHAR(50),
                name VARCHAR(50),
                location VARCHAR(50),
                country VARCHAR(50),
                latitude VARCHAR(50),
                longitude VARCHAR(50),
                url VARCHAR(100)
            );
        '''

        teams = '''
            CREATE TABLE teams(
                teamID INTEGER NOT NULL PRIMARY KEY,
                name VARCHAR(50),
                nationality VARCHAR(50),
                url VARCHAR(100)
            );
        '''
        drivers = '''
            CREATE TABLE drivers(
                driverID INTEGER NOT NULL PRIMARY KEY,
                driverRef VARCHAR(50),
                number INTEGER,
                code VARCHAR(3),
                forename VARCHAR(50),
                surname VARCHAR(50),
                dob VARCHAR(50),
                nationality VARCHAR(50),
                url VARCHAR(50)
            );
        '''


        races = '''
            CREATE TABLE races(
                raceID INTEGER NOT NULL PRIMARY KEY,
                year INTEGER,
                round INTEGER,
                trackID INTEGER NOT NULL,
                name VARCHAR(50),
                date VARCHAR(50),
                time VARCHAR(50),
                url VARCHAR(100)
            );
        '''

        cars = '''
            CREATE TABLE cars(
                carID INTEGER NOT NULL PRIMARY KEY,
                model VARCHAR(50),
                make VARCHAR(50),
                acceleration FLOAT,
                tires VARCHAR(50),
                engine VARCHAR(50)
            );
        '''
        queries = [tracks, teams, drivers, races, cars]
        for query in queries:
            run(query)
    
# run query 
def run(query):
    cursor.reset()
    cursor.execute(query)
    connection.commit()
    
#return single attribute from a table 
def single_record(query):
    cursor.reset()
    cursor.execute(query)
    record = cursor.fetchone()
    return record

def bulk_insert(query, records):
    cursor.executemany(query, records)
    connection.commit()

def multi_attribute(query):
    cursor.reset()
    cursor.execute(query)
    results = cursor.fetchall()
    cleaned_results = []
    for row in results:
        cleaned_row = []
        for i in row:
            if i is not None:
                cleaned_row.append(i)
        cleaned_results.append(cleaned_row)
    return cleaned_results

def tracks_preprocess():
    attribute_count = len(tracks[0])
    placeholders = ",".join(["%s"]*attribute_count)
    query = "INSERT INTO tracks VALUES(" + placeholders + ")"
    cursor.executemany(query, tracks)
    connection.commit()

def drivers_preprocess():
    attribute_count = len(drivers[0])
    print(attribute_count)
    placeholders = ",".join(["%s"]*attribute_count)
    query = "INSERT INTO drivers VALUES(" + placeholders + ")"
    cursor.executemany(query, drivers)
    connection.commit()

def races_preprocess():
    attribute_count = len(races[0])
    placeholders = ",".join(["%s"]*attribute_count)
    query = "INSERT INTO races VALUES(" + placeholders + ")"
    cursor.executemany(query, races)
    connection.commit()


# create_tables()
# main
tracks_preprocess()


connection.close()