from tkinter import*
import password
import tiny_diary
from random import randint
from tkinter.scrolledtext import*
win=Tk()
ac
#Info_lable
win.geometry("1000x900")
win.title("Secure_personal_Diary")

#Destrying the label and buttons of main menu 
def destro(task):
    task.destroy()
#setting Up backGround
#______________________________________________________________________________________
img="alice"   
pic=PhotoImage(file=img+".png")
l2=Label(image=pic)
l2.grid()
l2.place(x=0,y=0)
#_______________________________________________________________________________________
fame=Frame(bg='green',borderwidth=10)
fame.grid()
fame.place(x=900,y=300)
Label(fame,text="Information BOX",bg="blue",fg="yellow",font=("AmericanTypewriter Cn",20)).grid(row=0)
#_Information Box______________________________________________________________________________________
text_1=Text(fame,width=15,height=5,bg='white',wrap='word',font=("AmericanTypewriter Cn",20),fg="black")
text_1.insert(INSERT,"Hard work\nis key\nto success")
text_1.insert(END,"---")
text_1.grid(row=1)
password.check(win)
#Labels and Button of the main Menu____________________________________________________
def Main_menu():
    global l6,add_button,search_button,fi,main_menu_button,view_all_button,del_button,text_1,update_p
    #This quote list will randomoly printed On the information Box When You enter To MAin menu
    array=["Hard work\nis key\nto success","If you can\nDream it\nYou can do it","Character is \nalso A wepon","Never Give Up","Do you KNow\nWho is\nDr.Tiny?","Be Unique\nBe prcatical","Support TinySoft","It is better\nTo lose than\nnot fighting"]
    #Menu_label
    index=randint(0,7)
    text_1.delete(0.0,END)
    text_1.insert(INSERT,array[index])
    text_1.insert(END,"---")
    file=open("user.txt","r")
    data=file.readlines()
    l6=Label(text="Welcome "+data[0]+"___________________",bg="blue",fg="yellow",font=("AmericanTypewriter Cn",40),padx=40,pady=20,relief=SUNKEN)
    l6.grid()
    l6.place(x=370,y=50)
    file.close()
    #Making a Frame
    
    fi=Frame(bg='green',borderwidth=10)
    fi.grid(column=5)
    fi.place(x=500,y=250)
    add_button=Button(fi,text="ADD NEW Event",bg='red',fg='yellow',font=("Comic sans MS",20),command=add,width=20,borderwidth=3,relief=SUNKEN)
    add_button.grid(column=5)
    search_button=Button(fi,text="Search An Event",bg='red',fg='yellow',font=("Comic sans MS",20),command=search_event,width=20,borderwidth=3,relief=SUNKEN)
    search_button.grid(column=5)
    view_all_button=Button(fi,text="View All Events",bg='red',fg='yellow',font=("Comic sans MS",20),command=show,width=20,borderwidth=3,relief=SUNKEN)
    view_all_button.grid(column=5)
    
    del_button=Button(fi,text="Edit an event",bg='red',fg='yellow',font=("Comic sans MS",20),command=edit_event,width=20,borderwidth=3,relief=SUNKEN)
    del_button.grid(column=5)
    update_p=Button(fi,text="Update Password",bg='red',fg='yellow',font=("Comic sans MS",20),command=password.update_pas,width=20,borderwidth=3,relief=SUNKEN)
    update_p.grid(column=5)
    main_menu_button=Button(fi,text="Credits",bg='red',fg='yellow',font=("Comic sans MS",20),command=credit,width=20,borderwidth=3,relief=SUNKEN)
    main_menu_button.grid(column=5)
