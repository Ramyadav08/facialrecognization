from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

root = Tk()
root.title("STUDENT MANAGEMENT SYSTEM")
root.geometry("1508x790+0+0")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<functions>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def add_data():
    if dptvar.get()=="select department" or envar.get()=="" or namevar.get()=="" or emvar.get()=="":
        messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED!",parent=root)
    else:
        try:
            mydb = mysql.connector.connect(host="localhost",port='3306',user="root",password="ram81718",database="facial")
            mycursor = mydb.cursor()
            mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dptvar.get(),
            semvar.get(),yrvar.get(),crsvar.get(),envar.get(),namevar.get(),emvar.get(),contvar.get(),
                                                    addvar.get(),gnvar.get(),rd1var.get(), ))
            mydb.commit()
            fetch_data()
            mydb.close()
            messagebox.showinfo("Successful","data are added successfully!",parent=root)
        except Exception as es:
            messagebox.showerror("error",f"Due to:{str(es)}",parent=root)

#<<<<<<<<<<<<<<<<<<<<<<<<<fatch data>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def fetch_data():
    mydb = mysql.connector.connect(host="localhost", port='3306', user="root", password="ram81718", database="facial")
    mycursor = mydb.cursor()
    mycursor.execute("select * from student")
    rows = mycursor.fetchall()
    if len(rows) != 0:
        root.details.delete(*root.details.get_children())
        for row in rows:
            root.details.insert("", END, values=row)
        mydb.commit()
    mydb.close()
#<<<<<<<<<<<<<<<<get cursor>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
def get_cur(event=""):
    cur_focus=root.details.focus()
    content=root.details.item(cur_focus)
    data=content["values"]
    dptvar.set(data[0])
    semvar.set(data[1])
    yrvar.set(data[2])
    crsvar.set(data[3])
    envar.set(data[4])
    namevar.set(data[5])
    emvar.set(data[6])
    contvar.set(data[7])
    addvar.set(data[8])
    gnvar.set(data[9])
    rd1var.set(data[10])
#<<<<<<<<<<<<<<<<<<<<<<<<<<<,deletefunction>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def delete_data():
    if envar.get()=="":
        messagebox.showerror("error","id must be required!",parent=root)
    else:
        try:
            delete=messagebox.askyesno("delete page","do you want to delete this information!",parent=root)
            if delete > 0:
                mydb = mysql.connector.connect(host="localhost", port='3306', user="root", password="ram81718",database="facial")
                mycursor = mydb.cursor()
                sql="delete from student where enroll=%s"
                val=(envar.get(),)
                mycursor.execute(sql,val)
            else:
                if not delete:
                    return
            mydb.commit()
            fetch_data()
            reset_data()
            mydb.close()
            messagebox.showerror("successfull", "delete successfully!", parent=root)
        except Exception as es:
            messagebox.showerror("error", f"Due to:{str(es)}", parent=root)

#<<<<<<<<<<<<<<<<<<<<<<<<<<update function>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def update_data():
    if dptvar.get()=="select department" or envar.get()=="" or namevar.get()=="" or emvar.get()=="":
        messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED!",parent=root)
    else:
        try:
            update_dt=messagebox.askyesno("update","Do you want to update this information!",parent=root)
            if update_dt>0:
                mydb = mysql.connector.connect(host="localhost", port='3306', user="root", password="ram81718",database="facial")
                mycursor = mydb.cursor()
                mycursor.execute("update student set depatment=%s,sem=%s,year=%s,course=%s,enroll=%s,Name=%s,email=%s,contact=%s,address=%s,gender=%s,photosample=%s where enroll=%s",
                                 (dptvar.get(),semvar.get(),yrvar.get(),crsvar.get(),namevar.get(),emvar.get(),
                                  contvar.get(),addvar.get(),gnvar.get(),rd1var.get(),envar.get()))
            else:
                if not update_dt:
                    return
            mydb.commit()
            fetch_data()
            mydb.close()
            messagebox.showerror("successfull","updated successfully!",parent=root)


        except Exception as es:
            messagebox.showerror("error", f"Due to:{str(es)}", parent=root)

