


from tkinter import *
import string
import random


def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    number = string.digits
    special_characters = string.punctuation
    all=small_alphabets+capital_alphabets+number+special_characters
    password_length = int(length_box.get())
    if choice.get() == 1:
        passwordfield.insert(0,random.sample(small_alphabets,password_length))
    if choice.get() == 2:
        passwordfield.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    if choice.get() == 3:
        passwordfield.insert(0,random.sample(all,password_length))



    # password=random.sample(all,password_length)
    # passwordfield.insert(0,password)




root = Tk()
root.config(bg="gray20")
choice = IntVar()
font = ("aerial",13,'bold')
# root.geometry("300x450")
passwordLabel = Label(root,text = "PASSWORD GENERATOR",font=('times new roman',20,'bold'),bg="grey20",fg='white')
passwordLabel.grid()

weakradiobutton  = Radiobutton(root,text='weak',value=1,variable=choice,font= font)
weakradiobutton.grid(pady=5)

mediumradiobutton  = Radiobutton(root,text='medium',value=2,variable=choice,font= font)
mediumradiobutton.grid(pady=5)

strongradiobutton  = Radiobutton(root,text='strong',value=3,variable=choice,font= font)
strongradiobutton.grid(pady=5)

passwordLabel = Label(root,text = "password length",font=font,bg="grey20",fg='white')
passwordLabel.grid()

length_box = Spinbox(root,from_=5,to=18,width=5,font=font)
length_box.grid(pady=5)

generatebutton = Button(root,text="Generate",font=font,command=generator)
generatebutton.grid(pady=6)

passwordfield = Entry(root,width=25,bd=3,font=font)                  
passwordfield.grid(pady=5)

copybutton = Button(root,text="Copy",font=font)
copybutton.grid(pady=5)



root.mainloop()