from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    cnfrmpasswordEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or cnfrmpasswordEntry.get()=='':
        messagebox.showerror('Error','Fields Cannot Be Empty')
    elif passwordEntry.get() != cnfrmpasswordEntry.get():
        messagebox.showerror('Error','Both Password Should Be same')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept The Terms & Conditions')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Sid@2003')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table usrdata(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query='select * from usrdata where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username Already Exits')
        else:
            query = 'insert into usrdata(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'User Is Been Registered Successfully')
            clear()
            signup_window.destroy()
            import signin


def login_page():
    signup_window.destroy()
    import signin

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bgs.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=576,y=111)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Arial Rounded MT Bold',18)
              ,bg='white',fg='maroon4')
heading.grid(row=0,column=0,padx=9,pady=10)

emailLabel=Label(frame,text='Email',font=('Constantia',13,'bold'),bg='white',fg='maroon4')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=27,font=('Century',13,'bold'),
                 fg='black',bg='grey95')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Constantia',13,'bold'),bg='white',fg='maroon4')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=27,font=('Century',13,'bold'),
                 fg='black',bg='grey95')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Constantia',13,'bold'),bg='white',fg='maroon4')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=27,font=('Century',13,'bold'),
                 fg='black',bg='grey95')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

cnfrmpasswordLabel=Label(frame,text='Confirm Password',font=('Constantia',13,'bold'),bg='white',fg='maroon4')
cnfrmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

cnfrmpasswordEntry=Entry(frame,width=27,font=('Century',13,'bold'),
                 fg='black',bg='grey95')
cnfrmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termsandcondition=Checkbutton(frame,text='I Agree To All The Terms & Conditions',font=('Open Sans',9,'bold'),
                              fg='maroon4',bg='white'
                              ,activebackground='white',activeforeground='maroon4',cursor='hand2',variable=check)
termsandcondition.grid(row=9,column=0,sticky='w',pady=10,padx=18)

signupButton=Button(frame,text='SIGN UP', font=('Arail Black',16,'bold'),bd=0,bg='maroon4',fg='white'
                    ,activebackground='maroon4',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccnt=Label(frame,text="Don't Have An Account?",font=('Open Sans',9,'bold'),fg='maroon4',bg='white')
alreadyaccnt.grid(row=14,column=0,sticky='w',padx=65,pady=7)

loginButton=Button(frame,text='Log In',font=('Open Sans',9,'bold underline')
                   ,fg='blue',bg='white',activeforeground='blue'
                   ,activebackground='white',cursor='hand2',bd=0,command=login_page)
loginButton.place(x=207,y=412)




signup_window.mainloop()