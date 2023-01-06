#main menu
import mysql.connector as mc
con=mc.connect(host="localhost", user="root", password="200913")
cur=con.cursor()
s="use passdata"
cur.execute(s)
print('WELCOME')
while True:
    print('     MENU:    ')
    print('Press 1: To create an account')
    print('Press 2: LOGIN')
    print('Press 3: To exit')
    OPTION=int(input('Enter the desired option'))
    if OPTION==1:
        print('Thanks for choosing our services')
        userid=int(input('Enter a unique userid'))
        username=input('Enter the Account Username')
        password=input('Enter the Account Password')
        pswd=input('Please re-enter the password')
        s='insert into logintable values({},"{}","{}")'.format(userid,username,password)
        cur.execute(s)
        con.commit()
        con.close()
        print(' ')
        print('NOTE:   Remember the filled details for accessing the account in future')
        print('Congratulations! Your account is successfully made')
        break
    elif OPTION==2:
        print('Welcome Back')
        userid=int(input('Enter your unique userid'))
        password=input('Enter the password')
        pass1='select Password from logintable where UserID={}'.format(userid)
        cur.execute(pass1)
        d=cur.fetchall()
        print(' ')
        if password==d[0][0]:
            s='create view v1 as select*from passtable where userid={}'.format(userid)
            cur.execute(s)
            print('     MENU:    ')
            print('To add a password press 1')
            print('To change the password press 2')
            print('To delete a password press 3')
            print('To show the password press 4')
            print('To exit to Main Menu press 5')
            print(' ')
            import PASSWORD
            while True:
                CHOICE=int(input('Please enter your choice:'))
                if CHOICE==1:
                    PASSWORD.add_pass()
                elif CHOICE==2:
                    PASSWORD.edit_pass()
                elif CHOICE==3:
                    PASSWORD.delete_pass()
                elif CHOICE==4:
                    PASSWORD.view_pass()
                elif CHOICE==5:
                    m='drop view v1'
                    cur.execute(m)
                    break
        else:
            print(' ')
            print('password does not match')
    elif OPTION==3:
        exitapp=input('Are you sure you want to exit')
        if exitapp=='yes':
            break
        else:
            continue

        
