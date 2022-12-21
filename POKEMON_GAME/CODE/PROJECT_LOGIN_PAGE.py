##Import Libraries

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

##Function for Forget Password

def forget_password():
    def change_password():
        if username_entry.get() == "" or password_entry.get() == "" or confirm_password_entry.get() == "":
            messagebox.showerror("Invalid", "All Fields are Required", parent = forgetpass)

        elif password_entry.get() != confirm_password_entry.get():
            messagebox.showerror("Invalid", "Password and Confirm Password Should Match", parent = forgetpass)

        else:
            ##Connect with My Sql
            
            con = pymysql.connect(host = "localhost", user = "root", password = "root", database = "game_register")
            mycursor = con.cursor()
 
            query = "select * from game_data where Username = %s" 
            mycursor.execute(query, (username_entry.get()))
            row_1 = mycursor.fetchone()

            if row_1 == None:
                messagebox.showerror("Error", "Incorrect Username", parent = forgetpass)

            else:
                query = "update game_data set password = %s where username = %s"
                mycursor.execute(query, (password_entry.get(), username_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Password Updated", parent = forgetpass)
                forgetpass.destroy()
                
    ## New Window
            
    forgetpass = Toplevel()
    forgetpass.geometry("1024x640")
    forgetpass.title("CHANGE PASSWORD")
    
    image_1 = Image.open("./projimg18.png")
    resized = image_1.resize((1532,790))
    image_2 = ImageTk.PhotoImage(resized)
    lbl1 = Label(forgetpass, text = "", image = image_2).place(x = 0, y = 0)
    
    forgetpass.wm_iconbitmap(r"C:\Users\joseph jenis\AppData\Local\Programs\Python\Python310\Proj\projimg02.ico")

    ##Heading

    Label(forgetpass, text ="Change Your Password", bg = "Black", fg = "White", font = ("OCR A Extended", 40)).pack()

    ##Username

    username_label = Label(forgetpass, text = "USERNAME:", bg = "Black", fg = "White", font = ("OCR A Extended", 12, "bold")) 
    username_label.place(x = 580, y = 130)

    username_entry = Entry(forgetpass, width = 30, bg = "Black", fg = "White", font = ("OCR A Extended", 12, "bold"), bd = 0) 
    username_entry.place(x = 580, y = 155)

    username_frame = Frame(forgetpass, width = 400, height = 3, bg = "White")
    username_frame.place(x = 580, y = 175)

    ##Password

    password_label = Label(forgetpass, text = "PASSWORD:", bg = "Black", fg = "White", font = ("OCR A Extended", 12, "bold")) 
    password_label.place(x = 580, y = 190)

    password_entry = Entry(forgetpass, width = 30, bg = "Black", fg = "White", font = ("OCR A Extended", 12, "bold"), bd = 0) 
    password_entry.place(x = 580, y = 215)

    password_frame = Frame(forgetpass, width = 400, height = 3, bg = "White")
    password_frame.place(x = 580, y = 235)

    ##Password

    confirm_password_label = Label(forgetpass, text = "CONFIRM PASSWORD:", bg = "Black", fg = "White", font = ("OCR A Extended", 12, "bold")) 
    confirm_password_label.place(x = 580, y = 250)

    confirm_password_entry = Entry(forgetpass, width = 30, bg = "Black", fg = "White", font = ("OCR A Extended", 12, "bold"), bd = 0) 
    confirm_password_entry.place(x = 580, y = 275)

    confirm_password_frame = Frame(forgetpass, width = 400, height = 3, bg = "White")
    confirm_password_frame.place(x = 580, y = 295)

    ##Submit

    login_button = Button(forgetpass, text = "SUBMIT", bg = "Orange", fg = "Black", cursor = "hand2", font = ("OCR A Extended", 20), width = 10, height = 1, command = change_password)
    login_button.place(x = 690, y = 320)
    
    forgetpass.mainloop()

##Function to link Register page and Login page

def registerw():
    loginw.destroy()
    import PROJECT_REGISTER_PAGE

##Function Password eye button

def hide():
    openeye.config(file = "closeeye.png")
    password_entry.config(show = "*")
    eyebutton.config(command = show)

def show():
    openeye.config(file = "openeye.png")
    password_entry.config(show = "")
    eyebutton.config(command = hide) 

##Function for Username and Password

def username_enter(event):
    if username_entry.get() == "USERNAME":
      username_entry.delete(0, END)

def password_enter(event):
    if password_entry.get() == "PASSWORD":
      password_entry.delete(0, END)

##Function to Link Login Page with Database 

def login_user():
    if username_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror("Invalid", "All Fields are Required")
        
    else:
        try:
            con = pymysql.connect(host = "localhost", user = "root", password = "root")
            mycursor = con.cursor()
            
        except:
            messagebox.showerror("Error", "Connectivity is not Established, Try Again")
            return

        query = "use game_register"
        mycursor.execute(query)
        query = "select * from game_data where Username = %s and Password = %s" 
        mycursor.execute(query, (username_entry.get(), password_entry.get()))
        row_1 = mycursor.fetchone()
        
        if row_1 == None:
            messagebox.showerror("Error", "Invalid Username or Password")

        else:
            messagebox.showinfo("Welcome", "Login Successful!!")
            loginw.destroy()
            import PROJECT_OPTION_CARD
        
##Creating the Login Window
      
loginw = Tk()
loginw.geometry("1024x640")
loginw.title("LOGIN WINDOW")
loginw.config(bg = "Yellow")
loginw.wm_iconbitmap(r"C:\Users\joseph jenis\AppData\Local\Programs\Python\Python310\Proj\projimg02.ico")

##Background Image

image_1 = Image.open("./projimg06.png")
resized = image_1.resize((1532,790))
image_2 = ImageTk.PhotoImage(resized)
lbl1 = Label(loginw, text = "", image = image_2).place(x = 0, y = 0)

Label(loginw, text ="Login to Your Account", bg = "Black", fg = "White", font = ("OCR A Extended", 40)).pack()

##Username

username_entry = Entry(loginw, width = 36, bg = "Yellow", font = ("OCR A Extended", 12, "bold"), bd = 0) 
username_entry.place(x = 512, y = 100)
username_entry.insert(0, "USERNAME")

username_entry.bind("<FocusIn>", username_enter)

username_frame = Frame(loginw, width = 400, height = 3, bg = "Black")
username_frame.place(x = 512, y = 122)

##Password

password_entry = Entry(loginw, width = 36, bg = "Yellow", font = ("OCR A Extended", 12, "bold"), bd = 0) 
password_entry.place(x = 512, y = 140)
password_entry.insert(0, "PASSWORD")

password_entry.bind("<FocusIn>", password_enter)

password_frame = Frame(loginw, width = 400, height = 3, bg = "Black")
password_frame.place(x = 512, y = 162)

##Buttons

openeye = PhotoImage(file = "openeye.png")
eyebutton = Button(loginw, image = openeye, bd = 0, activebackground = "Yellow", cursor = "hand2", command = hide)
eyebutton.place(x = 880, y = 140)

forgotbutton = Button(loginw, text = "Forgot Password?", bd = 0, bg = "Yellow", activebackground = "Yellow", font = ("OCR A Extended", 10, "bold"), cursor = "hand2", command = forget_password)
forgotbutton.place(x = 760, y = 170)
 
login_button = Button(loginw, text = "LOGIN", bg = "Orange", fg = "Black", cursor = "hand2", font = ("OCR A Extended", 20), width = 10, height = 1, command = login_user)
login_button.place(x = 635, y = 200)

newaccbutton = Button(loginw, text = "Create a new account", bd = 0, bg = "Yellow", activebackground = "Yellow", font = ("OCR A Extended", 10, "bold underline"), cursor = "hand2", command = registerw)
newaccbutton.place(x = 730, y = 270)

##Label

signuplabel = Label(loginw, text ="Don't have an account?", bg = "Yellow", fg = "Black", font = ("OCR A Extended", 10, "bold"))
signuplabel.place(x = 510, y = 270)

loginw.mainloop()
