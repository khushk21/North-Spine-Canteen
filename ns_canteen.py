import tkinter as tk
import datetime
from tkinter import messagebox
from tkinter import simpledialog
import tkcalendar
import random
from PIL import Image,ImageTk
#declaring global variables
t1=""
user_date=""
user_time=""
user_day=""
#tuple for weekdays
weekday=("Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday","Sunday")
n= datetime.datetime.now()
n=n.replace(microsecond=0)
current_date=(datetime.datetime.now().date())
current_time=(datetime.datetime.now().time().replace(microsecond=0))
current_day=weekday[n.weekday()]
#stores waiting time for each store
wt_store_dict={"1":[(1,2,3,4,5,4,4),(2,3,4,5,4,3,5),(1,3,5,7,4,4,4)],"2":[(1,2,3,4,5,3,4),(5,2,3,4,5,3,4),(1,2,3,4,5,4,5)],"3":[(3,4,5,2,3,6,6),(5,6,4,4,1,2,3),(1,2,3,4,5,6,4)],
              "4":[(1,2,3,4,5,6,4),(3,5,4,6,4,5,2),(5,4,2,3,4,1,4)],"5":[(3,4,5,6,4,1,2),(5,6,4,3,4,5,1),(5,4,6,5,1,2,3)] }
#stores all menus
Mcdonald_Menu =  {"Breakfast": ["1.Big Breakfast: $8.50", "2.Chicken Muffin: $5.60",
"3.Sausage McMuffin: $6.00", "4.Filet-O-Fish: $5.50"], "Afternoon": ["1.Double Cheeseburger Meal: $6.20", "2.Four McWing Meal: $6.80",
"3.McChicken: $5.00", "4.Big Mac: $8.20" ,  "5.Filet-O-Fish: $5.50"]}

KFC_Menu =  {"Breakfast" : ["1.Riser Burger: $5.20", "2.Porridge: $4.50",
"3.American Twister: $7.70", "4.Brekkie Burger: $5.70"], "Afternoon": ["1.Two Piece Chicken Meal: $6.55", "2.Three Piece Chicken Meal: $8.55",
"3.Zinger Meal: $6.00", "4.Snack N Share: 12.95" ,  "5.Shroom Burger Meal: $5.10"]}

Long_John_Silvers = {"Breakfast" : ["1.Texas Chicken Double Toast: $6.30", "2.Chicken Sausage Double Toast: $5.90",
"3.Double Turkey and Bacon Double Toast: $5.90", "4.French Toast Platter : $9.50"], "Afternoon": ["1.Fish and Chicken: $6.50", "2.Fish and Two piece Shrimp: $6.90",
"3.Three Piece Fish: $7.50", "4.Three Piece Chicken: $6.50"]}

Chinese_delight_even = ["1.Roasted Chicken Rice: $3.20", "2.Roasted Duck Rice: $3.70",
"3.Steamed Chicken Rice: $3.50", "4.Steamed Duck Rice: $4.00"]

Chinese_delight_odd = ["1.Roasted Chicken Noodles: $3.50", "2.Roasted Duck Noodles: $3.90",
"3.Steamed Chicken Noodles: $4.20", "4.Steamed Duck Noodles: $4.50"]

Chinese_delight_weekdays = [Chinese_delight_even, Chinese_delight_odd]

Western_store_even = ["1.Chicken Chop: $6.00", "2.Pork Chop: $6.50",
"3.Grilled Fish: $7.00", "4.Aglio Olio: $5.00"]

Western_store_odd = ["1.Cheese Baked Rice: $7.00", "2.Lamb Chop: $7.50",
"3.Seafood Palette: $8.00", "4.Mac and Cheese Pasta: $6.50"]

Western_Store_weekdays = [Western_store_even, Western_store_odd]

Chinese_delight = {"Breakfast" : ["1.Shredded Chicken Porridge: $3.50", "2.Peanut Porridge: $2.50",
"3.Century Egg Porridge: $3.20"], "Afternoon": Chinese_delight_weekdays}

