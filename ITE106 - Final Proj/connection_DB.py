import pymysql

hostname = 'localhost' #this can be server IP or just localhost if you are refering to yourown server
username = 'root'
password = ''
database = 'inventorysystem'

myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database, autocommit=True)