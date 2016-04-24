'''
Perform a dummy query to check MySQL is working
'''

import mysql
import mongo

def mysql_test():
    '''
    ouhdoih
    '''
    mysql.CUR.execute('SHOW TABLES') # Get the table sin the database

    # Print the results to check all is working
    for row in mysql.CUR.fetchall():
        print row

def mongo_test_insert():
    '''
    ouhiof
    '''

    seed_data = [
        {
            'decade': '1970s',
            'artist': 'Debby Boone',
            'song': 'You Light Up My Life',
            'weeksAtOne': 10
        },
        {
            'decade': '1980s',
            'artist': 'Olivia Newton-John',
            'song': 'Physical',
            'weeksAtOne': 10
        },
        {
            'decade': '1990s',
            'artist': 'Mariah Carey',
            'song': 'One Sweet Day',
            'weeksAtOne': 16
        }
    ]

    mongo.DB.insert(seed_data)

def mongo_test_get():
    '''
    doihfoin
    '''
    cursor = mongo.DB.find({'weeksAtOne': {'$gte': 10}}).sort('decade', 1)

    for doc in cursor:
        print doc


mysql_test()
# mongo_test_insert()
mongo_test_get()
