from connection import *
from getTables import *
from getColumns import *
import os
import shutil 
from createFiles import *

def testConnection():
    if conn:
        print("Connection successful")
        # conn.close()
        return True
    else:
        print("Connection failed")
        return False

def main():
    testConnection()
    # print_all_tables(conn)
    tableList = table_list(conn)

    
    for t in tableList:
        columnList = get_columns(conn, t)
        for c in columnList:
            print(f"    {c}")



if __name__ == '__main__':
    main()
