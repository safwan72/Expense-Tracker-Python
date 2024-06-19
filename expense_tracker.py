from tkinter import *
from tkinter import messagebox 
import sqlite3
import datetime
from expense_db import *
from tkinter import ttk


ws = Tk()
ws.title('Registration Page')
ws.config(bg='#0B5A81')
ws.minsize(width=700,height=500)
ws.maxsize(width=900,height=500)
f = ('Times', 14)


data=Database(db='firstdb.db')


count=0
selected_rowId=0


def saveRecord():
    global data
    data.insertRecord(email='abc@gmail.com',itemName=itemVar.get(),itemPrice=itemPriceVar.get(),purchaseDate=itemPurchaseVar.get())

def deleteRecord():
    global data
    global selected_rowId
    data.removeRecord(selected_rowId)
    refreshData()
    clearEntries()

def updateRecord():
    global selected_rowId
    selected=tv.focus()
    
    try:
        data.updateRecord(itemVar.get(),itemPriceVar.get(),itemPurchaseVar.get(),selected_rowId)       
        tv.item(selected, text="", values=(itemVar.get(),itemPriceVar.get(),itemPurchaseVar.get())) 
    except Exception as ep:
        messagebox.showerror('Error',  ep)
    item_name.delete(0, END)
    item_price.delete(0, 'end')
    item_transaction.delete(0, 'end')
    tv.after(400, refreshData)

def get_currentDate():
    date=datetime.datetime.now()
    itemPurchaseVar.set(f'{date:%d %B %Y}')

def refreshData():
    for item in tv.get_children():
      tv.delete(item)
    fetchRecords()


def selectedRowID(event):
    global selected_rowId
    selected=tv.focus()
    val=tv.item(selected,'values')
    try:
        selected_rowId=val[0] 
        d=val[4]
        itemVar.set(val[2])
        itemPriceVar.set(val[3])
        itemPurchaseVar.set(str(d))
    except Exception as ep:
        print(ep)



def fetchRecords():
    f=data.fetchRecords('select rowid,* from expense_db')
    global count
    for rec in f:
        tv.insert(parent='', index='0', iid=count, values=(rec[0],rec[1], rec[2], rec[3], rec[4]))
        count += 1
    tv.after(400, refreshData)        
    
    
def clearEntries():
    item_name.delete(0, 'end')
    item_price.delete(0, 'end')
    item_transaction.delete(0, 'end')


itemVar=StringVar()
itemPriceVar=IntVar()
itemPurchaseVar=StringVar()



second_frame = Frame(
    ws, 
    bd=2, 
    padx=10, 
    pady=10
    )

first_frame = Frame(ws)

first_frame.pack()
second_frame.pack(expand=True,fill=BOTH)



Label(
    second_frame, 
    text="Item Name", 
    font=f).grid(row=0, column=0,pady=10)
Label(
    second_frame, 
    text="Item Price", 
    font=f).grid(row=1, column=0,pady=10)

Label(
    second_frame, 
    text="Purchase Date", 
    font=f).grid(row=2, column=0,pady=10)


item_name=Entry(second_frame,font=f,textvariable=itemVar)
item_price=Entry(second_frame,font=f,textvariable=itemPriceVar)
item_transaction=Entry(second_frame,font=f,textvariable=itemPurchaseVar)


item_name.grid(row=0,column=1,padx=10)
item_price.grid(row=1,column=1,padx=10)
item_transaction.grid(row=2,column=1,padx=10)


saveRecord_btn = Button(
    second_frame, 
    width=15, 
    text='Save Record', 
    font=f, 
    cursor='hand2',
    command=saveRecord
)

TotalRecord_btn = Button(
    second_frame, 
    width=15, 
    text='Total Record', 
    font=f, 
    cursor='hand2',
    command=None
)

clearEntry_btn = Button(
    second_frame, 
    width=15, 
    text='Clear Entry', 
    font=f, 
    cursor='hand2',
    command=clearEntries
)


update_btn = Button(
    second_frame, 
    width=15, 
    text='Update', 
    font=f, 
    cursor='hand2',
    command=updateRecord
)

exit_btn = Button(
    second_frame, 
    width=15, 
    text='Exit', 
    font=f, 
    cursor='hand2',
    command=lambda:ws.destroy(), 
)

delete_btn = Button(
    second_frame, 
    width=15, 
    text='Delete', 
    font=f, 
    cursor='hand2',
    command=deleteRecord
)


currentDate_btn = Button(
    second_frame, 
    width=10, 
    text='Current Date', 
    font=f, 
    cursor='hand2',
    command=get_currentDate
)

currentDate_btn.grid(row=3,column=1,sticky=EW,padx=10)
saveRecord_btn.grid(row=0,column=2,padx=(0,10))
TotalRecord_btn.grid(row=0,column=3,padx=(0,10))
clearEntry_btn.grid(row=1,column=2,padx=(0,10))
update_btn.grid(row=1,column=3,padx=(0,10))
exit_btn.grid(row=2,column=2,padx=(0,10))
delete_btn.grid(row=2,column=3,padx=(0,10))





# tableView

tv=ttk.Treeview(first_frame,columns=(1,2,3,4,5),show='headings',height='10')
tv.pack(side=LEFT)


tv.column(1,anchor='center',stretch=NO,width=80)
tv.column(2,anchor='center')
tv.column(3,anchor='center')
tv.column(4,anchor='center')

tv.heading(1,text='Serial No')
tv.heading(2,text='Email')
tv.heading(3,text='Item Name')
tv.heading(4,text='Item Price')
tv.heading(5,text='Purchase Date')


# binding records so that upon clicking function triggers 
tv.bind("<ButtonRelease-1>",selectedRowID)



# styling tables
style=ttk.Style()
style.theme_use("default")
style.map("Treeview")


scrollbar=Scrollbar(first_frame,orient='vertical')
scrollbar.configure(command=tv.yview)
scrollbar.pack(side='right',fill='y')
tv.config(yscrollcommand=scrollbar.set)


fetchRecords()

ws.mainloop()
