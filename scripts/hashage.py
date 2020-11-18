import sys
import hashlib
sys.path.append("../models")

from models import Database
from config import CONFIG



bd = Database(CONFIG)

action = input("New User(n) or Change Password(c)")
username = hashlib.sha3_256(input("Username : ").encode("utf-8")).hexdigest()
password = input("New password : ")

if action == "n":

        request = '''
            UPDATE User SET password = %s WHERE id=%s
        '''
        
        self.bd.cursor.execute(request,(hashlib.sha3_256(psd[i].encode("utf-8")).hexdigest(), i+1))
        self.bd.connex.commit()
        i = i+1
    self.bd.cursor.close()
    self.bd.connex.close()
    return self.passwordHash
        
hch = HashPassword().hashage()

print(hch)





