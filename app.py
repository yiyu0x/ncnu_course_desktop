import requests
from packages.GUI import *
# from tkinter import ttk
# from tkinter import *

def updateTable(courses):
	# delete old item
	for row in treeview.get_children():
		treeview.delete(row)
    # insert new item
	for index, course in enumerate(courses):
		treeview.insert("", index, values=[course[i] for i in columns])

def selectDep(*args):
	dep = comboxlist_department.get()
	courses = requests.get('https://api.ncnusa.ml/api/department/' + dep).json()
	updateTable(courses)
	

def selectFac(*args):
	fac = comboxlist_faculty.get()
	depList = requests.get('https://api.ncnusa.ml/api/depList/' + fac).json()
	# init department combox
	comboxlist_department['values']=[i for i in depList]
	comboxlist_department.current(0)  #defalut option

comboxlist_faculty.bind("<<ComboboxSelected>>", selectFac) # bind function
comboxlist_department.bind("<<ComboboxSelected>>", selectDep) # bind function

# default value
r = requests.get('https://api.ncnusa.ml/api/10')
courses = r.json()
# GUI.init()
updateTable(courses)

root.mainloop()