#.................................reset............
def reset_data():
    dpt_cmbo.set("")
    year_cmbo.set("")
    course_cmbo.set("")
    sem_cmbo.set("")
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    email_entry.delete(0,END)
    contact_entry.delete(0,END)
    address_entry.delete(0,END)
    combo_gender.set("")
    rd1var.set("")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<sample>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''def sample():
    if dptvar.get()=="select department" or envar.get()=="" or namevar.get()=="" or emvar.get()=="":
        messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED!",parent=root)
    else:

        try:

            mydb = mysql.connector.connect(host="localhost", port='3306', user="root", password="ram81718",database="facial")
            mycursor = mydb.cursor()
            mycursor.execute("select * from student")
            my_result=mycursor.fetchall()
            id=0
            for x in my_result:

                id+=1
                mycursor.execute(
                    "update student set depatment=%s,sem=%s,year=%s,course=%s,enroll=%s,Name=%s,email=%s,contact=%s,address=%s,gender=%s,photosample=%s where enroll=%s",
                    (dptvar.get(), semvar.get(), yrvar.get(), crsvar.get(), namevar.get(), emvar.get(), contvar.get(),
                     addvar.get(), gnvar.get(), rd1var.get(), envar.get()==id+1))
                mydb.commit()
                fetch_data()
                reset_data()
                mydb.close()
                # <<<<<<<<<<<<<<<<<<<<<face loading>>>>>>>>>>>>>>>>>..
                face_classified=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classified.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id +=1
                    face=cv2.resize(face_cropped(my_frame),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+""+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path)
                    cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow('cropped face',face)
                    if cv2.waitKey(1)==13 or int(img_id)==10:
                        break
                    cap.release
                    cv2.destroyAllWindows()
                    messagebox.showinfo("result","Generating data!!!!!!")'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>variable<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
dptvar=StringVar()
yrvar=StringVar()
semvar=StringVar()
crsvar=StringVar()
envar=StringVar()
namevar=StringVar()
emvar=StringVar()
contvar=StringVar()
addvar=StringVar()
gnvar=StringVar()
rd1var=StringVar()
rd2var=StringVar()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

img = Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\s1.jpg")
img = img.resize((490, 130), Image.ANTIALIAS)
root.photoimg = ImageTk.PhotoImage(img)
f_lbl = Label(root, image=root.photoimg).place(x=0, y=0, width=500, height=130)
# ****************************************************************************
img1 = Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\fc.jpg")
img1 = img1.resize((500, 130), Image.ANTIALIAS)
root.photoimg1 = ImageTk.PhotoImage(img1)
f1_lbl = Label(root, image=root.photoimg1).place(x=491, y=0, width=500, height=130)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
img2 = Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\s2.jpg")
img2 = img2.resize((500, 130), Image.ANTIALIAS)
root.photoimg2 = ImageTk.PhotoImage(img2)
f2_lbl = Label(root, image=root.photoimg2).place(x=983, y=0, width=500, height=130)
# background photo
bg_img = Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\SM1.jpg")
bg_img = bg_img.resize((1500, 790), Image.ANTIALIAS)
root.photobg = ImageTk.PhotoImage(bg_img)
bg_lbl = Label(root, image=root.photobg).place(x=0, y=130, width=1500, height=790)
# title label
title_lbl = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                  bg="#222A35", fg="red")
title_lbl.place(x=0, y=130,width=1500,height=45)
#main frame<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
main_frame=Frame(bg_lbl,bd=2)
main_frame.place(x=10,y=180,width=1335,height=500)
#left lable
left_lbl=LabelFrame(main_frame,bd=4,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",20,"bold"))
left_lbl.place(x=15,y=5,width=650,height=490)

img_left = Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\s2.jpg")
img_left = img_left.resize((650, 50), Image.ANTIALIAS)
root.photoimg_left = ImageTk.PhotoImage(img_left)
f_left = Label(left_lbl, image=root.photoimg_left).place(x=0, y=0, width=650, height=50)

left_lbl1=LabelFrame(left_lbl,bd=4,relief=RIDGE,text="current course",font=("times new roman",20,"bold"),bg="#222A35",fg="white")
left_lbl1.place(x=5,y=55,width=630,height=110)
dpt=Label(left_lbl1,text="DEPARTMENT",font=("arial",13,"bold"),bg="#222a35",fg="white")
dpt.grid(row=0,column=0)
dpt_cmbo=ttk.Combobox(left_lbl1,textvariable=dptvar,font=("arial",12,"bold"),state="readonly")
dpt_cmbo["values"]=("select department","CE","IT","CIVIL","EE","ME","MEDICAL","MANAGEMENT","SOS")
dpt_cmbo.current(0)
dpt_cmbo.grid(row=0,column=1,padx=2,pady=2)
#year
year=Label(left_lbl1,text="YEAR",font=("arial",13,"bold"),bg="#222A35",fg="white")
year.grid(row=1,column=0)
year_cmbo=ttk.Combobox(left_lbl1,textvariable=yrvar,font=("arial",12,"bold"),state="readonly")
year_cmbo["values"]=("select year","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025")
year_cmbo.current(0)
year_cmbo.grid(row=1,column=1,padx=2,pady=5)
#sem<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
sem=Label(left_lbl1,text="SEMESTER",font=("arial",13,"bold"),bg="#222A35",fg="white")
sem.grid(row=0,column=3)
sem_cmbo=ttk.Combobox(left_lbl1,textvariable=semvar,font=("arial",12,"bold"),state="readonly")
sem_cmbo["values"]=("select semeter","1","2","3","4","5","6","7","8")
sem_cmbo.current(0)
sem_cmbo.grid(row=0,column=4,padx=2,pady=2)
#courses9999999999999999999999999999999999999999999999999999999999999
course=Label(left_lbl1,text="COURSES",font=("arial",13,"bold"),bg="#222A35",fg="white")
course.grid(row=1,column=3)
course_cmbo=ttk.Combobox(left_lbl1,textvariable=crsvar,font=("arial",12,"bold"),state="readonly")
course_cmbo["values"]=("select COURSE","BCA","COMPUTER","IT","B.PHARMA","AYURBEDIC","BBA","MBA","SCIENCE","CIVIL","ME")
course_cmbo.current(0)
course_cmbo.grid(row=1,column=4,padx=2,pady=2)
#student details<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
left_lbl2=LabelFrame(left_lbl,bd=4,relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",20,"bold"),bg="#269B61",fg="white")
left_lbl2.place(x=5,y=170,width=630,height=280)
id=Label(left_lbl2,text="ENROLL",font=("arial",13,"bold"),bg="black",fg="white")
id.grid(row=0,column=0)
id_entry=ttk.Entry(left_lbl2,textvariable=envar,width=20,font=("arial",13,"bold"))
id_entry.grid(row=0,column=1,padx=2,pady=5)
#name
name=Label(left_lbl2,text="NAME",font=("arial",13,"bold"),bg="black",fg="white")
name.grid(row=1,column=0)
name_entry=ttk.Entry(left_lbl2,textvariable=namevar,width=20,font=("arial",13,"bold"))
name_entry.grid(row=1,column=1,padx=2,pady=5)

email=Label(left_lbl2,text="EMAIL",font=("arial",13,"bold"),bg="black",fg="white")
email.grid(row=2,column=0,)
email_entry=ttk.Entry(left_lbl2,textvariable=emvar,width=20,font=("arial",13,"bold"))
email_entry.grid(row=2,column=1,padx=2,pady=5)

contact=Label(left_lbl2,text="CONTACT",font=("arial",13,"bold"),bg="black",fg="white")
contact.grid(row=0,column=2,padx=10,pady=5,sticky=W)
contact_entry=ttk.Entry(left_lbl2,textvariable=contvar,width=20,font=("arial",13,"bold"))
contact_entry.grid(row=0,column=3,padx=0,pady=5)

address=Label(left_lbl2,text="ADDRESS",font=("arial",13,"bold"),bg="black",fg="white")
address.grid(row=1,column=2,padx=10,pady=5,sticky=W)
address_entry=ttk.Entry(left_lbl2,textvariable=addvar,width=20,font=("arial",13,"bold"))
address_entry.grid(row=1,column=3,padx=0,pady=5)

gender=Label(left_lbl2,text="Gender",font=("times new roman",13,"bold"),bg="black",fg="white")
gender.grid(row=2,column=2,padx=20,pady=10,sticky="w")
combo_gender=ttk.Combobox(left_lbl2,textvariable=gnvar,font=("atimes new roman",13,"bold"),state="readonly")
combo_gender["values"]=("Male","Female","Others")
combo_gender.grid(row=2,column=3,padx=0,pady=5)
#radio button<<<<<<<<<<<<<<<<<<<<
radio1=ttk.Radiobutton(left_lbl2,variable=rd1var,text="TAKE PHOTO SAMPLE",value="Yes")
radio1.grid(row=3,column=1)

radio2=ttk.Radiobutton(left_lbl2,variable=rd1var,text="NO PHOTO SAMPLE",value="No")
radio2.grid(row=3,column=2)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BUTTON FRAME<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
btn_frame=Frame(left_lbl2,bd=4,relief=RIDGE,bg="#222A35")
btn_frame.place(x=5,y=140,width=615,height=50)

save=Button(btn_frame,text="SAVE",command=add_data,font=("arial",13,"bold"),bg="green",fg="white",width=13,activebackground="green")
save.grid(row=0,column=0,padx=10,pady=5)

update=Button(btn_frame,command=update_data,text="UPDATE",font=("arial",13,"bold"),bg="green",fg="white",width=13,activebackground="green")
update.grid(row=0,column=1,padx=10,pady=5)

delete=Button(btn_frame,command=delete_data,text="DELETE",font=("arial",13,"bold"),bg="green",fg="white",width=13,activebackground="green")
delete.grid(row=0,column=2,padx=10,pady=5)

reset=Button(btn_frame,command=reset_data,text="RESET",font=("arial",13,"bold"),bg="green",fg="white",width=10,activebackground="green")
reset.grid(row=0,column=3,padx=5,pady=5)


#BTNFRAME
btn_frame1=Frame(left_lbl2,bd=4,relief=RIDGE,bg="#222A35")
btn_frame1.place(x=5,y=192,width=615,height=50)

photosample=Button(btn_frame1,text="TAKE PHOTO",font=("arial",13,"bold"),bg="green",fg="white",width=27,activebackground="green")
photosample.grid(row=0,column=0,padx=10,pady=5)

updatesample=Button(btn_frame1,text="UPDATE PHOTO",font=("arial",13,"bold"),bg="green",fg="white",width=27,activebackground="green")
updatesample.grid(row=0,column=1,padx=10,pady=5)

#right lable<<<<<<<<<<<<<<<<<<<<<<<
right_lbl=LabelFrame(main_frame,bd=4,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",20,"bold"))
right_lbl.place(x=670,y=5,width=650,height=490)
#search frame<<<<<<<<<<<<<<<<
search_frame=Frame(right_lbl,bd=4,relief=RIDGE,bg="#222a35")
search_frame.place(x=5,y=5,width=625,height=55)

search_lbl=Label(search_frame,text="SEARCH BY:",font=("arial",13,"bold"),bg="#222a35",fg="white")
search_lbl.grid(row=0,column=0,padx=5,pady=13)
search_cmbo=ttk.Combobox(search_frame,font=("arial",12,"bold"),state="readonly",width=10)
search_cmbo["values"]=("select ","ENROLL","NAME","CONTACT")
search_cmbo.current(0)
search_cmbo.grid(row=0,column=1,padx=2,pady=2)

search_entry=ttk.Entry(search_frame,width=13,font=("arial",13,"bold"))
search_entry.grid(row=0,column=2,padx=2,pady=2)

search_btn=Button(search_frame,text="SEARCH",font=("arial",13,"bold"),bg="green",fg="white",width=10,activebackground="green")
search_btn.grid(row=0,column=3,padx=7,pady=5)

showall=Button(search_frame,text="SHOW ALL",font=("arial",13,"bold"),bg="green",fg="white",width=10,activebackground="green")
showall.grid(row=0,column=4,padx=5,pady=5)

deatils_frame=Frame(right_lbl,bd=4,relief=RIDGE,bg="gray")
deatils_frame.place(x=5,y=60,width=625,height=390)
scroll_x=ttk.Scrollbar(deatils_frame,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(deatils_frame,orient=VERTICAL)
root.details=ttk.Treeview(deatils_frame,column=("DPT","SEM","YEAR","COURSE","ENROLL","NAME","EMAIL","CONTACT",
                "ADDRESS","GENDER","PHOTO"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=root.details.xview)
scroll_y.config(command=root.details.yview)

root.details.heading("DPT",text="DEPARTMENT")
root.details.heading("SEM",text="SEM")
root.details.heading("YEAR",text="YEAR")
root.details.heading("COURSE",text="COURSE")
root.details.heading("ENROLL",text="ENROLL")
root.details.heading("NAME",text="NAME")
root.details.heading("EMAIL",text="EMAIL")
root.details.heading("CONTACT",text="CONTACT")
root.details.heading("ADDRESS",text="ADDRESS")
root.details.heading("GENDER",text="GENDER")
root.details.heading("PHOTO",text="PHOTO")
root.details["show"]="headings"

root.details.column("DPT",width=100)
root.details.column("SEM",width=50)
root.details.column("YEAR",width=100)
root.details.column("COURSE",width=50)
root.details.column("ENROLL",width=100)
root.details.column("NAME",width=150)
root.details.column("EMAIL",width=150)
root.details.column("CONTACT",width=100)
root.details.column("ADDRESS",width=150)
root.details.column("GENDER",width=60)
root.details.column("PHOTO",width=60)
root.details.pack(fill=BOTH,expand=1)
root.details.bind("<ButtonRelease>",get_cur)
fetch_data()

root.mainloop()