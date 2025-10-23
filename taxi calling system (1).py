from tkinter import *

from tkinter.ttk import *

from tkinter import messagebox

import os

import csv



userFields = ["User ID","Name","Contact No","Place","Password","Role","Status"]

workList =['Taxi Driver']



def getPlace():

    lst = []    

    with open('user1.csv','r')as f:

        obj=csv.reader(f)

        for row in obj:

            if row[3] not in lst:

                lst.append(row[3])

    return lst



def getUserId():

    if os.path.isfile('user1.csv'):

        with open('user1.csv','r')as f:

            rd=csv.reader(f)

            for row in rd:

                uid = row[0]

        uid = int(uid) + 1

    else:

        uid = 1000

    return uid



def addUser(l):

    if os.path.isfile('user1.csv'):

        with open('user1.csv', "a", newline="") as f:

            obj = csv.writer(f)

            obj.writerow(l)

    else:

        with open('user1.csv', "w", newline="") as f:

            obj = csv.writer(f)

            obj.writerow(userFields)

            obj.writerow(l)    



def statusUpdate(s):

    lst=[]

    with open('user1.csv', "r", newline="") as f:

        obj = csv.reader(f)

        for row in obj:

            if row[0] == ulst[0]:

                row[6] = s

                lst.append(row)

            else:

                lst.append(row)

    with open('user1.csv', "w", newline="") as f:

        obj = csv.writer(f)

        obj.writerows(lst)



def getWorker(service):

    lst=[]

    with open('user1.csv', "r", newline="") as f:

        obj = csv.reader(f)

        for row in obj:

            if row[3] == service and row[5]=="Taxi Driver" and row[6]=="Yes":

                lst.append([row[1],row[2]])

    return lst



def editUser(l):

    lst=[]

    with open('user1.csv', "r", newline="") as f:

        obj = csv.reader(f)

        for row in obj:

            if row[0] == l[0]:

                lst.append(l)

            else:

                lst.append(row)

    with open('user1.csv', "w", newline="") as f:

        obj = csv.writer(f)

        obj.writerows(lst)

                         

def deleteUser():

    lst=[]

    with open('user1.csv', "r", newline="") as f:

        obj = csv.reader(f)

        for row in obj:

            if row[0] != ulst[0]:

                lst.append(row)

    with open('user1.csv', "w", newline="") as f:

        obj = csv.writer(f)

        obj.writerows(lst)



mainWindow = Tk()

size = "800x600"

mainWindow.geometry(size)

mainWindow.resizable(0, 0)

mainWindow.title("Login")



unmVar = StringVar()

pwdVar = StringVar()

uidVar = StringVar()

nameVar = StringVar()

mobVar = StringVar()

upwdVar = StringVar()

workVar1 = StringVar()

workVar2 = StringVar()

workVar3 = StringVar()

workVar4 = StringVar()

workVar5 = StringVar()



def searchWorker():

    service = selSerCombo.get()

    workerList = getWorker(service)

    if workerList==[]:

        messagebox.showerror("Error", "No Service Found")

        selSerCombo.current(0)

        selSerCombo.focus_set()

    else:

        k=120

        

        for i in workerList:

            wname = "Name: "+i[0]

            wmob = "Contact No: "+i[1]



            workerNameLabel = Label(customerSerWin, text=wname, font=("Arial", 10))

            workerNameLabel.place(x=20, y=k)

            

            workerMobLabel = Label(customerSerWin, text=wmob, font=("Arial", 10))

            workerMobLabel.place(x=180, y=k)

            

            k=k+30

        workerList.clear()



def mpBack():

    myProfileWin.destroy()

    myProfBtn.focus_set()



def editProfile1():

    userId = uidVar.get()

    userName = nameVar.get()

    userMob = mobVar.get()

    userPlace = userPlaceCombo.get()

    userPwd = upwdVar.get()

    userList = [userId,userName,userMob,userPlace,userPwd,ulst[5]]

    editUser(userList)

    messagebox.showinfo("Success", "User is Updated Successfully")

    userIdEntry.delete(0,END)

    userNameEntry.delete(0,END)

    userMobEntry.delete(0,END)

    userPwdEntry.delete(0,END)

    userPlaceCombo.current(0)

    editProfileWin.destroy()

    myProfileWin.destroy()

    serviceWin.destroy()

    unmEntry.focus_set()

    

