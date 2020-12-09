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

    def tour_tache(self,jour,tache):
        if tache == "ck":
            request = '''
                SELECT username FROM User 
                WHERE ind_uni_ck = 
                    (SELECT DATEDIFF(%s,(SELECT ck FROM Date_begin)))
                        %
                    (SELECT COUNT(id) FROM User WHERE ind_uni_ck IS NOT NULL)
                    ;
            '''
        elif tache == "mp":
            request = '''
                SELECT username FROM User 
                WHERE ind_uni_mp = 
                    (SELECT DATEDIFF(%s,(SELECT mp FROM Date_begin)))
                        %
                    (SELECT COUNT(id) FROM User WHERE ind_uni_mp IS NOT NULL)
                    ;
            '''
        elif tache == "ma":
            request = '''
                SELECT username FROM User 
                WHERE ind_uni_ma = 
                    (SELECT DATEDIFF(%s,(SELECT ma FROM Date_begin)))
                        %
                    (SELECT COUNT(id) FROM User WHERE ind_uni_ma IS NOT NULL)
                    ;
            '''

        self.cursor.execute(request,(jour,))
        fetch = self.cursor.fetchone()

        return fetch[0]