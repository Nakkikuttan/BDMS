# An Amatuerish Python App to maintain Bank Client Data

1. The App shows a Log-In Screen for the empployee running the program.
2. Log-In using EmpName in the mysql table 'emp', in a seperate database 'bankdata'
    * If no such database, automatically creates database 'bankdata' and proceeds to create mysql table 'emp'
    * If database is present but no table 'emp', automatically creates
3. If the name is entered wrong, then shows pop-up to **register**
4. If the password is entered wrong then shows pop-up to try again
5. If the password is correct then the program proceeds to the Data Bank Management System
    * Then it will show options to the Main Menu and Quit from the System

## Requirements:
 #### MySQL (any version)
 #### Python 3
 #### tkinter module
## Procedure:     
   1. Install MySQL from https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.28.0.msi 
   2. Remember the password in the setup
   3. Open Python IDLE or shell or command prompt and choose your path  with\
   `cd /d {your-path}` where it is downloaded and run\
   `py -m main`\
    ![image](https://user-images.githubusercontent.com/78297271/153719381-990ec37e-e7de-4646-97e6-dfb9d867f0b6.png) \
   4. The Application will open
   

##### *Important Notes*:
* Type and save the password you chose in mysql installer in Resources/pass.txt
* If no password where changed just run the commands as in the [Procedure](https://github.com/Nakkikuttan/BDMS/edit/main/README.md#procedure)
        
