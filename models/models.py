import mysql.connector
from config import CONFIG 



class Database:
    def __init__(self):
        self.connex = mysql.connector.connect(CONFIG)
        self.cursor = self.connex.cursor()


    def login(self,username,password):
        request = '''
            SELECT 1 FROM User WHERE username = %s AND password = %s 
        '''
        self.cursor.execute(request,(username,password))

        return len(self.cursor.fetchall())
        
    

