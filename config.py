'''
Get the config details
'''

import ConfigParser # Get the parser for extracting the database config details

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
