import mysql.connector as ms
con=ms.connect(host='localhost',user='root',passwd='tiger')
cur=con.cursor()

#Database creation and execution
cur.execute('create database if not exists library;')
cur.execute('use library;')

#Creation of Book Details table
query1='''CREATE TABLE IF NOT EXISTS BOOKS
            (BOOK_ID VARCHAR(5)PRIMARY KEY,
            BOOK_NAME VARCHAR(40),
            AUTHOR_NAME VARCHAR(30),
            QUANTITY INT(2),
            ST_ID VARCHAR(4),
            AVL_STATUS CHAR(3)DEFAULT 'AVL');'''

#Creation of Student Details table
query2='''CREATE TABLE IF NOT EXISTS STUDENT
        (ST_ID VARCHAR(4) PRIMARY KEY,
        STUDENT_NAME VARCHAR(30) NOT NULL,
        CLASS VARCHAR(3) NOT NULL,
        DIVISION CHAR(1) NOT NULL,
        ROLL_NO VARCHAR(3));'''

#Creation of Login Details Table 
user='''CREATE TABLE IF NOT EXISTS USER
        (USERNAME VARCHAR(30),
         PASSWORD VARCHAR(30));'''

#Creating a default username and password
defaultpass="INSERT INTO USER VALUES('user','1234');"

cur.execute(query2)
cur.execute(query1)
cur.execute(user)
cur.execute(defaultpass)

#Adding a Book to the database
def addbook():
    print("    ADDING BOOK DETAILS.........")
    print("    ****************************")
    print()
    bk_id=input("Enter Book ID for the book to be added:")
    bk_name=input("Enter Book Name for the book to be added:")
    auth_name=input("Enter Author for the book to be added:")
    qnty=int(input("Enter quantity of the respective book:"))
    query = "INSERT INTO books (BOOK_ID, BOOK_NAME, AUTHOR_NAME, QUANTITY) VALUES (%s, %s, %s, %s)"
    values = (bk_id, bk_name, auth_name, qnty)
    cur.execute(query, values)
    con.commit()
    print()
    print("Book Details is successfully added...")
    print()
    
#Adding Student Details to the database
def addstud() :
    print("    ADDING STUDENT DETAILS........")
    print("    ******************************")
    print()
    st_id=input("Enter Student ID to be added:")
    st_name=input("Enter the Name of the Student:")
    clas=input("Enter Class of the Student:")
    div=input("Enter Division of the Student:")
    rollno=input("Enter Roll Number of the Student:")
    query="INSERT INTO STUDENT(ST_ID,STUDENT_NAME,CLASS,DIVISION,ROLL_NO) VALUES (%s, %s, %s, %s,%s)"
    values=(st_id,st_name,clas,div,rollno)
    cur.execute(query, values)
    con.commit()
    print()
    print("Student Details is successfully added...")
    print()

#Removing student details from database
def studremove():
    print("    REMOVING STUDENT DATA........")
    print("    ******************************")
    print()
    st_id=input("Enter Student ID to be removed:")
    quer1="select * from student where ST_ID={0};".format(st_id)
    print("THE DETAILS OF THE STUDENT IS:")
    cur.execute(quer1)
    data=cur.fetchone()
    print(data)
    print()
    query="delete from student where ST_ID={0};".format(st_id)
    cur.execute(query)
    con.commit()
    print()
    print("Student Data Successfully Deleted")
    print()

#Removing a book from library
def bookremove():
    print(".........REMOVING BOOK DATA........")
    print("************************************")
    print()
    st_id=input("Enter Book ID to be removed:")
    quer1="select * from books where BOOK_ID={0};".format(st_id)
    print("THE DETAILS OF THE BOOK IS:")
    print('(BOOK_ID, BOOK_NAME, AUTHOR_NAME, QUANTITY,ST_ID,STATUS)')
    cur.execute(quer1)
    data=cur.fetchone()
    print(data)
    print()
    query="delete from books where BOOK_ID={0};".format(st_id)
    cur.execute(query)
    con.commit()
    print()
    print("Book Data Successfully Deleted")
    print()

