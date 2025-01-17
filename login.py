from tkinter import *
from tkinter import messagebox
import sqlite3
import registration
ws = Tk()
ws.title('Login Page')
ws.config(bg='#0B5A81')
ws.minsize(width=500,height=500)
ws.maxsize(width=500,height=500)

f = ('Times', 14)

class Login:
    def __init__(self):
        pass



def login_response():
    try:
        con = sqlite3.connect('firstdb.db')
        c = con.cursor()
        print(c.execute("Select * from record"))
        for row in c.execute("Select * from record"):            
            username = row[0]
            pwd = row[4]
        
    except Exception as ep:
        messagebox.showerror('', ep)

    uname = email_tf.get()
    upwd = pwd_tf.get()
    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uname == username and upwd == pwd):
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
        
        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)







left_frame = Frame(
    ws, 
    bd=2, 
    bg='#CCCCCC',   
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    left_frame, 
    text="Enter Email", 
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame, 
    text="Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame, 
    font=f
    )
pwd_tf = Entry(
    left_frame, 
    font=f,
    show='*'
    )
login_btn = Button(
    left_frame, 
    width=15, 
    text='Login', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=login_response
    )

signup_btn = Button(
    left_frame, 
    width=15, 
    text='Signup', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=go_signup_page
    )

email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
signup_btn.grid(row=2, column=0, pady=10, padx=20)
left_frame.pack()


ws.mainloop()