#Menu of add Event option 
def add():
    global text,name,frame,inpu,save_button,exit_button,name_label,exit_button,frame_2,text_1
    global exit_button
    destro()
    text_1.delete(0.0,END)
    text_1.insert(INSERT,"Try to Give\nEach Event\na different name\nor date")
    text_1.insert(END,"---")
    frame=Frame(bg="red",borderwidth=10)
    frame.grid()
    frame.place(x=300,y=200)
    frame_2=Frame(bg="red",borderwidth=10)
    frame_2.grid()
    frame_2.place(x=300,y=260)
    pics=PhotoImage(file="alice.png")
    l2=Label(image=pics)
    #l2.grid()
    #l2.place(x=300,y=300)
    name_label=Button(frame,text='Event Date/name->',font=("Comic Sans MS",16),command=destro,bg='blue',fg='yellow',width=15)
    name_label.grid(row=0,column=0)
    name=StringVar()
    password=StringVar()
    inpu=Entry(frame,textvariable=name,bg='grey',fg='yellow',font=("Comic Sans MS",17))
    inpu.grid(row=0,column=1)
    text=ScrolledText(frame_2,width=30,wrap='word',height=10,bg='grey',font=("Comic Sans MS",20),fg="black")
    text.insert(INSERT,"EVENT DETAILS")
    text.insert(END,"--- ")
    text.grid(row=2,column=0)
    save_button=Button(win,text="Save and Exit",bg='blue',fg='yellow',font=("AmericanTypewriter cs",17),command=save)
    save_button.grid()
    save_button.place(x=295,y=155)
    exit_button=Button(win,text="Exit",bg="blue",fg="yellow",font=("AmericanTypewriter cs",17),command=ext)
    exit_button.grid()
    exit_button.place(x=750,y=155)
    
#When User want to exiit without save the event   
def ext():
    global exit_button
    destroy_add()
    exit_button.destroy()
    Main_menu()
#When user want to exit with sava 
def save():
    global t,text_1
    start="START"
    end="END"
    p=str(name.get())
    p=p.upper()
    #Checking if enterd event name is Valid
    if len(p)<=0:
        text_1.delete(0.0,END)
        text_1.insert(INSERT,"Event name should\nNot be Empty")
        text_1.insert(END,"---")
        return
    #if Entered event name is Valid then opens the file For reading To check If event name Already Exist
    file=open("data.txt","r")
    data=file.readlines()
    i=0
    while i<len(data):

        if data[i]==start+"\n":
            data[i+1]=data[i+1].upper()
            if data[i+1]==p+"\n":
                text_1.delete(0.0,END)   #If Event name Already exist It will not save the File and Information Box will send an Information To User
                text_1.insert(INSERT,"This Event name already Exist")
                text_1.insert(END,"---")
                file.close()
                return
                
        i+=1
    file.close()
    #when Every thing is right then open file to Append data
    t=text.get(0.0,END)
    file=open("data.txt","a")
    file.write(start)
    file.write("\n")
    file.write(str(name.get()))
    file.write("\n")
    file.write("->")
    file.write(t)
    file.write("\n")
    file.write(end)
    file.write("\n")
    file.close()
    destroy_add() #after appending data destroy add menu and Call main Menu
    Main_menu()
    
#Function to destroy add_event menu
def destroy_add():
    global exit_button,frame_2
    frame_2.destroy()
    save_button.destroy()
    text.destroy()
    inpu.destroy()
    name_label.destroy()
    frame.destroy()
    exit_button.destroy()
#Credit Menu Not to work hard on this Just inform users who you are
def credit():
    global credit_label,back_button
    destro()
    st="devoloped by Dr.Tiny\nFor Learning Purpose only\nFree for non_commercial use\nIf you want you can Try it\n-----------------Thank you\n"
    st_2="\nContact vishwajitrauniyar123@gmail.com\n For information You can Also Suppor me by\nJoining TinySoft"
    credit_label=Label(text=st+st_2,font=("AmericanTypewriter Cn",30),bg="blue",fg="black")
    credit_label.grid()
    credit_label.place(x=150,y=200)
    back_button=Button(text="<-BACK",bg="yellow",command=destroy_credit,font=("AmericanTypewriter Cn",16),width=7)
    back_button.grid()
    back_button.place(x=800,y=620)
    text_1.delete(0.0,END)
    text_1.insert(INSERT,"We work in\nthe dark \nso that\nlight may\nExist")
    text_1.insert(END,"---")
    
