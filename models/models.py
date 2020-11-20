import mysql.connector
import hashlib

###Register the __SESSION on login

_SESSION = {
        "username" : None,
        "priv" : None
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
        ###Hash the password from the input and compare it
        password = hashlib.sha3_256(password.encode("utf-8")).hexdigest()
        self.cursor.execute(request,(username,password))

        fetch = self.cursor.fetchall()

        ###NOT IMPORTANT FOR THE MOMENT
        if fetch != []:
            _SESSION["username"] = fetch[0][0]
            _SESSION["priv"] = fetch[0][1]

        return True \
            if len(fetch) > 0 else False
