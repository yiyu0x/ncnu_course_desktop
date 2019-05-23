import requests
from packages.GUI import *

def updateTable(courses):
	# delete old item
	for row in treeview.get_children():
		treeview.delete(row)
    # insert new item
	for index, course in enumerate(courses):
		# API 處理時應該將沒有 location, time, teacher 的欄位自動填入空字串，保持全部資料統一格式
		if course.get('location') == None: 
			course['location'] = ''
		if course.get('time') == None:
			course['time'] = ''
		if course.get('teacher') == None:
			course['teacher'] = ''
		treeview.insert("", index, values=[course[i] for i in columns])

def selectName(*args):
	name = comboxlist_name.get()
	ans = [s for s in all_course_name if name.lower() in str(s).lower()]
	comboxlist_name['values']=[i for i in ans]
	if len(ans) > 0:
		courses = requests.get('https://api.ncnusa.ml/api/course/' + name).json()
		# remove duplicate dict in list
		courses = [dict(t) for t in {tuple(d.items()) for d in courses}]
		updateTable(courses)

def selectTea(*args):
	tea = comboxlist_teacher.get()
	ans = [s for s in all_teacher if tea in str(s)]
	comboxlist_teacher['values']=[i for i in ans]
	if len(ans) > 0:
		courses = requests.get('https://api.ncnusa.ml/api/teacher/' + tea).json()
		updateTable(courses)

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
	courses = requests.get('https://api.ncnusa.ml/api/faculty/' + fac).json()
	updateTable(courses)

comboxlist_faculty.bind("<<ComboboxSelected>>", selectFac) # bind function
comboxlist_department.bind("<<ComboboxSelected>>", selectDep) # bind function

comboxlist_teacher.bind("<<ComboboxSelected>>", selectTea) # bind function
comboxlist_teacher.bind("<KeyRelease>", selectTea) # dynamic binding

comboxlist_name.bind("<<ComboboxSelected>>", selectName) # bind function
comboxlist_name.bind("<KeyRelease>", selectName) # dynamic binding
# default value
all_teacher = requests.get('https://api.ncnusa.ml/api/teacherList/all').json()
all_course_name = requests.get('https://api.ncnusa.ml/api/courseList/all').json()
r = requests.get('https://api.ncnusa.ml/api/10')
courses = r.json()
# GUI.init()
updateTable(courses)

root.mainloop()