Western_Store = {"Breakfast" : ["1.Bacon Breakfast Set: $4.00", "2.Scrambled Eggs Set: $3.50",
"3.Hotdog with Sunny Side Up Egg: $3.00"], "Afternoon": Western_Store_weekdays}
#creating tkinter window
root=tk.Tk()
root.configure(bg='black')
root.geometry('400x500')
s1="North Spine App "
s= s1+" "+str(n.replace(microsecond=0,second=0))+"  "+ str(weekday[n.weekday()])
root.title(s)
d=str(n)+" "+str(weekday[n.weekday()])
now = datetime.datetime.now().time()
time_8am=now.replace(hour=8,minute=0,second=0,microsecond=0)
time_9am=now.replace(hour=9,minute=0,second=0,microsecond=0)
time_10am= now.replace(hour=10,minute=0,second=0,microsecond=0)
time_11am= now.replace(hour=11,minute=0,second=0,microsecond=0)
time_17pm= now.replace(hour=17,minute=0,second=0,microsecond=0)
time_19pm=now.replace(hour=19,minute=0,second=0,microsecond=0)
time_20pm= now.replace(hour=20,minute=0,second=0,microsecond=0)
time_22pm= now.replace(hour=22,minute=0,second=0,microsecond=0)
#displays the content when first option is chosen
def today_stores():
    for widget in root.winfo_children():
        widget.forget()
    date_label=tk.Label(root, text=d,fg="red",bg="black",font="Calibri 16")
    date_label.pack(anchor="n",fill=tk.X)
    w1=tk.Label(root,text="Choose a store to view menu",fg="red",font="Callibiri 16",bg="black")
    w1.pack(anchor="n",fill=tk.X)
    if(current_day=="Saturday" or current_day=="Sunday"):
        store1_button=tk.Button(root,text="1.McDonald's",fg="red",font="Chalkboard 15",command= lambda: menu1(current_time,current_date,current_day))
        store1_button.pack(anchor="n",fill=tk.X)
        store2_button=tk.Button(root,text="2.KFC",fg="red",font="Chalkboard 15",command=lambda: menu2(current_time,current_date,current_day))
        store2_button.pack(anchor="n",fill=tk.X)
        store5_button=tk.Button(root,text="3.Long John Silver's",fg="red",font="Chalkboard 15", command=lambda: menu5(current_time,current_date,current_day))
        store5_button.pack(anchor="n",fill=tk.X)
        img1 = ImageTk.PhotoImage(Image.open("mcd logo.jpg"))
        img1_label=tk.Label(root,image=img1,bg="black")
        img1_label.pack(anchor="n")
        img1_label.image=img1
        img2=ImageTk.PhotoImage(Image.open("kfc_logo.jpg"))
        img2_label=tk.Label(root,image=img2,bg="black")
        img2_label.pack(anchor="n")
        img2_label.image=img2
        img3=ImageTk.PhotoImage(Image.open("ljs_logo.jpg"))
        img3_label=tk.Label(root,image=img3,bg="black")
        img3_label.pack(anchor="n")
        img3_label.image=img3
    else:
        store1_button = tk.Button(root, text="1.McDonald's",fg="red",font="Chalkboard 13",command=lambda: menu1(current_time, current_date, current_day))
        store1_button.pack(side="top", fill=tk.X)
        store2_button = tk.Button(root, text="2.KFC",fg="red",font="Chalkboard 13", command=lambda: menu2(current_time, current_date, current_day))
        store2_button.pack(side="top", fill=tk.X)
        store3_button = tk.Button(root, text="3.Chinese Delight",fg="red",font="Chalkboard 13",command=lambda: menu3(current_time, current_date, current_day))
        store3_button.pack(side="top", fill=tk.X)
        store4_button = tk.Button(root, text="4.Western Store",fg="red",font="Chalkboard 13", command=lambda: menu4(current_time, current_date, current_day))
        store4_button.pack(side="top", fill=tk.X)
        store5_button = tk.Button(root, text="5.Long John Silver's",fg="red",font="Chalkboard 13",command=lambda: menu5(current_time, current_date, current_day))
        store5_button.pack(side="top", fill=tk.X)
        img1 = ImageTk.PhotoImage(Image.open("s1.jpg"))
        img1_label = tk.Label(root, image=img1, bg="black")
        img1_label.pack(anchor="n")
        img1_label.image = img1
        img2 = ImageTk.PhotoImage(Image.open("s2.jpg"))
        img2_label = tk.Label(root, image=img2, bg="black")
        img2_label.pack(anchor="n")
        img2_label.image = img2
        img3 = ImageTk.PhotoImage(Image.open("s3.jpg"))
        img3_label = tk.Label(root, image=img3, bg="black")
        img3_label.pack(anchor="n")
        img3_label.image = img3
        img4=ImageTk.PhotoImage(Image.open("s4.jpg"))
        img4_label=tk.Label(root,image=img4,bg="black")
        img4_label.pack(anchor="n")
        img4_label.image=img4
    back_button=tk.Button(root,text="Back",fg="red",font="Chalkboard 15",command=opening_screen)
    back_button.pack(side="bottom",fill=tk.X)
