import mysql.connector


class Database:
    def __init__(self, config):
        self.connex = mysql.connector.connect(**config)
        self.cursor = self.connex.cursor()


    def login(self,username,password):
        request = '''
            SELECT 1 FROM User WHERE username = %s AND password = %s 
        '''
        self.cursor.execute(request,(username,password))

        return True \
            if len(self.cursor.fetchall()) > 0 else False

        
    def sendPassword(self):

        request = '''
            SELECT password FROM User
        '''
        self.cursor.execute(request,id)

        return self.cursor.fetchall()
