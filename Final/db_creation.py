import sqlite3
conn=sqlite3.connect("project.db")
c=conn.cursor()
usernameinput="Jen"
c.execute('''CREATE TABLE user ([First Name] text,[Last Name] text, [DOB] date, [Gender] text, [State] text, [Blood Group] text, [Mobile] numeric, [Email ID] text, [Donation Details] text, [Medical Details] text, [Username] text primary key, [Password] text)''')
c.execute('''INSERT INTO user VALUES ("Jennifer","Anniston","1969-02-11","Feamle","Maharashtra","A+","9988776501","jen@gmail.com","NA","NA","Jen","jen2020")''')
conn.commit()
c.execute('''SELECT * FROM user''')
r=c.fetchall()
print(r)

c.execute('''SELECT Username FROM user''')
names={name[0] for name in c.fetchall()}
print(names)
if usernameinput in names:
   print("Username Taken")
else:
   print("Available")


c.execute('''CREATE TABLE admin ([Username] TEXT PRIMARY KEY,[Password] text)''')
conn.commit()
c.execute('''INSERT INTO admin VALUES ("Jake","jake20")''')
conn.commit()
c.execute('''INSERT INTO admin VALUES ("Sarah","sara99")''')
conn.commit()
c.execute('''SELECT * FROM admin''')
r=c.fetchall()
print(r)

c.execute('''CREATE TABLE hospital ([Hospital Name] TEXT PRIMARY KEY,[Address] text, [City] text, [State] text, [Contact Details] text)''')
conn.commit()
c.execute('''INSERT INTO hospital VALUES ("City Hospital","Road 121, Mumbai","Mumbai","Maharashtra","RMO-9008877549")''')
conn.commit()
c.execute('''SELECT * FROM hospital''')
r=c.fetchall()
print(r)

c.execute('''CREATE TABLE camps ([Date of camp] date,[Address] text, [City] text, [State] text, [Time] text, [Contact Details] text)''')
conn.commit()
c.execute('''INSERT INTO camps VALUES ("2020-05-11","Road 121, Mumbai","Mumbai","Maharashtra","10-4","RMO-9008877549")''')
conn.commit()
c.execute('''SELECT * FROM camps''')
r=c.fetchall()
print(r)

c.execute('''CREATE TABLE requests ([Receiver Name] text, [DOB] date, [Gender] text, [Blood Group] text, [City] text, [State] text, [Mobile] numeric)''')
conn.commit()
c.execute('''INSERT INTO requests VALUES ("Jack Greene","1980-12-15","Male","O+","Mumbai","Maharashtra",9005678690)''')
conn.commit()
c.execute('''SELECT * FROM requests''')
r=c.fetchall()
print(r)
