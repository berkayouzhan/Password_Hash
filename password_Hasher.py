import hashlib

def hash_password(password):

    hasher = hashlib.sha256()

    hasher.update(password.encode('utf-8'))

    return hasher.hexdigest()

def save_password(username, password):

    hashed_password = hash_password(password)

    with open('passwords.txt', 'a') as f:
        f.write(f"{username}:{hashed_password}\n")

def check_password(username, password):

    hashed_password = hash_password(password)

    with open('passwords.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(username):
                saved_password = line.split(':')[1]
                if saved_password == hashed_password:
                    return True

    return False
# Burada kendi isminizi ve şifrenizi yazarak uygulamanın bulunduğu klasörde bir text dosyası oluşturarak şifrelerinizi saklayabilirsiniz
save_password('Adınızı Girin', 'Şifrenizi girin')