#menu function for McDonald's
def menu1(t,d,m):
    for widget in root.winfo_children():
        widget.forget()
    date_and_time_label=tk.Label(text=(str(t)+" "+str(d)+" "+m),fg="red",bg="black",font="Calibri 15")
    date_and_time_label.pack(anchor="n",fill=tk.X)
    if (m!="Saturday" and m!="Sunday"):
        if (time_8am <= t < time_11am):
            list1 = Mcdonald_Menu["Breakfast"]
            for i in list1:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"1"))
            waiting_time.pack(anchor="n", fill=tk.X)
        elif (time_11am <= t < time_22pm):
            l = Mcdonald_Menu["Afternoon"]
            for i in l:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",font="Chalkboard 15",fg="red", command=lambda: avg_waiting_time(t,"1"))
            waiting_time.pack(anchor="n", fill=tk.X)
        else:
            display_label = tk.Label(text="Sorry, we are closed now!", fg="red", bg="black",font="Calibri 22")
            display_label.pack(anchor='n', fill=tk.X)
    else:
        if (time_9am <= t < time_11am):
            list1 = Mcdonald_Menu["Breakfast"]
            for i in list1:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",font="Chalkboard 15", fg="red",command=lambda: avg_waiting_time(t,"1"))
            waiting_time.pack(anchor="n", fill=tk.X)
        elif (time_11am <= t < time_19pm):
            l = Mcdonald_Menu["Afternoon"]
            for i in l:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"1"))
            waiting_time.pack(anchor="n", fill=tk.X)
        else:
            display_label = tk.Label(text="Sorry, we are closed now!", fg="red", bg="black",font="Calibri 22")
            display_label.pack(anchor='n', fill=tk.X)
    op_hours=tk.Button(root,text="Operating hours",font="Chalkboard 15",fg="red", command=lambda: op(1))
    op_hours.pack(anchor="n",fill=tk.X)
    i1=ImageTk.PhotoImage(Image.open("m1.jpg"))
    i1_label=tk.Label(root,image=i1,bg="black")
    i1_label.pack(anchor='n',fill='both')
    i1_label.image=i1
    back_button = tk.Button(root, text="Back",font="Chalkboard 15",fg="red", command=opening_screen)
    back_button.pack(side="bottom", fill=tk.X)
#menu function for KFC
def menu2(t,d,m):
    for widget in root.winfo_children():
        widget.forget()
    date_and_time_label = tk.Label(text=(str(t) + " " + str(d) + " " + m), fg="red", bg="black",font="Calibri 15")
    date_and_time_label.pack(anchor="n",fill=tk.X)
    if (m!="Saturday" and m!="Sunday"):
        if (time_8am <= t < time_11am):
            list1 = KFC_Menu["Breakfast"]
            for i in list1:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"2"))
            waiting_time.pack(anchor="n", fill=tk.X)
        elif (time_11am <= t < time_22pm):
            l = KFC_Menu["Afternoon"]
            for i in l:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"2"))
            waiting_time.pack(anchor="n", fill=tk.X)
        else:
            display_label = tk.Label(text="Sorry, we are closed now!", fg="red", bg="black",font="Calibri 22")
            display_label.pack(anchor='n', fill=tk.X)
    else:
        if (time_9am <= t < time_11am):
            list1 = KFC_Menu["Breakfast"]
            for i in list1:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"2"))
            waiting_time.pack(anchor="n", fill=tk.X)
        elif (time_11am <= t < time_19pm):
            l = KFC_Menu["Afternoon"]
            for i in l:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"2"))
            waiting_time.pack(anchor="n", fill=tk.X)
        else:
            display_label = tk.Label(text="Sorry, we are closed now!", fg="red", bg="black",font="Calibri 22")
            display_label.pack(anchor='n', fill=tk.X)
    op_hours=tk.Button(root,text="Operating Hours",fg="red",font="Chalkboard 15", command=lambda: op(2))
    op_hours.pack(anchor="n", fill=tk.X)
    i2 = ImageTk.PhotoImage(Image.open("m2.jpg"))
    i2_label = tk.Label(root, image=i2, bg="black")
    i2_label.pack(anchor='n', fill='both')
    i2_label.image = i2
    back_button=tk.Button(root,text="Back",fg="red",font="Chalkboard 15", command=opening_screen)
    back_button.pack(side="bottom",fill=tk.X)
