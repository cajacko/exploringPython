'''Get config file'''

import ConfigParser

CONFIG = ConfigParser.ConfigParser()
CONFIG.read("config.ini")

def config_section_map(section):
    '''Return the sections of the config'''
    dict1 = {}
    options = CONFIG.options(section)
    for option in options:
        dict1[option] = CONFIG.get(section, option)
    return dict1

print config_section_map("MySql")
