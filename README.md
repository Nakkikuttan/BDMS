# An Amatuerish Python App to maintain Bank Client Data

1. The App shows a Log-In Screen for the employee running the program.
2. Log-In using EmpName in the mysql table 'emp', in a seperate database 'bankdata'
    - If no such database, automatically creates database 'bankdata' and proceeds to create mysql table 'emp'
    - If database is present but no table 'emp', automatically creates
3. If the name is entered wrong, then shows pop-up to **register**
4. If the password is entered wrong then shows pop-up to try again
5. If the password is correct then the program proceeds to the Data Bank Management System
    - Then it will show options to the Main Menu and Quit from the System


## To-Read
<details>
<summary>Requirements:</summary>

#### Database
- ##### [MySQL](https://mysql.com)
        
    Any Version of MySQL is Ok but mysql_native_password in 
    [this](https://github.com/Nakkikuttan/BDMS/blob/662d90d9692d1c79046616121f26df06401a9401/app.py#L22) line of [app](/app.py) is depreciated in MySQL 5.7 and after.\
    The code will run nonetheless but is better to remove it and all its occurences if you have MySQL 5.7 and after.

- ##### [Python 3](https://python.org)
        
    The Application is made mostly made of Python. So the code will not run if it is not present.\
    Please Download it.

- ##### [tkinter module](https://docs.python.org/3/library/tk.html)
        
    The Application's GUI is powered by tkinter module of Python and comes with Python when it is downloaded.\
    If not present please run\
    ``py -m pip tk``\
    in your shell or command prompt

</details>

### Procedure:     
   1. Remember the password in the MySQL setup
   2. Open Python IDLE or shell or command prompt and choose your path  with `cd /d {your-path}` where it is downloaded and run\
   `py -m main` 
   
   3. The Application will open
   4. Try it out!
   

##### *Important Notes*:
* Type and save the password you chose in mysql installer in Resources/pass.txt
* If no password where changed just run the commands as in the [Procedure](https://github.com/Nakkikuttan/BDMS/edit/main/README.md#procedure)
        