#menu function for chinese delight
def menu3(t,d,m):
    for widget in root.winfo_children():
        widget.forget()
    if (m == 'Tuesday' or m == 'Thursday'):
        odd_even = 0
    else:
        odd_even = 1
    date_and_time_label = tk.Label(text=(str(t) + " " + str(d) + " " + m), fg="red", bg="black",font="Calibri 15")
    date_and_time_label.pack(anchor="n",fill=tk.X)
    if (time_8am <= t < time_11am):
        list1 = Chinese_delight["Breakfast"]
        for i in list1:
            menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
            menu_label.pack(anchor="nw")
        waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"3"))
        waiting_time.pack(anchor="n", fill=tk.X)
    elif (time_11am <= t < time_22pm):
        l = Chinese_delight["Afternoon"][odd_even]
        for i in l:
            menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
            menu_label.pack(anchor="nw")
        waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"3"))
        waiting_time.pack(anchor="n", fill=tk.X)
    else:
        display_label = tk.Label(text="Sorry, we are closed now!", fg="red", bg="black",font="Calibri 22")
        display_label.pack(anchor='n', fill=tk.X)
    op_hours=tk.Button(root,text="Operating Hours",fg="red",font="Chalkboard 15", command=lambda: op(3))
    op_hours.pack(anchor="n", fill=tk.X)
    i3 = ImageTk.PhotoImage(Image.open("m3.jpg"))
    i3_label = tk.Label(root, image=i3, bg="black")
    i3_label.pack(anchor='n', fill='both')
    i3_label.image = i3
    back_button=tk.Button(root,text="Back",fg="red",font="Chalkboard 15", command=opening_screen)
    back_button.pack(side="bottom",fill=tk.X)
#menu function for western store
def menu4(t,d,m):
    for widget in root.winfo_children():
        widget.forget()
    if(m=='Tuesday' or m=='Thursday'):
        odd_even=0
    else:
        odd_even=1
    date_and_time_label = tk.Label(text=(str(t) + " " + str(d) + " " + m), fg="red", bg="black",font="Calibri 15")
    date_and_time_label.pack(anchor="n",fill=tk.X)
    if (time_8am <= t < time_11am):
        list1 = Western_Store["Breakfast"]
        for i in list1:
            menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
            menu_label.pack(anchor="nw")
        waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"4"))
        waiting_time.pack(anchor="n", fill=tk.X)
    elif (time_11am <= t < time_22pm):
        l = Western_Store["Afternoon"][odd_even]
        for i in l:
            menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
            menu_label.pack(anchor="nw")
        waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"4"))
        waiting_time.pack(anchor="n", fill=tk.X)
    else:
        display_label = tk.Label(text="Sorry, we are closed now!", fg="red", bg="black",font="Calibri 22")
        display_label.pack(anchor='n', fill=tk.X)
    op_hours=tk.Button(root,text="Operating Hours",fg="red",font="Chalkboard 15", command=lambda: op(4))
    op_hours.pack(anchor="n", fill=tk.X)
    i4 = ImageTk.PhotoImage(Image.open("m4.jpg"))
    i4_label = tk.Label(root, image=i4, bg="black")
    i4_label.pack(anchor='n', fill='both')
    i4_label.image = i4
    back_button=tk.Button(root,text="Back",fg="red",font="Chalkboard 15", command=opening_screen)
    back_button.pack(side="bottom",fill=tk.X)
