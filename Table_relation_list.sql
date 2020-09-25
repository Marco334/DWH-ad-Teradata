-- Quali tabelle hanno chiavi esterne e con quali altre ?
-- Tables having FK belonging as PK to other tables (rleations )
SELECT DISTINCT ChildDB || '.' || ChildTable AS ForeignTable 
               ,ParentDB || '.' || ParentTable AS PrimaryTable
                 
           FROM DBC.All_RI_ChildrenV
		   
          WHERE ChildDB NOT IN ('All', 'Crashdumps', 'DBC', 'dbcmngr', 
              'Default', 'External_AP', 'EXTUSER', 'LockLogShredder', 'PUBLIC',
              'Sys_Calendar', 'SysAdmin', 'SYSBAR', 'SYSJDBC', 'SYSLIB', 
              'SystemFe', 'SYSUDTLIB', 'SYSUIF', 'TD_SERVER_DB', 'TDStats',
              'TD_SYSGPL', 'TD_SYSXML', 'TDMaps', 'TDPUSER', 'TDQCD',
              'tdwm', 'SQLJ', 'TD_SYSFNLIB', 'SYSSPATIAL')
      ORDER BY 1,2;
