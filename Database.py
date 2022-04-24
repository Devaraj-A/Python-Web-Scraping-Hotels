import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='';DATABASE=Airbnb;Trusted_connection=yes')
conn.autocommit=True
cursor=conn.cursor()
#cursor.execute('CREATE DATABASE Airbnb')
#cursor.execute('Use Airbnb')
#cursor.execute('Create table hotels(ID INT,Name VARCHAR,Description VARCHAR,Rating VARCHAR,Price VARCHAR,Ref_url VARCHAR)')
#conn.commit()
