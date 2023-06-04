from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system") 

        img=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\a.jpg")
        img=img.resize((350,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=350,height=150)

        img1=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\b.jpg")
        img1=img1.resize((350,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=350,y=0,width=350,height=150)

        img2=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\ref.PNG")
        img2=img2.resize((350,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=690,y=0,width=360,height=150)

        img3=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\t.JPG")
        img3=img3.resize((350,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1020,y=0,width=350,height=150)

        #background image
        img4=Image.open(r"C:\react js\Face_Recogination_Attandence\collage_images\d.jpg")
        img4=img4.resize((1530,690),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=140,width=1530,height=710)

        title_lbl=Label(bg_img,text="Attendance Management System " ,font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left  lable frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("timesnew romans" ,12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=580)

        #attendence information
        current_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Attendence imformation",font=("timesnew romans" ,12,"bold"))
        current_frame.place(x=15,y=10,width=620,height=450)
         
        #attendence
        attdid_lbl=Label(current_frame,text="AttdID",font=("timesnew romans" ,12,"bold"),bg="white")
        attdid_lbl.grid(row=0,column=1,padx=10,sticky=W)

        AttendenceID_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        AttendenceID_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        #rollnbr
        roll_lbl=Label(current_frame,text="Roll No",font=("timesnew romans" ,12,"bold"),bg="white")
        roll_lbl.grid(row=0,column=3,padx=10,sticky=W)

        Rollno_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        Rollno_entry.grid(row=0,column=4,padx=10,pady=10,sticky=W)

        #student name
        stdname_lbl=Label(current_frame,text="Name",font=("timesnew romans" ,12,"bold"),bg="white",width=6)
        stdname_lbl.grid(row=1,column=1,padx=10,sticky=W)

        Studentname_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        Studentname_entry.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        #department
        dep_lbl=Label(current_frame,text="Department",font=("timesnew romans" ,12,"bold"),bg="white")
        dep_lbl.grid(row=1,column=3,padx=10,sticky=W)

        dep_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        dep_entry.grid(row=1,column=4,padx=10,pady=10,sticky=W)

        #time
        time_lbl=Label(current_frame,text="Time",font=("timesnew romans" ,12,"bold"),bg="white",width=6)
        time_lbl.grid(row=2,column=1,padx=10,sticky=W)

        time_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        time_entry.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        #date
        date_lbl=Label(current_frame,text="Date",font=("timesnew romans" ,12,"bold"),bg="white",width=6)
        date_lbl.grid(row=2,column=3,padx=10,sticky=W)

        date_entry=ttk.Entry(current_frame,font=("timesnew romans" ,12,"bold"),width=18,state="read only")
        date_entry.grid(row=2,column=4,padx=10,pady=10,sticky=W)

        #Attensence Status
        status_lbl=Label(current_frame,text="Status",font=("timesnew romans" ,12,"bold"),bg="white",width=6)
        status_lbl.grid(row=3,column=1,padx=10,sticky=W)

        status_combo=ttk.Combobox(current_frame,font=("timesnew romans" ,12,"bold"),width=17,state="read only")
        status_combo['values']=("Present ","absent")
        status_combo.current(0)
        status_combo.grid(row=3,column=2,padx=2,pady=10,sticky=W)

        #button
        
        btn_frame=Frame(current_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=15,y=270,width=580,height=100)

        #save button
        save_btn=Button(btn_frame,text="import csv",width=13,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0, column=1,padx=4,pady=30,sticky=W)

        update_btn=Button(btn_frame,text="export csv",width=13,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0, column=2)

        delete_btn=Button(btn_frame,text="update",width=13,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0, column=3)

        reset_btn=Button(btn_frame,text="reset",width=13,font=("timesnew romans" ,12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0, column=4)

        #right frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attandence",font=("timesnew romans" ,12,"bold"))
        right_frame.place(x=680,y=10,width=650,height=550)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=635,height=450)


        #table scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()