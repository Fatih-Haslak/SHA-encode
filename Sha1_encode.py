import hashlib

def brute_force(hash_code):
    
    for c in [c1 + c2 + c3 + c4 + c5 for c1 in chars for c2 in chars for c3 in chars for c4 in chars for c5 in chars]:
        password = c #şifre kombinasyonu
        hashed = hashlib.sha1(password.encode()).hexdigest() #sha1 algoritması
        if hashed == hash_code: #kontrol blogu
            return password
    return None

if __name__ == "__main__":
    
    hash_code = "adcc7586d7c0a60b26760aefcdb21b93a7978511"
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    result = brute_force(hash_code)
    
    if (result):
        print(f"Hash çözümlendi. Şifre: {result}")
    
    else:
        print("Hash çözümlenemedi.")