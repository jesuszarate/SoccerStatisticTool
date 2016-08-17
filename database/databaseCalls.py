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

def updateMatchScore(matchId, homeGoals, awayGoals, winner):
    query = "UPDATE matches SET homeGoals=%s, awayGoals=%s, winner=%s WHERE matchId=%s"
    values = (homeGoals, awayGoals, winner, matchId)
    insert(query, values)


def insertPrediction(matchId, prediction):
    query = "INSERT INTO predictions (matchId, prediction) VALUES (%s, %s)"
    values = (matchId, prediction)

    insert(query, values)

def insert(query, values):
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


def insertMatch(homeTeamId, homeGoals, awayTeamId, awayGoals, winner, date):
    print 'in hereeeee'
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
def getMatches(date):
    print 'Getting matches...'
    query = 'SELECT * FROM matches WHERE date=' + date
    return getAll(query);

# Table for Gana/Pierde/Empata
def getResults():
    print 'Getting results...'
    query = 'SELECT * FROM results'
    return getAll(query)

def getMatchId(homeTeamId, awayTeamId, date):
    query = 'SELECT matchId FROM matches WHERE homeTeamId=' + str(homeTeamId) +\
        ' AND awayTeamId='+ str(awayTeamId) +\
        ' AND date=' + date
    return getOne(query)[0]

def getPredictionId(prediction):
    query = "SELECT resultId FROM results WHERE result = '" + prediction +"'"
    result = getOne(query)
    if result is not None:
        return result[0]
    return None
    

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

        '''
        while row is None:
        print 'fetching data...'
        row = cursor.fetchone()
        '''
        return row

     
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
