from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox 

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')
        
        # Variable
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_status=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()


        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman' ,37, 'bold'),fg='darkblue' , bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)
        
        # main frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=70,width=1500,height=600)

        # upper frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman' ,11, 'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)
         


         # labels and entry fields
        lbl_dep=Label(upper_frame, text='Department',font=('arial' ,11, 'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial' ,12, 'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department' , 'HR' , 'software Engineer' , 'Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10 ,sticky=W)
        
        # name
        lbl_Name=Label(upper_frame,font=('arial' ,12, 'bold'),text='Name:',bg='white')
        lbl_Name.grid(row=0,column=2,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,font=('arial' ,11, 'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        # # lbl_designition
        lbl_Designition=Label(upper_frame,font=('arial' ,12, 'bold'),text='Designition:',bg='white')
        lbl_Designition.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(upper_frame,width=22,textvariable=self.var_designition,font=('arial' ,11, 'bold'))
        txt_Designition.grid(row=4,column=3,padx=5,pady=7)


        
        # email
        lbl_email=Label(upper_frame,font=('arial' ,12, 'bold'),text='Email:',bg='white')
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(upper_frame,width=22,textvariable=self.var_email,font=('arial' ,11, 'bold'))
        txt_email.grid(row=1,column=3,padx=5,pady=7)

        
        
        # address
        lbl_address=Label(upper_frame,font=('arial' ,12, 'bold'),text='Address' ,bg='white')
        lbl_address.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,width=22,textvariable=self.var_address,font=('arial' ,11, 'bold'))
        txt_address.grid(row=1,column=1,padx=5,pady=7)

         
        
        # Married
        lbl_married_status=Label(upper_frame,font=('arial' ,12, 'bold'),text='Status:',bg='white')
        lbl_married_status.grid(row=2,column=2,sticky=W,padx=5,pady=7)
        
        com_txt_married=ttk.Combobox(upper_frame,state='readonly',textvariable=self.var_status,
                                                        font=('arial',12,'bold'),width=18)

        com_txt_married['value']=('married','unmarried')
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=2,pady=7)
        
        # dob
        lbl_dob=Label(upper_frame,font=('arial' ,12, 'bold'),text='DOB:',bg='white')
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('arial' ,11, 'bold'))
        txt_Designition.grid(row=3,column=1,padx=5,pady=7)

         

        # doj
        lbl_doj=Label(upper_frame,font=('arial' ,12, 'bold'),text='DOJ:',bg='white')
        lbl_doj.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('arial' ,11, 'bold'))
        txt_doj.grid(row=2,column=1,padx=5,pady=7)
        

        # proof
        com_txt_proof=ttk.Combobox(upper_frame,state='readonly',
                                                      font=('arial',12,'bold'),width=18)

        com_txt_proof['value']=('select ID proof','ADHAR CARD','PAN CARN' ,'DRIVING LICENSE')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=5,pady=7)
        
        txt_proof=ttk.Entry(upper_frame,width=22,textvariable=self.var_idproof,font=('arial' ,11, 'bold'))
        txt_proof.grid(row=4,column=1,padx=5,pady=7)
        
        # gender
        lbl_gender_status=Label(upper_frame,font=('arial' ,11, 'bold'),text='Gender:',bg='white')
        lbl_gender_status.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        
        com_txt_gender=ttk.Combobox(upper_frame,state='readonly',textvariable=self.var_gender,
                                                        font=('arial',12,'bold'),width=18)

        com_txt_gender['value']=('Male','Female')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        # phone
        lbl_phone=Label(upper_frame,font=('arial' ,12, 'bold'),text='Phone_Number:',bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(upper_frame,width=22,textvariable=self.var_phone,font=('arial' ,11, 'bold'))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        # country
        lbl_Country=Label(upper_frame,font=('arial' ,12, 'bold'),text='Country:',bg='white')
        lbl_Country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_Country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial' ,11, 'bold'))
        txt_Country.grid(row=1,column=5,padx=2,pady=7)


        # ctc
        lbl_ctc=Label(upper_frame,font=('arial' ,12, 'bold'),text='Salary(CTC):',bg='white')
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_Ctc=ttk.Entry(upper_frame,width=22,textvariable=self.var_salary,font=('arial' ,11, 'bold'))
        txt_Ctc.grid(row=2,column=5,padx=2,pady=7)
        
     


       # button frame
        button_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1100,y=110,width=172,height=230)
        btn_add=Button(button_frame,text='Save',command=self.add_data,font=('arial' ,15, 'bold'),width=13,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=2)

        btn_update=Button(button_frame,text='Update',command=self.update_data,font=('arial' ,15, 'bold'),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=10)

        btn_delete=Button(button_frame,text='Delete',command=self.delete_data,font=('arial' ,15, 'bold'),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=10)

        # btn_clear=Button(button_frame,text='Clear',font=('arial' ,15, 'bold'),width=13,bg='blue',fg='white')
        # btn_clear.grid(row=3,column=0,padx=1,pady=10)

        

        # down frame 
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman' ,11, 'bold'),fg='red',)
        down_frame.place(x=10,y=280,width=1480,height=270)
        
        # search frame 
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman' ,11, 'bold'),fg='red',)
        search_frame.place(x=0,y=0,width=1470,height=60)
       
        search_by=Label(search_frame,font=('arial',11,'bold'),text='Search By:',fg='white',bg='blue')
        search_by.grid(row=0,column=0,padx=5,sticky=W,pady=5)

       # search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state='readonly',
                                    font=('arial',12,'bold'),width=18)
        com_txt_search['value']=('Select Option','Phone','id_proof')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5,pady=5)


        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5,pady=5)


        btn__search=Button(search_frame,command=self.search_data,text='search',font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn__search.grid(row=0,column=3,padx=5,pady=5)

        btn_ShowAll=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn_ShowAll.grid(row=0,column=4,padx=5)

        
#============Employee_Table============

  # Table frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','degi','email','address','married','dob','doj','idproofcomb','idproof','gender','phone','country','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('degi',text='Designition')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Status')
        self.employee_table.heading('dob',text='DOP')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID Type')
        self.employee_table.heading('idproof',text='ID Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Coutry')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'
        
        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('degi',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('married',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcomb',width=100)
        self.employee_table.column('idproof',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()


        # ========function declarations============

    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields Are Required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='1234',database='mydata')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO employee1 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                     
                                                                                                             self.var_dep.get(),
                                                                                                             self.var_name.get(),
                                                                                                             self.var_designition.get(),
                                                                                                             self.var_email.get(),
                                                                                                             self.var_address.get(),
                                                                                                             self.var_status.get(),
                                                                                                             self.var_dob.get(),
                                                                                                             self.var_doj.get(),
                                                                                                             self.var_idproofcomb.get(),
                                                                                                             self.var_idproof.get(),
                                                                                                             self.var_gender.get(),
                                                                                                             self.var_phone.get(),
                                                                                                             self.var_country.get(),
                                                                                                             self.var_salary.get(),

                       
                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showerror('Success','Employee has been added!',parent=self.root)
            except Exception as es:
                 messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee1')
        data=my_cursor.fetchall()
        if len(data)!=0:
          self.employee_table.delete(*self.employee_table.get_children())
          for i in data:
               self.employee_table.insert("",END,values=i)
          conn.commit
        conn.close()

 # GET CURSOR
    def get_cursor(self,event=""):
         cursor_row=self.employee_table.focus()
         content=self.employee_table.item(cursor_row)
         data=content['values']

         self.var_dep.set(data[0])
         self.var_name.set(data[1])
         self.var_designition.set(data[2])
         self.var_email.set(data[3])
         self.var_address.set(data[4])
         self.var_status.set(data[5])
         self.var_dob.set(data[6])
         self.var_doj.set(data[7])
         self.var_idproofcomb.set(data[8])
         self.var_idproof.set(data[9])
         self.var_gender.set(data[10])
         self.var_phone.set(data[11])
         self.var_country.set(data[12])
         self.var_salary.set(data[13])

    def update_data(self):
         if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields Are Required')
         else:
             try:
                update=messagebox.askyesno('update','Are sure update this employee data')
                if update>0:
                  conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='mydata')
                  my_cursor=conn.cursor()
                  my_cursor.execute('update employee1 set Department=%s,Name=%s,Designition=%s,Email=%s,Address=%s,status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,phone=%s,country=%s,salary=%s',(
                       self.var_dep.get(),
                                                                                                             self.var_name.get(),
                                                                                                             self.var_designition.get(),
                                                                                                             self.var_email.get(),
                                                                                                             self.var_address.get(),
                                                                                                             self.var_status.get(),
                                                                                                             self.var_dob.get(),
                                                                                                             self.var_doj.get(),
                                                                                                             self.var_idproofcomb.get(), 
                                                                                                             self.var_gender.get(),
                                                                                                             self.var_phone.get(),
                                                                                                             self.var_country.get(),
                                                                                                             self.var_salary.get(),
                                                                                                             self.var_idproof.get()
             
                                                                                                                                                                                                     ))
                else:
                    if not update:
                         return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success",'Employee Successfully updated',parent=self.root)
             except Exception as es:
                       messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
        

# delete
    def delete_data(self):
         if self.var_idproof.get()=="":
              messagebox.showerror('Error','All fields are required')
         else:
             try:
                Delete=messagebox.askyesno('Delete','Are you sure delete this employee',parent=self.root) 
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='mydata')
                    my_cursor=conn.cursor()
                    sql='DELETE FROM employee1 WHERE id_proof = %s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                         return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete",'Employee Successfully Deleted',parent=self.root)
             except Exception as es:
                       messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
        
         
# search
    def search_data(self):
         if self.var_com_search.get()=='' or self.var_search.get()=='':
              messagebox.showerror('Error','please select option')
         else:
             try:
                  conn=mysql.connector.connect(host='localhost',username='root',password='1234',database='mydata')
                  my_cursor=conn.cursor()
                  my_cursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE' %"+str(self.var_search.get()+"%'"))
                  rows=my_cursor.fetchall()
                  if len(rows)!=0:
                       self.employee_table.delete(*self.employee_table.get_children())
                       for i in rows:
                           self.employee_table.insert("",END,values=i)
                       conn.commit
                  conn.close()
             except Exception as es:
                       messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
        






if __name__=="__main__":
                root=Tk()
                obj=Employee(root)
                root.mainloop()
