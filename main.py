from tkinter import *
from tkinter import messagebox
import pyperclip
from PIL import Image,ImageTk
import random
import re
#------------------Generate Password Mechanism--------------#
def pass_gen():
    special_character = [
        '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=',
        '{', '}', '[', ']', '|', '\\', ';', ':', '"', '<', '>', ',', '.', '/', '?', ')'
    ]
    lower_case = [chr(n) for n in range(97, 123)]
    upper_case = [n.upper() for n in lower_case]
    number = [str(n) for n in range(1, 10)]
    password = []
    password.extend(random.sample(lower_case, 3))
    password.extend(random.sample(upper_case, 3))
    password.extend(random.sample(special_character, 3))
    password.extend(random.sample(number, 3))
    random.shuffle(password)
    pyperclip.copy("".join(password))
    password_entry.delete(0,END)
    password_entry.insert(0,string="".join(password))
#---------------Register the text ---------------#
def add():
    password = password_entry.get()
    email = email_entry.get()
    web = web_entry.get()


#--------Checking Whether the Email is Entered in the Correct Gmail Format-----#
    pattern = r"[@]gmail\.com"
    found = re.search(pattern,email)
    if found != None and password != "" and web != "":
        with open("./password_backup.txt","a+") as file:
            file.seek(0)
            lines = file.readlines()
            credentials = f"{web} | {email} | {password}\n"
            if credentials not in lines:
                file.write(credentials)
            else:
                print("It already exists!")


    else:
        messagebox.showinfo("Alert!","Fill all the Fields Correctly and Your email should be {}@gmail.com format")
window = Tk()
window.config(bg = "#FFFFFF")

#------------------------Canvas Config----------------------------------#
canvas= Canvas(width=300,height=300,bg='#FFFFFF',highlightthickness=0)
#------------Resizing the Image-----------#
image = Image.open("lock.png")
resized_img = image.resize((250,250))
img = ImageTk.PhotoImage(resized_img)
#------------Canvas Image-----------------#
canvas_image = canvas.create_image(150,150,image = img)

#----------------------Enteries----------------#
web_label = Label(text="Website:",font = ("FreeMono",14,"bold"),bg = "#FFFFFF")
web_entry = Entry(width=42)
email_label = Label(text="Email/Username:",font = ("FreeMono",14,"bold"),bg = "#FFFFFF")
email_entry = Entry()
password_label = Label(text="Password:",font = ("FreeMono",14,"bold"),bg = "#FFFFFF")
password_entry = Entry()
#------------------Buttons------------#
pass_gen_btn = Button(text = "Generate Password",bg = "#FFFFFF",font="FreeMono",width = 15,height = 1,command=pass_gen)
add_btn = Button(text = "Add",font="FreeMono",bg = "#FFFFFF",command=add)
#-------------------Grid Configuration---------------#
canvas.grid(row = 0,column = 2)
web_label.grid(row = 1 , column = 1)
web_entry.grid(row = 1, column=2,columnspan=2)
email_label.grid(row = 2, column= 1)
email_entry.grid(row = 2 , column = 2)
password_label.grid(row = 3, column = 1)
password_entry.grid(row = 3,column = 2)
pass_gen_btn.grid(row = 3,column = 3)
add_btn.grid(row = 4, column=2)






























window.mainloop()