#Destroy Credit menu    
def destroy_credit():
    credit_label.destroy()
    back_button.destroy()
    Main_menu()
#Search event BUtton will call this and it will take only 
def search_event():
    global find,search_label,entry,back,submit,frames
    frames=Frame(bg='red')
    destro()
    search_label=Button(text="Enter an Event to Search",bg="blue",fg="yellow",font=(13))
    search_label.grid()
    search_label.place(x=300,y=100)
    find=StringVar()
    entry=Entry(textvariable=find,bg='white',fg='black',font=(13))
    entry.grid()
    entry.place(x=500,y=100)
    submit=Button(text="Submit",bg="blue",fg="yellow",font=(20),command=searching)
    submit.grid()
    submit.place(x=450,y=150)
    back=Button(text="BACK",bg='blue',fg='yellow',font=("Comic Sans MS",12),command=destroy_search)
    back.grid()
    back.place(x=200,y=100)
    
b=[]
l=[]
i=0    
def searching():
    global b,l,frames
    start="START\n"
    end="END\n"
    if len(b)>0:
        for al in b:
            al.destroy()
            i=0
    if len(l)>0:
        for al in l:
            al.destroy()
            i=0
            frames.destroy()
    l=[]
    b=[]
    i=0
    frames=Frame(bg="red",borderwidth=10)
    frames.grid()
    frames.place(x=300,y=200)
    
    file=open("data.txt","r")
    data=file.readlines()
    temp=str(find.get())
    temp=temp.upper()
    j=0
    loop=0          #looop counter so I can track how many more lines to be read
    """Since I uses Only Flat files so it is Tought to read a specific data so this code
be a little bit confusing don't worry about it I will update it in future.
Here is the algorihtm--->
1.->I sotred Each Users Information in Following manner
START\n
event name\n
event details\n



END\n
2.->When user enter an event name I will check all line which has "START\n" 
3.->If a line has "START\n" then I will comapare its next line to Event name 
4.->If three digit match then it will be as search successful
5.->You can make your own source code using this algo
6.->Remember to store event details and name if search is successful
"""
    
    while loop<len(data):
        info=[]
        loop+=1
        if(data[loop-1]==start):
            while True:
                if data[loop]==end:
                    break
                info.append(data[loop])
                loop+=1
            if len(info)>0:
            
                fin=str(info[0])
                fin=fin.upper()
                cmp=fin
                fin=list(fin)
                if(cmp[:len(temp)]==temp):     #temp[0]==fin[0] and temp[1]==fin[1]
                    full_name=str(info[0])
                
                    b.append(Button(frames,text=full_name,bg='blue',fg='yellow',font=(30),width=10))
                
                
                    l.append(ScrolledText(frames,bg='green',fg='black',wrap='word',font=('Comic Sans MS',15),height=10,width=40))
                    for inf in range(1,len(info)-1):
                        l[i].insert(INSERT,info[inf])
                    del(info)
                    l[i].grid()
                    b[i].grid()        
                    l[i].insert(END,"")
                    
                    
                    i+=1
                    text_1.delete(0.0,END)
                    text_1.insert(INSERT,"One Result Found\nif you don't\n find what you\nExpect try to\n see all event")
                    text_1.insert(END,"---")
                    if(i>0):
                        return l[0].get(0.0,END),full_name
                        #As yOu can see It returns To thing it is useful when you import this
                        #Module to others module
                        #For Example when You search it to edit or delete then it will return even name and Details to edit
                    
                    break

    file.close()
    password.update("No search Found/nTry to visit\n'See All Events'\nmenu\n")
    return 0,0#if nothing found Then it will return integer 0,0 so that I can know search was not success
    
    
