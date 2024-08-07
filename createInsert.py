from connection import *
from getTables import *
from getColumns import *

def generate_insert_statement(table, columns):
    column_names = ',\n '.join(columns)
    select_columns = ',\n NULL AS '.join([f't.{col}' for col in columns])
    insert_statement = (
        f"INSERT INTO {table} (\n {column_names}\n)\n"
        f"SELECT\n NULL AS {select_columns}\n"
        f"FROM temp_{table} t;"
    )

    return insert_statement