#menu for Long John Silver
def menu5(t,d,m):
    for widget in root.winfo_children():
        widget.forget()
    date_and_time_label = tk.Label(text=(str(t) + " " + str(d) + " " + m), fg="red", bg="black",font="Calibri 15")
    date_and_time_label.pack(anchor="n",fill=tk.X)
    if (m!="Saturday" and m!="Sunday"):
        if (time_8am <= t < time_11am):
            list1 = Long_John_Silvers["Breakfast"]
            for i in list1:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"5"))
            waiting_time.pack(anchor="n", fill=tk.X)
        elif (time_11am <= t < time_22pm):
            l = Long_John_Silvers["Afternoon"]
            for i in l:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"5"))
            waiting_time.pack(anchor="n", fill=tk.X)
        else:
            display_label = tk.Label(text="Sorry, we are closed now!", fg="red", bg="black", font="Calibri 22")
            display_label.pack(anchor='n', fill=tk.X)
    else:
        if (time_9am <= t < time_11am):
            list1 = Long_John_Silvers["Breakfast"]
            for i in list1:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"5"))
            waiting_time.pack(anchor="n", fill=tk.X)
        elif (time_11am <= t < time_19pm):
            l = Long_John_Silvers["Afternoon"]
            for i in l:
                menu_label = tk.Label(root, text=i, fg="red", bg="black",font="Calibri 15")
                menu_label.pack(anchor="nw")
            waiting_time = tk.Button(root, text="Average Waiting Time",fg="red",font="Chalkboard 15", command=lambda: avg_waiting_time(t,"5"))
            waiting_time.pack(anchor="n", fill=tk.X)
        else:
            display_label = tk.Label(text="Sorry, we are closed now!", fg="red", bg="black", font="Calibri 22")
            display_label.pack(anchor='n', fill=tk.X)
    op_hours=tk.Button(root,text="Operating Hours",fg="red",font="Chalkboard 15", command=lambda: op(5))
    op_hours.pack(anchor="n", fill=tk.X)
    i5 = ImageTk.PhotoImage(Image.open("m5.jpg"))
    i5_label = tk.Label(root, image=i5, bg="black")
    i5_label.pack(anchor='n', fill='both')
    i5_label.image = i5
    back_button=tk.Button(root,text="Back",fg="red",font="Chalkboard 15", command=opening_screen)
    back_button.pack(side="bottom",fill=tk.X)
#returns average time
def convert(wt):
    hr=wt//60
    m=wt%60
    if(hr==1):
        out=str(hr)+" hour and "+str(m)+" minutes."
    elif(m==0 and hr==1):
        out=str(hr)+" hour."
    elif(m==0):
        out=str(hr)+" hours."
    elif(hr==0 and m!=1):
        out=str(m)+" minutes"
    elif(hr==0 and m==1):
        out=str(m)+" minute"
    else:
        out=str(hr)+" hours and "+str(m)+" minutes."
    return out
def avg_waiting_time(t,i):
    people=simpledialog.askinteger("Waiting time", "Enter number of people",minvalue=1)
    q=random.randint(0,6)
    waiting_time=0
    if(people!= None):
        if (time_8am <= t < time_11am):
            waiting_time=people*wt_store_dict[i][0][q]
        elif (time_11am <= t < time_17pm):
            waiting_time=people*wt_store_dict[i][1][q]
        elif (time_17pm <= t < time_22pm):
            waiting_time=people*wt_store_dict[i][2][q]
        output=convert(waiting_time)
        messagebox.showinfo("Waiting time", output)
def op(i):
    if(i==1 or i==2 or i==5):
        f=open("Mcdonald's.txt","r")
        messagebox.showinfo("Operating Hours", f.read())
    else:
        f = open("Western Store.txt", "r")
        messagebox.showinfo("Operating Hours", f.read())
