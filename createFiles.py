import os
import shutil

def create_files():
    # Define the tables directory
    tables_dir = 'tables'

    # Remove the entire 'tables' directory if it exists
    if os.path.exists(tables_dir):
        shutil.rmtree(tables_dir)

    # Create a new 'tables' directory
    os.makedirs(tables_dir)

    # Function to create and write to a file
    def write_to_file(filename, content):
        file_path = os.path.join(tables_dir, filename)
        with open(file_path, 'w') as file:
            file.write(content)