import pyodbc

SERVER = '<server-address>'
DATABASE = '<database-name>'
USERNAME = '<username>'
PASSWORD = '<password>'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};
                    SERVER={SERVER};DATABASE={DATABASE};
                    UID={USERNAME};
                    PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

