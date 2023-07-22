import itertools
import hashlib

hash_code = "52d755c3ebf0f70fdb41bc1569b5fa4fd30690000511948626301c8207422c97496e4068cbe463aabe37e4caf919ca21"

alfabe = "0123456789abcdefghijklmnopqrstuvwxyz"

şifre_kombinasyonu = 5

flag=0

for i in itertools.product(alfabe, repeat=şifre_kombinasyonu):
    şifre = ''.join(i)
    hashli_şifre = hashlib.sha384(şifre.encode()).hexdigest()
    if hashli_şifre == hash_code:
        print("Şifre:",şifre)
        flag=1
        break
if(flag==0):
    print("Şifre çözülemedi")



