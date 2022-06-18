# from sre_parse import expand_template
# from tkinter import *
# import sqlite3
# root=Tk()

# root.title('Datatbase Addresss Book')


# #create a database or connect to one

# conn = sqlite3.connect('address_book.db')


# c = conn.cursor()


# c.execute(""" CREATE TABLE address(
#     first_name text,
#     last_name text, 
#     address text, 
#     city text, 
#     state text, 
#     zipcode integer
#     )""")
# print("TABLE created successfully")

# conn.commit()
# conn.close()
# root.mainloop()




# from tkinter import *

# import sqlite3
# from tkinter import messagebox

# root = Tk()
# root.tile('Message Box')

# conn = sqlite3.connect('address-book.db')
# c = conn.cursor()







# def submit():
#    e.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)", {
#         'f_name': f_name.get(),
#         'l_name': l_name.get(),
#         'address': address.get(),
#         'city': city.get(),
#         'state': state.get(),
#         'zipcode': zipcode.get()})
#     messagebox.showinfo("Addresses", "Inserted suscessfully")
#     conn.commit()
#     conn.close()


# conn.commit()
# conn.close()
#     #CLEAR THE TEXT BOXES
#     f_name.delete(0,END)
#     l_name.delete(0,END)
#     address.delete(0,END)
#     city.delete(0,END)
#     state.delete(0,END)
#     zipcode.delete(0,END)


#     #CREATE TEXT BOXES
# f_name = Entry(root, width=30)
# f_name.grid(row=0,column=1, padx = 20)

# l_name = Entry(root, width=30)
# l_name.grid(row=1, column= 1)

# address = Entry(root, width=30)
# address.grid(row=2, column=1)

# city = Entry(root, width=30)
# city.grid(row=3, column=1)

# state = Entry(root, width=30)
# state.grid(row=3, column=1)

# zipcode = Entry(root, width=30)
# zipcode.grid(row=4, column=1)



# f_name_label = Label(root, text="First name")
# f_name_label.grid(row=0, column=0)



# l_name_label = Label(root, text="Last name")
# l_name_label.grid(row=1, column=0)


# address_label = Label(root, text="Address")
# address_label.grid(row=2, column=0)


# city_label = Label(root, text="City")
# city_label.grid(row=3, column=0)


# state_label = Label(root, text="State")
# state_label.grid(row=3, column=0)



# submit_btn = Button(root, text="Add Records")
# submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx= 100)

# conn.commit()

# conn.close()




# Suyogya
# Suyogya Dhoj Adhikary
# from tkinter import *
# import sqlite3 
# from tkinter import messagebox
# root= Tk()

# conn= sqlite3.connect("address_book.db")
# c=conn.cursor()

# # c.execute(""" CREATE TABLE addresses(
# #     first_name text,
# #     last_name text,
# #     address text,
# #     city text,
# #     state text,
# #     zipcode integer
# # )""")
# # print("Table created successfully")

# def submit():
#     conn=sqlite3.connect("address_book.db")
#     c=conn.cursor()

#     c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",{
#         "f_name":f_name.get(),
#         "l_name":l_name.get(),
#         "address":address.get(),
#         "city":city.get(),
#         "state":state.get(),
#         "zipcode":zipcode.get()
#     })
#     messagebox.showinfo("Addresses","Inserted successfully")
#     conn.commit()
#     conn.close()

#     f_name.delete(0,END)
#     l_name.delete(0,END)
#     address.delete(0,END)
#     city.delete(0,END)
#     state.delete(0,END)
#     zipcode.delete(0,END)

# def query():
#     conn= sqlite3.connect("address_book.db")
#     c=conn.cursor()

#     c.execute("SELECT *, oid from addresses")
    
#     records=c.fetchall()
#     print(records)

#     conn.commit()
#     conn.close()

# f_name = Entry(root, width=30)
# f_name.grid(row=0, column=1, padx=20)

# l_name = Entry(root, width=30)
# l_name.grid(row=1, column=1)

# address = Entry(root,width=30)
# address.grid(row=2, column=1)

# city = Entry(root,width=30)
# city.grid(row=3, column=1)

# state = Entry(root,width=30)
# state.grid(row=4, column=1)

# zipcode = Entry(root,width=30)
# zipcode.grid(row=5, column=1)

# f_name_label= Label(root, text="First Name")
# f_name_label.grid(row=0, column=0)

# l_name_label= Label(root, text="Last Name")
# l_name_label.grid(row=1, column=0)

# address_label= Label(root, text="Address")
# address_label.grid(row=2, column=0)

# city_label= Label(root, text="City")
# city_label.grid(row=3, column=0)

# state_label= Label(root, text="State")
# state_label.grid(row=4, column=0)

# zipcode_label= Label(root, text="Zipcode")
# zipcode_label.grid(row=5, column=0)

# submit_btn = Button(root,text="Add Records", command=submit)
# submit_btn.grid(row=6,column=0, columnspan=2, pady=10,padx=10, ipadx=100)

# query_button = Button(root, text="Show Records",command=query)
# query_button.grid(row=7,column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# conn.commit()
# conn.close()

# root.mainloop()





from tkinter import *
import sqlite3 
from tkinter import messagebox
root= Tk()

conn= sqlite3.connect("address_book.db")
c=conn.cursor()

c.execute(""" CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)""")
print("Table created successfully")
conn.commit()
conn.close()
mainloop()


def submit():
    conn=sqlite3.connect("address_book.db")

    c=conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",{
        "f_name":f_name.get(),
        "l_name":l_name.get(),
        "address":address.get(),
        "city":city.get(),
        "state":state.get(),
        "zipcode":zipcode.get()
    })
    messagebox.showinfo("Addresses","Inserted successfully")
    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def query():
    conn= sqlite3.connect("address_book.db")
    c=conn.cursor()

    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    print(records)
    print_records = ''
    for i in records:
        print_records += str(record[6])+":-"+record[0] + \
            " "+str(record[1])+","+"\t" + str(record[4])+"\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0,columnspan=2)        
    
    records=c.fetchall()
    print(records)

    conn.commit()
    conn.close()

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root,width=30)
address.grid(row=2, column=1)

city = Entry(root,width=30)
city.grid(row=3, column=1)

state = Entry(root,width=30)
state.grid(row=4, column=1)

zipcode = Entry(root,width=30)
zipcode.grid(row=5, column=1)

zipcode = Entry(root,width=30)
zipcode.grid(row=9,column=1, pady=5)


f_name_label= Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label= Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label= Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label= Label(root, text="City")
city_label.grid(row=3, column=0)

state_label= Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label= Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

f_name_editor = Entry(editor, width=30)
f_name_editor.grid(row=0,column=1, padx = 20, pady= (10,0))


submit_btn = Button(root,text="Add Records", command=submit)
submit_btn.grid(row=6,column=0, columnspan=2, pady=10,padx=10, ipadx=100)

query_button = Button(root, text="Show Records",command=query)
query_button.grid(row=7,column=0, columnspan=2, padx=10, pady=10, ipadx=100)


query_btn = Button(root,text= "Show Records", command=query)
query_btn.grid(row=7,column=0,)
conn.commit()
conn.close()


root.mainloop()
