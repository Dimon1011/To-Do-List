#To Do List GUI By Dima__!

#Python 3.6
#Part 1: crate the GUI Elements
# For testing purposes
import Tkinter
import random 
from Tkinter import *
from tkMessageBox import *

#Create root window
root = Tkinter.Tk()

#Change root window background color
root.configure(bg="white")

#Change the title
root.title("Dimas Cool To Do List")

#Change the window size
root.geometry("400x275")

#Create and emty list
tasks = []

#For testing purposes use a defult list
#tasks = ["Call Nastya", "Walk the dogs", "Buy milk"]


#Create functions

def update_listbox():
	#Clear the current list	
	clear_listbox()
	#Populate the listbox
	for task in tasks:
		lb_tasks.insert("end", task)

def clear_listbox():
	lb_tasks.delete(0, "end")

def add_task():
	#Get the task to add
	task = txt_input.get()
	#Make sure the task is not empty if pressing "Add task"
	if task !="":
		#Append to the list
		tasks.append(task)
		#Update the Listboxxx
		update_listbox()
	else:
		lbl_display["text"] = "Please enter Yo bitch ass task"
	txt_input.delete(0, "end")	


def del_all():
	#Since we are changing the list, it needs to be global!!!!!!!!
	global tasks
	#Clear the tasks list
	tasks = []
	#Update the listbox
	update_listbox()
	#Warning "DO YOU WANT TO DELETE?"
	messagebox.showwarning("Warning","Delete?")
	



def del_one():
	#Get the text of the current selected item
	task = lb_tasks.get("active")
	#Confirm it is in the list
	if task in tasks:
		tasks.remove(task)
	#Update the Listbox
	update_listbox()	

def sort_asc():
	#Sort the list
	tasks.sort()
	#Update the listbox
	update_listbox()

def sort_desc():
	#Sort the list
	tasks.sort()
	#Reverse the list
	tasks.reverse()
	#Update the listbox
	update_listbox()

def choose_rendom():
	#Choose a rendom task
	task = random.choice(tasks)
	#Update the display label
	lbl_display["text"]=task	

def number_of_tasks():
	#Get the number of tasks
	number_of_tasks = len(tasks)
	#Create and format the message
	msg = "Number of Shit you gotta do today: %s"	%number_of_tasks
	#Display the message
	lbl_display["text"]=msg

def Exit():
	pass








lbl_title = Tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = Tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=0,column=1)

txt_input = Tkinter.Entry(root, width=15)
txt_input.grid(row=1,column=1)

btn_add_task = Tkinter.Button(root, text="Add task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all = Tkinter.Button(root, text="Delete All", fg="green", bg="white", command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one = Tkinter.Button(root, text="Delete", fg="green", bg="white", command=del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_asc = Tkinter.Button(root, text="SORT (ASC)", fg="green", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc = Tkinter.Button(root, text="SORT (DESC)", fg="green", bg="white", command=sort_desc)
btn_sort_desc.grid(row=5,column=0)

btn_choose_rendom = Tkinter.Button(root, text="Choose Rendom", fg="green", bg="white", command=choose_rendom)
btn_choose_rendom.grid(row=6,column=0)

btn_number_of_tasks = Tkinter.Button(root, text="Number Of Tasks", fg="green", bg="white", command=number_of_tasks)
btn_number_of_tasks.grid(row=7,column=0)

btn_quit = Tkinter.Button(root, text="Exit", fg="green", bg="white", command=quit)
btn_quit.grid(row=8,column=0)

lb_tasks = Tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1, rowspan=7)







#Start the main events loop
root.mainloop()

 
