from connection import create_connection

def main():
    conn = create_connection()
    if conn:
        print("Connection successful")
        # Use the connection here
        conn.close()
        return True
    else:
        print("Connection failed")
        return False

if __name__ == '__main__':
    result = main()
    print(f"Connection test result: {result}")
    