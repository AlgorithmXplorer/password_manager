
import datetime
file_path = "C:/Users/VICTUS/Masaüstü/PYTHON_ALL/eğitim dışı kodlar/password_manager/passwords.txt"
delete_file_path = "C:/Users/VICTUS/Masaüstü/PYTHON_ALL/eğitim dışı kodlar/password_manager/deleted_passwords.txt"
transactions = ["şifrelere bakma", "şifre ekleme", "şifre düzenleme","şifre silme","silinen şifreler bakma","çıkış"] 
#* fonksiyonların sonuna print ile "\n\n" str verisini yazdır 
def date_func():
    now = datetime.datetime.now()
    year ,month,day,hour,minute  = now.year,  now.month, now.day, now.hour,now.minute
    return f"{year}.{month}.{day}.{hour}.{minute},"

#!eğerki silinmiş dosyalar okunuyorsa silinme tarihide yazıcak
def file_read(path):
    with open(path,"r+",encoding = "utf-8") as file:

        for index,line in enumerate(file.readlines(),1):
            line = line.split(",")
            print(f"{index}:\ninternet sitesi: {line[0]}\nkullanıcı adı: {line[1]}\nşifre: {line[2]}\ndeğiştirme tarihi: {line[3]}")
            print("-"*50)
    print("\n\n")   

#!try
def question():
    print("işlemler:")
    for index,transaction in enumerate(transactions):
        print(f"{index + 1}- {transaction}")
    transaction_inp = int(input("hangi işlem(sayı giriniz): "))
    print("\n\n")
    return transaction_inp

#! try
def add_a_password(path):
    website =  input("internet sitesi(HTTPS): ")
    user_name = input("kullanıcı adı: ")
    password = input("şifre: ")
    print("\n\n")

    with open(path,"a",encoding="utf-8") as file:
        file.write(f"{website},{user_name},{password},{date_func()}\n")

#! burda değiştirme tarihi yazıcak ayrıca diğer birimlerde değiştirilebilir olucak
#!try
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

#! silinme terihi olarak satıra bir tarih daha yazılcak.
#!try
def delete_a_password(path,path_2):
    #!TRY
    file_read(path)
    choise = int(input("hangisi silincek(sayı): ")) -1
    sure = input("emin misin(e/h): ").lower().replace(" ","")
    if sure == "e":
        with open(path,"r+",encoding="utf-8") as file:
            lines = file.readlines()
            line = lines[choise]
            print(lines)
            lines.pop(choise)
            print(lines) 
        with open(path,"w",encoding="utf-8") as file:
            file.writelines(lines)
        with open(path_2,"r+",encoding="utf-8") as file:
            file.write(line)
            print(file.readlines())

        print("şifre silinmiştir\n\n")
    else:
        pass

#!eğerki şifre geri getirilcek ise silinme tarihi çıkarılcak satırdan ve geri getirilme tarihi yazılcak       
def deleted_passwords(normal_path,path):
    file_read(path)
    print("silinen şifreler")
    return_password = input("şifre getirilcek mi(e/h): ")
    if return_password == "e":
        which_password = int(input("hangi şifre(sayı): ")) -1 
        with open(path,"r+",encoding="utf-8") as file:
            lines = file.readlines()
            password = lines[which_password].split(",")
            password[-2] = date_func()
            password = ",".join(password)
            password = password[0:len(password)-2]
            password += "\n"
        #*geri getirilcek şifre elde edildi
        with open(path,"r+",encoding="utf-8") as file:
            lines = file.readlines()
            line = lines[which_password]
            print(lines)
            lines.pop(which_password)
            print(lines) 
        with open(path,"w",encoding="utf-8") as file:
            file.writelines(lines)
        #* siliniş şifre dosyasından şifre kaldırıldı
        with open(normal_path,"a",encoding="utf-8") as file:
            file.write(password)
            
            

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
        delete_a_password(path,delete_file_path)
        main(path)
    elif num == 5:
        deleted_passwords(path,delete_file_path)
        main(path)
    elif num == 6:
        print("çıkıldı".upper())
    
    
    
main(file_path)