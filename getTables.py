from connection import *

def print_all_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE'")
        tables = cursor.fetchall()
        
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(f"- {table[0]}")
        else:
            print("No tables found in the database.")
        
        cursor.close()
    except pyodbc.Error as e:
        print(f"Error fetching tables: {e}")

def table_list(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE'")
        tables = cursor.fetchall()
        tablesList = []
        
        if tables:
            print("Tables in the database:")
            for table in tables:
                tablesList.append(table[0])
        else:
            print("No tables found in the database.")
        
        cursor.close()
    except pyodbc.Error as e:
        print(f"Error fetching tables: {e}")

    return tablesList