def editProfile():

    global userIdEntry

    global userNameEntry

    global userMobEntry

    global userPwdEntry

    global userPlaceCombo

    global editProfileWin

    

    editProfileWin = Toplevel()

    editProfileWin.title("Edit Profile")

    editProfileWin.geometry(size)

    editProfileWin.resizable(0, 0)



    editHeadLabel = Label(editProfileWin,text="Edit Profile",font=("Arial", 20, "bold"))

    editHeadLabel.place(x=270, y=20)



    uidVar.set(ulst[0])

    nameVar.set(ulst[1])

    mobVar.set(ulst[2])

    upwdVar.set(ulst[4])



    userIdLabel = Label(editProfileWin, text="User Id", font=("Arial", 10))

    userIdLabel.place(x=260, y=80)

    userIdEntry = Entry(editProfileWin, textvariable=uidVar, state = "disabled" )

    userIdEntry.place(x=370, y=80)



    userNameLabel = Label(editProfileWin, text="Name", font=("Arial", 10))

    userNameLabel.place(x=260, y=110)

    userNameEntry = Entry(editProfileWin, textvariable=nameVar)

    userNameEntry.place(x=370, y=110)

    userNameEntry.focus_set()



    userMobLabel = Label(editProfileWin, text="Contact No", font=("Arial", 10))

    userMobLabel.place(x=260, y=140)

    userMobEntry = Entry(editProfileWin, textvariable=mobVar)

    userMobEntry.place(x=370, y=140)



    placeItems = ("--Select--","Vytilla","Petta","Maharajas","MG Road","Town Hall","Kaloor","JLN Stadium","Palarivattom","Changampuzha Park","Edapally","Pathadipalam","Kalamassery","Ambattukavu","Companypady","Pulinchodu","Aluva","Kakkanad")

    for i in range(len(placeItems)):

        if placeItems[i]==ulst[3]:

            pos = i

            break

    userPlaceLabel = Label(editProfileWin, text="Place", font=("Arial", 10))

    userPlaceLabel.place(x=260, y=170)

    userPlaceCombo = Combobox(editProfileWin)

    userPlaceCombo["values"] = placeItems

    userPlaceCombo.current(pos)

    userPlaceCombo.place(x=370, y=170)



    userPwdLabel = Label(editProfileWin, text="Password", font=("Arial", 10))

    userPwdLabel.place(x=260, y=200)

    userPwdEntry = Entry(editProfileWin, textvariable=upwdVar)

    userPwdEntry.place(x=370, y=200)



    editButton = Button(editProfileWin, text="Edit", command=editProfile1)

    editButton.place(x=330, y=260)



def deactiveUser():

    res=messagebox.askquestion('Delete', 'Do you really want to delete')

    if res == 'yes' :

        deleteUser()

        myProfileWin.destroy()

        serviceWin.destroy()

        unmEntry.focus_set()

    else:

        mpEditBtn.focus_set()



def myProfile():

    global myProfileWin

    global mpEditBtn

    

    myProfileWin = Toplevel()

    myProfileWin.title("My Profile")

    myProfileWin.geometry(size)

    myProfileWin.resizable(0, 0)



    userId = "ID: "+ulst[0]

    userName = "Name: "+ulst[1]

    userContact = "Contact No: "+ulst[2]

    userPlace = "Place: "+ulst[3]

    userPassword = "Password: "+ulst[4]



    mpHeadLabel = Label(myProfileWin, text="My Profile", font=("Arial", 15, "bold"))

    mpHeadLabel.place(x=20, y=20)

    

    mpIdLabel = Label(myProfileWin, text=userId, font=("Arial", 10))

    mpIdLabel.place(x=20, y=60)



    mpNameLabel = Label(myProfileWin, text=userName, font=("Arial", 10))

    mpNameLabel.place(x=20, y=90)



    mpMobLabel = Label(myProfileWin, text=userContact, font=("Arial", 10))

    mpMobLabel.place(x=20, y=120)



    mpPlaceLabel = Label(myProfileWin, text=userPlace, font=("Arial", 10))

    mpPlaceLabel.place(x=20, y=150)



    mpPwdLabel = Label(myProfileWin, text=userPassword, font=("Arial", 10))

    mpPwdLabel.place(x=20, y=180)



    mpEditBtn = Button(myProfileWin, text="Edit", command=editProfile)

    mpEditBtn.place(x=20,y=210)



    mpDeactivateBtn = Button(myProfileWin, text="Deactivate", command=deactiveUser)

    mpDeactivateBtn.place(x=120,y=210)



    mpBackBtn = Button(myProfileWin, text="Back", command=mpBack)

    mpBackBtn.place(x=220,y=210)



