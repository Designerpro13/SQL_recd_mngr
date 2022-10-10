import mysql.connector as sql
import sys
#connect to mysql database
db=sql.connect(host="localhost",user="root",passwd="rithu2005",database="mysql")
con=sql.connect(**db)
cursor=con.cursor()


#check database is connected
if db.is_connected():
    print("Database connected")


#MENU FOR STUDENT MARKS MANAGEMENT SYSTEM SOFTWARE
print("*************************************************")
print("WELCOME TO MY PROJECT STUDENT MARKS MANAGEMENT SYSTEM")
print("*************************************************")
print()
a="1:Displaying tables of database"
b="2:Displaying Tables fields"
c="3.Displaying all records of table"
d="4:Inserting new record into table"
e="5:Searching student details"
f="6:To update student marks"
g="7:Delete student record from table"
h="8:Graphical Representation"
i="9:Exit from program"

while True:
    print(a)
    print(b)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
    print()
    ch=input("ENTER YOUR CHOICE: ")
    
#Displaying tables of database
    if ch=='a':
        try:
            cursor.execute("SHOW TABLES")
            for i in cursor:
                print(i)
        except:
            print("! SORRY SOME ERROR OCCURRED !")

#Displaying Tables fields
    if ch=='b':
        try:
            table=str(input("ENTER TABLE NAME: "))
            a=cursor.execute("desc %s"%table)
            for i in a:
                print(i)
        except:
            print("! SORRY SOME ERROR OCCURRED !")

