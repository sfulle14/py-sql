import pyodbc

SERVER = 'DESKTOP-TVGKBDE\\SQLEXPRESS01'
DATABASE = 'Benchmark_Ohio'
USERNAME = 'test'
PASSWORD = 'password'

# connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;TrustServerCertificate=yes;'

def create_connection():
    try:
        # print(f"Attempting to connect with string: {connectionString}")
        conn = pyodbc.connect(connectionString)
        return conn
    except pyodbc.Error as e:
        # print(f"Error connecting to database: {e}")
        return None

# Instead of creating the connection immediately, use a function
conn = create_connection()

