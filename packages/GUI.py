from tkinter import ttk
from tkinter import *

root = Tk()  
root.title('暨大課程快速搜尋')
frame = Frame(root)
frame.pack()

###window_center##################################################################
w = 900 # width for the Tk root
h = 600 # height for the Tk root
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
###select_div####################################################################
Label(frame, text='學院: ').grid(row=0, column=0)
comvalue_faculty=StringVar()
comboxlist_faculty=ttk.Combobox(frame, textvariable=comvalue_faculty, state="readonly")
comboxlist_faculty['values']=('人文學院', '管理學院', '科技學院', '教育學院')
comboxlist_faculty.current(0)  #defalut option
comboxlist_faculty.grid(row=0, column=1)
Label(frame, text='系所: ').grid(row=0, column=2)
comvalue_department=StringVar()
comboxlist_department=ttk.Combobox(frame, textvariable=comvalue_department, state="readonly")
comboxlist_department['values']=()
comboxlist_department.grid(row=0, column=3)
Label(frame, text='教師姓名: ').grid(row=1, column=0)
comvalue_teacher=StringVar()
comboxlist_teacher=ttk.Combobox(frame, textvariable=comvalue_teacher)
comboxlist_teacher['values']=()
comboxlist_teacher.grid(row=1, column=1)
Label(frame, text='課程名稱: ').grid(row=1, column=2)
comvalue_name=StringVar()
comboxlist_name=ttk.Combobox(frame, textvariable=comvalue_name)
comboxlist_name['values']=()
comboxlist_name.grid(row=1, column=3)
###info_table####################################################################
columns = ('course_cname', 'course_id', 'faculty', 'division', 'course_credit', 'time', 'location', 'teacher')
treeview = ttk.Treeview(root, height=18, show='headings', columns=columns)
vsb = ttk.Scrollbar(root, orient="vertical", command=treeview.yview)
vsb.pack(side='right', fill='y')
treeview.configure(yscrollcommand=vsb.set)
###scroll_bar####################################################################
table_header = ['課程名稱', '課號', '開課單位', '年級', '學分', '時段', '開課地點', '教師名稱']
for column in columns:
	if column == 'course_cname':
		treeview.column(column, width=190) # course_name need more space
	else:
		treeview.column(column, width=100)
for column, txt in zip(columns, table_header):
	treeview.heading(column, text=txt)
treeview.pack(side=LEFT, fill=BOTH)
# root.mainloop()

