#Start of app.py
############################################################

#Please check intendation

#importing modules and its components
import os
import tkinter as tk
import mysql.connector as msc
from tkinter import *
from dotenv import load_dotenv

#load_dotenv()
#pss=os.getenv('Pass')
path=os.path.abspath('Resources/pass.txt')
with open(path,'r') as f:
    global pss
    pss=f.read().strip("'").strip('"')

#Connecting to MySQL Server with Existing Database 'bankdata'
#Please use the latest version of mysql
mnp='mysql_native_password'

create2='create table cdata(CustomerName varchar(30) not null primary key,\
CustomerID int not null,AccountNo int not null, Balance decimal(15,2) not null default 0.00,\
Address varchar(50),PhoneNo int not null,AadhaarNo int not null)'

trycon=msc.connect(host='localhost',user='root',passwd=f'{pss}',db='bankdata',auth_plugin=mnp)
trycur=trycon.cursor()

def pressmainM():
    while True:
        #1)Checking if Database 'bankdata' exists 
        # and creates Table 'cdata' if missing
        #2)Creates Database 'bankdata' if missing and 
        # creates Table 'cdata'
        global mycon
        global mycursor
        try:
            trycur.execute('select * from cdata')
            trycon.close()
            mycon=msc.connect(host='localhost',user='root',
            passwd=f'{pss}',db='bankdata',auth_plugin=mnp
            )
            print('Table "cdata" Present\n')
        except msc.Error:
            trycur.execute(create2)
            trycon.close()
            mycon=msc.connect(host='localhost',user='root',
            passwd=f'{pss}',db='bankdata',auth_plugin=mnp
            )
            print('Created Table: cdata\n')
        mycursor=mycon.cursor()
        print('Logged-In\nGood to go!!')
        app()
        break

#Common
dimen='724x408' #Dimensions for most of the windows
bgw='#331dad'	#Colour for background of all windows
bgc='#88cffa'   #Colour for background of most of the Labels and Entry,
                #Text boxes
fgc='#5c19e3'	#Colour for the texts in some sections of the window
 
