import sys
import hashlib
sys.path.append("../models")

from models import Database
from config import CONFIG

def insert(username,password):
    

        request = '''
            INSERT INTO User(username,password) VALUES(%s, %s);
        '''
        bd.cursor.execute(request,(username,password))
        bd.connex.commit()


def update(username,password):
    request = '''
        UPDATE User SET password = %s WHERE username = %s;
    '''

    bd.cursor.execute(request,(password,username))

    print(bd.cursor.lastrowid)
    bd.connex.commit()

    bd.connex.close()

bd = Database(CONFIG)

action = input("Choose[Default c] : New User(n) or Change Password(c) :")
username = input("Username : ")
password = hashlib.sha3_256(input("Password : ").encode("utf-8")).hexdigest()

insert(username,password) if action == "n" else update(username,password)

    