'''def addWork():

    workList1 = []

    n = serviceListbox.index("end")

    for i in range(n):

        workList1.append(serviceListbox.get(i))

    workLst = ",".join(workList1)

    updateUser(workLst)

    messagebox.showinfo("Success", "Record is Saved Successfully")



def removeWork():

    if serviceListbox.curselection():

        index = serviceListbox.curselection()[0]

        serviceListbox.delete(index)'''



def serviceBack():

    workerSerWin.destroy()

    myProfBtn.focus_set()



def serviceBack1():

    customerSerWin.destroy()

    myProfBtn.focus_set()



def service():

    global serviceListbox

    global selSerCombo

    global customerSerWin

    global workerSerWin

    

    if ulst[5]=="Customer":

        customerSerWin = Toplevel()

        customerSerWin.title("Taxi Calling System")

        customerSerWin.geometry(size)

        customerSerWin.resizable(0, 0)



        serviceHeadLabel = Label(customerSerWin,text="ZAPSO",font=("Arial", 25, "bold"))

        serviceHeadLabel.place(x=270,y=20)



        serviceBackBtn = Button(customerSerWin, text="Back", command=serviceBack1)

        serviceBackBtn.place(x=700, y=10)



        placeItems = getPlace()



        selSerLabel = Label(customerSerWin, text="Select Location", font=("Arial", 10))

        selSerLabel.place(x=20, y=70)

        selSerCombo = Combobox(customerSerWin)

        selSerCombo["values"] = placeItems

        selSerCombo.current(0)

        selSerCombo.place(x=150, y=70)



        selSerBtn = Button(customerSerWin, text="Search", command=searchWorker)

        selSerBtn.place(x=300, y=70)




def logout():

    serviceWin.destroy()

    unmEntry.focus_set()



def updateStatus():

    avail = statusCombo.get()

    statusUpdate(avail)

    messagebox.showinfo("Success", "Status is Updates Successfully")

    statusCombo.current(0)

    myProfBtn.focus_set()



def serviceHome():

    global serviceWin

    global myProfBtn

    global statusCombo

    

    if ulst[5]=="Customer":

        serviceWin = Toplevel()

        serviceWin.title("Taxi Calling System")

        serviceWin.geometry(size)

        serviceWin.resizable(0, 0)



        serviceHeadLabel = Label(serviceWin,text="ZAPSO",font=("Arial", 25, "bold"))

        serviceHeadLabel.place(x=270,y=10)

    

        myProfBtn = Button(serviceWin, text="My Profile", command=myProfile)

        myProfBtn.place(x=10, y=60)



        serviceBtn = Button(serviceWin, text="Service", command=service)

        serviceBtn.place(x=10, y=90)



        logoutBtn = Button(serviceWin, text="Logout", command=logout)

        logoutBtn.place(x=700, y=20)

        

    elif ulst[5]=="Taxi Driver":

        serviceWin = Toplevel()

        serviceWin.title("Taxi Calling System")

        serviceWin.geometry(size)

        serviceWin.resizable(0, 0)



        serviceHeadLabel = Label(serviceWin,text="ZAPSO",font=("Arial", 25, "bold"))

        serviceHeadLabel.place(x=270,y=10)

    

        myProfBtn = Button(serviceWin, text="My Profile", command=myProfile)

        myProfBtn.place(x=10, y=60)



        statusLabel = Label(serviceWin,text="Select the Availability")

        statusLabel.place(x=10,y=100)

        statusCombo = Combobox(serviceWin)

        statusCombo["values"] = ("--Select--","Yes","No")

        statusCombo.current(0)

        statusCombo.place(x=150, y=100)

        

        StatusBtn = Button(serviceWin, text="Update Status", command=updateStatus)

        StatusBtn.place(x=300, y=100)



        logoutBtn = Button(serviceWin, text="Logout", command=logout)

        logoutBtn.place(x=700, y=20)

        



def signUp1():

    userId = uidVar.get()

    userName = nameVar.get()

    userMob = mobVar.get()

    userPlace = userPlaceCombo.get()

    userPwd = upwdVar.get()

    userRole = userRoleCombo.get()

    userList = [userId,userName,userMob,userPlace,userPwd,userRole,"NULL"]

    addUser(userList)

    messagebox.showinfo("Success", "Record is Saved Successfully")

    userIdEntry.delete(0,END)

    userNameEntry.delete(0,END)

    userMobEntry.delete(0,END)

    userPwdEntry.delete(0,END)

    userPlaceCombo.current(0)

    userRoleCombo.current(0)

    signWindow.destroy()

    unmEntry.focus_set()



