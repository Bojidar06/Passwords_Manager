import hashlib

def Hash(string):
  h = hashlib.sha256(string.encode('utf-8')).hexdigest()
  return h
