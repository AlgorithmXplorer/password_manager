
import datetime
file_path = "C:/Users/VICTUS/Masaüstü/PYTHON_ALL/eğitim dışı kodlar/password_manager/passwords.txt"
transactions = ["şifrelere bakma", "şifre ekleme", "şifre düzenleme","çıkış"] 
#* fonksiyonların sonuna print ile "\n\n" str verisini yazdır 
def file_read(path):
    with open(path,"r+",encoding = "utf-8") as file:

        for i in file.readlines():
            i = i.split(",")
            print(f"internet sitesi: {i[0]}\nkullanıcı adı: {i[1]}\nşifre: {i[2]}\ndeğiştirme tarihi: {i[3]}")
            print("-"*50)
    print("\n\n")   

def question():
    print("işlemler:")
    for index,transaction in enumerate(transactions):
        print(f"{index + 1}- {transaction}")
    transaction_inp = int(input("hangi işlem(sayı giriniz): "))
    print("\n\n")
    return transaction_inp

def add_a_password(path):
    def date_func():
        now = str(datetime.datetime.now()).split(" ")
        year_month_day = now[0]
        hour_minutes = now[1].split(":")
        hour_minute = f"{hour_minutes[0]},{hour_minutes[1]}"

        print(hour_minute)
        
    
    date_func()
    website =  input("internet sitesi(HTTPS): ")
    user_name = input("kullanıcı adı: ")
    password = input("şifre: ")

    with open(path,"a",encoding="utf-8") as file:
        file.write(f"{website},{user_name},{password},\n")


def main(path):
    num = question()
    if  num == 1:
        file_read(path)
        main(path)
    
    elif num == 2:
        add_a_password(path)
        main(path)
    
    elif num == 3:
        print("şifre düzenleme fonksiyonu")
        main(path)
    elif num == 4:
        print("çıkıldı".upper())
    
    
main(file_path)