#Issue a book
def issue():
    print("    ISSUE A BOOK FROM LIBRARY.......")
    print("    ********************************")
    print()
    bk_id=input("Enter The ID of The Book to be issued:")
    st_id=input("Enter the ID of The Student to whom book is issued:")
    quer1="select * from books where BOOK_ID={0};".format(bk_id)
    print("THE DETAILS OF THE ISSUING BOOK IS:")
    cur.execute(quer1)
    data=cur.fetchone()
    print(data)
    if data:
        if data[3]>0:
            quer2="UPDATE BOOKS SET AVL_STATUS='ISD' WHERE  BOOK_ID={0};".format(bk_id)
            cur.execute(quer2)
            quer3="UPDATE BOOKS SET QUANTITY=QUANTITY-1 WHERE  BOOK_ID={0};".format(bk_id)
            cur.execute(quer3)
            quer4="UPDATE BOOKS SET ST_ID={0} WHERE  BOOK_ID={1};".format(st_id,bk_id)
            cur.execute(quer4)
            con.commit()
            print()
            print("Book issued successfully.")
            print()
        else:
            print()
            print("No available copies of the book.")
            print()
    else:
        print()
        print("Book not found.")
        print()

#Return a book to the library
def returna():
    print("    RETURN A BOOK TO LIBRARY.......")
    print("    ********************************")
    print()
    bk_id=input("Enter The ID of The Book to be returned:")
    quer1="select * from books where BOOK_ID={0};".format(bk_id)
    print("THE DETAILS OF THE RETURNING BOOK IS:")
    cur.execute(quer1)
    data=cur.fetchone()
    print(data)
    quer2="UPDATE BOOKS SET AVL_STATUS='AVL' WHERE  BOOK_ID={0};".format(bk_id)
    quer3="UPDATE BOOKS SET QUANTITY=QUANTITY+1 WHERE  BOOK_ID={0};".format(bk_id)
    quer4="UPDATE BOOKS SET ST_ID=NULL WHERE BOOK_ID={0};".format(bk_id)
    cur.execute(quer2)
    cur.execute(quer3)
    cur.execute(quer4)
    con.commit()
    print()
    print("Book Return Command successfully completed....")
    print()

#Edit book details
def editbook():
    print("..........UPDATE BOOK DETAILS...........")
    print("****************************************")
    print()
    print("WHAT INFORMATION DO YOU WANT TO UPDATE?")
    print("  1.BOOK NAME")
    print("  2.AUTHOR NAME")
    print("  3.QUANTITY")
    print()
    opt=int(input("Select an option from the above menu:"))
    print()
    if opt==1:
        print("     .......EDITING BOOK NAME.......")
        print("    ********************************")
        print()
        bk_id=input("Enter The ID of The Book to be Edited:")
        quer1="select * from books where BOOK_ID={0};".format(bk_id)
        print("THE DETAILS OF THE BOOK IS:")
        cur.execute(quer1)
        data=cur.fetchone()
        print(data)
        newname=input("Enter the new name of the Book:")
        quer2="UPDATE BOOKS SET BOOK_NAME=('{0}') WHERE  BOOK_ID={1};".format(newname,bk_id)
        cur.execute(quer2)
        con.commit()
        print()
        print("BOOK NAME IS SUCCESSFULLY UPDATED")
        print()
    elif opt==2:
        print("     .......EDITING AUTHOR NAME.......")
        print("    **********************************")
        print()
        bk_id=input("Enter The ID of The Book to be Edited:")
        quer1="select * from books where BOOK_ID={0};".format(bk_id)
        print("THE DETAILS OF THE BOOK IS:")
        cur.execute(quer1)
        data=cur.fetchone()
        print(data)
        newname=input("Enter the new Author name of the Book:")
        quer2="UPDATE BOOKS SET AUTHOR_NAME=('{0}') WHERE  BOOK_ID=({1});".format(newname,bk_id)
        cur.execute(quer2)
        con.commit()
        print()
        print("AUTHOR NAME IS SUCCESSFULLY CHANGED")
        print()
    elif opt==3:
        print("     .......EDITING BOOK QUANTITY.......")
        print("     **********************************")
        print()
        bk_id=input("Enter The ID of The Book to be Edited:")
        quer1="select * from books where BOOK_ID=({0});".format(bk_id)
        print("THE DETAILS OF THE BOOK IS:")
        cur.execute(quer1)
        data=cur.fetchone()
        print(data)
        newqty=int(input("Enter the Quantity of the Book:"))
        quer2="UPDATE BOOKS SET QUANTITY=({0}) WHERE  BOOK_ID=({1});".format(newqty,bk_id)
        cur.execute(quer2)
        con.commit()
        print()
        print("QUANTITY IS SUCCESSFULLY UPDATED")
        print()
                 
