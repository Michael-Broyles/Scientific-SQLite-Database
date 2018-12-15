import sqlite3
from tkinter import *
from tkinter import ttk


conn = sqlite3.connect('test.db')
c = conn.cursor()


root = Tk()
# root.geometry('500x480+50+100')


label = ttk.Label(root, text="Periododic Table Database")
label.grid(row=0, column=0, columnspan=5)
label.config(foreground='black', background='yellow')
label.config(font=('Courier', 18, 'bold'))


logo = PhotoImage(file='images/microscope.png').subsample(4, 4)
label.config(image=logo)
label.config(compound='text')
label.config(compound='center')
label.config(compound='left')

label.img = logo
label.config(image=label.img)

element_number = IntVar()
element_number_entry_label = ttk.Label(root, text="Element number: ").grid(row=1, column=0)
element_number_entry = ttk.Entry(root, width = 30, textvariable = element_number).grid(row=1, column=1, pady = 5, sticky = 'w')

element_name = StringVar()
name_entry_label = ttk.Label(root, text="Element name: ").grid(row=2, column=0)
name_entry = ttk.Entry(root, width = 30, textvariable = element_name).grid(row=2, column=1, pady = 5, sticky = 'w')

element_symbol = StringVar()
symbol_entry_label = ttk.Label(root, text="Element symbol: ").grid(row=3, column=0)
symbol_entry = ttk.Entry(root, width = 30, textvariable = element_symbol).grid(row=3, column=1, pady = 5, sticky = 'w')

density = DoubleVar()
density_entry_label = ttk.Label(root, text="Element density: ").grid(row=4, column=0)
density_entry = ttk.Entry(root, width = 30, textvariable = density).grid(row=4, column=1, pady = 5, sticky = 'w')

weight = DoubleVar()
weight_entry_label = ttk.Label(root, text="Element's atomic weight: ").grid(row=5, column=0)
weight_entry = ttk.Entry(root, width = 30, textvariable = weight).grid(row=5, column=1, pady = 5, sticky = 'w')

discovered_by = StringVar()
discovered_by_entry_label = ttk.Label(root, text="Discovered by: ").grid(row=6, column=0)
discovered_by_entry = ttk.Entry(root, width = 30, textvariable = discovered_by).grid(row=6, column=1, pady = 5, sticky = 'w')

discovered_date = StringVar()
discovered_date_entry_label = ttk.Label(root, text="Date Discovered: ").grid(row=7, column=0)
discovered_date_entry = ttk.Entry(root, width = 30, textvariable = discovered_date).grid(row=7, column=1, pady = 5, sticky = 'w')


button_logo = PhotoImage(file='images/database-symbol.png')
small_logo = button_logo.subsample(60, 60)

def get_values():

    enum = str(element_number.get())
    enam = element_name.get()
    esym = element_symbol.get()
    ewe = str(weight.get())
    eden = str(density.get())
    edd = str(discovered_date.get())
    edb = discovered_by.get()

    c.execute("""CREATE TABLE IF NOT EXISTS elements (
                element_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                element_num INTEGER,
                name TEXT NOT NULL,
                symbol TEXT,
                atomic_weight REAL,
                density REAL,
                discovered_date DATE,
                discovered_by TEXT
                )""")

    c.execute("INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)VALUES ("+enum, enam, esym, ewe, eden, edd, edb+")")
    conn.commit()

    c.execute("SELECT * FROM elements")

    for row in c.fetchall():
        print(row)

    conn.close()

enter_data_button = ttk.Button(root, text="Enter Element Data",
                               command=get_values, image=small_logo, compound=LEFT).grid(row=8, column=1, pady = 10)

root.mainloop()
