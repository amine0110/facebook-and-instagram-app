from tkinter import *

root = Tk()
root.title("S M")
root.geometry("300x400")
root.iconbitmap("logo.ico")
root.configure(bg="#4D4749")

username = "username"
password = "password"

def log_i(a,b):
    if a == "amine" and b == "amine":
        print = Label(new, text=("hi " + a), font="android 20", bg="#F58AAB")
        print.grid(row=4, column=0, columnspan=2)
    else:
        print = Label(new, text="try again", font="android 20", bg="#F58AAB")
        print.grid(row=4, column=0, columnspan=2)

def log_f(a,b):
    if a == "amine" and b == "amine":
        print = Label(new1, text=("hi " + a), font="android 20", bg="#4A7BEE")
        print.grid(row=4, column=0, columnspan=2)
    else:
        print = Label(new1, text="try again", font="android 20", bg="#4A7BEE")
        print.grid(row=4, column=0, columnspan=2)

def login_f():
    global new1
    # global box_f_user
    # global box_f_pass

    new1 = Toplevel()
    new1.configure(bg="#4A7BEE")
    new1.title("Facebook")
    new1.iconbitmap("facebook.ico")
    new1.geometry("300x400")

    login_f_user = Label(new1, text=username, font="none 13", bg="#4A7BEE")
    login_f_pass = Label(new1, text=password, font="none 13", bg="#4A7BEE")
    box_f_user = Entry(new1, w=20, font="none 13")
    box_f_pass = Entry(new1, w=20, font="none 13", show="*")
    facebook_logo = Label(new1, text="Facebook",bg="#4A7BEE", font="Propaganda 20")
    facebook_login = Button(new1, text="LOGIN", font="none 10", padx=40, command=lambda :log_f(box_f_user.get(), box_f_pass.get()))

    login_f_user.grid(row=1, column=0, padx=10, pady=20)
    login_f_pass.grid(row=2, column=0)
    box_f_user.grid(row=1, column=1)
    box_f_pass.grid(row=2, column=1)
    facebook_logo.grid(row=0, column=0, columnspan=2)
    facebook_login.grid(row=3, column=0, columnspan=2, pady=50)

def login_i():
    global new
    # global box_i_user
    # global box_i_pass


    new = Toplevel()
    new.configure(bg="#F58AAB")
    new.title("Instagram")
    new.iconbitmap("i.ico")
    new.geometry("300x400")

    login_i_user = Label(new, text=username, font="none 13", bg="#F58AAB")
    login_i_pass = Label(new, text=password, font="none 13", bg="#F58AAB")
    box_i_user = Entry(new, w=20, font="none 13")
    box_i_pass = Entry(new, w=20, font="none 13", show="*")
    instagram_logo = Label(new, text="Instagram",bg="#F58AAB", font="Propaganda 20")
    instagram_login = Button(new, text="LOGIN", font="none 10", padx=40, command=lambda :log_i(box_i_user.get(), box_i_pass.get()))

    login_i_user.grid(row=1, column=0, padx=10, pady=20)
    login_i_pass.grid(row=2, column=0)
    box_i_user.grid(row=1, column=1)
    box_i_pass.grid(row=2, column=1)
    instagram_logo.grid(row=0, column=0, columnspan=2)
    instagram_login.grid(row=3, column=0, columnspan=2, pady=50)


facebook = Button(root, text="Facebook", padx=30, pady=10, bg="white", command=login_f)
instagram = Button(root, text="Instagram", padx=30, pady=10, bg="white", command=login_i)

facebook.grid(row=0, column=0, columnspan=2, pady=50, padx=85)
instagram.grid(row=1, column=0, columnspan=2, pady=10)


mainloop()