#Edit student details
def editstud():
    print("...........UPDATE STUDENT DETAILS...........")
    print("********************************************")
    print()
    print("WHAT INFORMATION DO YOU WANT TO UPDATE?")
    print("  1.STUDENT NAME")
    print("  2.CLASS")
    print("  3.DIVISION")
    print("  4.ROLL NO")
    print()
    opt=int(input("Select an option from the above menu:"))
    print()
    if opt==1:
        print("     .......UPDATING STUDENT NAME.......")
        print("    ************************************")
        print()
        bk_id=input("Enter The ID of The Student to be Updated:")
        quer1="select * from student where ST_ID={0};".format(bk_id)
        print("THE DETAILS OF THE STUDENT IS:")
        cur.execute(quer1)
        data=cur.fetchone()
        print(data)
        newname=input("Enter the new name of the Student:")
        quer2="UPDATE STUDENT SET STUDENT_NAME='{0}' WHERE  ST_ID={1};".format(newname,bk_id)
        cur.execute(quer2)
        con.commit()
        print()
        print("STUDENT NAME IS SUCCESSFULLY UPDATED!")
        print()
    elif opt==2:
        print("     .......UPDATING STUDENT CLASS.......")
        print("    ************************************")
        print()
        bk_id=input("Enter The ID of The Student to be Updated:")
        quer1="select * from student where ST_ID={0};".format(bk_id)
        print("THE DETAILS OF THE STUDENT IS:")
        cur.execute(quer1)
        data=cur.fetchone()
        print(data)
        print()
        newcls=input("Enter the new CLASS of the Student:")
        quer2="UPDATE STUDENT SET CLASS=({0}) WHERE  ST_ID=({1});".format(newcls,bk_id)
        cur.execute(quer2)
        con.commit()
        print()
        print("STUDENT CLASS IS SUCCESSFULLY UPDATED")
        print()
    elif opt==3:
        print("     .......UPDATING STUDENT DIVISION.......")
        print("    ************************************")
        print()
        bk_id=input("Enter The ID of The Student to be Updated:")
        quer1="select * from student where ST_ID=('{0}');".format(bk_id)
        print("THE DETAILS OF THE STUDENT IS:")
        cur.execute(quer1)
        data=cur.fetchone()
        print(data)
        print()
        newcls=input("Enter the new division of the Student:")
        quer2="UPDATE STUDENT SET DIVISION=('{0}') WHERE  ST_ID=({1});".format(newcls,bk_id)
        cur.execute(quer2)
        con.commit()
        print()
        print("STUDENT DIVISION IS SUCCESSFULLY UPDATED")
        print()
    elif opt==4:
        print("     .......UPDATING STUDENT ROLL NUMBER.......")
        print("    *******************************************")
        print()
        bk_id=input("Enter The ID of The Student to be Updated:")
        quer1="select * from student where ST_ID=('{0}');".format(bk_id)
        print("THE DETAILS OF THE STUDENT IS:")
        cur.execute(quer1)
        data=cur.fetchone()
        print(data)
        print()
        newno=input("Enter the new roll number of the Student:")
        quer2="UPDATE STUDENT SET ROLL_NO=({0}) WHERE  ST_ID=({1});".format(newno,bk_id)
        cur.execute(quer2)
        con.commit()
        print()
        print("ROLL NUMBER IS SUCCESSFULLY UPDATED")
        print()

#Display details of all books
def bookdisp():
    print()
    quer="select * from books;"
    cur.execute(quer)
    data=cur.fetchall()
    print('        LIST OF ALL THE BOOKS IN THE LIBRARY')
    print('        ************************************')
    print()
    format_string = "%5s %25s %25s %7s %7s %13s"
    print(format_string %("BOOK_ID", "Book Name","Auth Name","Qty", "St_ID", "Status"))
    print('*'*90)
    for row in data:
        print('%5s'%(row[0]),'%25s'%(row[1]),'%25s'%(row[2]),'%7s'%(row[3]),'%7s'%(row[4]),'%13s'%(row[5]))

