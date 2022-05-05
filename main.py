from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import student

def stu_details():
    new_win=Toplevel(root)
    st=student(new_win)





root = Tk()
root.title("FACIAL RECOGNIZATION AND ATTENDACE SYSTEM")
root.geometry("1508x790+0+0")
img = Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\standford.jpg")
img = img.resize((490, 130), Image.ANTIALIAS)
root.photoimg = ImageTk.PhotoImage(img)
f_lbl = Label(root, image=root.photoimg).place(x=0, y=0, width=500, height=130)
# ****************************************************************************
img1 = Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\fc.jpg")
img1 = img1.resize((500, 130), Image.ANTIALIAS)
root.photoimg1 = ImageTk.PhotoImage(img1)
f1_lbl = Label(root, image=root.photoimg1).place(x=491, y=0, width=500, height=130)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
img2 = Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\rk.png")
img2 = img2.resize((500, 130), Image.ANTIALIAS)
root.photoimg2 = ImageTk.PhotoImage(img2)
f2_lbl = Label(root, image=root.photoimg2).place(x=983, y=0, width=500, height=130)
# background photo
bg_img = Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\moon.jpg")
bg_img = bg_img.resize((1500, 790), Image.ANTIALIAS)
root.photobg = ImageTk.PhotoImage(bg_img)
bg_lbl = Label(root, image=root.photobg).place(x=0, y=130, width=1500, height=790)
# title label
title_lbl = Label(bg_lbl, text="FACIAL RECOGNIZATION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"),
                  bg="white", fg="red")
title_lbl.place(x=0, y=130,width=1500,height=45)
#button<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
img3=Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\studentdetails.jpg")
img3=img3.resize((170,170),Image.ANTIALIAS)
root.photoimg3=ImageTk.PhotoImage(img3)
b1=Button(bg_lbl,image=root.photoimg3,cursor="hand2",command=stu_details)
b1.place(x=150,y=200,width=170,height=170)
b_1=Button(bg_lbl,text="STUDENT DETAILS",cursor="hand2",font=("times new roman",13,"bold"),
           bg="gray",fg="white",activebackground="gray",command=stu_details)
b_1.place(x=150,y=370,width=170,height=40)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
img4=Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\facedetect.png")
img4=img4.resize((170,170),Image.ANTIALIAS)
root.photoimg4=ImageTk.PhotoImage(img4)
b2=Button(bg_lbl,image=root.photoimg4,cursor="hand2")
b2.place(x=420,y=200,width=170,height=170)
b_2=Button(bg_lbl,text="FACE DETECTION",cursor="hand2",font=("times new roman",13,"bold"),bg="gray",fg="white",activebackground="gray")
b_2.place(x=420,y=370,width=170,height=40)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
img5=Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\attendance.jpg")
img5=img5.resize((170,170),Image.ANTIALIAS)
root.photoimg5=ImageTk.PhotoImage(img5)
b3=Button(bg_lbl,image=root.photoimg5,cursor="hand2")
b3.place(x=680,y=200,width=170,height=170)
b_3=Button(bg_lbl,text="ATTENDANCE",cursor="hand2",font=("times new roman",18,"bold"),bg="gray",fg="white",activebackground="gray")
b_3.place(x=680,y=370,width=170,height=40)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
img6=Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\help.jpg")
img6=img6.resize((170,170),Image.ANTIALIAS)
root.photoimg6=ImageTk.PhotoImage(img6)
b4=Button(bg_lbl,image=root.photoimg6,cursor="hand2")
b4.place(x=980,y=200,width=170,height=170)
b_4=Button(bg_lbl,text="HELP DESK",cursor="hand2",font=("times new roman",18,"bold"),bg="gray",fg="white",activebackground="gray")
b_4.place(x=980,y=370,width=170,height=40)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<train data<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
img7=Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\fcdt.jpeg")
img7=img7.resize((170,170),Image.ANTIALIAS)
root.photoimg7=ImageTk.PhotoImage(img7)
b5=Button(bg_lbl,image=root.photoimg3,cursor="hand2")
b5.place(x=150,y=450,width=170,height=170)
b_5=Button(bg_lbl,text="TRAIN DATA",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="gray")
b_5.place(x=150,y=605,width=170,height=40)
#<<<<<<<<<<<<<<<<<<<<<<<,,PHOTOS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
img8=Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\photos.jpg")
img8=img8.resize((170,170),Image.ANTIALIAS)
root.photoimg8=ImageTk.PhotoImage(img8)
b6=Button(bg_lbl,image=root.photoimg8,cursor="hand2")
b6.place(x=420,y=450,width=170,height=170)
b_6=Button(bg_lbl,text="PHOTOS",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="gray")
b_6.place(x=420,y=605,width=170,height=40)
#<<<<<<<<<<<<<<<<<<<<<<<<<<,DEVELOPER>>>>>>>>>>>>>>>>>>>>>>>>
img9=Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\developer.jpg")
img9=img9.resize((170,170),Image.ANTIALIAS)
root.photoimg9=ImageTk.PhotoImage(img7)
b7=Button(bg_lbl,image=root.photoimg9,cursor="hand2")
b7.place(x=680,y=450,width=170,height=170)
b_7=Button(bg_lbl,text="DEVELOPER",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="gray")
b_7.place(x=680,y=605,width=170,height=40)
#<<<<<<<<<<<<<<<<<<<<<<,,,EXIT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
img10=Image.open(r"C:\Users\Computer Solution\facial_recognization\photos\exit.jpg")
img10=img10.resize((170,170),Image.ANTIALIAS)
root.photoimg10=ImageTk.PhotoImage(img7)
b10=Button(bg_lbl,image=root.photoimg10,cursor="hand2")
b10.place(x=980,y=450,width=170,height=170)
b_10=Button(bg_lbl,text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg="gray",fg="white",activebackground="gray")
b_10.place(x=980,y=605,width=170,height=40)


root.mainloop()