def add():
    #Sub-Level to root
    global add_scrn
    add_scrn=tk.Toplevel(root)
    add_scrn.title('Add Data! ⤵')
    add_scrn.geometry(dimen)
    add_scrn.configure(bg=bgw)
 
    #Frame to hold the Label with image
    frm1=tk.Frame(add_scrn)
    frm1.pack()
    lbl=tk.Label(frm1,image=img2)
    lbl.pack(fill=tk.BOTH)
 
    #Labels that hold the Contents
    lbladd=tk.Label(lbl,text='The Required Details of The Client are ⤵',
    bg=bgc,fg=fgc,
    height=2,width=35,font=('Times New Roman',18,'bold')
    )
    lbladd.place(x=120,y=6)
 
    #To distinguish the Order and Limit of each field
    lbldetails=tk.Label(lbl,text="Customer Name(20 Characters),Customer ID(11 Digits), Account No.(12-16 Digits),\nBalance(15 Digits), Address(50 Characters), Phone No.(10 Digits), Aadhaar No.(16 digits)",
    width=70,height=2,
    bg='lightblue',fg=fgc
    )
    lbldetails.place(x=120,y=52)
 
 
    #--START OF ENTRY PART--#
    #########################
    lbla=tk.Label(lbl,bg=bgc, height=20,width=70)
    lbla.place(x=120,y=85)
    #########################
    Label(lbl,bg=bgc,
    text='Please Enter the Details Below ⤵').place(x=125, y=92)
 
    #Customer Name(CN)
 
    lCN=tk.Label(master=lbl, text='Customer Name', bg=bgc)
    lCN.place(x=170,y=115)
    tCN=tk.StringVar()
    eCN=tk.Entry(master=lbl,textvariable=tCN, width=50, bg='lightblue')
    eCN.place(x=270,y=115)
 
    #Customer ID
    lCId=tk.Label(master=lbl, text='Customer ID',bg=bgc)
    lCId.place(x=170,y=140)
    tCId=tk.IntVar()
    tCId.set('')
    eCId=tk.Entry(master=lbl,textvariable=tCId, width=50,bg='lightblue')
    eCId.place(x=270,y=140)
 
    #Account Number
    lAcN=tk.Label(master=lbl, text='Account No',bg=bgc)
    lAcN.place(x=170,y=165)
    tAcN=tk.IntVar()
    tAcN.set('')
    eAcN=tk.Entry(master=lbl,textvariable=tAcN, width=50 ,bg='lightblue')
    eAcN.place(x=270,y=165)
 
    #Balance
    lBa=tk.Label(master=lbl, text='Balance',bg=bgc)
    lBa.place(x=170,y=190)
    tBa=tk.IntVar()
    tBa.set('')
    eBa=tk.Entry(master=lbl,textvariable=tBa, width=50,bg='lightblue')
    eBa.place(x=270,y=190)
 
    #Address
    lAdd=tk.Label(master=lbl, text='Address\n\n\n',bg=bgc)
    lAdd.place(x=170,y=215)
    tAdd=StringVar()
    eAdd=tk.Entry(master=lbl,textvariable=tAdd, width=45, bg='lightblue')
    eAdd.place(x=270,y=215)
 
    #Phone No
    lPN=tk.Label(master=lbl, text='Phone No', bg=bgc)
    lPN.place(x=170,y=265)
    tPN=tk.IntVar()
    tPN.set('')
    ePN=tk.Entry(master=lbl,textvariable=tPN, width=50,bg='lightblue')
    ePN.place(x=270,y=265)
 
    #Aadhaar No
    lAAD=tk.Label(master=lbl, text='Aadhaar No',bg=bgc)
    lAAD.place(x=170,y=290)
    tAAD=tk.IntVar()
    tAAD.set('')
    eAAD=tk.Entry(master=lbl,textvariable=tAAD, width=50, bg='lightblue')
    eAAD.place(x=270,y=290)
    #######################
    #--END OF ENTRY PART--#
 
    #Function to store the values entered into variables
    #and to be executed in query
    def detailrec():
        #Window for showing that the query is inserted into table
        succs=tk.Toplevel(add_scrn)
        succs.title('Success')
        succs.geometry('300x80')
        succs.configure(bg=bgw)
 
        #Assigning Variables to the Values of the Entries that was entered
        tCN_=tCN.get()
        tCId_=tCId.get()
        tAcN_=tAcN.get()
        tBa_=tBa.get()
        tAdd_=tAdd.get()
        tPN_=tPN.get()
        tAAD_=tAAD.get()
        query=f"insert into cdata values('{tCN_}',{tCId_},{tAcN_},{tBa_},\
        '{tAdd_}',{tPN_},{tAAD_})"
        mycursor.execute(query)
        mycon.commit()
 
        #Set the Entry Spaces to blank
        eCN.delete(0, END)
        eCId.delete(0, END)
        eAcN.delete(0, END)
        eBa.delete(0, END)
        eAdd.delete(0, END)
        ePN.delete(0, END)
        eAAD.delete(0, END)
 
        #Layout and button for the pop-up
        Label(succs,
        text='Data Added to Database!\nPlease Press "Back" to return to Add Data Page',
        bg=bgc,
        fg='darkgreen'
        ).pack()
 
        Button(succs,text='OKay!',relief='raised',bg='blue',
        fg='white',borderwidth=2,width=20,
        command=succs.destroy
        ).pack()
 
    
    #Submit and Back Buttons
    #Creating the submit button
    btnS=tk.Button(master=lbl, text='Submit',
    bg='lightblue', relief='raised',width=15,
    command=detailrec
    )
    btnS.place(x=235,y=340)
 
    #Creating the back button and function to return to main menu
    def closeadd():
        add_scrn.destroy()
        mainM()
    btnB=tk.Button(master=lbl, text='Back',
    bg='blue',fg='white',relief='raised',width=10,
    command=closeadd
    )
    btnB.place(x=365,y=340)
 
