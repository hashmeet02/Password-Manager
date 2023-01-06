#
#adding a new password
#
def add_pass():
    dname=input("please enter the name of domain")
    uname=input("please enter the username")
    uid=input('please enter the unique userid')
    import mysql.connector as mc
    con=mc.connect(host="localhost", user="root", password="200913")
    cur=con.cursor()
    s="use passdata"
    cur.execute(s)
    print("press 1:user added password, 2:auto generated password")
    x=int(input("please enter your choice"))
    if x==1:
        n=0
        while n==0:
            pass1=input('enter the password')
            a,b=0,0
            for i in range(0,len(pass1)):
                if pass1[i].isnumeric():
                    a+=1
                elif pass1[i] in ['!','@','$','%','^','&','*','/','?',':',';']:
                    b+=1
            if len(pass1)<=7:
                print('Password must be of 8 characters')
                continue
            elif a<2:
                print('Weak Password','Password must contain atleast two digits')
                continue
            elif b<1:
                print('Weak Password')
                print('Password must contain atleast one special character out of the following:')
                print(['!','@','$','%','^','&','*','/','?',':',';'])
                continue
            else:
                print('strong password')
                n=1
        pass2=input("please re-enter the password")
        if pass1==pass2:
            s1="insert into passtable values(%s,%s,%s,%s)"
            cur.execute(s1,(dname,uname,pass1,uid))
            con.commit()
            con.close()
            print("the password is successfully added")
        else:
            print("the passwords don't match please try again")
    elif x==2:
        pass3=""
        import random as r
        pass3+=chr(r.randint(65,90))
        pass3+=chr(r.randint(48,57))
        pass3+=chr(r.randint(97,122))
        pass3+=chr(r.randint(97,122))
        pass3+=chr(r.randint(97,122))
        pass3+=chr(r.randint(97,122))
        pass3+=chr(r.randint(97,122))
        pass3+=chr(r.randint(97,122))
        print("your new password is",pass3)
        s1="insert into passtable values(%s,%s,%s,%s)"
        cur.execute(s1,(dname,uname,pass3,uid))
        con.commit()
        con.close()
        print("the password is successfully added") 
#
#changing your password
#
def edit_pass():
    
    uname=input('Please enter your username:')
    import mysql.connector as mc
    con=mc.connect(host="localhost", user="root", password="200913")
    cur=con.cursor()
    s="use passdata"
    cur.execute(s)
    print("Press 1:User added password, 2:Auto-generated password")
    x=int(input("Please enter your choice:"))
    if x==1:
        n=0
        while n==0:
            pass1=input('Enter the password:')
            a,b=0,0
            for i in range(0,len(pass1)):
                if pass1[i].isnumeric():
                    a+=1
                elif pass1[i] in ['!','@','$','%','^','&','*','/','?',':',';']:
                    b+=1
            if len(pass1)<=7:
                print('Password must be of 8 characters')
                continue
            elif a<2:
                print('Weak Password','Password must contain atleast two digits')
                continue
            elif b<1:
                print('Weak Password')
                print('Password must contain atleast one special character out of the following:')
                print(['!','@','$','%','^','&','*','/','?',':',';'])
                continue
            else:
                print('Strong Password')
                n=1
        pass2=input("Please re-enter the password:")
        if pass1==pass2:
            s1="update passtable set password='{}' where username='{}'".format(pass1,uname)
            cur.execute(s1)
            con.commit()
            con.close()
            print("The Password is successfully changed")
        else:
            print("The Passwords don't match please try again")
    elif x==2:
        pass3=''
        import random as r
        pass3+=chr(r.randint(65,90))
        pass3+=chr(r.randint(48,57))
        pass3+=chr(r.randint(97,122))
        pass3+=chr(r.randint(97,122))
        pass3+=chr(r.randint(97,122))
        pass3+=chr(r.randint(97,122))
        pass3+=chr(r.randint(97,122))
        pass3+=chr(r.randint(97,122))
        print("your new password is",pass3)
        pass4=input('Re-enter the password: ')
        s1="update passtable set password='{}' where username='{}'".format(pass4,uname)
        cur.execute(s1)
        con.commit()
        con.close()
        print("The password is successfully changed")
#
#deleting a password
#
def delete_pass():
    dname=input("please enter the name of domain")
    uid=input("please enter unique userid")
    import mysql.connector as mc
    con=mc.connect(host="localhost", user="root", password="200913")
    cur=con.cursor()
    s="use passdata"
    cur.execute(s)
    s1="select * from passtable where Domain_name='{}' and UserID={}".format(dname,uid)
    cur.execute(s1)
    d=cur.fetchall()
    if len(d)>=1: #password exists
        s2="delete from passtable where Domain_name='{}' and UserID={}".format(dname,uid)
        cur.execute(s2)
        con.commit()
        con.close()
        print("your password is successfully deleted")
    else:
        print("the passwords doesn't exist")
#
#viewing a password
#
def view_pass():
    dname=input("please enter the name of domain")
    uid=input("please enter the unique userid")
    import mysql.connector as mc
    con=mc.connect(host="localhost", user="root", password="200913")
    cur=con.cursor()
    s="use passdata"
    cur.execute(s)
    s1="select * from v1 where Domain_name='{}' and UserId={}".format(dname,uid)
    cur.execute(s1)
    d=cur.fetchall()
    if len(d)>=1:
        print("the password is",d)
    else:
        print("the password doesn't exist")
