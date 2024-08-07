from connection import *
from getTables import *
from getColumns import *
import os
import shutil 
from createFiles import *
from createInsert import *

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

    columnList = get_columns(conn, tableList[0])
    for c in columnList:
        print(f"    {c}")
    
    # for t in tableList:
    #     columnList = get_columns(conn, t)
    #     for c in columnList:
    #         print(f"    {c}")

    # clear_files()
    # for table in tableList:
    #     columnList = get_columns(conn, table)
    #     columns = [column[0] for column in columnList]

    #     insertStatment = generate_insert_statement(table, columns)
    #     write_to_file(f'{table}_insert.sql', insertStatment + '\n')



if __name__ == '__main__':
    main()
