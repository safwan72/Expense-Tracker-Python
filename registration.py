from tkinter import *
from tkinter import messagebox 
import sqlite3
import re
ws = Tk()
ws.title('Registration Page')
ws.config(bg='#0B5A81')
ws.minsize(width=500,height=500)
ws.maxsize(width=500,height=500)
f = ('Times', 14)
con = sqlite3.connect('firstdb.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    email text, 
                    contact number, 
                    gender text, 
                    country text,
                    password text
                )
            ''')
con.commit()

def insert_record():
    check_counter=0
    warn = ""
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'    
    
    if register_email.get() == "":
        warn = "Email can't be empty"
    elif not (re.fullmatch(regex,register_email.get())):
        warn='Email Not Valid'
    else:
        check_counter += 1

    if register_mobile.get() == "":
       warn = "Contact can't be empty"
    else:
        check_counter += 1
    
    if  genVar.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if variable.get() == "":
       warn = "Select Country"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if pwd_again.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1

    if register_pwd.get() != pwd_again.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1

    if check_counter == 7:        
        try:
            con = sqlite3.connect('firstdb.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:email, :contact, :gender, :country, :password)", {
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'gender': genVar.get(),
                            'country': variable.get(),
                            'password': register_pwd.get()

            })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')

        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)





genVar=StringVar()
genVar.set("Male")



country_Vars=[]
variable=StringVar()
world=open('countries.txt','r')
for country in world:
    country=country.rstrip('\n')
    country_Vars.append(country)
variable.set(country_Vars[13])


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
    font=f).grid(row=0, column=0,pady=10)

Label(
    left_frame, 
    text="Enter Number", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=10)

Label(
    left_frame, 
    text="Select Gender", 
    bg='#CCCCCC',
    font=f
    ).grid(row=2, column=0, pady=10)

Label(
    left_frame, 
    text="Select Country", 
    bg='#CCCCCC',
    font=f
    ).grid(row=3, column=0, pady=10)

Label(
    left_frame, 
    text="Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=4, column=0, pady=10)

Label(
    left_frame, 
    text="Re-Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=5, column=0, pady=10)


email_tf = Entry(
    left_frame, 
    font=f
    )

number = Entry(
    left_frame, 
    font=f
    )
pwd_tf = Entry(
    left_frame, 
    font=f,
    show='*'
    )
repwd_tf = Entry(
    left_frame, 
    font=f,
    show='*'
    )


gender_frame = LabelFrame(
    left_frame,
    bg='#CCCCCC',
    padx=10, 
    pady=10,
    )


register_name = Entry(
    left_frame, 
    font=f
    )

register_email = Entry(
    left_frame, 
    font=f
    )

register_mobile = Entry(
    left_frame, 
    font=f
    )


male_rb = Radiobutton(
    gender_frame, 
    text='Male',
    bg='#CCCCCC',
    variable=genVar,
    value='male',
    font=('Times', 10),
    
)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    bg='#CCCCCC',
    variable=genVar,
    value='female',
    font=('Times', 10),
  
)

others_rb = Radiobutton(
    gender_frame,
    text='Others',
    bg='#CCCCCC',
    variable=genVar,
    value='others',
    font=('Times', 10)
   
)

register_country = OptionMenu(
    left_frame, 
    variable, 
    *country_Vars)

register_country.config(
    width=15, 
    font=('Times', 12)
)
register_pwd = Entry(
    left_frame, 
    font=f,
    show='*'
)
pwd_again = Entry(
    left_frame, 
    font=f,
    show='*'
)

register_btn = Button(
    left_frame, 
    width=15, 
    text='Register', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)





register_email.grid(row=0, column=1, pady=10, padx=20) 
register_mobile.grid(row=1, column=1, pady=10, padx=20)
register_country.grid(row=3, column=1, pady=10, padx=20)
register_pwd.grid(row=4, column=1, pady=10, padx=20)
pwd_again.grid(row=5, column=1, pady=10, padx=20)
register_btn.grid(row=6, column=1, pady=10, padx=20)
left_frame.pack()

gender_frame.grid(row=2, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)

ws.mainloop()