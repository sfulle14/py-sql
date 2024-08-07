from connection import *
from getTables import *
from getColumns import *

def generate_insert_statement(table, columns, dataTypes):
    column_names = ',\n '.join(columns)

    default_values = []
    for dataType in dataTypes:
        if dataType == 'int':
            default_values.append('0')
        elif dataType == 'varchar':
            default_values.append("''")
        elif dataType == 'bit':
            default_values.append('NULL')
        elif dataType == 'money':
            default_values.append('0.00')
        elif dataType == 'data':
            default_values.append("CURRENT_DATE")
        elif dataType == 'datetime':
            default_values.append("CURRENT_TIMESTAMP")
        else:
            default_values.append('NULL')
        
    default_values_str = ',\n '.join([f"{default} AS {col}" for default, col in zip(default_values, columns)])

    insert_statement = (
        f"INSERT INTO {table} (\n {column_names}\n)\n"
        f"SELECT\n {default_values_str} \n"
        f"FROM temp_{table} t;"
    )

    return insert_statement