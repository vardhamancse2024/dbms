import cx_Oracle
# Create a table in Oracle database
try:
con = cx_Oracle.connect('tiger/scott@localhost:1521/xe')
print(con.version)
# Now execute the sqlquery
cursor = con.cursor()
# Creating a table employee
cursor.execute("create table employee(empid integer primary key, name varchar2(30), salary
number(10, 2))")
print("Table Created successfully")
 data = [[10007, 'Vikram', 48000.0], [10008, 'Sunil', 65000.1], [10009, 'Sameer', 75000.0]]
 cur = con.cursor()
 cur.executemany('insert into employee values(:1,:2,:3)', data)
 con.commit()
 print('Multiple records are inserted successfully')
 cur.execute('select * from employee')
 rows = cur.fetchall()
 print(rows)
 cur.execute(‘update employee set salary=20000 where empno=501’)
print('one record updated successfully')
except cx_Oracle.DatabaseError as e:
print("There is a problem with Oracle", e)
# by writing finally if any error occurs
# then also we can close the all database operation
finally:
if cursor:
cursor.close()
if con:
con.close()
