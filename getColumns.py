from getTables import table_list, conn, pyodbc

tableList = table_list(conn)

def get_columns(conn, table):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = ?", (table,))
        columns = cursor.fetchall()

        columnsList = []
        columntypeList = [[]]

        if columns:
            print(f"Columns in: {table}")
            for column in columns:
                columntypeList.append([column[0], column[1]])
        else:
            print("No columns in table.")
    except pyodbc.Error as e:
        print(f"Error fetching tables: {e}")


    return columntypeList

