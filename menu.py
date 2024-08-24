import main

operations = ["register a password", "read passwords" , "read deleted passwords", "delete a password", "change a password", "bring back a password","exit"]
repo = main.password_repo(path=main.file_path , delete_path= main.delete_data_path)

def inputs():
    name = input("kullanıcı ismi: ")
    url = input("site url'si: ")
    mail = input("mail: ")
    password = input("şifre: ")
    return [url,name,mail,password]
while True:
    for index,opr in enumerate(operations,1):
        print(f"{index}- {opr}")
    choice = input("hangi işlem: ")
    if choice == "1":
        inp = inputs()
        repo.register_a_password(param= main.password(url=inp[0], name= inp[1], mail= inp[2], password= inp[-1]))
    elif choice == "2":
        repo.read_passwords()
    elif choice == "3":
        repo.read_deleted_passwords()
    elif choice == "4":
        repo.delete_a_password()
    elif choice == "5":
        repo.change_a_password()
    elif choice == "6":
        repo.bring_back_a_password()
    elif choice == "7":
        break




