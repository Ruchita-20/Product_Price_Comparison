from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


import pymysql


#Functionality Part

def clear():
    username_entry.delete(0,END)
    newpasswrd_entry.delete(0,END)

def forget_pass():
    def change_psswrd():
        if user_entry.get()=='' or newpass_entry.get()=='' or cnfrmpass_entry.get()=='':
            messagebox.showerror('Error','Fields Cannot Be Empty',parent=window)
        elif newpass_entry.get()!=cnfrmpass_entry.get():
            messagebox.showerror('Error','Both Password Should Be same',parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='Sid@2003',database='userdata')
            mycursor = con.cursor()
            query='select * from usrdata where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query='update usrdata set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password Is Been Reset Successfully, Now Login With New Password',parent=window)
                window.destroy()

    window =Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bgLabel = Label(window, image=bgPic)
    bgLabel.grid()

    heading_label = Label(window, text='RESET PASSWORD', font=('Arial Rounded MT Bold','18'),
                          bg='white', fg='VioletRed3')
    heading_label.place(x=490,y=60)

    userLabel = Label(window,text='Username', font=('Constantia',14,'bold'),bg='white',fg='PaleVioletRed2')
    userLabel.place(x=480, y=130)

    user_entry=Entry(window,width=25,fg='black',font=('Century',12,'bold'),bd=0)
    user_entry.place(x=480,y=160)

    Frame(window, width=250, height=2,bg='PaleVioletRed3').place(x=480,y=180)

    passwordLabel = Label(window, text='New Password', font=('Constantia',14,'bold'), bg='white', fg='PaleVioletRed2')
    passwordLabel.place(x=480, y=210)

    newpass_entry = Entry(window, width=25, fg='black', font=('Century', 12, 'bold'), bd=0)
    newpass_entry.place(x=480, y=240)

    Frame(window, width=250, height=2, bg='PaleVioletRed3').place(x=480, y=260)

    cnfrmpasswordLabel = Label(window, text='Confirm Password', font=('Constantia',14,'bold'), bg='white', fg='PaleVioletRed2')
    cnfrmpasswordLabel.place(x=480, y=290)

    cnfrmpass_entry = Entry(window, width=25, fg='black', font=('Century', 12, 'bold'), bd=0)
    cnfrmpass_entry.place(x=480, y=320)

    Frame(window, width=250, height=2, bg='PaleVioletRed3').place(x=480, y=340)

    submitButton = Button(window, text='SUBMIT', font=('Arial Black', 16, 'bold')
                         , fg='white', bg='VioletRed3', activeforeground='white'
                         , activebackground='VioletRed3', cursor='hand2', bd=0, width=16,command=change_psswrd)
    submitButton.place(x=485, y=390)


    window.mainloop()

def login_user():
    if username_entry.get()=='' or newpasswrd_entry.get()=='':
        messagebox.showerror('Error','Fields Cannot Be Empty')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Sid@2003')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Connectivity Issue')
            return

        query='use userdata'
        mycursor.execute(query)
        query='select * from usrdata where username=%s and password=%s'
        mycursor.execute(query,(username_entry.get(),newpasswrd_entry.get()))

        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid Username Or Password')
        else:
            messagebox.showinfo('Success','User Is Been Logged In Successfully')
            con.commit()
            con.close()
            clear()
            login_window.destroy()
            import ppc







def signup_page():
    login_window.destroy()
    import signup



def show():
    closeeye.configure(file='openeye.png')
    newpasswrd_entry.configure(show='')
    eyeButton.config(command=hide)
def hide():
    newpasswrd_entry.configure(show='*')
    closeeye.configure(file='closeeye.png')

    eyeButton.config(command=show)

#Gui Part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bgs.jpg')

bgLabel = Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Arial Rounded MT Bold',23)
              ,bg='white',fg='maroon4')
heading.place(x=620,y=125)


usernameLabel = Label(login_window,text='Username', font=('Constantia',14,'bold'),bg='white',fg='PaleVioletRed2')
usernameLabel.place(x=600, y=200)

username_entry=Entry(login_window,width=25,fg='black',font=('Century',12),bd=0)
username_entry.place(x=600,y=230)


Frame(login_window,width=250,height=2,bg='maroon4').place(x=600,y=253)



passwrd_Label = Label(login_window, text='Password', font=('Constantia', 14, 'bold'), bg='white', fg='PaleVioletRed2')
passwrd_Label.place(x=600, y=270)

newpasswrd_entry = Entry(login_window, width=25, fg='black', font=('Century', 12), bd=0,show='*')
newpasswrd_entry.place(x=600, y=300)

Frame(login_window,width=250,height=2,bg='maroon4').place(x=600,y=323)

closeeye=PhotoImage(file='closeeye.png')
eyeButton=Button(login_window,image=closeeye,bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',command=show)
eyeButton.place(x=820,y=295)

forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',font=('Constantia',11)
                    ,fg='maroon4',activeforeground='maroon4',command=forget_pass)
forgetButton.place(x=730,y=340)

loginButton=Button(login_window,text='LOGIN',font=('Arial Black',16,'bold')
                   ,fg='white',bg='maroon4',activeforeground='white'
                   ,activebackground='maroon4',cursor='hand2',bd=0,width=16,command=login_user)
loginButton.place(x=600,y=400)

signupLabel=Label(login_window,text="Don't Have An Account?",font=('Open Sans',9,'bold'),fg='maroon4',bg='white')
signupLabel.place(x=610,y=460)

newaccountButton=Button(login_window,text='Create New One',font=('Open Sans',9,'bold underline')
                   ,fg='blue',bg='white',activeforeground='blue'
                   ,activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=750,y=459)

login_window.mainloop()