#displays menus according to date and time chosen in the second feature
def menus(t,d,m):
    for widget in root.winfo_children():
        widget.forget()
    date_time=("Your choice: "+ str(d)+" "+str(m)+" "+str(t))
    d_label=tk.Label(root,text=date_time,fg="red",font="Calibri 15",bg="black")
    d_label.pack(anchor="n",fill=tk.X)
    w1 = tk.Label(root, text="Choose a store to view menu", fg="red", font="Callibiri 15", bg="black")
    w1.pack(anchor="n", fill=tk.X)
    if(m=='Sunday' or m=='Saturday'):
        m1=tk.Button(root, text="1.McDonald's",fg="red",font="Chalkboard 15",command=lambda: menu1(t,d,m))
        m1.pack(anchor="n",fill=tk.X)
        m2=tk.Button(root, text="2.KFC",fg="red",font="Chalkboard 15", command=lambda: menu2(t,d,m))
        m2.pack(anchor="n",fill=tk.X)
        m3=tk.Button(root,text="3.Long John Silver's",fg="red",font="Chalkboard 15", command=lambda: menu5(t,d,m))
        m3.pack(anchor="n",fill=tk.X)
        img1 = ImageTk.PhotoImage(Image.open("mcd logo.jpg"))
        img1_label = tk.Label(root, image=img1, bg="black")
        img1_label.pack(anchor="n")
        img1_label.image = img1
        img2 = ImageTk.PhotoImage(Image.open("kfc_logo.jpg"))
        img2_label = tk.Label(root, image=img2, bg="black")
        img2_label.pack(anchor="n")
        img2_label.image = img2
        img3 = ImageTk.PhotoImage(Image.open("ljs_logo.jpg"))
        img3_label = tk.Label(root, image=img3, bg="black")
        img3_label.pack(anchor="n")
        img3_label.image = img3
    else:
        m1=tk.Button(root, text="1.Mcdonald's",fg="red",font="Chalkboard 13",command=lambda: menu1(t,d,m))
        m1.pack(anchor="n", fill=tk.X)
        m2=tk.Button(root, text="2.KFC",fg="red",font="Chalkboard 13",command=lambda: menu2(t,d,m))
        m2.pack(anchor="n",fill=tk.X)
        m3=tk.Button(root, text="3.Chinese Delight",fg="red",font="Chalkboard 13", command=lambda: menu3(t,d,m))
        m3.pack(anchor="n",fill=tk.X)
        m4=tk.Button(root, text="4.Western Store",fg="red",font="Chalkboard 13",command=lambda: menu4(t,d,m))
        m4.pack(anchor="n",fill=tk.X)
        m5=tk.Button(root, text="5.Long John Silver's",fg="red",font="Chalkboard 13",command=lambda: menu5(t,d,m))
        m5.pack(anchor="n",fill=tk.X)
        img1 = ImageTk.PhotoImage(Image.open("s1.jpg"))
        img1_label = tk.Label(root, image=img1, bg="black")
        img1_label.pack(anchor="n")
        img1_label.image = img1
        img2 = ImageTk.PhotoImage(Image.open("s2.jpg"))
        img2_label = tk.Label(root, image=img2, bg="black")
        img2_label.pack(anchor="n")
        img2_label.image = img2
        img3 = ImageTk.PhotoImage(Image.open("s3.jpg"))
        img3_label = tk.Label(root, image=img3, bg="black")
        img3_label.pack(anchor="n")
        img3_label.image = img3
        img4 = ImageTk.PhotoImage(Image.open("s4.jpg"))
        img4_label = tk.Label(root, image=img4, bg="black")
        img4_label.pack(anchor="n")
        img4_label.image = img4
    back_button=tk.Button(root,text="Back",fg="red",font="Chalkboard 15",command=opening_screen)
    back_button.pack(side="bottom",fill=tk.X)
#to get time input from user
def time_func(d, m):
    for widget in root.winfo_children():
        widget.forget()
    l1 = tk.Label(root, text="Enter hours:", fg="red", bg="black", font="Calibri 20")
    l1.pack(anchor="nw")
    hr_entry = tk.Entry(root)
    hr_entry.pack(anchor="nw")
    l2 = tk.Label(root, text="Enter minutes:", fg="red", bg="black", font="Calibri 20")
    l2.pack(anchor="nw")
    min_entry = tk.Entry(root)
    min_entry.pack(anchor="nw")
