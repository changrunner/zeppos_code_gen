zeppos_logging (1.0.7)
-- WatchTower>=0.8.0
-- deprecated>=1.2.10
-- cachetools = ">=4.1.1"  

-----
zeppos_core (1.0.7)
-- zeppos_logging>=1.0.7
-- -- WatchTower>=0.8.0
-- -- deprecated>=1.2.10
-- -- cachetools = ">=4.1.1" 

-----
zeppos_root (0.0.11)
-- zeppos_core (1.0.7) 
-- -- zeppos_logging>=1.0.7
-- -- -- WatchTower>=0.8.0
-- -- -- deprecated>=1.2.10
-- -- -- cachetools = ">=4.1.1" 

-----
zeppos_git (0.0.5)
-- gitpython = ">=3.1.13"
-- zeppos_root (0.0.11)
-- -- zeppos_core (1.0.7) 
-- -- -- zeppos_logging>=1.0.7
-- -- -- -- WatchTower>=0.8.0
-- -- -- -- deprecated>=1.2.10
-- -- -- -- cachetools = ">=4.1.1" 

-----
zeppos_application (0.0.8)
-- zeppos_git (0.0.5)
-- -- gitpython = ">=3.1.13"
-- -- zeppos_root (0.0.11)
-- -- -- zeppos_core (1.0.7) 
-- -- -- -- zeppos_logging>=1.0.7
-- -- -- -- -- WatchTower>=0.8.0
-- -- -- -- -- deprecated>=1.2.10
-- -- -- -- -- cachetools = ">=4.1.1" 

zeppos_ms_sql_server_proxy (0.0.4)
-- requests = ">=2.25.1"
-- pandas = ">=1.2.1"

zeppos-file-manager(0.0.32)
-- zeppos_core (1.0.7)
-- -- zeppos_logging>=1.0.7
-- -- -- WatchTower>=0.8.0
-- -- -- deprecated>=1.2.10
-- -- -- cachetools = ">=4.1.1" 

zeppos-data-manager(0.0.16) -- 3.7
-- pandas = ">=1.1.4"
-- tzwhere = ">=3.0.3"

zeppos-bcpy (0.0.39)
-- zeppos-file-manager = ">=0.0.32"
-- -- zeppos_core (1.0.7)
-- -- -- zeppos_logging>=1.0.7
-- -- -- -- WatchTower>=0.8.0
-- -- -- -- deprecated>=1.2.10
-- -- -- -- cachetools = ">=4.1.1" 
-- zeppos-data-manager = ">=0.0.16"
-- -- pandas = ">=1.1.4"
-- -- tzwhere = ">=3.0.3"
-- pyodbc = ">=4.0.30"


zeppos-csv (0.0.28)
-- zeppos-bcpy (0.0.39)
-- -- zeppos-file-manager = ">=0.0.32"
-- -- -- zeppos_core (1.0.7)
-- -- -- -- zeppos_logging>=1.0.7
-- -- -- -- -- WatchTower>=0.8.0
-- -- -- -- -- deprecated>=1.2.10
-- -- -- -- -- cachetools = ">=4.1.1" 
-- -- zeppos-data-manager = ">=0.0.16"
-- -- -- pandas = ">=1.1.4"
-- -- -- tzwhere = ">=3.0.3"
-- -- pyodbc = ">=4.0.30"

zeppos-microsoft-sql-server (0.0.23)
-- sqlalchemy = ">=1.2.17"
-- zeppos-csv (0.0.28)
-- -- zeppos-bcpy (0.0.39)
-- -- -- zeppos-file-manager = ">=0.0.32"
-- -- -- -- zeppos_core (1.0.7)
-- -- -- -- -- zeppos_logging>=1.0.7
-- -- -- -- -- -- WatchTower>=0.8.0
-- -- -- -- -- -- deprecated>=1.2.10
-- -- -- -- -- -- cachetools = ">=4.1.1" 
-- -- -- zeppos-data-manager = ">=0.0.16"
-- -- -- -- pandas = ">=1.1.4"
-- -- -- -- tzwhere = ">=3.0.3"
-- -- -- pyodbc = ">=4.0.30"

zeppos-api (0.0.3)
-- zeppos_application (0.0.8)
-- -- zeppos_git (0.0.5)
-- -- -- gitpython = ">=3.1.13"
-- -- -- zeppos_root (0.0.11)
-- -- -- -- zeppos_core (1.0.7) 
-- -- -- -- -- zeppos_logging>=1.0.7
-- -- -- -- -- -- WatchTower>=0.8.0
-- -- -- -- -- -- deprecated>=1.2.10
-- -- -- -- -- -- cachetools = ">=4.1.1"
-- psutil
-- flask-restful = ">===0.3.8"
-- flasgger = ">===0.9.5"

