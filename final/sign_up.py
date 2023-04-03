from tkinter import *
from tkinter import messagebox
import json
import login as lg
from PIL import Image, ImageTk

# #FFFFFA: trắng, #A41623: đỏ, #141204: đen
# #c1e2cd: xanh mint, #3b225c: tím, #ffb601: vàng, #ea574f: đỏ
class Sign_up:
    def __init__(self,root):
        self.sign_up = root
        self.sign_up.title("Sign up")
        self.sign_up.geometry("800x720")
        self.sign_up.resizable(False,False)    

        self.image_path = "D:/usth/advance py/pp2023/final/bg.png"
        self.image = Image.open(self.image_path)
        self.bg_img = ImageTk.PhotoImage(self.image)
        self.bg = Label(self.sign_up, image = self.bg_img)
        self.bg.place(x = 0, y = 0, relheight = 1, relwidth = 1)

        self.Sign_in = Label(self.sign_up, text = "Sign up", fg = '#ea574f', bg = '#FFFFFA', font=('Montserrat Bold',30)).place(x = 340 , y = 100)
        self.User = Label(self.sign_up, text = "User", fg = '#ffb601', bg = '#FFFFFA', font=('Montserrat',18,'bold')).place(x = 100 , y = 200)
        self.User_box = Entry(self.sign_up, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',18), textvariable = StringVar())
        self.User_box.place(x = 350 , y = 200)
        self.Password = Label(self.sign_up, text = "Password", fg = '#ffb601', bg = '#FFFFFA', font=('Montserrat ',18,'bold')).place(x = 100 , y = 300)
        self.Password_box = Entry(self.sign_up, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',18), textvariable = StringVar())
        self.Password_box.place(x = 350 , y = 300)
        self.Conf_Password = Label(self.sign_up, text = "Confirm Password", fg = '#ffb601', bg = '#FFFFFA', font=('Montserrat', 18,'bold')).place(x = 100 , y = 400)
        self.Conf_Password_box = Entry(self.sign_up, fg = '#141204', bg = '#FFFFFA', font=('Montserrat',18), textvariable = StringVar())
        self.Conf_Password_box.place(x = 350 , y = 400)
        self.Sign_up_button = Button(self.sign_up, text = "Sign up", fg = 'white', bg = '#ea574f', font=('Montserrat Bold',20), command = self.do_sign_up).place(x = 340 , y = 500)
        self.Login = Label(self.sign_up, text = "Already have an account ?", fg = '#ea574f', bg = '#FFFFFA', font=('Montserrat',15)).place(x = 250 , y = 605)
        self.Login_button = Button(self.sign_up, text = "Login", fg = 'white', bg = '#ea574f', font=('Montserrat Bold',15), command= self.open_log_in).place(x = 550 , y = 600)

    def do_sign_up(self):
        user = self.User_box.get()
        password = self.Password_box.get()
        conf_password = self.Conf_Password_box.get()
        
        if password != conf_password:
            messagebox.showwarning("showinfo", "Password dont match")
            return

        f = open("account.txt", "r")

        try:
            account = json.loads(f.read())
        except:
            with open("account.txt", 'w') as w:
                w.write(json.dumps({user:password}))
            messagebox.showwarning("showinfo", "Success")
            return


        if user in account:
            messagebox.showwarning("showinfo", "Exist user")
            return
        
        account[user] = password
        f = open("account.txt", "w")
        f.truncate(0)
        account = json.dumps(account)
        f.write(account)
        f.close()
        messagebox.showwarning("showinfo", "Success")

    def open_log_in(self):
        self.sign_up.destroy()
        login = Tk()
        lg.Login(login)
        login.mainloop()    