#destroying Search menu________________>>>>>><<<<<<>>>>>><<<<<<>>>>><<<<<<>>>><<<<<>>>>>><<<<>><<<>>            
def destroy_search():
    global frames
    for i in l:
        i.destroy()
    for j in b:
        j.destroy()
    search_label.destroy()
    entry.destroy()
    back.destroy()
    frames.destroy()
    submit.destroy()
    Main_menu()
"""
Show is and show_all are most likely search and serching functionn but it will print all the
data in the file
"""
def show():
    global rec_button,pre_button,frame_1,back_button,pre,num,b,l,current
    back_button=Button(text="Main Menu",bg="blue",fg="yellow",command=destroy_all,font=("Comic sans MS",16),width=10)
    back_button.grid()
    back_button.place(x=495,y=255)
    rec_button=Button(text="Next->",bg="blue",fg="yellow",command=show_all,font=("Comic sans MS",16),width=7)
    pre_button=Button(text="<-Preveous",bg="blue",fg="yellow",command=prev,font=("Comic sans MS",16),width=10)
    rec_button.grid()
    rec_button.place(x=690,y=255)
    pre_button.place(x=300,y=255)
    current=0
    pre=[]
    num=0
    b=[]
    l=[]
    frame_1=Frame(bg="red",borderwidth=10)
    frame_1.grid()
    frame_1.place(x=300,y=300)
    text_1.delete(0.0,END)
    text_1.insert(INSERT,"See all \nyour saves\nuse next\nand previous button")
    text_1.insert(END,"---")
    show_all()
def show_all():
    global current,num,b,l,i,pre,rec_button,pre_button,frame_1,back_button

    
    destro()
    i=0
    
    if len(l)>0:
        for al in l:
            al.destroy()
        for al in b:
            al.destroy()
    b=[]
    l=[]
    start="START\n"
    end="END\n"
    file=open("data.txt","r")
    data=file.readlines()
    
    record_num=0
    if num>len(data)-2:
        l.append(Label(frame_1,text='No more Events\nplease add some\nin add event option',bg='blue',fg='yellow',font=("Comic sans MS",20)))
        l[i].grid()
        i+=1
        return
    while num<len(data):
        if data[num]==start:
            pre.append(num)
            current+=1
            num+=1
            info=[]
            while data[num]!=end:
                info.append(data[num])
                num+=1
            

            b.append(Text(frame_1,bg='green',fg='black',font=('Comic Sans MS',15),wrap='word',height=10,width=40))
            for inf in range(1,len(info)-1):
                b[i].insert(INSERT,info[inf])
            b[i].insert(END,"//////")
            b[i].grid()
            l.append(Label(frame_1,text=info[0],bg='yellow',width=10,font=("Comic sans MS",20)))
            l[i].grid()
            i+=1
            del(info)
            break
        else:
            num+=1
        if(i==1):
            i=0
            break

#_____________________________________________________   
#Here I uses doubly linked list data Structure So that
#It make possible to use doubly Linked List___________
#_____________________________________________________
def prev():
    global pre,current,num
    if len(pre)>0:
        num=pre[current-2]
        current-=2
        pre.pop()
        show_all()
    
    else:
        return
        
        
#destroying show all menu<---------<----><<<|>>><|>------>
def destroy_all():
    global b,l,rec_button,pre_button,frame_1,back_button,num,pre,current
    if len(b)>0:
        for al in b:
            al.destroy()
        for al in l:
            al.destroy()
    rec_button.destroy()
    pre_button.destroy()
    frame_1.destroy()
    back_button.destroy()
    Main_menu()
    current=0
    del(pre)
    pre=[]
    num=0
    current=0
#Edit Event menu
def edit_event():
    global back,submit
    search_event()
    back.destroy()
    submit.destroy()
    password.update("Search an event\nto edit")
    tiny_diary.make(win)
  
    
win.mainloop()