#Display details of available books
def bookavlbl():
    print()
    quer="select * from books where AVL_STATUS='AVL';"
    cur.execute(quer)
    data=cur.fetchall()
    print('        LIST OF CURRENTLY AVAILABLE BOOKS')
    print('        *********************************')
    print()
    format_string = "%5s %25s %25s %7s %7s %13s"
    print(format_string %("BOOK_ID", "Book Name","Auth Name","Qty", "St_ID", "Status"))
    print('*'*90)
    for row in data:
        print('%5s'%(row[0]),'%25s'%(row[1]),'%25s'%(row[2]),'%7s'%(row[3]),'%7s'%(row[4]),'%13s'%(row[5]))

#Display details of issued books
def bookissue():
    quer='''SELECT *
            FROM BOOKS NATURAL JOIN STUDENT
            WHERE AVL_STATUS='ISD';'''
    try:
        cur.execute(quer)
        data=cur.fetchall()
        nrec=cur.rowcount
        print()
        print('        LIST OF ISSUED BOOKS FROM LIBRARY')
        print('        *********************************')
        print()
        print()
        print('(STUDENT_ID,BOOK_ID,BOOK NAME,AUTHOR NAME,QTY,STATUS,STUDENT NAME,CLASS,DIVISION,ROLL NO)')
        print('----------------------------------------------------------------------------------------')
        for row in data:
            print(row)
            print()
    except Exception as e:
        print("Error:", e)

#Display details of students
def studentdet():
    quer="SELECT * FROM STUDENT;"
    cur.execute(quer)
    data=cur.fetchall()
    nrec=cur.rowcount
    format_string = "%5s %26s %6s %7s %7s"
    print('         LIST OF STUDENT DETAILS')
    print('         ***********************')
    print()
    print(format_string %("STUDENT_ID", "Student Name","Class","Division", "Roll No"))
    print('*'*65)
    for row in data:
        print('%5s'%(row[0]),'%30s'%(row[1]),'%5s'%(row[2]),'%7s'%(row[3]),'%7s'%(row[4]))

#About the program
def about():
    f=open("about.txt",'r')
    data=f.readlines()
    for each in data:
        print(each,end='')
    f.close()

#Help
def help1():
    f=open("help1.txt",'r')
    data=f.readlines()
    for each in data:
        print(each,end='')
    f.close()
        
