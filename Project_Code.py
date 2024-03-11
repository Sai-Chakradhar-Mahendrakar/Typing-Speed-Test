#importing Libraries
from tkinter import *
from random import randint

windows=Tk()
windows.title('Typing Speed Test')

windows.minsize(width='1200',height='800')
background = PhotoImage(file = "py1.png")

label1 = Label(windows,image = background)
label1.place(x = 0,y = 0)

running = False
seconds = 60

errors=0
tychar=1
char=0
read=0
str=''

def rectangle():
    canvas = Canvas(windows,width=1000,height=300)
    canvas.place(x=100,y=80)
    canvas.create_rectangle(0, 0, 1100, 400, fill="#edc7b7")
    
def calculator():
    global errors
    global tychar
    global char
    global accuracy
    global netwpm
    netwpm = char
    if read!=0:
        accuracy = (tychar/read)*100

def random_text_generate():
    rectangle()
    names=["We","I","They","He","She","Jack","Jim","Rose"]
    verbs=["is","was", "are", "were"]
    nouns=["reading","playing", "watching TV", "talking", "dancing", "speaking"]
    l=23          
    global str
    str=''
    for i in range(1,l+1):
        str+=names[randint(0,len(names)-1)]+" "+verbs[randint(0,len(verbs)-1)]+" "+nouns[randint(0,len(nouns)-1)]
        str+='. '
    global main_text
    main_text = Label(windows,text=str,font=('Times New Roman',20,'bold'),bg="#edc7b7",bd=0,foreground='#123c69',wraplength=950)
    main_text.place(x=140,y=150)
    
    global typch
    typch = Label(windows,text='Type: ',font=('Times New Roman',20,'bold'),bg="#edc7b7",bd=0,foreground='#123c69')
    typch.place(x=500,y=100)

    global typdis
    typdis = Label(windows,text=str[0], font=('Times New Roman','20','bold'),bg="#edc7b7")
    typdis.place(x=570,y=100)

    global lens
    lens =  len(str)

def write():
    if seconds<=60:
        global writeAble
        writeAble = True
        windows.bind('<Key>', keyPress)

def keyPress(event=None):
    global errors
    global tychar
    global char
    global spot
    global typdis
    global err_dis
    global read         
    global running
    global lens
    if spot == lens-1:
        main_text.configure(text=main_text.cget('text')[1:])
        timer.after_cancel(update_time)
        running = False
        global timeup
        timeup = Label(windows,text="Congratulations",font=('Times New Roman',50,'bold'),bg="#A0E4CB",bd=0,foreground='Red')
        timeup.place(x=350,y=200)
        typdis.config(text='Completed')
        return
    elif event.char == main_text.cget('text')[0] and seconds>=00 and seconds<60:
        main_text.configure(text=main_text.cget('text')[1:])
        tychar+=1
        spot+=1
        if str[spot]==' ' and spot!=lens:
            typdis.config(text='Space')
        else:
            typdis.config(text=main_text.cget('text')[0])
        if main_text.cget('text')[0]==' ':
            char+=1
        if (event.char>='a' and event.char<='z') or (event.char>='A' and event.char<='Z') or (event.char==' ') or (event.char==',') or (event.char=='.'):
            read+=1
    else:
        if ((event.char>='a' and event.char<='z') or (event.char>='A' and event.char<='Z') or (event.char==' ') or (event.char==',') or (event.char=='.')) and seconds>00 and seconds<60:
            errors+=1
            err_dis.config(text=errors)
            read+=1
    global accu_dis
    global speed_dis
    calculator()
    global accuracy
    global netwpm
    if read!=0:
        accu_dis.config(text="{:.2f} %".format(accuracy))
    speed_dis.config(text=f'{netwpm} WPM')

def start():
    global errors
    global tychar
    global running
    if not running:
        update()
        errors=0
        tychar=0
        running = True
        timer.config(foreground='black')

def reset():
    global running
    if running:
        timer.after_cancel(update_time)
        running = False
    global seconds
    seconds =60
    timer.config(text='60')
    timer.config(foreground='black')
    global errors
    errors=0
    err_dis.config(text=errors)
    global accuracy
    global netwpm
    accuracy=0
    netwpm=0
    global tychar
    tychar=0
    accu_dis.config(text='0.0 %')
    speed_dis.config(text='00 WPM')
    global read
    read = 0
    global char
    char=0
    global spot
    spot=0

def update():
    global seconds
    seconds -= 1
    if seconds == -1:
        global timeup
        timeup = Label(windows,text="Time's up",font=('Times New Roman',50,'bold'),bg="#A0E4CB",bd=0,foreground='Red')
        timeup.place(x=450,y=200)
        return
    elif seconds < 10:
        timer.config(foreground='red')
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    timer.config(text=seconds_string)
    global update_time
    update_time = timer.after(1000, update)

def start_type():
    for widgets in windows.winfo_children():
        widgets.destroy()

    windows.config(bg="#eee2dc")
    title = Label(text='TYPING SPEED TEST',font=('Rockwell Extra Bold',25,'bold'),bg="#eee2dc",foreground='#ac3b61')
    title.place(x=400,y=10)

    global timer
    timer = Label(windows,text='60', font=('Bree serif','20','bold'),bg="#eee2dc")
    timer.place(x=270,y=417)

    text1=Label(windows,text='Time: ',font=('Times New Roman',20,'bold'),bg="#eee2dc",bd=0,foreground='#123c69')
    text1.place(x=190,y=417)

    random_text_generate()

    start_btn = Button(windows,text='START',font=('Bree serif','10','bold'),bg='#ea3548',bd=0,fg='#fff',width=20,height=2,command=lambda:[start(),write()])
    start_btn.place(x=200,y=650)

    speed_tx = Label(windows,text='Speed: ',font=('Times New Roman',20,'bold'),bg="#eee2dc",bd=0,foreground='#123c69')
    speed_tx.place(x=440,y=417)

    global speed_dis
    speed_dis = Label(windows,text='00 WPM', font=('Bree serif','20','bold'),bg="#eee2dc")
    speed_dis.place(x=525,y=417)

    accu_tx = Label(windows,text='Accuracy: ',font=('Times New Roman',20,'bold'),bg="#eee2dc",bd=0,foreground='#123c69')
    accu_tx.place(x=800,y=417)

    global accu_dis
    accu_dis = Label(windows,text='0.0%', font=('Bree serif','20','bold'),bg="#eee2dc")
    accu_dis.place(x=930,y=417)

    global spot
    spot=0

    err_tx = Label(windows,text='Errors: ',font=('Times New Roman',20,'bold'),bg="#eee2dc",bd=0,foreground='#123c69')
    err_tx.place(x=480,y=480)

    global err_dis
    err_dis = Label(windows,text='0', font=('Bree serif','20','bold'),bg="#eee2dc")
    err_dis.place(x=580,y=480)

    reset_btn = Button( windows,text='RESET',font=('Bree serif','10','bold'),bg='#ea3548',bd=0,fg='#fff',width=20,height=2,command=lambda:[reset(),random_text_generate()])
    reset_btn.place(x=800,y=650)

start_img = PhotoImage(file='button_start.png')
button = Button(windows,image=start_img,bg='white',command=start_type)
button.place(x = 900,y=250)

windows.mainloop()
