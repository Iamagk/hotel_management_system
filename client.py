print("...........STAY WITH US............")
print("\n........BY ALLENN GEORGE KANNADICKAL...........")


#Establishing connection of program with Mysql
import mysql.connector as sql
myConnection =""
cursor=""
cid=""
#Establishing connection with the database
def mysqlconnection():
    global myConnection
myConnection = sql.connect(host = "localhost", user='root', passwd=
'Password', database='Hotel_management_system' auth_plugin='mysql_native_password')

if myConnection:
    print("\nCongrats, Successfully Established Connection with the Database!!")
    return myConnection
else:
    print("ERROR can't establish connection with database!")
myConnection.close()
mysqlconnection()
ch = input("\n Press SPACE to continue..............................")

#Creating home page
if ch == ' ':
    print("\n.......WELCOME TO THE INN PLAZA......................")

def home():
    print("\n1.Show Room Information:")
    print("2.Customers:")
    print("3. Reservations:")
    print("4. Payments:")
    print("5. Employee:")
    print("6.Reports")
home()
choice = int(input("\nEnter your choice:"))
#room information
if choice == 1:
    def roominfo():
        print(".............Room Information...............")
        print("\n 1. Standard 2 Bed AC")
        print(" 2. 3 Bed AC")
        print(" 3. Suite")
        ch = int(input("Enter your choice"))
        if ch == 1:
            print("\n Standard 2 Bed AC")
            print("Package includes access to restaurant, swimming pool")
            print("Price = 2000/day")
        if ch == 2:
            print(" \n 3-Bed AC")
            print("Package includes access to restaurant, swimming pool")
            print("Price = 3000/day")
        if ch == 3:
            print("\n Suite")
            print("Room description - 2 Bedroom, 1 living room, 2 baths")
            print("Package includes access to restaurant, swimming pool")
            print("Price = 5000/day")
    roominfo()