#Displaying all records of table
    if ch=='c':
        try:
            cursor.execute("select * from students;")
            data=cursor.fetchall()
            print("ADMN,NAME,CLASS,SECTION,GENDER,CONTACT,ENG_MARKS,MATHS_MARKS,BIO_MARKS,CHE_MARKS,PHY_MARKS,IP_MARKS,CS_MARKS,TOTAL,PERCENTAGE")
            for i in data:    
                j=str(i).split()
                for k in j:
                    print(k,end=" ")
                print()
        except:
            print("! SORRY SOME ERROR OCCURED !")

    #inserting new record into table
    if ch=='d':
        r=int(input("Enter student roll number: "))
        name=input("ENTER STUDENT NAME: ")
        c=str(input("ENTER CLASS OF STUDENT: "))
        st=str(input("ENTER SECTION OF STUDENT: "))
        co=int(input('ENTER CONTACT NUMBER: '))
        g=str(input('ENTER GRNDER: '))
        m1=int(input("ENTER MARKS IN ENGLISH: "))
        m2=int(input("ENTER MARKS IN MATHS: "))
        m3=int(input("ENTER MARKS IN BIOLOGY: "))
        m4=int(input("ENTER MARKS IN CHEMISTRY: "))
        m5=int(input("ENTER MARKS IN PHYSICS: "))
        m6=int(input("ENTER MARKS IN IP: "))
        m7=int(input("ENTER MARKS IN COMPUTER: "))
        t=m1+m2+m3+m4+m5+m6+m7
        per=t/7
        query="insert into students values(%d,\'%s\',\'%s\',\'%s\',\'%s\',%i,%d,%d,%d,%d,%d,%d,%d,%d,%d)"%(r,name,c,st,g,co,m1,m2,m3,m4,m5,m6,m7,t,per)
        cursor.execute(query)
        print("#####STUDENT RECORD SAVED IN TABLE######\n")
        con.commit()
    
    #searching student details
    if ch=='e':
        print("1:TO SERACH BY STUDENT ROLL NUMBER")
        print("2:TO SEARCH BY STUDENT NAME")
        c=int(input("ENTER YOUR CHOICE: "))
        #searching by student roll number
        if c==1:
            try:
                roll=int(input("ENTER STUDENT ROLL NUMBER TO SEARCH: "))
                qry="select * from student where roll=%d"%roll
                cursor.execute(qry)
                data=cursor.fetchall()
                if len(data)==0:
                    print("STUDENT NOT FOUND")
                print("ADMN,NAME,CLASS,SECTION,GENDER,CONTACT,ENG_MARKS,MATHS_MARKS,BIO_MARKS,CHE_MARKS,PHY_MARKS,IP_MARKS,CS_MARKS,TOTAL,PERCENTAGE")
                for i in data:
                    j=str(i).split()
                    for k in j:
                        print(k,end=" ")
                    print()
            except:
                print("! SORRY SOME ERROR OCCURED !")
    
    #searching by student name
        if c==2:
            try:
                name=input("ENTER STUDENT NAME TO SEARCH: ")
                qry="select * from student where name='%s'"%name
                cursor.execute(qry)
                data=cursor.fetchall()
                if len(data)==0:
                    print("! STUDENT NOT FOUND !")
                    print("ROLL NO","STUDENT NAME","CLASS","SECTION","SUBJECT 1","SUBJECT 2","SUBJECT 3","SUBJECT 4","SUBJECT 5","TOTAL MARKS","PERCENTAGE")
                    for i in data:
                        j=str(i).split()
                        for k in j:
                            print(k,end=" ")
                        print()
            except:
                print("! SORRY SOME ERROR OCCURED !")
    
    #To update student marks
    if ch=='f':
        try:
            roll=int(input("ENTER ROLL NUMBER OF STUDENT WHOSE MARKS TO BE UPDATE: "))
            qry="select * from students where roll=%d"%roll
            cursor.execute(qry)
            data=cursor.fetchall()
            if len(data)==0:
                print("! STUDENT NOT FOUND !")
            else:
                m1=int(input("ENTER UPDATED MARKS IN ENGLISH: "))
                m2=int(input("ENTER UPDATED MARKS IN MATHS: "))
                m3=int(input("ENTER UPDATED MARKS IN BIOLOGY: "))
                m4=int(input("ENTER UPDATED MARKS IN CHEMISTRY: "))
                m5=int(input("ENTER UPDATED MARKS IN PHYSICS: "))
                m6=int(input("ENTER UPDATED MARKS IN IP: "))
                m7=int(input("ENTER UPDATED MARKS IN COMPUTER SCIENCE: "))
                t=m1+m2+m3+m4+m5+m6+m7
                per=t/5
                qry="update STUDENT SET mark1=%d,mark2=%d,mark3=%d,mark4=%d,mark5=%d,mark6=%d,mark7=%d,total=%d,per=%d where roll=%d"%(m1,m2,m3,m4,m5,m6,m7,t,per,roll)
                cursor.execute(qry)
                print("STUDENT RECORD UPDATED")
                con.commit()
        except:
            print("! SORRY SOME ERROR OCCURED !")
    # Delete student record from table
    if ch=='g':
        try:
            roll=int(input("ENTER STUDENT ROLL NUMBER ,YOU WANT TO DELETE: "))
            qry="select * from students where roll=%d"%roll
            cursor.execute(qry)
            data=cursor.fetchall()
            if len(data)==0:
                print("! STUDENT NOT FOUND IN TABLE !")
            else:
                qry="delete from students where roll=%d"%(roll)
                cursor.execute(qry)
                print("STUDENT RECORD DELETED FROM TABLE")
                con.commit()
        except:
            print("! SORRY SOME ERROR OCCURED !")
    
    #Graphical Representation
    if ch=='h':
        def teachgr():
            print("1. Student's Classes \n2. Gender graph")
            x=int(input("Enter the no: "))
            if x==1:
                classgraph()
            elif x==2:
                sexgraph()
            elif x not in [1,2]:
                print("! INVAILD INPUT !")
        def classgraph():
            import pymysql
            import matplotlib.pyplot as plt
            d1=pymysql.connect(host="localhost",user="root",passwd=" ",database="school")
            c1=d1.cursor()
            
            quer="select count(*) from students where class='1';"
            c1.execute(quer)
            x=c1.fetchone()
            lst=list(x)
            quer="select count(*) from students where class='2';"
            c1.execute(quer)
            y=c1.fetchone()
            lst1=list(y)
            quer="select count(*) from students where class='3';"
            c1.execute(quer)
            z=c1.fetchone()
            lst2=list(z)
            quer="select count(*) from students where class='4';"
            c1.execute(quer)
            a=c1.fetchone()
            lst3=list(a)
            quer="select count(*) from students where class='5';"
            c1.execute(quer)
            d1.commit()
            a=c1.fetchone()
            lst4=list(a)
            lstt=lst+lst1+lst2+lst3+lst4
            y=["Class 1",'Class 2','Class 3','Class 4','Class 5']
            plt.bar(y,lstt,width=0.50)
            plt.xlabel("Classes")
            plt.ylabel("No. of Students")
            plt.show()
        def sexgraph():
            import pymysql
            import matplotlib.pyplot as plt
            d1=pymysql.connect(host="localhost",user="root",passwd=" ",database="school")
            c1=d1.cursor()
            quer='select count(*) from students where gender="male";'
            c1.execute(quer)
            x=c1.fetchone()
            lst=list(x)
            quer='select count(*) from students where gender="female";'
            c1.execute(quer)
            y=c1.fetchone()
            lst1=list(y)
            lstt=lst+lst1
            y=["Male","Female"]
            plt.bar(y,lstt,width=0.50)
            plt.xlabel("Sex")
            plt.ylabel("No. of Students")
            plt.show()
        teachgr()
    
    #Exit from program
    if ch=='i':
        print('''See you Later
###:-)###''')
        sys.exit()
    con.close()
