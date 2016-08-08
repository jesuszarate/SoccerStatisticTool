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



def insertMatch(homeTeamId, homeGoals, awayTeamId, awayGoals, winner):
    query = "insert into matches (homeTeamId, homeGoals, awayTeamId, awayGoals, winner)"\
        " values (%s, %s, %s, %s, %s)"
    match = (homeTeamId, homeGoals, awayTeamId, awayGoals, winner)
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



#import pdb; pdb.set_trace()
insertMatch(8, 3, 2, 2, 8)
