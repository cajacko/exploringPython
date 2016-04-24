'''
Perform a dummy query to check MySQL is working
'''

import mysql

mysql.CUR.execute('SHOW TABLES') # Get the table sin the database

# Print the results to check all is working
for row in mysql.CUR.fetchall():
    print row
