from getTables import table_list, conn, pyodbc

tableList = table_list(conn)

def get_columns(conn, table):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = ?", (table,))
        columns = cursor.fetchall()

        columnsList = []

        if columns:
            print(f"Columns in: {table}")
            for column in columns:
                columnsList.append(column[0])
        else:
            print("No columns in table.")
    except pyodbc.Error as e:
        print(f"Error fetching tables: {e}")

    return columnsList
