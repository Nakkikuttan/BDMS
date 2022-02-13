import mysql.connector as msc
from app import *

fir_con=msc.connect(host='localhost',user='root',passwd=f'{pss}',auth_plugin=mnp)
fir_cursor=fir_con.cursor(buffered=True)

create1="create table emp(EmpName varchar(20) not null primary key,EmpPass varchar(20) not null)"

while True:
    try:
        fir_cursor.execute('use bankdata')
        print('Using Database: bankdata')
        try:
            fir_cursor.execute('select * from emp')
            print('Affirmed Table: emp\nMySQL is connected!!\n')
        except msc.Error:
            fir_cursor.execute(create1)
            print('Created Table: emp\nMySQL is connected!!!\n')
    except msc.Error:
        fir_cursor.execute('create database bankdata')
        fir_cursor.execute('use bankdata')
        print('Created Database: bankdata')
        fir_cursor.execute(create1)
        fir_cursor.execute('select * from emp')
        print('Created Table: emp')
        if fir_con.is_connected()==True:
            print('MySQL is Connected!!!\n')
    print('Initialisation Done.... Please Log-In!!\n')
    break


def registernew():
    new=tk.Toplevel(lr)
    new.title('Register Now')
    new.geometry('350x200')
    new.configure(bg=bgw)

    frmrn=tk.Frame(new)
    frmrn.pack()

    lblrn=tk.Label(frmrn,image=img3)
    lblrn.pack(fill=tk.BOTH)

    Label(lblrn,text="Please Enter your username:",
    bg=bgc,fg=fgc).place(x=20,y=40)

    namer=tk.StringVar()
    nameE=tk.Entry(lblrn,textvariable=namer,bg=bgc,
    width=40)
    nameE.place(x=20,y=70)

    Label(lblrn,text="Please Enter your password",
    bg=bgc,fg=fgc).place(x=20,y=100)

    passr=tk.StringVar()
    passE=tk.Entry(lblrn,textvariable=passr,bg=bgc,show='*')
    passE.place(x=20,y=130)


    def backtologin():
        namer_=namer.get()
        passr_=passr.get()
        print(namer_,passr_)
        query=f"insert into emp values('{namer_}','{passr_}')"
        fir_cursor.execute(query)
        fir_con.commit()
        new.destroy()
    brn=tk.Button(lblrn, text='Register',width=10,
    bg='blue',command=backtologin)
    brn.place(x=80,y=160)

    Button(lblrn,text='Back', bg='blue',fg='white',
    width=10,command=new.destroy).place(x=170,y=160)

def login():
    global lr
    lr=tk.Tk()
    lr.title('Login/Register Page ⤵')
    lr.geometry('680x421')
    lr.configure(bg=bgw)

    global img3
    img3=tk.PhotoImage(file='Resources/bank3.png')

    frml=tk.Frame(lr)
    frml.pack()

    lbl=tk.Label(frml,image=img3)
    lbl.pack(fill=tk.BOTH)
    
    lblL=tk.Label(lbl, bg=bgc, width=70, height=21)
    lblL.place(x=95,y=45)

    Label(lblL,text='Log-In/Register⤵',
    bg=bgc,fg=fgc,font=('Times New Roman',20),
    width=20, height=3
    ).place(x=5,y=20)

    Nlbl=tk.Label(lbl,text='Enter your Name:',width=18,bg=bgc)
    Nlbl.place(x=95,y=150)

    lname=tk.StringVar()
    tname=tk.Entry(lbl,relief='sunken',textvariable=lname,
    borderwidth=2,width=40,
    bg='lightblue'
    )
    tname.place(x=115,y=170)
 
    Plbl=tk.Label(lbl,text='Enter your password:', width=20, bg=bgc)
    Plbl.place(x=95,y=200)
    lpass=tk.StringVar()
    tpass=tk.Entry(lbl,relief='sunken',textvariable=lpass,
    borderwidth=2,width=40,
    bg='lightblue',show='*'
    )
    tpass.place(x=115,y=220)
    

    def loginsuccs():
        global lpass_
        global lname_
        lname_=lname.get()
        lpass_=lpass.get()
        query=f"select emppass from emp where empname='{lname_}'"
        fir_cursor.execute(query)
        queryresult=fir_cursor.fetchone()
        if queryresult!=None:
            pssfromemp=''.join(queryresult)
            if  pssfromemp==lpass_:
                fir_con.close()
                #mycursor.execute(f'alter user "localhost"@"root" set new_password={pss}')
                lr.destroy()
                pressmainM()
            else:
                rn=tk.Toplevel(lr)
                rn.title('Login Failure!!')
                rn.geometry('300x80')
                rn.configure(bg=bgw)

                frmrn=tk.Frame(rn)
                frmrn.pack()

                rlbl=tk.Label(frmrn,image=img3)
                rlbl.pack(fill=tk.BOTH)
                Label(rlbl,
                text=f"Wrong Password\nPlease Register or Try Again!!",
                bg=bgc,fg=fgc).place(x=65,y=5)

                def gotoregister():
                    tpass.delete(0,END)
                    tname.delete(0,END)
                    rn.destroy()
                    registernew()

                rbtn=tk.Button(rlbl,text='Register Now!!',
                relief='raised', bg='blue',fg='white',
                width=10,command=gotoregister)
                rbtn.place(x=55,y=45)

                Button(rlbl,text='Back',bg='blue',fg='white',
                width=10,command=rn.destroy
                ).place(x=150,y=45)
        else:
            rn=tk.Toplevel(lr)
            rn.title('Login Failure!!')
            rn.geometry('300x80')
            rn.configure(bg=bgw)

            frmrn=tk.Frame(rn)
            frmrn.pack()

            rlbl=tk.Label(frmrn,image=img3)
            rlbl.pack(fill=tk.BOTH)
            Label(rlbl,
            text=f"Wrong Username '{lname_}'\nPlease Register or Try Again!!",
            bg=bgc,fg=fgc).place(x=65,y=5)

            def gotoregister():
                tpass.delete(0,END)
                tname.delete(0,END)
                rn.destroy()
                registernew()

            rbtn=tk.Button(rlbl,text='Register Now!!',
            relief='raised', bg='blue',fg='white',
            width=10,command=gotoregister)
            rbtn.place(x=55,y=45)
            
            Button(rlbl,text='Back',bg='blue',fg='white',
            width=10,command=rn.destroy
            ).place(x=150,y=45)

    #Function and Button to Update Record
    blogin=tk.Button(lbl,text='Login',
    bg='lightblue',relief='raised',borderwidth=2,height=1,
    width=15,command=loginsuccs
    )
    blogin.place(x=230,y=280)
 
    breg=tk.Button(lbl,text='Register', bg='lightblue',
    relief='raised',borderwidth=2,height=1,
    width=15,command=registernew
    )
    breg.place(x=360,y=280)

    def exit():
        print('Exiting Log-In Page.... Done!')
        lr.destroy()
    bq=tk.Button(lbl,text='Exit',bg='blue',fg='white',
    relief='raised',borderwidth=2,width=10,command=exit)
    bq.place(x=305,y=320)
    lr.mainloop()

login()