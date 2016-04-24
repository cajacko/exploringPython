'''
Setup MongoDB
'''

import pymongo
import config # Get the parser for extracting the database config details

# Get the database details
HOST = config.config_section_map('MongoDB')['host']
USER = config.config_section_map('MongoDB')['user']
PASSWORD = config.config_section_map('MongoDB')['password']
DATABASE = config.config_section_map('MongoDB')['database']

MONGODB_URI = 'mongodb://' + USER + ':' + PASSWORD + '@' + HOST

CLIENT = pymongo.MongoClient(MONGODB_URI)
TEMP = CLIENT.get_default_database()
DB = TEMP[DATABASE]
