import main

repo = main.password_repo(path=main.file_path , delete_path= main.delete_data_path)
def registering():
    inp = inputs()
    repo.register_a_password(param= main.password(url=inp[0], name= inp[1], mail= inp[2], password= inp[-1]))
def inputs():
    name = input("username: ")
    url = input("website's url: ")
    mail = input("mail: ")
    password = input("password: ")
    return [url,name,mail,password]

operations = {"register a password" : registering,
              "read passwords": repo.read_passwords,
              "read deleted passwords": repo.read_deleted_passwords,
              "delete a password": repo.delete_a_password,
              "change a password": repo.change_a_password,
              "bring back a password": repo.bring_back_a_password,
              "exit": "q"}
while True:
    keys = []
    x = 1
    for key,value in operations.items():
        print(f"{x}-{key}")
        keys.append(key)
        x += 1
    choice = int(input("which operation(number): ")) -1
    func = operations[keys[choice]]
    if func == "q":
        break
    func()





