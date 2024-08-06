from connection import *

SQL_QUERY = """
SELECT 
TOP 5 c.CustomerID, 
c.CompanyName, 
COUNT(soh.SalesOrderID) AS OrderCount 
FROM 
SalesLT.Customer AS c 
LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID 
GROUP BY 
c.CustomerID, 
c.CompanyName 
ORDER BY 
OrderCount DESC;
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

