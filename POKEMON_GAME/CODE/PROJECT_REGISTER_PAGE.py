##Import Libraries

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
import random
import string
from captcha.image import ImageCaptcha

##Creating a New Window

registerw = Tk()
registerw.geometry("1024x640")
registerw.title("REGISTER WINDOW")
registerw.config(bg = "Yellow")
registerw.wm_iconbitmap(r"C:\Users\joseph jenis\AppData\Local\Programs\Python\Python310\Proj\projimg02.ico")

image_1 = Image.open("./projimg14.png")
resized = image_1.resize((1532,790))
image_2 = ImageTk.PhotoImage(resized)
lbl1 = Label(registerw, text = "", image = image_2).place(x = 0, y = 0)

Label(registerw,text ="Create Your Account", bg = "Yellow", fg = "Black", font = ("OCR A Extended", 40)).pack()

##Function to Delete Data After Registration

def clear():
    email_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    confirm_password_entry.delete(0, END)
    
##Function to Link with My Sql

def connect_database():
    
    if email_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "" or confirm_password_entry.get() == "":
        messagebox.showerror("Invalid", "All Fields are Required")

    elif check(captcha_entry.get(), random_string):
        messagebox.showerror("Invalid", "Captcha Mismatch")
        
    elif password_entry.get() != confirm_password_entry.get():
        messagebox.showerror("Invalid", "Password Mismatch")

    else:
        try:
            con = pymysql.connect(host = "localhost", user = "root", password = "root")
            mycursor = con.cursor()

        except:
            messagebox.showerror("Error", "Database Connectivity Issue, Try Again")
            return

        try:
            query = "create database game_register"
            mycursor.execute(query)
            query = "use game_register"
            mycursor.execute(query)
            query = "create table game_data(Id int auto_increment primary key not null, Email varchar(50), Username varchar(100), Password varchar(20))"
            mycursor.execute(query)

        except:
            mycursor.execute("use game_register")

        ##Query for Duplicate Email
            
        query = "select * from game_data where Email = %s"
        mycursor.execute(query, (email_entry.get()))
        row_1 = mycursor.fetchone()
        
        ##Query for Duplicate Username

        query = "select * from game_data where Username = %s"
        mycursor.execute(query, (username_entry.get()))
        row_2 = mycursor.fetchone()
        
        if row_1 != None:
            messagebox.showerror("Error", "Email Already Exists.\nTry Again.")

        elif row_2 != None:
            messagebox.showerror("Error", "Username Already Exists.\nTry Again.")

        else:
            ##Query for Inserting Data into Database
            
            mycursor.execute("insert into game_data (Email, Username, Password) values ('{}','{}','{}');".format(email_entry.get(), username_entry.get(), password_entry.get()))                                                                                                                                                                     
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration Done.")
            clear()

            registerw.destroy()
            import PROJECT_LOGIN_PAGE
        
##Function to Link Register page and Login page

def loginw():
    registerw.destroy()
    import PROJECT_LOGIN_PAGE

##Captcha
def createImage(flag = 0):
    global random_string
    global image_label
    global image_display
    global entry
    global verify_label
   
    if flag == 1:
        verify_label.grid_forget()

    captcha_entry.delete(0, END)

    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k = 6))

    image_captcha = ImageCaptcha(width = 250, height = 125)
    image_generated = image_captcha.generate(random_string)
    image_display = ImageTk.PhotoImage(Image.open(image_generated))

    image_label.grid_forget()
    image_label = Label(registerw, image = image_display)
    image_label.place(x = 510, y = 350)

def check(x, y):
   
    global verify_label

    verify_label.grid_forget()
    createImage()

if __name__ == "__main__":

    verify_label = Label(registerw)
    image_label = Label(registerw)

    captcha_entry = Entry(registerw, width=10, font = ("OCR A Extended", 12))
    captcha_entry.place(x = 792, y = 400)

    createImage()

    reload_button = Button(text= "REFRESH", bg = "Orange", fg = "Black", font = ("OCR A Extended", 12, "bold"), command = lambda: createImage(1))
    reload_button.place(x = 797, y = 365)

##Email Label and Entry
m_e = StringVar()

email_label = Label(registerw, text = "Email", bg = "Yellow", fg = "Black", font = ("OCR A Extended", 12, "bold"))
email_label.place(x = 510, y = 100)

email_entry = Entry(registerw, width = 35, bg = "White", font = ("OCR A Extended", 12, "bold"), bd = 0, textvariable = m_e) 
email_entry.place(x = 510, y = 125)

##Username Label and Entry

u_e = StringVar()

username_label = Label(registerw, text = "Username", bg = "Yellow", fg = "Black", font = ("OCR A Extended", 12, "bold"))
username_label.place(x = 510, y = 155)

username_entry = Entry(registerw, width = 35, bg = "White", font = ("OCR A Extended", 12, "bold"), bd = 0, textvariable = u_e) 
username_entry.place(x = 510, y = 180)

##Password Label and Entry

p_e = StringVar()

password_label = Label(registerw, text = "Password", bg = "Yellow", fg = "Black", font = ("OCR A Extended", 12, "bold"))
password_label.place(x = 510, y = 210)

password_entry = Entry(registerw, width = 35, bg = "White", font = ("OCR A Extended", 12, "bold"), bd = 0,textvariable = p_e) 
password_entry.place(x = 510, y = 235)

##Confirm Password Label and Entry

cp_e = StringVar()

confirm_password_label = Label(registerw, text = "Confirm Password", bg = "Yellow", fg = "Black", font = ("OCR A Extended", 12, "bold"))
confirm_password_label.place(x = 510, y = 265)

confirm_password_entry = Entry(registerw, width = 35, bg = "White", font = ("OCR A Extended", 12, "bold"), bd = 0, textvariable = cp_e) 
confirm_password_entry.place(x = 510, y = 290)

##Register Button

register_button = Button(registerw, text = "REGISTER", bg = "Orange", fg = "Black", cursor = "hand2", font = ("OCR A Extended", 20), width = 10, height = 1, command = connect_database)
register_button.place(x = 600, y = 500)

##Signup Label

signuplabel = Label(registerw, text ="Already have an account?", bg = "Yellow", fg = "Black", font = ("OCR A Extended", 10, "bold"))
signuplabel.place(x = 510, y = 570)

##Login into existing Account

accbutton = Button(registerw, text = "Login", bd = 0, bg = "Yellow", activebackground = "Yellow", font = ("OCR A Extended", 10, "bold underline"), cursor = "hand2", command = loginw)
accbutton.place(x = 840, y = 570)

registerw.mainloop()
