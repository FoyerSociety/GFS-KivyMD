import sys
import hashlib
sys.path.append("../models")

from models import Database
from config import CONFIG



class HashPassword:
    def __init__(self):
        self.bd = Database(CONFIG)
        self.password = self.bd.sendPassword()
        self.passwordHash = []


    def hashage(self):
        i = 0
        for psd in self.password:
            request = '''
                UPDATE User SET password = %s WHERE id=%s
            '''
            self.passwordHash.append(hashlib.sha3_256(psd[i].encode("utf-8")).hexdigest())
            self.bd.cursor.execute(request,(hashlib.sha3_256(psd[i].encode("utf-8")).hexdigest(), i+1))
            self.bd.connex.commit()
            i = i+1
        self.bd.cursor.close()
        self.bd.connex.close()
        return self.passwordHash
        
hch = HashPassword().hashage()

print(hch)





