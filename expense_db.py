import sqlite3




class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS expense_db(
                    email text, 
                    item_name text, 
                    item_price number, 
                    purchase_date date
                )
            ''')
        self.con.commit()
        
        
    def fetchRecords(self,query):
        self.cur.execute(query)
        rows=self.cur.fetchall()
        return rows

    def insertRecord(self,email,itemName,itemPrice,purchaseDate):
        self.cur.execute("INSERT Into expense_db VALUES (?,?,?,?)",(email,itemName,itemPrice,purchaseDate))
        self.con.commit()

    def removeRecord(self,rowName):
        self.cur.execute("DELETE from expense_db where rowid=?",(rowName,))
        self.con.commit()
        
    def updateRecord(self, item_name, item_price, purchase_date, rid):
        self.cur.execute("UPDATE expense_db SET item_name = ?, item_price = ?, purchase_date = ? WHERE rowid = ?",
                         (item_name, item_price, purchase_date, rid))
        self.con.commit()

    def __del__(self):
        self.con.close()
    
    