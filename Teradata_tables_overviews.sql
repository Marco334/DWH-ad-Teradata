-- You will be able to retrive , object type, Table rowcount , Last statistic refresh )

-- 2 QUERY
----- REMOUVE THE FLAST UNION ALL 

 SELECT CAST( SQL_TXT AS VARCHAR (1000) ) as SQL_TXT 
   FROM (SELECT 'REPLAVE VIEW TEMP_DB_INFO_V AS ( ' 
         AS SQL_TXT) as dd 
 	UNION ALL
SELECT 'SELECT   '''||TRIM(DATABASENAME)|| '.' || TRIM(TABLENAME) || ''' '   ||  ' AS TABLE_NAME,COUNT(*) AS ROW_COUNT FROM ' || TRIM(DATABASENAME) || '.' || TRIM (TABLENAME) || ' UNION ALL '  
  FROM DBC.TABLES WHERE TABLEKIND IN ('T','V')  
   AND DATABASENAME = 'TEST_DB_PAYROLL'
   
   UNION 
    SELECT CAST( SQL_TXT AS VARCHAR (1000) ) as SQL_TXT 
   FROM (SELECT '); ' 
         AS SQL_TXT) as ff 
;




           SELECT DD.TABLE_NAME                          AS TABLE_NAME  
                 ,TABLE_KIND                             AS TABLE_KIND     
                 ,ROW_COUNT                              AS ROW_COUNT      
                 ,LAST_COLLECT_S                         AS LAST_COLLECT_STAT 
                 ,FF.ACTUALSPACE                         AS ACTUALSPACE 
                 
             FROM TEMP_DB_INFO_V                         AS DD 
  LEFT OUTER JOIN (SELECT DatabaseName ||'.'|| TableName AS TABLE_NAME
                         ,MAX( LastCollectTimeStamp)     AS LAST_COLLECT_S
                     FROM DBC.STATSV
                    WHERE StatsId = 0
                      
 AND DatabaseName = 'DB_NAME'
                    GROUP BY 1 
                  ) AS ee
               ON ee.TABLE_NAME  = DD.TABLE_NAME
  LEFT OUTER JOIN (SELECT TRIM(DatabaseName) ||'.'|| TRIM(TableName) AS TABLE_NAME
                         ,SUM(CURRENTPERM)/(1024)                    AS ACTUALSPACE 
                         
                     FROM DBC.TABLESIZE
                    WHERE DATABASENAME = 'DB_NAME'  
 
                 GROUP BY 1
                  ) AS FF 
ON FF.TABLE_NAME  = DD.TABLE_NAME
;