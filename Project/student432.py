from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
from addCourse import inserted_courses
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import webbrowser
from pass_student432 import Pass



class Student432:
    def __init__(self,root,id,name) :
        self.root = root
        self.root.geometry("900x650+100+5")
        self.root.title("منظومة تنزيل المواد")
        self.root.config(background="silver")
        self.root.resizable(False, False)
        self.root.iconbitmap('photo//downloading_download_icon_176859.ico')


        self.id = id
        self.name = name
        # Variables
        self.idvar = StringVar()
        self.namevar = StringVar()
        self.sub1var = StringVar()
        self.sub2var = StringVar()
        self.sub3var = StringVar()
        self.sub4var = StringVar()
        self.sub5var = StringVar()
        self.sub6var = StringVar()
        self.wahdavar = StringVar()
        self.semvar = StringVar()

        self.subvar = StringVar()
        self.sub0var = StringVar()
        
      
        # --------------------Database connection----------------------------
        self.lo = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#User#Root:#123',
            database='studentdb'
        )
        self.cur = self.lo.cursor()
        self.cur.execute("SELECT name FROM students WHERE id = %s LIMIT 1", (self.id,))
        u = self.cur.fetchone()
        self.namevar.set(u[0] if u else "Unknown")
        self.lo.commit()
        self.lo.close()

        self.create_widgets()
  
    def num(self):
        lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb'
            )
       
        cur2=lo.cursor()        
        cur2.execute("select num from students where id= %s LIMIT 1",(self.id,))
        k=cur2.fetchone()
        self.numvar = k[0] 
        lo.commit()
        lo.close()

        return self.numvar
    
    def create_widgets(self):

        self.fr1 = Frame(self.root, bg='#A7D0F1')
        self.fr1.place(x=5, y=5, height=635, width=890)

        lb1 = Label(self.root, text="نظام إدارة التسجيل و الدراسة لجامعة طرابلس - كلية الهندسة ليبيا", font=("monospace", 14), fg="white", bg='#2045f8')
        lb1.pack(fill=X)

        lb2 = Label(self.fr1, text=f"{self.id} : رقم القيد", height=5, width="19")
        lb2.place(x=744, y=30)
        lb3 = Label(self.fr1, text='اسم الطالب : '+self.namevar.get(), height=5, width="27")
        lb3.place(x=545, y=30)
        lb4 = Label(self.fr1, text="القسم : الكهربائيةو الالكترونية", height=5, width="25")
        lb4.place(x=360, y=30)
        lb5 = Label(self.fr1, text="الفصل الدراسي : ربيع 2024", height=5, width="20")
        lb5.place(x=210, y=30)


        self.create_menu()

        self.create_image_frame()

        self.create_photo_frame()

    def create_menu(self):
        fr2 = Frame(self.root, bg='white')
        fr2.place(x=10, y=200, height=435, width=200)

        menu_font = tkFont.Font(family="Arial", size=14)
        label_font = tkFont.Font(family="Arial", size=20)

        self.menu_bar_frame = Frame(fr2, bg='white')
        self.menu_bar_frame.pack(side=TOP, fill=X)

        self.courses_label = Label(self.menu_bar_frame, text="تسجيل المواد", font=label_font, bg='#A7D0F1', cursor="hand2")
        self.courses_label.pack( padx=15, pady=5)
        self.courses_label.bind("<Button-1>", self.show_menu)

        self.courses_menu = Menu(self.root, tearoff=0, font=menu_font)
        courses = ["تنزيل", "عرض المواد"]
        for course in courses:
            self.courses_menu.add_command(label=course, command=lambda c=course: self.select_course(c))

      #================================teaching=========================
        self.teaching_bar_frame = Frame(fr2, bg='white')
        self.teaching_bar_frame.pack(side=TOP, fill=X)

        teaching_label = Label(self.teaching_bar_frame, text="خطة التدريس", font=label_font, bg='#A7D0F1', cursor="hand2")
        teaching_label.pack( padx=15, pady=5)
        teaching_label.bind("<Button-1>", self.show_menu2)

        self.teaching_menu = Menu(self.root, tearoff=0, font=menu_font)
        teaching1 = ["EE432", "EE434", "EE319", "EE302", "EE303", "EE304"]
        for t in teaching1:
            self.teaching_menu.add_command(label=t, command=lambda t1=t: self.teaching(t1))

        #======================schedule========================
        self.sch_bar_frame = Frame(fr2, bg='white')
        self.sch_bar_frame.pack(side=TOP, fill=X)

        self.sch_label = Label(self.sch_bar_frame, text="الجداول", font=label_font, bg='#A7D0F1', cursor="hand2")
        self.sch_label.pack(padx=15, pady=5)
        self.sch_label.bind("<Button-1>", self.show_menu1)

        self.sch_menu = Menu(self.root, tearoff=0, font=menu_font)
        sch = ["الجدول الدراسي", "جدول الامتحانات"]
        for s in sch:
            self.sch_menu.add_command(label=s, command=lambda s1=s: self.schedule(s1))   

        #==========================stream=====================

        self.stream_frame = Frame(fr2, bg='white')
        self.stream_frame.pack(side=TOP, fill=X)

        self.stream_label = Label(self.sch_bar_frame, text="Stream UOT", font=label_font, bg='#A7D0F1', cursor="hand2")
        self.stream_label.pack(padx=15, pady=5)
        self.stream_label.bind("<Button-1>", self.show_menu3)

        self.stream_menu = Menu(self.root, tearoff=0, font=menu_font)
        stream = ["Online Courses"]

        for stream_v in stream:
            self.stream_menu.add_command(label=stream_v, command=lambda s2=stream_v: self.stream(s2))

        #==============================PassWord========================================

        self.pass_frame = Frame(fr2, bg='white')
        self.pass_frame.pack(side=TOP, fill=X)

        self.pass_label = Label(self.sch_bar_frame, text="اعادة تعيين \n  كلمة المرور", font=label_font, bg='#A7D0F1', cursor="hand2")
        self.pass_label.pack(padx=15, pady=5)
        self.pass_label.bind("<Button-1>", self.show_menu4)

        self.pass_menu = Menu(self.root, tearoff=0, font=menu_font)
        pass1 = ["تعيين"]

        for p in pass1:
            self.pass_menu.add_command(label=p, command=lambda p1=p:self.pass_student(p1) )   

        self.out_frame = Frame(fr2, bg='white')
        self.out_frame.pack(side=TOP, fill=X)  

        self.out_label = Label(self.sch_bar_frame, text="تسجيل الخروج", font=label_font, bg='#A7D0F1', cursor="hand2")
        self.out_label.pack(padx=15, pady=5)
        self.out_label.bind("<Button-1>", self.show_menu5)  
           

    def pass_student (self,p):
        change= Pass(self.id)

    def create_image_frame(self):
        self.fr3 = Frame(self.fr1, bg='red')
        self.fr3.place(x=210, y=120, width=671, height=490)

        pic = Image.open("photo//calendar.png")#================calendar pic================
        res = pic.resize((671, 486))
        pic1 = ImageTk.PhotoImage(res)
        self.lab2 = Label(self.fr3, image=pic1)
        self.lab2.pack()
        self.lab2.image = pic1

    def create_photo_frame(self):
        fr4 = Frame(self.fr1, bg='red')
        fr4.place(x=5, y=30, width=200, height=160)

        pic = Image.open("photo//uotlogo.png ")#==============uotlogo pic=======================
        res = pic.resize((200, 160))
        pic1 = ImageTk.PhotoImage(res)
        lab3 = Label(fr4, image=pic1)
        lab3.pack()
        lab3.image = pic1

    def sem(self):
        lo = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#User#Root:#123',
            database='studentdb'
        )
        cur = lo.cursor()
        c = 'SELECT coursescol FROM courses WHERE id = %s LIMIT 1'
        cur.execute(c, (self.id,))
        u = cur.fetchone()
        out = u[0] if u else "Unknown"
        lo.commit()
        lo.close()

        return out
    
    def wehda(self):
        lo = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#User#Root:#123',
            database='studentdb'
        )
        cur = lo.cursor()
        c = 'SELECT score FROM courses WHERE id = %s LIMIT 1'
        cur.execute(c, (self.id,))
        u = cur.fetchone()
        out = u[0] if u else "Unknown"
        lo.commit()
        lo.close()

        return out    
    
    def persent(self):
        lo = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#User#Root:#123',
            database='studentdb'
        )
        cur = lo.cursor()
        c = 'SELECT pecent FROM courses WHERE id = %s LIMIT 1'
        cur.execute(c, (self.id,))
        u = cur.fetchone()
        out = u[0] if u else "Unknown"
        lo.commit()
        lo.close()
        return out

    def show(self):
    
        # ===============================Create and place main frame=====================
        self.f3 = Frame(self.fr1, bg='#2045f8')
        self.f3.place(x=210, y=120, width=671, height=490)

        #======================== Create and place sub-frame========================
        self.fr = Frame(self.f3, bg='#2045f8')
        self.fr.place(x=2, y=80, width=666, height=248)

        rows = 7  
        columns = 6 


        first_row_height = 50  # Height of the first row
        remaining_height = 248 - first_row_height  # Remaining height for other rows
        other_row_height = remaining_height // (rows - 1)  # Height of each of the other rows
        cell_width = 666 // columns  # Width of each cell

        # First row labels (column headers)
        headers = ["المواد", "الحضور", "درجة اعمال السنة", "درجة النهائي", "الدرجة الكلية", "التقدير"]

        for col, header in enumerate(headers):
            label = Label(self.fr, text=header, bg="white", borderwidth=1, relief="solid", width=cell_width // 10)
            # Place headers starting from the right (i.e., last column first)
            label.place(x=(columns - 1 - col) * cell_width, y=0, width=cell_width, height=first_row_height)

        # ======================================Fetch data from the MySQL database==================================
        try:
            lo = mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb'
            )
            cur = lo.cursor()
    
            query = "SELECT sub, attend, midterm, final, total, evaluation FROM score_table WHERE id = %s"
            cur.execute(query, (self.id,))  
            rows_data = cur.fetchall()  

            for row_index, row_data in enumerate(rows_data):
                if row_index >= rows - 1:
                    break  
                for col_index, value in enumerate(row_data):
                    lb = Label(self.fr, text=value, bg="white", borderwidth=1, relief="solid", width=cell_width // 10)
                    # Place data starting from the right (i.e., last column first)
                    lb.place(x=(columns - 1 - col_index) * cell_width,
                             y=first_row_height + row_index * other_row_height,
                             width=cell_width, height=other_row_height)

            lo.close()

        except mysql.connector.Error as err:
            messagebox.showerror('Error', f"Database error: {err}")


        f3 = Frame(self.f3, bg='#A7D0F1')
        f3.place(x=40, y=360, width=150, height=100)
        Label(f3, text=f" : عدد الوحدات  \n \n {self.wehda()}", bg='white', font='30').pack(padx=5, pady=20)

   
        f4 = Frame(self.f3, bg='#A7D0F1')
        f4.place(x=220, y=360, width=120, height=100)
        v = self.sem()  
        Label(f4, text=f" : المعدل العام  \n \n {self.persent()}%", bg='white', font='30').pack(padx=5, pady=20)

    def select_course(self, c):
        if c == "تنزيل":
           self.add()
        elif c == 'عرض المواد': 
            self.show()  

    def teaching(self, t1):
        if t1 =="EE432":
            webbrowser.open("https://drive.google.com/file/d/1ySTKTmWojlOoavObz_iPj5EWWgPTCOKS/view?usp=drive_link")

        elif t1 == "EE434":
            webbrowser.open('https://drive.google.com/file/d/1BRlv0gYP5P59Ree190Q84PI666r5RAzr/view?usp=sharing')

        elif t1== "EE319":
            webbrowser.open('https://drive.google.com/file/d/1O0iFQyDjZxBSj7zBntPrYoiCx2HGRjKm/view?usp=sharing')
        elif t1== "EE302": 
            webbrowser.open('https://drive.google.com/file/d/12eNeDwvginVrqbG8RS39IQbj5dJTby46/view?usp=sharing')

        if t1== "EE303":
            webbrowser.open('https://drive.google.com/file/d/1iv6ci6UgZChB33WRbLtkQf3QAkZJtMas/view?usp=sharing')
        if t1== "EE304":
            webbrowser.open('https://drive.google.com/file/d/1WDbhAt17N1yrBmeeRpV69o9h1EHnFeUE/view?usp=sharing')
                             
    def stream(self, s):
            webbrowser.open("https://www.youtube.com/@eee_uot/playlists")
        
    def schedule(self, s):
        if s == "الجدول الدراسي":
            self.fr3.destroy()
            self.fr3 = Frame(self.fr1, bg='red')
            self.fr3.place(x=210, y=120, width=671, height=490)

            pic = Image.open("photo//schedule.jpg")#================schedule pic ====================
            res = pic.resize((671, 486))
            pic1 = ImageTk.PhotoImage(res)
            self.lab2 = Label(self.fr3, image=pic1)
            self.lab2.pack()
            self.lab2.image = pic1            

        if s == "جدول الامتحانات":
            self.fr3.destroy()
            self.fr3 = Frame(self.fr1, bg='red')
            self.fr3.place(x=210, y=120, width=671, height=490)

            pic = Image.open("photo//final.jpg")#=============================final pic=======================
            res = pic.resize((671, 486))
            pic1 = ImageTk.PhotoImage(res)
            self.lab2 = Label(self.fr3, image=pic1)
            self.lab2.pack()
            self.lab2.image = pic1

    def show_menu(self, event):
        self.courses_menu.post(event.x_root, event.y_root)

    def show_menu1(self, event):
        self.sch_menu.post(event.x_root, event.y_root)

    def show_menu2(self, event):
        self.teaching_menu.post(event.x_root, event.y_root)

    def show_menu3(self, event):
        self.stream_menu.post(event.x_root, event.y_root)

    def show_menu4(self, event):
        self.pass_menu.post(event.x_root, event.y_root) 

    def show_menu5(self, event):

        self.root.quit()               

    def wahadat(self):
      try:
        sum = 0
        all = []
        hash = {}
        for i in range(55):
            hash[inserted_courses[i][0]]=inserted_courses[i][1]

        id = self.idvar.get()
        k=0
        lo = mysql.connector.connect(
        host='localhost',
        user='root',
        password='#User#Root:#123',
        database='studentdb'
        )
    
        cur = lo.cursor()
        do0=lo.cursor()
        add=lo.cursor()
        num=lo.cursor()
        sub=lo.cursor()
        do1=lo.cursor()
        do2=lo.cursor()

        num.execute('select num from students where id=%s limit 1',(id,))
        h = num.fetchone()

    #--------------------Student Subject------------------------
        for i in range(1,7):
            sub = f'subject{i}'
            query = f"SELECT {sub} FROM courses WHERE id = %s LIMIT 1"
            cur.execute(query, (id,))
            u = cur.fetchone()
            all.append(u[0])
        
        lolo = str(h[0])    #======================add in course===============next  
        
        while k < 6 :
            if all[k] in hash.keys() and all[k] != 'None':
                sum+=hash[all[k]]
            else:
                break   
            k+=1
            
        if sum <= 18:
            do0.execute('update courses set score=%s where id='+ self.idvar.get(),(sum,))

        do1.execute('delete from score_table where num=%s', (str(lolo),))

        for i in range(6):
           if all[i] != 'None' :  
             c=f'update  subject_table set {all[i]} = %s  where num = '
             add.execute(c + lolo , ([self.idvar.get()]))
              
             t='insert into score_table (num , sub , id , name ) values (%s,%s,%s,%s) '
             do2.execute(t, (lolo , all[i],self.idvar.get(),self.namevar.get()))  

        lo.commit()
        self.comeback_sub()        
        lo.close()
  
      except:
            messagebox.askretrycancel('Error','الرجاء التأكد من القيم المدخلة و اعادة المحاولة !')   
    def add(self):
     self.fr3.destroy()
     self.fr3 = Frame(self.fr1, bg='#2045f8')
     self.fr3.place(x=210, y=120, width=671, height=490)

     f1 = Frame(self.fr3, bg='#A7D0F1')
     f1.place(x=40, y=50, width=580, height=300)

    # استرجاع المواد التي اختارها الطالب من قاعدة البيانات
     lo = mysql.connector.connect(
        host='localhost',
        user='root',
        password='#User#Root:#123',
        database='studentdb'
    )
     cur = lo.cursor()

    # استرجاع المواد المختارة مسبقًا من قاعدة البيانات
     cur.execute('SELECT subject1, subject2, subject3, subject4, subject5, subject6 FROM courses WHERE ID = %s', (self.id,))
     row = cur.fetchone()
    
     if row:
        # إذا كانت المواد موجودة بالفعل، نقوم بتخزينها
        sb = row
     else:
        # إذا لم تكن هناك مواد مختارة سابقًا، نملأها بالقيم الافتراضية
        sb = ['None', 'None', 'None', 'None', 'None', 'None']

    # إغلاق الاتصال بقاعدة البيانات بعد استرجاع البيانات
     lo.close()

     all_courses = [course[0] for course in inserted_courses[:55]]  # الحصول على المواد من القائمة

     labels = ["المادة 1", "المادة 2", "المادة 3", "المادة 4", "المادة 5", "المادة 6" ]
     positions = [490, 393, 297, 197, 100, 7]

    # عرض تسميات المواد
     for label_text, x in zip(labels, positions):
        Label(f1, text=label_text, bg='white', width=11, height=2, font=('arial','9','bold')).place(x=x, y=30)

     sub1 = ttk.Combobox(f1, textvariable=self.sub1var, width=10, height=10)
     sub1['values'] = tuple(all_courses)  
     if sb[0] != 'None' and sb[0] in all_courses:
          sub1.set(sb[0]) 
     else:
            sub1.set('')  
     sub1.place(x=490, y=90)


     label_sub1 = Label(f1, text=sb[0] if sb[0] != 'None' else "لم يتم اختيار مادة", bg='white', width=11, height=2)
     label_sub1.place(x=490, y=120)

     sub2 = ttk.Combobox(f1, textvariable=self.sub2var, width=10, height=10)
     sub2['values'] = tuple(all_courses)  # تحديد المواد المتاحة     
     if sb[1] != 'None' and sb[1] in all_courses:
            sub2.set(sb[1]) 
     else:
            sub2.set('')
     sub2.place(x=393, y=90)

     label_sub2 = Label(f1, text=sb[1] if sb[1] != 'None' else "لم يتم اختيار مادة", bg='white', width=11, height=2)
     label_sub2.place(x=393, y=120)

     sub3 = ttk.Combobox(f1, textvariable=self.sub3var, width=10, height=10)
     sub3['values'] = tuple(all_courses)  # تحديد المواد المتاحة     
     if sb[2] != 'None' and sb[2] in all_courses:
            sub3.set(sb[2]) 
     else:
            sub3.set('')
     sub3.place(x=297, y=90)

     label_sub3 = Label(f1, text=sb[2] if sb[2] != 'None' else "لم يتم اختيار مادة", bg='white', width=11, height=2)
     label_sub3.place(x=297, y=120)

     sub4 = ttk.Combobox(f1, textvariable=self.sub4var, width=10, height=10)
     sub4['values'] = tuple(all_courses)  # تحديد المواد المتاحة
     if sb[3] != 'None' and sb[3] in all_courses:
              sub4.set(sb[3]) 
     else:
            sub4.set('')  
     sub4.place(x=197, y=90)

     label_sub4 = Label(f1, text=sb[3] if sb[3] != 'None' else "لم يتم اختيار مادة", bg='white', width=11, height=2)
     label_sub4.place(x=197, y=120)

     sub5 = ttk.Combobox(f1, textvariable=self.sub5var, width=10, height=10)
     sub5['values'] = tuple(all_courses)  # تحديد المواد المتاحة     
     if sb[4] != 'None' and sb[4] in all_courses:
              sub5.set(sb[4]) 
     else:
            sub5.set('')  
     sub5.place(x=100, y=90)

     label_sub5 = Label(f1, text=sb[4] if sb[4] != 'None' else "لم يتم اختيار مادة", bg='white', width=11, height=2)
     label_sub5.place(x=100, y=120)

     sub6 = ttk.Combobox(f1, textvariable=self.sub6var, width=10, height=10)
     sub6['values'] = tuple(all_courses)  # تحديد المواد المتاحة     
     if sb[5] != 'None' and sb[5] in all_courses:
            sub6.set(sb[5]) 
     else:
            sub6.set('')  
     sub6.place(x=7, y=90)

     label_sub6 = Label(f1, text=sb[5] if sb[5] != 'None' else "لم يتم اختيار مادة", bg='white', width=11, height=2)
     label_sub6.place(x=7, y=120)

    # إضافة الأزرار
     f2 = Frame(self.fr3, bg='#A7D0F1')
     f2.place(x=230, y=370, width=392, height=100)
     Button(f2, text="اضافة", bg='yellow', width=23, height=2, command=self.courses).place(x=204, y=30)
     Button(f2, text="حذف", bg='red', width=23, height=2, command=self.delete_courses).place(x=24, y=30)

    # عرض بيانات الفصل الدراسي
     f3 = Frame(self.fr3, bg='#A7D0F1')
     f3.place(x=40, y=370, width=100, height=100)
     c = self.sem() 
     Label(f3, text=f" :الفصل الدراسي \n \n{c}", bg='white', font='30').pack(padx=5, pady=20)

    # عرض بيانات المعدل العام
     f4 = Frame(self.fr3, bg='#A7D0F1')
     f4.place(x=145, y=370, width=80, height=100)
     v = self.persent()
     Label(f4, text=f" :المعدل العام  \n \n %{v}", bg='white', font='30').pack(padx=5, pady=20)

    def courses(self):  
            sb=[self.sub1var.get(),self.sub2var.get(),self.sub3var.get(),self.sub4var.get(),self.sub5var.get(),self.sub6var.get()]
            
            num1 = self.num()
        
            if len(sb)!=len(set(sb)):
                messagebox.askretrycancel('Error','مواد متكررة') 

            new = sorted(sb)
            check = False
            for i in range(6):
               for j in range(55):
                 if new[i] == inserted_courses[j][0] :
                     for i in range(6):
                          if new[i] in inserted_courses[3] and new[i] != inserted_courses[3]: 
                             check = True
                          else: 
                             continue   
            print(check)
            
            if check == False:
                lo=mysql.connector.connect(
                host='localhost',
                user='root',
                password='#User#Root:#123',
                database='studentdb')
                cur=lo.cursor()
                cur1=lo.cursor()
                cur2=lo.cursor()
                cur3=lo.cursor()


                for i in range(6):
                 if sb[i] :
                    j=i+1
                    r=f"UPDATE courses SET subject{j} = %s WHERE ID = %s"
                    cur.execute(r,(sb[i],int(self.id),))


                    #delete_score_query = "DELETE FROM score_table WHERE sub = %s AND id = %s"
                    #cur3.execute(delete_score_query, (sb[i], self.id))


                cur1.execute('delete from score_table where num=%s', (str(num1),))
                for i in range(6):
                   if sb[i] != 'None' :  
                      c=f'update  subject_table set {sb[i]} = %s  where num = '
                      cur.execute(c + str(num1) , (self.id,))

                      t='insert into score_table (num , sub , id , name ) values (%s,%s,%s,%s)'
                      cur2.execute(t ,(str(num1) , sb[i] , self.id , self.namevar.get()))   
                lo.commit()
                lo.close()
                if len(sb)==len(set(sb)):
                   
                   messagebox.askokcancel('Error','تم تنزيل المواد بنجاح!')                        
                
            else:
                messagebox.showerror('Error','الرجاء اعادة المحاولة و تتبع شجرة المواد !')   
 

    def delete_courses(self):
    # الحصول على المواد المختارة من القوائم
     sb = [self.sub1var.get(), self.sub2var.get(), self.sub3var.get(), self.sub4var.get(), self.sub5var.get(), self.sub6var.get()]
    
    # التحقق من وجود مادة مختارة للحذف
     selected_subject = None
     for subject in sb:
        if subject and subject != 'None':  # نبحث عن مادة مختارة ليست None
            selected_subject = subject
            break  # إذا وجدنا مادة، نوقف البحث

     if not selected_subject:  # إذا لم يتم العثور على مادة للاختيار
        messagebox.showerror('Error', 'لم يتم اختيار مادة للحذف!')
        return

    # الاتصال بقاعدة البيانات
     try:
        lo = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#User#Root:#123',
            database='studentdb'
        )
        cur = lo.cursor()

        # تحديث بيانات المواد في جدول "courses"
        delete_subject_query = """
            UPDATE courses 
            SET
                subject1 = IF(subject1 = %s, NULL, subject1),
                subject2 = IF(subject2 = %s, NULL, subject2),
                subject3 = IF(subject3 = %s, NULL, subject3),
                subject4 = IF(subject4 = %s, NULL, subject4),
                subject5 = IF(subject5 = %s, NULL, subject5),
                subject6 = IF(subject6 = %s, NULL, subject6)
            WHERE id = %s
        """
        cur.execute(delete_subject_query, (selected_subject, selected_subject, selected_subject, selected_subject, selected_subject, selected_subject, self.id))
        
        try:            
           delete_score_query = "DELETE FROM score_table WHERE sub = %s AND id = %s"
           cur.execute(delete_score_query, (selected_subject, self.id))
        except:
            messagebox.askretrycancel('Success', f"المادة: {selected_subject} غير موجودة ضمن المواد المنزلة!")           
        # حفظ التغييرات
        lo.commit()
        lo.close()

        messagebox.showinfo('Success', f'تم حذف المادة: {selected_subject} بنجاح!')
    
     except mysql.connector.Error as err:
        messagebox.showerror('Error', f"حدث خطأ أثناء الحذف: {err}")
