
import datetime
file_path = "C:/Users/VICTUS/Masaüstü/PYTHON_ALL/eğitim dışı kodlar/password_manager/passwords.txt"
transactions = ["şifrelere bakma", "şifre ekleme", "şifre düzenleme","çıkış"] 
#* fonksiyonların sonuna print ile "\n\n" str verisini yazdır 

def file_read(path):
    with open(path,"r+",encoding = "utf-8") as file:

        for index,line in enumerate(file.readlines()):
            line = line.split(",")
            print(f"{index+1}:\ninternet sitesi: {line[0]}\nkullanıcı adı: {line[1]}\nşifre: {line[2]}\ndeğiştirme tarihi: {line[3]}")
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
        now = datetime.datetime.now()
        year ,month,day,hour,minute  = now.year,  now.month, now.day, now.hour,now.minute
        return f"{year}.{month}.{day}.{hour}.{minute},"

    website =  input("internet sitesi(HTTPS): ")
    user_name = input("kullanıcı adı: ")
    password = input("şifre: ")
    print("\n\n")

    with open(path,"a",encoding="utf-8") as file:
        file.write(f"{website},{user_name},{password},{date_func()}\n")

def change_a_password(path):
    file_read(path)
    changed_password_num = int(input("hangi şifre değişicek(numara girin): ")) -1
    with open(path,"r+",encoding="utf-8") as file:
        lines = file.readlines()
    chang_lines = lines[changed_password_num].split(",")
    new_password = input("yeni şifre: ")
    chang_lines.insert(2,new_password)
    chang_lines.pop(3)
    new_line =",".join(chang_lines)
    print(new_line)
    #*yeni şifre 0-1-2 2. index e koyuldu ve eski index 3. index e geçti. ardından 3. indexdeki veri silindi.
    #*  son liste str olması join metodu ile str oldu
    #* aynı işlrem txt dosyasındaki satırlar için yapılcak
    lines.insert(changed_password_num , new_line)
    lines.pop(changed_password_num +1)
    with open(path,"w",encoding="utf-8") as file:
        print(lines)
        file.writelines(lines)

    
def main(path):
    num = question()
    if  num == 1:
        file_read(path)
        main(path)
    
    elif num == 2:
        add_a_password(path)
        main(path)
    
    elif num == 3:
        change_a_password(path)
        main(path)
    elif num == 4:
        print("çıkıldı".upper())
    
    
main(file_path)