def display():
    #Sub-Level to root
    dis=tk.Toplevel(root)
    dis.title('Details Recorded ⤵')
    dis.geometry(dimen)
    dis.configure(bg=bgw)
 
    #layout for disframe
    disframe=tk.Frame(dis)
    disframe.pack()
    lbl=tk.Label(disframe, image=img2)
    lbl.pack(fill=tk.BOTH)
 
    #Label Layout
    lbld=tk.Label(lbl, height=26,width=100)
    lbld.place(x=7,y=7)
 
    dislbl=tk.Label(lbl,
    text='The Stored Details Are ⤵',
    font=('Times New Roman',18),fg=fgc, width=35
    )
    dislbl.place(x=110,y=9)
 
    Label(lbl,
    text='In the Order\nCustomer Name, Customer ID, Account No.,\
    Balance, Address, Phone No., Aadhaar No.',
    fg=fgc,
    width=90,
    ).place(x=10,y=40)
 
    #Text box to show the Result
    disT=tk.Text(lbld,
    bg=bgc,
    fg=fgc,
    height=10,
    width=86,
    highlightthickness=2,
    relief='sunken',
    spacing1=2,
    wrap=WORD
    )
    disT.place(x=4,y=70)
 
 
    #Gathering the Data from the DB Table
    mycursor.execute('select * from cdata')
    allD=mycursor.fetchall()
 
    nextline=1.0
 
    #Displaying the Data
    for x in allD:
        n=1
        n*=0.1
        i=n+nextline
        disT.insert(f'{i}',x)#inserting in vertical
        disT.insert(END,'\n')#inserting escape sequence at end of each entry
        nextline+=1.0
        n+=1
 
    #Function and button to close and return to Main Menu
    def closedisplay():
        dis.destroy()
        mainM()
 
    sbtn=tk.Button(lbl,text='Okay!',
    relief='raised',bg='blue',fg='white',
    borderwidth=2,height=1,width=60,
    command=closedisplay
    )
    sbtn.place(x=155,y=360)
 
 
def search():
    #Sub-Level to root
    srch=tk.Toplevel(root)
    srch.title('Name To Search ⤵')
    srch.geometry('300x100')
    srch.configure(bg=bgw)
 
    #Label For Client Name
    srchl=tk.Label(srch,
    text='Enter the Name of the Client :(Case-Sensitive)',
    bg=bgc,fg=fgc
    )
    srchl.pack()
 
    #Entry field for Client Name
    global tsrche
    tsrche=tk.StringVar()
    srche=tk.Entry(srch,relief='sunken',textvariable=tsrche,
    borderwidth=2,width=40,
    bg='lightblue'
    )
    srche.pack()
 
    #Function and Button To  call search_mainM
    def gosearch():
        srch.destroy()
        search_mainM()
    bsrch=tk.Button(srch,text='Search For The Record',
    bg='lightblue',relief='raised',borderwidth=2,height=1,
    width=20,command=gosearch)
    bsrch.place(x=23,y=60)
 
    #Function and Button to close and return to Main Menu
    def closesearch():
        srch.destroy()
        mainM()
    csrch=tk.Button(srch,text='Back', bg='blue',fg='white',
    relief='raised',borderwidth=2,height=1,
    width=10,command=closesearch
    )
    csrch.place(x=195,y=60)
 
