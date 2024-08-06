from connection import *
from getTables import *

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
        print(t)



if __name__ == '__main__':
    main()
