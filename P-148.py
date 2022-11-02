from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

list_of_items = Label(root)
random_number_label = Label(root)

items = ["Water Bottle", "Chocolate", "Sandwich", "Cookies", "Toys"]
list_of_items['text'] = "Listed items: " + str(items)

def randomlist():
    random_number = random.sample(range(0,5),1)
    random_number_label["text"] = "Put item no " + str(random_number) + "in bag."

btn=Button(root,text="Generate random list ",command=randomlist)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

list_of_items.place(relx=0.5,rely=0.5,anchor=CENTER)
random_number_label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()
