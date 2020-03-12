from des import DesKey
import hashlib

def encripta(key,message):
    if isinstance(key, DesKey):
        c_message =  key.encrypt(b'%b'%message,initial=0,padding=True)
        return c_message
    else:
        return 0

def haser(file, length):

    hasher = hashlib.md5()

    with open(file, "rb") as _file:
        buffer = _file.read(length)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = _file.read(length)
        _file.close()
    
    return hasher.hexdigest()