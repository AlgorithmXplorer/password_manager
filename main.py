
file_path = "C:/Users/VICTUS/Masaüstü/PYTHON_ALL/eğitim dışı kodlar/password_manager/passwords.txt"


def file_read(path):
    with open(path,"r+",encoding = "utf-8") as file:

        for i in file.readlines():
            i = i.split(",")
            print(f"internet sitesi: {i[0]}\nkullanıcı adı: {i[1]}\nşifre:{i[2]}\ndeğiştirme tarihi: {i[3]}")
            print("-"*50)
            