def search_mainM():
    #Sub-Level to root
    global srch_mainM
    srch_mainM=tk.Toplevel(root)
    srch_mainM.title('Search Result ⤵')
    srch_mainM.geometry(dimen)
    srch_mainM.configure(bg=bgw)
 
    #Window for search_mainM
    srch_frame=tk.Frame(srch_mainM)
    srch_frame.pack()
    lbl=tk.Label(srch_frame, image=img2)
    lbl.pack(fill=tk.BOTH)
 
    #Label layout
    lbls=tk.Label(lbl, height=26,width=100)
    lbls.place(x=7,y=7)
 
    lblt=tk.Label(lbl,
    text='The Details of The Client Requested are ⤵',
    font=('Times New Roman',18),fg=fgc, width=35
    )
    lblt.place(x=110,y=9)
 
    Label(lbl,
    text='In the Order\nCustomer Name, Customer ID, Account No.,Balance, Address, Phone No., Aadhaar No.',
    fg=fgc,
    width=90,
    ).place(x=10,y=40)
 
 
    #TextBox to hold the Result
    stb=tk.Text(lbls,bg=bgc,fg=fgc,height=10,
    width=86,highlightthickness=2,
    relief='sunken',
    wrap=WORD
    )
    stb.place(x=4,y=73)
 
    #To get what was entered
    #Checks if CustomerName exists
    #else shows 'No such Client' in TextBox 'stb'
    tsrche_=tsrche.get()
    mycursor.execute(f"select * from cdata where CustomerName='{tsrche_}'")
    sD=mycursor.fetchone()
    if sD!=None:
        stb.insert(INSERT,sD)
    else:
        stb.insert(INSERT,f"No Client under the Name '{tsrche_}'")
 
    #Function and Button to close and return to Search
    def closesrch_M():
        srch_mainM.destroy()
        search()
 
    sbtn=tk.Button(lbl,text='Okay!',
    relief='raised',bg='darkblue',fg='white',
    borderwidth=2,height=1,width=60,
    command=closesrch_M
    )
    sbtn.place(x=155,y=360)
 
 
def update():
    global upd
    #Sub-Level to root
    upd=tk.Toplevel(root)
    upd.title('Update ⤵')
    upd.geometry('300x180')
    upd.configure(bg=bgw)
 
    updL1=tk.Label(upd, text='Enter the Name of the Client :(Case-Sensitive)',
    bg=bgc,fg=fgc
    )
    updL1.pack()
 
 
    #Entry field for Client Name
    global upden
    tupdn=tk.StringVar()
    upden=tk.Entry(upd,relief='sunken',textvariable=tupdn,
    borderwidth=2,width=40,
    bg='lightblue'
    )
    upden.pack()
 
    Label(upd,bg=bgw).pack()
 
    updL2=tk.Label(upd, text='Enter the New Balance :',
    bg=bgc,fg=fgc
    )
    updL2.pack()
 
    #Entry to get the CustomerName Required
    global updeb
    tupdb=tk.StringVar()
    updeb=tk.Entry(upd,relief='sunken',textvariable=tupdb,
    borderwidth=2,width=40,
    bg='lightblue'
    )
    updeb.pack()
 
    #Function to get entries in Name and Balance
    def goupdateM():
        global tupdn_
        global tupdb_
        tupdb_=tupdb.get()
        tupdn_=tupdn.get()
        upd.destroy()
        updateM()
    
    #Function and Button to Update Record
    bupd=tk.Button(upd,text='Update Balance',
    bg='lightblue',relief='raised',borderwidth=2,height=1,
    width=20,command=goupdateM
    )
    bupd.place(x=23,y=120)
 
 
    #Function and Button to close and return to Main Menu
    def closeupd():
        upd.destroy()
        mainM()
    cupd=tk.Button(upd,text='Back', bg='blue',fg='white',
    relief='raised',borderwidth=2,height=1,
    width=10,command=closeupd
    )
    cupd.place(x=195,y=120)
 