#checks if input entered is correct or not
    def check_inp():
            try:
                t = hr_entry.get() + min_entry.get()
                x = int(hr_entry.get())
                y = int(min_entry.get())
                if not (0 <= (x) <= 23 and 0 <= (y) <= 60):
                    messagebox.showerror("Error", "Wrong input.Please try again.")
                    time_func(d, m)
                else:
                    t1 = datetime.datetime.strptime(t, '%H%M').time()
                    menus(t1,d,m)
            except:
                messagebox.showerror("Error", "Wrong input.Please try again.")
                time_func(d, m)
    back_button = tk.Button(root, text="Back", fg="red", font="Chalkboard 15", command=opening_screen)
    back_button.pack(side="bottom", fill=tk.X)
    continue_button = tk.Button(root, text="Continue",fg="red",font="Chalkboard 15", command=check_inp)
    continue_button.pack(side="bottom",fill=tk.X)
    ti = ImageTk.PhotoImage(Image.open("t1.jpg"))
    ti_label = tk.Label(root, image=ti, bg="black")
    ti_label.pack(side="bottom")
    ti_label.image = ti
#gets input of date from the user using tkcalendar
def date_func():
    def print_sel():
        for widget in root.winfo_children():
            widget.forget()
        l=tk.Label(root, text="Date chosen: " + str(ent.selection_get()),fg='red',bg="black",font="Calibri 22")
        l.pack(anchor="n",fill=tk.X)
        user_date=ent.selection_get()
        user_day=weekday[user_date.weekday()]
        di = ImageTk.PhotoImage(Image.open("t.jpg"))
        di_label = tk.Label(root, image=di, bg="black")
        di_label.pack(anchor="n",fill="both",expand="yes")
        di_label.image = di
        back_button = tk.Button(root, text="Back",font="Chalkboard 15",fg="red", command=opening_screen)
        back_button.pack(side="bottom", fill=tk.X)
        time_button=tk.Button(root, text="Choose time",font="Chalkboard 15",fg="red", command=lambda: time_func(user_date,user_day))
        time_button.pack(side="bottom",fill=tk.X)
    for widget in root.winfo_children():
        widget.forget()
    ent = tkcalendar.Calendar(root,font="Comic 20",selectmode="day",year=2019,month=10,day=28,foreground="red",bg="black", background="blue",selectforeground="red")
    ent.pack(side="top",expand=True,fill=tk.BOTH)
    ok_button=tk.Button(root,text="OK",fg="red",font="Chalkboard 16",highlightbackground="black", command=print_sel)
    ok_button.pack(fill=tk.X)
    back_button=tk.Button(root,text="Back",fg="red",font="Chalkboard 16",highlightbackground="black",command=opening_screen)
    back_button.pack(fill=tk.X)
def other_day_stores():
    for widget in root.winfo_children():
        widget.forget()
    choose_date=tk.Button(root,text="Choose Date",fg="red",font="Chalkboard 18", command=date_func)
    choose_date.pack(side="top",fill=tk.X)
    di = ImageTk.PhotoImage(Image.open("d.gif"))
    di_label = tk.Label(root, image=di, bg="black")
    di_label.pack(anchor="n", fill="both", expand="yes")
    di_label.image = di
    back_button=tk.Button(root,text="Back",fg="red",font="Chalkboard 18",command=opening_screen)
    back_button.pack(side="bottom",fill=tk.X)
#closing the window when exit button is clicked
def exit():
    root.destroy()
#displays the content when the program is run
def opening_screen():
    for widget in root.winfo_children():
        widget.forget()
    img=ImageTk.PhotoImage(Image.open("2.png"))
    open_message= "Welcome to North Spine Canteen!"
    open_message_label= tk.Label(root, font='Calibri 25', fg="red", bg="black", text=open_message)
    open_message_label.pack(anchor="n",fill=tk.X)
    option1_button=tk.Button(root, text="View today's stores", font="Chalkboard 15", fg="red", background='blue', command=today_stores)
    option1_button.pack(anchor="n",fill=tk.X)
    option2_button=tk.Button(root, text="View stores on other date",font="Chalkboard 15", fg="red",bg='blue',command=other_day_stores)
    option2_button.pack(anchor="n",fill=tk.X)
    image_label=tk.Label(root,image=img,bg="black")
    image_label.pack(anchor="n",fill="both",expand="yes")
    image_label.image=img
    option3_button=tk.Button(root, text="Exit",font="Chalkboard 15", fg="red", command=exit)
    option3_button.pack(side="bottom",fill=tk.X)
opening_screen()
root.mainloop()