#Adding new customer
if choice == 2:
    print("\n1.Add new Customer:")
    print("2.Show Customer Information:")
    ch = int(input("Enter your choice"))

    if ch == 1:
    #Creating customer information table
        def customerinfo():
            print("...........Add a new Customer.............")
            global cid
            import random
            cid = random.randint(0,100000)
            print("Your Customer_ID is", cid)
            if myConnection:
                cur = myConnection.cursor()
                createtable =("CREATE TABLE Customer_Information(Customer_IDint(20) primary key, Customer_FirstName varchar(50), Customer_LastName varchar(50), Address varchar (50), Email varchar(50), Checkin_Date date, Checkout_Date date )")

                cur.execute(createtable)
                fname = input ("Enter Customer_FirstName:")
                lname = input ("Enter Customer_LastName:")
                print("\n Welcome Mr/Ms",fname,lname,"To The Inn Plaza")
                address = input ("Enter the Customer's address:")
                email = input ("Enter Customer email address:")
                checkin = input("Enter Checkin_Date:")
                checkout = input ("Enter Checkout_Date:")
                s = "INSERT INTO Customer_Information VALUES(%s,%s,%s,%s,%s,%s,%s)"

                values = (cid, fname, lname, address, email, checkin, checkout)
                cur.execute(s,values)
                myConnection.commit()
                print("Successfully entered new customer into the system!")
                cur.close()
            else:
                print("ERROR can't establish connection with database!")
        customerinfo()
    if ch == 2:
    #Retrieving customer data from database
        def showcustomerinfo():
            print("\n Loading customer information from database........................")

            if myConnection:
                cur = myConnection.cursor()
                cur.execute("Select * from Customer_Information")
                myrecords = cur.fetchall()
                for x in myrecords:
                    print(x)
        showcustomerinfo()

    #Generating reservation
    if choice == 3:
        print("\n1.Create new reservation:")
        print("2.Show Reservation Information:")
        ch = int(input("Enter your choice :"))
        if ch == 1:
            #create a new reservation
            def createreservation():
                print("........Add a new Reservation............")
                name = input("Enter name of Customer:")
                checkin = input("Enter the Check in date:")
                import random
                rid = random.randint(0,100000)
                cid = random.randint(0,100000)
                print("Your Customer_ID is", cid)
                print("Thank You Mr/Ms", name,".Your reservation for", checkin,"has been saved. Your Reservation ID is",rid)
                if myConnection:
                    cur = myConnection.cursor()
                    createtable = ("CREATE TABLE Reservations (Reservation_ID int(20), Customer_ID int(20), FOREIGN KEY (Customer_ID) REFERENCES Customer_Information (Customer_ID), Customer_Name varchar(50), Room_ID varchar(20), Reservation_Date date, Checkin_Date date, Checkout_Date date,Duration int(20))")

                    cur.execute(createtable)

                    roomid=input ("Enter the Room_ID:")
                    reservedate = input("Enter Reservation_Date date:")
                    checkout = input("Enter Check out date:")
                    duration = input ("Number of days of stay:")
                    s = "INSERT INTO Reservations VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    values=(rid,cid,name,roomid,reservedate,checkin,checkout,duration)
                    cur.execute(s,values)
                    myConnection.commit()
                    print("Successfully updated the database!")
                    cur.close()
                else:
                    print("ERROR can't establish connection with database!")
                    createreservation()
                    if ch == 2:
                    #Retrieving reservation data from database
                        def showreservationinfo():
                            print("\n Loading Reservation Information from database...................")
                            if myConnection:
                                cur = myConnection.cursor()
                                cur.execute("Select * from Reservations")
                                myrecords = cur.fetchall()
                                for x in myrecords:
                                    print(x)
                    showreservationinfo()

                    #New payment
    if choice == 4:
        print("1.Generate bill")
        print("2.Show Payment Information:")
        ch = int(input("Enter your choice:"))
        if ch == 1:
        #Creating Payments table
            def paymentinfo():
                print("\n.......................................Prices..............................................")
                print("Restaurant = 150/meal")

                global cid
                import random
                pid = random.randint(0,100000)
                print("\nYour Payment ID is",pid)
                days=int(input("Enter total number of days:"))
                meal =int(input("Enter total number of meals:"))
                room = input("Enter room type")
                print("\n.......................................Prices..............................................")
                print("\n 2-Bed = 2000/day")
                print(" 3-Bed = 3000/day")
                print(" Suite = 5000/day")
                price = int(input("Enter price for room:"))
                restaurant = 150
                amount = days*price
                total = meal*restaurant
                name = input("Enter the customer name:")
                print("Mr/Ms",name,"Your total bill amount =", amount+total)
                if myConnection:
                    cur = myConnection.cursor()
                    createtable = ("CREATE TABLE Payments (Payment_ID int(20) primary key, Customer_ID int(20) , Payment_date date, FOREIGN  KEY(Customer_ID) REFERENCES Customer_Information (Customer_ID), Name varchar(100), Amount int(50), Payment_mode varchar(50), Services varchar(100))")

                    cur.execute(createtable)
                    cid = input ("Enter the Customer_ID:")
                    date = input("Enter payment date:")
                    mode = input("Enter payment mode:")
                    services = input ("List the services used:")
                    s = "INSERT INTO Payments VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    values = (pid,cid,date,name,amount+total,mode,services)
                    cur.execute(s,values)
                    myConnection.commit()
                    print("Successfully updated the database!")
                    cur.close()
                    print("Successfully updated the database!")
                    print("Generating Bill........................")

                    print("\n.................The Inn Plaza...................")
                    print("\nDate :",date)
                    print("Customer ID :",cid)
                    print("Payment ID:",pid)
                    print("Payment Mode :",mode)
                    print("Room Type :",room)
                    print("Services used :",services)
                    print("\n Total bill amount :",amount+total)
                else:
                    print("ERROR can't establish connection with database!")
                    paymentinfo()
                    #Retrieving payment data from database
        if ch == 2:
            def showpaymentinfo():
                print("\n Loading Payments Information from database.................")
                if myConnection:
                    cur = myConnection.cursor()
                    cur.execute("Select * from Payments")
                    myrecords = cur.fetchall()
                    for x in myrecords:
                        print(x)
            showpaymentinfo()

            #employee table
    if choice == 5:
        print("\n1.Add new employee")
        print("2. Show Employees Table:")
        ch = int(input("Enter your choice:"))
        #Adding new employee
        if ch == 1:
            def employeeinfo():
                print("..........Add a new Employee............")
                import random
                eid = random.randint(0,100000)
                print("Your Employee ID is", eid)
                if myConnection:
                    cur = myConnection.cursor()

                    createtable = ("CREATE TABLE Employees (Employee_ID int(20) primary key, Employee_FirstName varchar(10), Employee_LastName varchar(20), Job_Department CHAR(20), Address varchar (30), Contact_Number varchar(100), Username varchar(50), Password varchar(10))")
                    cur.execute(createtable)
                    fname = input ("Enter the Employee_FirstName:")
                    lname = input ("Enter the Employee_LastName:")
                    job = input("Enter Job Department:")
                    address = input("Enter Contact Address:")
                    phone = input ("Enter Contact Number:")
                    user = input ("Enter username:")
                    password = input ("Enter password")
                    s = "INSERT INTO Employees VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

                    values = (eid,fname,lname,job,address,phone,user,password)
                    cur.execute(s,values)
                    myConnection.commit()
                    print("Successfully updated the database!")
                    cur.close()
                else:
                    print("ERROR can't establish connection with database!")
                    employeeinfo()
                    #Retrieving employment data from database
        if ch == 2:
            def showemploymentinfo():
                print("\n Loading Employment Information from database...................")
                if myConnection:
                    cur = myConnection.cursor()
                    cur.execute("Select * from Employees")
                    myrecords = cur.fetchall()
                    for x in myrecords:
                        print(x)
            showemploymentinfo()

#Show Reports
    if choice == 6:
        print("\n 1. Add a new Report :")
        print(" 2. Show Reports Table :")
        ch = int(input("Enter your choice :"))
    #Add a new report
        if ch == 1:
            def reportsinfo():
                print("................Add a new Report....................")
                import random
                rid = random.randint(0,100000)
                print("Your Report ID is", rid)
                if myConnection:
                    cur = myConnection.cursor()
                    createtable = ("CREATE TABLE Reports(Reports_ID int(20) primary key, Customer_ID int(20), FOREIGN KEY (Customer_ID) REFERENCES Customer_Information (Customer_ID), Room_ID varchar(30), Information varchar(30), Date date)")

                    cur.execute(createtable)
                    cid = input ("Enter the Customer_ID:")
                    roomid=input ("Enter the Room_ID:")
                    info = input("Enter Report:")
                    date = input("Enter report date:")
                    s = "INSERT INTO Reports VALUES(%s,%s,%s,%s,%s)"
                    values = (rid,cid,roomid,info,date)
                    cur.execute(s,values)
                    myConnection.commit()
                    print("Successfully updated the database!")
                    cur.close()
                else:
                    print("ERROR can't establish connection with database!")
                    reportsinfo()
                    #Retrieving employment data from database
        if ch == 2:
            def showreportsinfo():

                print("\n Loading Reports Table from database.................................")
                if myConnection:
                    cur = myConnection.cursor()
                    cur.execute("Select * from Reports")
                    myrecords = cur.fetchall()
                    for x in myrecords:
                        print(x)
            showreportsinfo()