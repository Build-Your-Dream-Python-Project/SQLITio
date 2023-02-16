import os
import ftplib
import hashlib

class encryptor(self):
    pass
def mkfile(name):
    with open(f'{name}', 'w') as f:
        f.close()

def create_db(name2):
    if not os.path.exists('LitIO'):
        os.mkdir('LitIO')
    os.chdir('LitIO')
    mkfile(f'{name2}.sqio')