def updateM():
    #Result window after using update function
    upd.destroy()
    succu=tk.Toplevel(root)
    succu.title('Update Status ⤵')
    succu.geometry('300x80')
    succu.configure(bg=bgw)
 
    mycursor.execute(f"select * from cdata where CustomerName='{tupdn_}'")
    uD=mycursor.fetchone()
 
    #Checks if CustomerName entered exists
    #Else shows 'No such Client'
    if uD!=None:
        query=f"update cdata set Balance={tupdb_} where CustomerName='{tupdn_}'"
        mycursor.execute(query)
        mycon.commit()
        updm=tk.Label(succu,text=f"{tupdn_}'s New Balance has been Updated!!!",
        bg=bgc,fg=fgc
        )
        updm.pack()
    else:
        updf=tk.Label(succu,text=f"No Such Client under the Name '{tupdn_}'",
        bg=bgc
        )
        updf.pack()
 
    #Function and Button to close and reopen update
    def closeupdM():
        succu.destroy()
        update()
 
    updbtn=tk.Button(succu,text='Okay!',
    relief='raised',bg='darkblue',fg='white',
    borderwidth=2,height=1,width=10,
    command=closeupdM
    )
    updbtn.place(x=110,y=45)
 
 
def delete():
    #Sub-Level to root
    global deld
    deld=tk.Toplevel(root)
    deld.title("Delete Data of a Client's ⤵")
    deld.geometry('300x110')
    deld.configure(bg=bgw)
 
    #Label For Client Name
    ldeld=tk.Label(deld, text='Enter the Name of the Client :(Case-Sensitive)',
    bg=bgc,fg=fgc
    )
    ldeld.pack()
 
    #Entry to get the Name of the Client
    global tdeldn
    tdeldn=tk.StringVar()
    dele=tk.Entry(deld,relief='sunken',textvariable=tdeldn,
    bg=bgc,borderwidth=2,width=40
    )
    dele.pack()
 
    #Function and Button To go to deleteM
    def godelete():
        deld.destroy()
        deleteM()
    bdel=tk.Button(deld,text='Delete The Record',
    bg='lightblue',relief='raised',borderwidth=2,height=1,width=20,
    command=godelete)
    bdel.place(x=23,y=70)
 
    #Function and Button to Close and return to main menu
    def closedelete():
        deld.destroy()
        mainM()
    cdel=tk.Button(deld,text='Back', bg='blue',fg='white',
    relief='raised',borderwidth=2,height=1,width=10,
    command=closedelete)
    cdel.place(x=195,y=70)
 
def deleteM():
    #Sub-Level to root
    deld.destroy()
    succd=tk.Toplevel(root)
    succd.title("Delete Status ⤵")
    succd.geometry('300x80')
    succd.configure(bg=bgw)
 
    #Get the CustomerName from the entry in delete()
    tdeldn_=tdeldn.get()
    mycursor.execute(f"select * from cdata where CustomerName='{tdeldn_}'")
    dD=mycursor.fetchone()
 
    #Checks if CustomerName doesn't exist
    #Else runs query to delete
    if dD!=None:
        query=f"delete from cdata where CustomerName='{tdeldn_}'"
        mycursor.execute(query)
        mycon.commit()
        dldm=tk.Label(succd,text=f"{tdeldn_}'s Data has been Removed!!!",
                      bg=bgc)
        dldm.pack()
    
    else:
        dldf=tk.Label(succd,
                      text=f"No Such Client under the name '{tdeldn_}'",
                      bg=bgc)
        dldf.pack()
 
    #Function and Button to close window and go to delete()
    def closesuccdM():
        succd.destroy()
        delete()
 
    dldbtn=tk.Button(succd,text='Okay!',
    relief='raised',bg='darkblue',fg='white',
    borderwidth=2,height=1,width=10,
    command=closesuccdM
    )
    dldbtn.place(x=110,y=45)
 
	