def signUp():

    global userIdEntry

    global userNameEntry

    global userMobEntry

    global userPwdEntry

    global userPlaceCombo

    global userRoleCombo

    global signWindow

    

    signWindow = Toplevel()

    size = "800x600"

    signWindow.geometry(size)

    signWindow.resizable(0, 0)

    signWindow.title("Sign Up")



    signHeadLabel = Label(signWindow,text="Create Account",font=("Arial", 20, "bold"))

    signHeadLabel.place(x=270, y=20)



    uid = getUserId()

    uidVar.set(uid)



    userIdLabel = Label(signWindow, text="User Id", font=("Arial", 10))

    userIdLabel.place(x=260, y=80)

    userIdEntry = Entry(signWindow, textvariable=uidVar, state = "disabled" )

    userIdEntry.place(x=370, y=80)



    userNameLabel = Label(signWindow, text="Name", font=("Arial", 10))

    userNameLabel.place(x=260, y=110)

    userNameEntry = Entry(signWindow, textvariable=nameVar)

    userNameEntry.place(x=370, y=110)

    userNameEntry.focus_set()



    userMobLabel = Label(signWindow, text="Contact No", font=("Arial", 10))

    userMobLabel.place(x=260, y=140)

    userMobEntry = Entry(signWindow, textvariable=mobVar)

    userMobEntry.place(x=370, y=140)



    placeItems = ("--Select--","Vytilla","Petta","Maharajas","MG Road","Town Hall","Kaloor","JLN Stadium","Palarivattom","Changampuzha Park","Edapally","Pathadipalam","Kalamassery","Ambattukavu","Companypady","Pulinchodu","Aluva","Kakkanad")

    userPlaceLabel = Label(signWindow, text="Place", font=("Arial", 10))

    userPlaceLabel.place(x=260, y=170)

    userPlaceCombo = Combobox(signWindow)

    userPlaceCombo["values"] = placeItems

    userPlaceCombo.current(0)

    userPlaceCombo.place(x=370, y=170)



    userPwdLabel = Label(signWindow, text="Password", font=("Arial", 10))

    userPwdLabel.place(x=260, y=200)

    userPwdEntry = Entry(signWindow, textvariable=upwdVar)

    userPwdEntry.place(x=370, y=200)



    userRoleLabel = Label(signWindow, text="Sign in As", font=("Arial", 10))

    userRoleLabel.place(x=260, y=230)

    userRoleCombo = Combobox(signWindow)

    userRoleCombo["values"] = ("--Select--","Customer","Taxi Driver")

    userRoleCombo.current(0)

    userRoleCombo.place(x=370, y=230)



    signInButton = Button(signWindow, text="Sign In", command=signUp1)

    signInButton.place(x=330, y=260)



def login1():

    global ulst

    

    u = unmVar.get()

    p = pwdVar.get()

    flag = 0

    with open('user1.csv', "r", newline="") as f:

        obj = csv.reader(f)

        for row in obj:

            if row[0] == u and row[4] == p:

                ulst = row

                flag = 1

                break

    if flag==0:

        messagebox.showerror("Error", "Invalid User Id or Password")

        unmEntry.delete(0, END)

        pwdEntry.delete(0, END)

        unmEntry.focus_set()

    else:

        unmEntry.delete(0, END)

        pwdEntry.delete(0, END)

        serviceHome()



headLabel = Label(mainWindow,text="ZAPSO",font=("Arial", 25))

headLabel.place(x=270, y=10)



unmLabel = Label(mainWindow, text="User Id", font=("Arial", 10))

unmLabel.place(x=300, y=200)

unmEntry = Entry(mainWindow, textvariable=unmVar)

unmEntry.place(x=380, y=200)

unmEntry.focus_set()



pwdLabel = Label(mainWindow, text="Password", font=("Arial", 10))

pwdLabel.place(x=300, y=240)

pwdEntry = Entry(mainWindow, textvariable=pwdVar, show="*")

pwdEntry.place(x=380, y=240)



loginButton = Button(mainWindow, text="Login", command=login1)

loginButton.place(x=320, y=280)



signButton = Button(mainWindow, text="Sign Up", command=signUp)

signButton.place(x=410, y=280)



mainWindow.mainloop()

