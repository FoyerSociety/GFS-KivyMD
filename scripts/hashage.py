import sys
import hashlib
sys.path.append("../models")

from models import Database
from config import CONFIG

def insert(username,password):

        request = '''
            INSERT INTO User(username,password,priv) VALUES(%s, %s,%s);
        '''
        bd.cursor.execute(request,(username,password,priv))
        bd.connex.commit()


def update(username,password):
    request = '''
        UPDATE User SET password = %s, priv = %s WHERE username = %s;
    '''

    bd.cursor.execute(request,(password,priv, username))

    print(bd.cursor.lastrowid)
    bd.connex.commit()

    bd.connex.close()

bd = Database(CONFIG)

action = input("Choose[Default c] : New User(n) or Update User(c) :")
username = input("Username : ")
password = hashlib.sha3_256(input("Password : ").encode("utf-8")).hexdigest()
priv = input("Privilege : ")
insert(username,password) if action == "n" else update(username,password)

    



