'''Get config file'''

import ConfigParser
import MySQLdb

CONFIG = ConfigParser.ConfigParser()
CONFIG.read('config.ini')

def config_section_map(section):
    '''Return the sections of the config'''
    dict1 = {}
    options = CONFIG.options(section)
    for option in options:
        dict1[option] = CONFIG.get(section, option)
    return dict1

# print config_section_map('MySql')['host']

HOST = config_section_map('MySql')['host']
USER = config_section_map('MySql')['user']
PASSWORD = config_section_map('MySql')['password']
DATABASE = config_section_map('MySql')['database']

DB = MySQLdb.connect(
    host=HOST,
    user=USER,
    passwd=PASSWORD,
    db=DATABASE
)

# You must create a Cursor object. It will let
# you execute all the queries you need
CUR = DB.cursor()

# Use all the SQL you like
CUR.execute('SELECT * FROM stories')

# print all the first cell of all the rows
for row in CUR.fetchall():
    print row[0]

DB.close()
