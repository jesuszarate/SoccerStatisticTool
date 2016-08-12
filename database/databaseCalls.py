from mysql.connector import Error
from dbconfig import read_db_config
import mysql.connector

def connect():
    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn = mysql.connector.connect(**db_config)

        if conn.is_connected():
            print('connection established.')
            return conn
        else:
            print('connection failed.')
    except Error as e:
        print(e)


def getTeamId(teamName):
    query = 'SELECT * FROM teams WHERE teamName = "' + teamName + '"'
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()

        if row is not None:
            return row[0]

    except Error as e:
        print(e)
    else:
        print('Connection closed.')
        cursor.close()
        conn.close()
    

def insertMatch(homeTeamId, homeGoals, awayTeamId, awayGoals, winner, date):
    query = "insert into matches (homeTeamId, homeGoals, awayTeamId, awayGoals, winner, date)"\
        " values (%s, %s, %s, %s, %s, %s)"
    match = (homeTeamId, homeGoals, awayTeamId, awayGoals, winner, date)
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, match)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
        
        conn.commit()

    except Error as error:
        print(error)
    else:    
        print('Connection closed.')
        conn.close()
        cursor.close()

def insertRachaEntry(matchId, teamId, result, date):

    query = "insert into racha(matchId, teamId, result, date) values (%s, %s, %s, %s)" #(1, 4, '2016-08-06', 2)"
    values = (matchId, teamId, result, date)
    insert(query, values)
    

def insert(query, values):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, values)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
            
    except Error as error:
        print(error)
    else:
        print('Connection closed.')
        conn.close()
        cursor.close()


# GET CALLS
def getMatches():
    print 'Getting matches...'
    query = 'SELECT * FROM matches'
    return getAll(query);


def getResults():
    print 'Getting results...'
    query = 'SELECT * FROM results'
    return getAll(query)


def getAll(query):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows
        
    except Error as e:
        print(e)
 
    else:
        cursor.close()
        conn.close()


def getOne(query):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query)
 
        row = cursor.fetchone()
 
        while row is not None:
            print(row)
            row = cursor.fetchone()
 
    except Error as e:
        print(e)
 
    else:
        cursor.close()
        conn.close()

#import pdb; pdb.set_trace()

#Inserting new match
#insertMatch(8, 3, 2, 2, 8)

#Get teamNameId
#getTeamId('America');
