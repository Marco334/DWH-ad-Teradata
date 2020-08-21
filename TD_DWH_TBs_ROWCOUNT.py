#pip install teradatasql
#Script useful to extract all the DWH Table list and the related rowcount in easy way 
#IMPORTANT !! -- CHANGE  DB NAME in the query BEFORE USE IT  
import teradata
import teradatasql
import pandas as pd

print ( '\n WELCOME  \n' )

host    =  input('\nPlease insert IP Adress       :'                                                   ) 
ID_USER =  input('Please insert User ID           :'                                                   ) 
PW_USER =  input('Please insert Password          :'                                                   ) 
  
 
udaExec = teradata.UdaExec (appName="HelloWorld", version="1.0",
        logConsole=False)
 
session = udaExec.connect(method="odbc", system=host,
        username=ID_USER, password=PW_USER);
 
print( ' \n CONNESSIONE EFFETTUATA \n' )
   
#Tables and Views   
#query =" SELECT 'SELECT   '''||TRIM(DATABASENAME)|| '.' || TRIM(TABLENAME) || ''' '   ||  ' AS TABLE_NAME,COUNT(*) AS ROW_COUNT FROM ' || TRIM(DATABASENAME) || '.' || TRIM (TABLENAME) || ' '  FROM DBC.TABLES WHERE TABLEKIND IN ('T','V') ;  "  
#ONLY Tables  
#query =" SELECT 'SELECT   '''||TRIM(DATABASENAME)|| '.' || TRIM(TABLENAME) || ''' '   ||  ' AS TABLE_NAME,COUNT(*) AS ROW_COUNT FROM ' || TRIM(DATABASENAME) || '.' || TRIM (TABLENAME) || ' '  FROM DBC.TABLES WHERE TABLEKIND IN ('T') ;  "  
#To filter on specific DB , tables and views
query =" SELECT 'SELECT   '''||TRIM(DATABASENAME)|| '.' || TRIM(TABLENAME) || ''' '   ||  ' AS TABLE_NAME,COUNT(*) AS ROW_COUNT FROM ' || TRIM(DATABASENAME) || '.' || TRIM (TABLENAME) || ' '  FROM DBC.TABLES WHERE TABLEKIND IN ('T','V')  AND DATABASENAME = 'DB_NAME';  "  
 
QUERY_2 = []
#ciclo = 0
print('\n PREPARING QUERY \n') 
curr_1 =  session.execute(query)
sql_subq = pd.DataFrame(curr_1.fetchall())
sql_subq['UNION']='UNION ALL'
sql_subq1 = sql_subq[sql_subq.columns].astype(str).apply(lambda x: ' '.join(x), axis = 1)
sql_subq1 =  ' '.join(sql_subq1)

QUERY_2 =  str(sql_subq1)[:int(-9) ]
QUERY_2 = QUERY_2 + str(' ;\n')
print(QUERY_2)
#for row in session.execute(query):
#   #print(row) 
#   if ciclo != 0:
#        QUERY_2.append(str(' \n UNION ALL \n') )
#     
#   QUERY_2.append(str(row)[int(8):int(-1) ])
#   ciclo = +1
 
print('')
print('--------------------------------------------------------')
print('')
QUERY_3 = ''.join( QUERY_2 )
print(QUERY_3)
print('--------------------------------------------------------')

print('\n EXECUTING QUERY \n') 
print('\n IN THE DWH THE FOLLOWING TABLES ARE AVAILABLE,\n YOU WILL FIND THE RELATED ROWCOUNT ON THE SIDE  \n') 


curr_2 = session.execute(QUERY_3)
sql_data = pd.DataFrame(curr_2.fetchall())
print(sql_data)
print('\n\n\n')
    
  
