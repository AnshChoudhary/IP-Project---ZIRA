import mysql.connector as con

mycon = con.connect(host="localhost", user="root", passwd="root", database="")
mycursor = mycon.cursor()

def enternewrecord():
    to = txtbillno.get()
    subject = txtname.get()
    content = txtdata.get()

qry = "insert into ST values
mycursor.execute(qry.format(rno, name, marks))
mycon.commit()