#Main program
ch='y'
while ch in['y','Y']:   
    print()
    print("                WELCOME TO SCHOOL LIBRARY MANAGEMENT SOFTWARE")
    print("                ---------------------------------------------")
    print()
    print("                *************MAIN MENU****************")
    print()
    print('                    1.USER/BASIC MODE')
    print('                    2.ADMIN MODE')
    print('                    3.HELP')               
    print('                    4.ABOUT')
    print('                    5.CHECK MYSQL CONNECTION')
    print('                    6.EXIT THE PROGRAM')
    print()
    inp=int(input("Enter your desired option from above(1-5):"))
    if inp==1:
        cha='y'
        while cha in['Y','y']:
            print()
            print()
            print("                WELCOME TO SCHOOL LIBRARY MANAGEMENT SOFTWARE")
            print("                ---------------------------------------------")
            print()
            print("                *************USER MENU****************")
            print()
            print('                    1.ISSUE A BOOK')
            print('                    2.RETURN A BOOK')
            print('                    3.DISPLAY ALL THE BOOKS')
            print('                    4.DISPLAY DETAILS OF ISSUED BOOKS')
            print('                    5.DISPLAY DETAILS OF AVAILABLE BOOKS')
            print('                    6.DISPLAY DETAILS OF STUDENTS')
            print('                    7.HELP')                
            print('                    8.ABOUT')
            print('                    9.RETURN TO MAIN MENU')
            print()
            usinp=int(input("Enter your desired option from above(1-9):"))
            if usinp==1:
                issue()
                cha=input("Do you want to continue to user menu(Y/N)?")
            elif usinp==2:
                returna()
                cha=input("Do you want to continue to user menu(Y/N)?")
            elif usinp==3:
                bookdisp()
                print()
                cha=input("Do you want to continue to user menu(Y/N)?")
            elif usinp==4:
                bookissue()
                print()
                cha=input("Do you want to continue to user menu(Y/N)?")
            elif usinp==5:
                bookavlbl()
                print()
                cha=input("Do you want to continue to user menu(Y/N)?")
            elif usinp==6:
                studentdet()
                print()
                cha=input("Do you want to continue to user menu(Y/N)?")
            elif usinp==7:
                help1()
                print()
                cha=input("Do you want to continue to user menu(Y/N)?")
                print()
            elif usinp==8:
                about()
                print()
                cha=input("Do you want to continue to user menu(Y/N)?")
                print()
            elif usinp==9:
                print()
                cha='n'
    elif inp==2:
        print()
        print("              WELCOME TO SCHOOL LIBRARY MANAGEMENT SOFTWARE")
        print("              ---------------------------------------------")
        print()
        print("              ******WELCOME TO LOGIN MENU,PLEASE LOGIN*****")
        usr=input("Enter the user name:")
        print()
        pas=input("Enter the password:")
        cur.execute("select * from user;")
        for row in cur:
            username,password=row
        if usr==username and pas==password:
            print()
            print("******LOGIN SUCCESS!*******")
            print()
            cha='y'
            while cha in['Y','y']:
                print("                WELCOME TO SCHOOL LIBRARY MANAGEMENT SOFTWARE")
                print("                ---------------------------------------------")
                print()
                print("                *************ADMIN MENU***************")
                print()
                print('                    1.ADD A BOOK')
                print('                    2.REMOVE A BOOK')
                print('                    3.EDIT BOOK DETAILS')
                print('                    4.ADD A STUDENT')
                print('                    5.REMOVE A STUDENT')
                print('                    6.EDIT STUDENT DETAILS')
                print('                    7.HELP')
                print('                    8.ABOUT')
                print('                    9.RETURN TO MAIN MENU')
                print()
                adinp=int(input("Enter your desired option from above(1-9):"))
                if adinp==1:
                    addbook()
                    cha=input("Do you want to continue to admin menu(Y/N)?")
                elif adinp==2:
                    bookremove()
                    cha=input("Do you want to continue to admin menu(Y/N)?")
                elif adinp==3:
                    editbook()
                    cha=input("Do you want to continue to admin menu(Y/N)?")
                elif adinp==4:
                    addstud()
                    cha=input("Do you want to continue to admin menu(Y/N)?")
                elif adinp==5:
                    studremove()
                    cha=input("Do you want to continue to admin menu(Y/N)?")
                elif adinp==6:
                    editstud()
                    cha=input("Do you want to continue to admin menu(Y/N)?")
                elif adinp==7:
                    help1()
                    print()
                    cha=input("Do you want to continue to admin menu(Y/N)?")
                    print()
                elif adinp==8:
                    about()
                    print()
                    cha=input("Do you want to continue to admin menu(Y/N)?")
                    print()
                elif adinp==9:
                    print()
                    cha='n'
        else:
            print()
            print('          ***INCORRECT LOGIN DETAILS***')
            print()
            print("          Login Failed,Try Again!!!!!!!   ")
            print()
    elif inp==3:
        cha='y'
        while cha in['Y','y']:
            help1()
            print()
            cha=input("Please enter any key to return to main menu:")
            print()
    elif inp==4:
        cha='y'
        while cha in['Y','y']:
            about()
            print()
            cha=input("Please enter any key to return to main menu:")
            print()
    elif inp==5:
        cha='y'
        while cha in['Y','y']:
            connection = ms.connect(host='localhost',database='library',user='root',passwd='tiger')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
            else:
                print("Connection Failed")
            print()
            cha=input("Please enter any key to return to main menu:")
            print()
    elif inp==6:
        print()
        print("Are you sure?Press any other key to cancel")
        print()
        final=input("Enter N to confirm exit,or else press other key to cancel:")
        if final in['N','n']:
            ch='N'
            print()
            print('----------PROGRAM ENDED,THANK YOU--------------------')
            print()
            print('********************************************************')
            print('Thank you for using our School Library Management System')
            print('*********************************************************')
            print()
            print("(Please execute the program again to use again!!!!!)")
            




    
            
                











    
    
            
            
