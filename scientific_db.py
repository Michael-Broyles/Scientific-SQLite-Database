# sqlite3 is used for small to medium size databases
import sqlite3
from scientific_helpers import Ele_func


# Make a connection to the DB & Creates the DB file
conn = sqlite3.connect('scientific.db')

# Create cursor that enables SQL commands
c = conn.cursor()

# CREATE TABLE
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

c.execute("""CREATE TABLE IF NOT EXISTS discovered (
            detail_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            element_id INTEGER,
            scientist_id INTEGER,
            scientist_firstname TEXT,
            scientist_lastname TEXT,
            location_discovered TEXT,
            date_discovered DATE,
            FOREIGN KEY(element_id) REFERENCES elements(element_id)
            )""")
# c.execute("""INSERT INTO discovered (
# element_id, scientist_id, scientist_firstname, scientist_lastname, location_discovered, date_discovered)
#     VALUES (1, 1, 'Robert', 'Boyle', Null, '1776')""")
conn.commit()



# DROP TABLE
# c.execute("DROP TABLE IF EXISTS elements")
# conn.commit()




# ALTER TABLE
# c.execute("ALTER TABLE elements ADD COLUMN symbol TEXT")
# c.execute("ALTER TABLE elements DROP COLUMN solid_temp REAL")
# conn.commit()



# INSERT data INTO the new TABLE
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (1, 'hydrogen', 'H', 1.00794, 0.0000899, '1766', 'Robert Boyle')""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (2, 'helium', 'He', 4.002602, 0.0001785, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (3, 'lithium', 'Li', 6.941, 0.535, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (4, 'beryllium', 'Be', 9.012182, 1.848, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (5, 'boron', 'B', 10.8111, 2.460, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (6, 'carbon', 'C', 12.0107, 2.260, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (7, 'nitrogen', 'N', 14.0067, 0.001251, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (8, 'oxygen', 'O', 15.9994, 0.001429, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (9, 'fluorine', 'F', 18.9984032, 0.0001696, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (10, 'neon', 'Ne', 20.1797, 0.000900, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (11, 'sodium', 'Na', 22.989770, 0.968, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (12, 'magnesium', 'Mg', 24.3050, 1.738, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (13, 'aluminum', 'Al', 26.981538, 2.7, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (14, 'silicon', 'Si', 28.0855, 2.330, Null, Null)""")

# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (15, 'phosphorus', 'P', 30.973761, 1.823, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (16, 'sulfur', 'S', 32.065, 1.960, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (17, 'chlorine', 'Cl', 35.453, 0.003214, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (18, 'argon', 'Ar', 39.948, 0.001784, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (19, 'potassium', 'K', 39.0983, 0.856, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (20, 'calcium', 'Ca', 40.078, 1.550, Null, Null)""")

# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (21, 'scandium', 'Sc', 44.955910, 2.985, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (22, 'titanium', 'Ti', 47.867, 4.507, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (23, 'vanadium', 'V', 50.9415, 6.110, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (24, 'chromium', 'Cr', 51.9961, 7.140, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (25, 'manganese', 'Mn', 54.938049, 7.470, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (26, 'iron', 'Fe', 55.845, 7.874, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (27, 'cobalt', 'Co', 58.9332, 8.9, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (28, 'nickel', 'Ni', 58.6934, 8.908, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (29, 'copper', 'Cu', 63.546, 8.920, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (30, 'zinc', 'Zn', 65.409, 7.140, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (31, 'gallium', 'Ga', 69.723, 5.904, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (32, 'germanium', 'Ge', 72.64, 5.323, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (33, 'arsenic', 'As', 74.92160, 5.727, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (34, 'selenium', 'Se', 78.96, 4.819, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (35, 'bromine', 'Br', 79.904, 3.120, Null, Null)""")

# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (36, 'Krypton', 'Kr', 83.798, 0.00375, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (37, 'Rubidium', 'Rb', 85.4678, 1.532, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (38, 'Strontium', 'Sr', 87.62, 2.630, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (39, 'Yttrium', 'Y', 88.90585, 4.472, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (40, 'Zirconium', 'Zr', 91.224, 6.511, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (41, 'Nibium', 'Nb', 92.90638, 8.570, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (42, 'Molybdenum', 'Mo', 95.94, 10.280, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (43, 'Technetium', 'Tc', 98, 11.5, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (44, 'Ruthenium', 'Ru', 101.07, 12.370, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (45, 'Rhodium', 'Rh', 102.90550, 12.450, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (46, 'Palladium', 'Pd', 106.42, 12.023, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (47, 'Silver', 'Ag', 107.8682, 10.490, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (48, 'Cadmium', 'Cd', 112.411, 8.650, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (49, 'Indium', 'In', 114.818, 7.310, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (50, 'Tin', 'Sn', 118.710, 7.310, Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (51, 'Antimony', 'Sb', 121.760, 6.97, Null, Null)""")

# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (52, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (53, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (54, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (55, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (56, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (57, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (58, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (59, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (60, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (61, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (62, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (63, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (64, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (65, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (66, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (67, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (68, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (69, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (70, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (71, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (72, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (73, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (74, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (75, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (76, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (77, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (78, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (79, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (80, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (81, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (82, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (83, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (84, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (85, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (86, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (87, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (88, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (89, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (90, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (91, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (92, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (93, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (94, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (95, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (96, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (97, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (98, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (99, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (100, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (101, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (102, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (103, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (104, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (105, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (106, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (107, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (108, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (109, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (110, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (111, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (112, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (113, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (114, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (115, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (116, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (117, '', '', , , Null, Null)""")
#
# c.execute("""INSERT INTO elements (element_num, name, symbol, atomic_weight, density, discovered_date, discovered_by)
#     VALUES (118, '', '', , , Null, Null)""")

conn.commit()




# UPDATE statement
# c.execute("UPDATE elements SET discovered='08-01-2015' WHERE element=2")
# c.execute("UPDATE elements SET discovered_by='John Doe' WHERE element=2")
# c.execute("UPDATE elements SET solid_temp=32 WHERE element=2")
# conn.commit()




# DELETE statement
# c.execute("DELETE FROM elements WHERE name='zinc' AND firstname ='Jane'")
# c.execute("DELETE FROM elements")
# conn.commit()




# SELECT statement
c.execute("SELECT * FROM elements")
# c.execute("SELECT * FROM discovered")
# c.execute("SELECT * FROM elements WHERE discovered < '11-20-2018' ORDER BY discovered")
# c.execute("SELECT * FROM elements WHERE element=13")
# c.execute("SELECT element, name, density FROM elements WHERE name='gold'")
# c.execute("SELECT element, name, density FROM elements WHERE density > 1 ORDER BY density")



# FETCH statement
# print(c.fetchone())
# print(c.fetchmany(5))
# print(c.fetchall())
for row in c.fetchall():
    print(row)




# Closes the DB after use
conn.close()

