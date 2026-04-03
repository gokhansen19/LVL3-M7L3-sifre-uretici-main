import random
import string

def generate_password(length=12): #fonksiyonun varsayılan şifre uzunluğu 12 olarak ayarlanmıştır, istenirse farklı bir uzunluk da belirtilebilir
    """Belirtilen uzunlukta rastgele bir şifre oluşturur."""
    characters = string.ascii_letters + string.digits + string.punctuation # Şifre oluşturmak için kullanılacak karakterler: büyük harfler, küçük harfler, rakamlar ve özel karakterler
    password = '' #Başlangıçta boş bir şifre oluşturulur
    for i in range(length): #Belirtilen uzunluk kadar döngü çalıştırılır
        password += random.choice(characters) #Her döngüde, characters dizisinden rastgele bir karakter seçilir ve şifreye eklenir
    return password

# Kullanım örneği
password_length = 12  # İstediğiniz herhangi bir şifre uzunluğunu seçebilirsiniz
print("Yeni şifreniz:", generate_password(password_length))
