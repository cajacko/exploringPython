'''
Set up MySQL
Get the database details from the config file and set up the connection
'''

import ConfigParser # Get the parser for extracting the database config details
import MySQLdb

CONFIG = ConfigParser.ConfigParser()
CONFIG.read('config.ini') # Get the config file

def config_section_map(section):
    '''
    Return the sections of the config
    '''
    dict1 = {}
    options = CONFIG.options(section)
    for option in options:
        dict1[option] = CONFIG.get(section, option)
    return dict1

# Get the database details
HOST = config_section_map('MySql')['host']
USER = config_section_map('MySql')['user']
PASSWORD = config_section_map('MySql')['password']
DATABASE = config_section_map('MySql')['database']

# Connect to the database
DB = MySQLdb.connect(
    host=HOST,
    user=USER,
    passwd=PASSWORD,
    db=DATABASE
)

# Set up a cursor which is needed to make queries
CUR = DB.cursor()