def mainM():
    #Main Menu Window
    global mw
    mw=tk.Toplevel(root)
    mw.title('Main Menu!')
    mw.geometry(dimen)
    mw.configure(bg=bgw)
 
    #Layout for mainM
    mainMframe=tk.Frame(mw)
    mainMframe.pack()
    lbl=tk.Label(mainMframe, image=img2)
    lbl.pack(fill=tk.BOTH)
 
    #Layout for lightblue bg that contains the options
    lblm=tk.Label(lbl, bg=bgc, height=21, width=70)
    lblm.place(x=115,y=45)
 
    Label(lbl, text='Main Menu',bg=bgc,
    fg=fgc,font=('Times New Roman',20),
    width=27
    ).place(x=155, y=78)
 
 
    #Function and button for Add Data
    def cMta():
        mw.destroy()
        add()
 
    btnadd=tk.Button(lbl, text='Add Data', bg='lightblue',
    relief='sunken',borderwidth=2,height=1,
    width=60,command=cMta
    )
    btnadd.place(x=147,y=145)
 
    #Function and Button for Display Records
    def cMtd():
        mw.destroy()
        display()
 
    btndis=tk.Button(lbl, text='Display All Data', bg='lightblue',
    relief='sunken',borderwidth=2,height=1,width=60,
    command=cMtd
    )
    btndis.place(x=147,y=175)
 
    #Function and button for Search Record
    def cMts():
        mw.destroy()
        search()
    
    btns=tk.Button(lbl,text='Search A Record',bg='lightblue',relief='sunken',
    borderwidth=2,height=1,width=60,command=cMts
    )
    btns.place(x=147,y=205)
 
 
    #Function and button for Update Balance
    def cMtupd():
        mw.destroy()
        update()
    btnupd=tk.Button(lbl,text='Update Balance',bg='lightblue', relief='sunken',
    borderwidth=2,height=1,width=60,command=cMtupd
    )
    btnupd.place(x=147,y=235)
 
    #Function and Button to Delete Data
    def cMtdel():
        mw.destroy()
        delete()
    btnupd=tk.Button(lbl,text="Delete a Client's Detail",bg='lightblue',
    relief='sunken',borderwidth=2,height=1,width=60,
    command=cMtdel
    )
    btnupd.place(x=147,y=265)
 
    #Button to go back to the Welcome Screen
    btnb=tk.Button(lbl,text='Back to Welcome Screen',bg='blue',fg='white',
    relief='sunken',borderwidth=2,height=1,width=60,
    command=mw.destroy
    )
    btnb.place(x=147,y=320)
 
def app():
    #The Root Window
    global root
    root=tk.Tk()
    root.title('Welcome!')
    root.geometry(dimen)
    root.configure(bg=bgw)

    #Making 'img1' and 'img2' as global to use in other sub functions
    global img1
    img1=tk.PhotoImage(file='Resources/bank1.png')
    #Resources is local folder containing image 'bank1.png'
    global img2
    img2=tk.PhotoImage(file='Resources/bank2.png')
    #Resources is local folder containing image 'bank2.png'

    #Frame to hold the widgets
    rootf=tk.Frame(root)
    rootf.pack()
    labl=tk.Label(rootf, image=img1)
    labl.pack(fill=tk.BOTH)
 
    #Label with bgcolour
    lblr=tk.Label(labl,bg=bgc, height=20, width=70)
    lblr.place(x=120,y=80)
 
    lblw=tk.Label(labl,
    text='Welcome To\nThe\nBank Data Management System',
    bg=bgc, fg=fgc,
    font=('Times New Roman',22),width=27
    )
    lblw.place(x=148,y=110)
 
    #Buttons to Main Menu and to Quit and close all windows
    btnr=tk.Button(labl,
    text='Main Menu',bg=bgc,borderwidth=2,height=1,
    width=20, relief='raised',command=mainM
    )
    btnr.place(x=225,y=275)

    #Thank you message
    def appc():
        root.destroy()
        print('\n--Thank You!--')
 
    btnb=tk.Button(labl,text='Quit',
    bg='blue',fg='white',borderwidth=2,height=1,width=15,
    relief='raised',command=appc
    )
    btnb.place(x=395,y=275)

    root.mainloop()
 
############################################################
#END OF app.py
 
