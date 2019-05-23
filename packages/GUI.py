from tkinter import ttk
from tkinter import *

root = Tk()  




comvalue_faculty=StringVar()
comboxlist_faculty=ttk.Combobox(root, textvariable=comvalue_faculty) #初始化
comboxlist_faculty['values']=('人文學院', '管理學院', '科技學院', '教育學院')
comboxlist_faculty.current(0)  #defalut option
comboxlist_faculty.pack()

comvalue_department=StringVar()
comboxlist_department=ttk.Combobox(root, textvariable=comvalue_department) #初始化
comboxlist_department['values']=()
comboxlist_department.pack()


columns = ('course_cname', 'course_id', 'faculty', 'division', 'course_credit', 'time', 'location', 'teacher')
table_header = ['課程名稱', '課號', '開課單位', '年級', '學分', '時段', '開課地點', '教師名稱']
treeview = ttk.Treeview(root, height=18, show='headings', columns=columns)
for column in columns:
	if column == 'course_cname':
		treeview.column(column, width=190) # course_name need more space
	else:
		treeview.column(column, width=100)
for column, txt in zip(columns, table_header):
	treeview.heading(column, text=txt)
treeview.pack(side=LEFT, fill=BOTH)

# root.mainloop()

