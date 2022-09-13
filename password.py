class User:
    def __init__(self,username,mail,password):
        self.username = username
        self.mail = mail
        self.password = password

check = True
user_1 = User("rinsall0","asawtell0@themeforest.net","oOe63Lj")
user_2 = User("vlarrosa1","jdyke1@weebly.com","TdelLY")
user_3 = User("rhasted2","bprover2@salon.com","ruglQJ")
user_4 = User("amarsy3","gdmitrievski3@shop-pro.jp","XhtDOrw")

while check:
      str = input("Enter Username or Email : ")
      psw = input("Enter Password : ")
      if (str == user_1.username or str == user_1.mail) and psw == user_1.password:
       print("LOGIN SUCCESFUL")
       check=False

      elif (str == user_2.username or str == user_2.mail) and psw == user_2.password:
         print("LOGIN SUCCESFUL")
         check = False

      elif (str == user_3.username or str == user_3.mail) and psw == user_3.password:
        print("LOGIN SUCCESFUL")
        check = False

      elif (str == user_4.username or str == user_4.mail) and psw == user_4.password:
        print("LOGIN SUCCESFUL")
        check=False

      else:
            print("Username or Password is incorrect...\n")


