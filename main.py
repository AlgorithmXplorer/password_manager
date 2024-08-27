
import json
from datetime import datetime as date
import os
try:
    os.mkdir(os.getcwd() + "/passwords")
    path = os.getcwd() +"/passwords"
    os.system(f"attrib +h {path}")
except:
    path = os.getcwd() +"/passwords"


file_path , delete_data_path  = path + "/passwords.json" , path + "/delete_passwords.json"

class password:
    def __init__(self,url,name,mail,password):
        self.url = url
        self.username = name
        self.email = mail
        self.password = password
        self.create_time = date.strftime(date.now() , "%X - %d/%m/%Y")
    
    def dicti_maker(self):
        return self.__dict__
    
x = password(url=1,name=1,mail=1,password=1)


class password_repo:
    def __init__(self,path,delete_path) :
        self.path = path
        self.delete_path = delete_path
        try:
            with open(self.path,"r",encoding="utf-8") as file:
                self.normal_datas = json.load(file)
        except:
            self.normal_datas = []

        try:
            with open(self.delete_path,"r",encoding="utf-8") as file:
                self.delete_datas = json.load(file)
        except:
            self.delete_datas = []


    def register_a_password(self,param):
        if type(param) == password:
            new_psw = param.dicti_maker()
            self.normal_datas.append(new_psw)
            with open(self.path,"w",encoding="utf-8") as file:
                json.dump(self.normal_datas,file , indent=4 , sort_keys=False)
        else:
            with open(self.path,"w",encoding="utf-8") as file:
                json.dump(self.normal_datas,file , indent=4 , sort_keys=False)

    def read_passwords(self):
        for index,psw in enumerate(self.normal_datas,1):
            print(f"{index}".center(30,"-"))
            for key,value in psw.items():
                print(f"{key}  = {value}")
            print("")
    
    def read_deleted_passwords(self):
        for index,psw in enumerate(self.delete_datas,1):
            print(f"{index}".center(30,"-"))
            for key,value in psw.items():
                print(f"{key}  = {value}")
            print("")
    
    def delete_a_password(self):
        self.read_passwords()
        choice = int(input("which password will be delete (no): ")) -1
        deleted_psw = self.normal_datas[choice]
        self.normal_datas.pop(choice)
        self.delete_datas.append(deleted_psw)

        with open(self.delete_path,"w",encoding="utf-8") as file:
            json.dump(self.delete_datas, file,indent=5,sort_keys=False)
        self.register_a_password(None)

    def change_a_password(self):
        #* choice of password
        self.read_passwords()
        index = int(input("which password(number): ")) - 1
        psw = self.normal_datas[index]  
        self.normal_datas.pop(index)

        #*feature selection to change
        print("*"*20)
        for keys in psw:
            if keys == "create_time":
                break
            print(f"-{keys}")
        print("*"*20)
        choice = input("which number will be changed(enter to name): ")
        new_setting = input(f"What will the new {choice} be: ")

        #*  the save to changes
        psw[choice] = new_setting
        self.normal_datas.insert(index,psw)
        self.register_a_password(None)

    def bring_back_a_password(self):
        if self.delete_datas == []:
            print("there are not deleted passwords")
            return None
        self.read_deleted_passwords()
        index = int(input("which password will be return back: ")) -1
        psw = self.delete_datas[index]

        self.delete_datas.pop(index)
        with open(self.delete_path,"w",encoding="utf-8") as file:
            json.dump(self.delete_datas,file)

        self.normal_datas.append(psw) 
        self.register_a_password(None)


