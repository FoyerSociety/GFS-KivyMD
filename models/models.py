import mysql.connector
import hashlib

session={
    "username" : "",
    "password" : ""
}

class Database:
    def __init__(self, config):
        self.connex = mysql.connector.connect(**config)
        self.cursor = self.connex.cursor()


    def login(self,username,password):
        request = '''
            SELECT username, priv
            FROM User WHERE username = %s AND password = %s 
        '''
        password = hashlib.sha3_256(password.encode("utf-8")).hexdigest()
        self.cursor.execute(request,(username,password))

        # return True \
        #     if len(self.cursor.fetchall()) > 0 else False
