'''
Set up MySQL
Get the database details from the config file and set up the connection
'''

import MySQLdb
import config # Get the parser for extracting the database config details

# Get the database details
HOST = config.config_section_map('MySql')['host']
USER = config.config_section_map('MySql')['user']
PASSWORD = config.config_section_map('MySql')['password']
DATABASE = config.config_section_map('MySql')['database']

# Connect to the database
DB = MySQLdb.connect(
    host=HOST,
    user=USER,
    passwd=PASSWORD,
    db=DATABASE
)

# Set up a cursor which is needed to make queries
CUR = DB.cursor()
