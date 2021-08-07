import tkinter as tk
from tkinter import *
import pyttsx3
import speech_recognition as sr


root = Tk()
root.title("Voice Calculator")
root.geometry("350x500")
root.minsize(350, 500)
root.maxsize(350, 500)
root.configure(bg='lightgrey')

canvaswidth = 350
canvasheight = 500
canvaswidget = Canvas(root, width=canvaswidth, height=canvasheight)


bg = PhotoImage(file='rain-6243559_1920.png')


canvaswidget.pack(fill='both', expand=True)
canvaswidget.create_image(0, 0, image=bg, anchor='nw')



####################################################



def takeCommand():
    # it take microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:#for this you have to install pipwin
        #and then "pipwin install pyaudio"
        print("Listening...")
        r.pause_threshold = 1  # it help to not complete it if user stop speaking
        # you can also control voice energy level by r.dynamic energy threshold
        r.energy_threshold = 150
        audio =r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        print(e,"please say again")
        return "None"
    return query

    
def calculate():
    canvaswidget.itemconfig(l, text='Listening...')
    query = takeCommand().lower()
    query = ''.join(query.split())
    if  query.isalpha() or 'one' in query :
        canvaswidget.itemconfig(c, text='Not valid Say Again')
    elif 'equalto' in query:
        try:
            query = query.replace('equalto','')
            canvaswidget.itemconfig(c, text=f'{query} = {eval(query)}')
        except Exception as e:
            canvaswidget.itemconfig(c, text='Not valid Say Again')
    else:
        canvaswidget.itemconfig(c, text=query)



c = canvaswidget.create_text(170,30,fill="blue",font="Times 20 italic bold",
                        text="Click button below to say")


button1 = Button(root, text="Say it", bg="blue",
                 fg="white", height=2, width=15,command=calculate)
button1.pack(pady=10)
button1_canvas = canvaswidget.create_window(120, 90,
                                            anchor="nw", window=button1)

label1 = Label(root, text="1.Say English words(one,two)")
label1.pack(pady=10)
label1_canvas = canvaswidget.create_window(95, 150,
                                           anchor="nw",
                                           window=label1)
label2 = Label(
    root, text="2.For operations say(plus,minus,multiply by and divide by")
label2.pack(pady=10)
label2_canvas = canvaswidget.create_window(35, 190,
                                           anchor="nw",
                                           window=label2)
label3 = Label(root, text="3.For results say(equals to)")
label3.pack(pady=10)
label3_canvas = canvaswidget.create_window(105, 230,
                                           anchor="nw",
                                           window=label3)



l = canvaswidget.create_text(170,340,fill="white",font="Times 20 italic bold",
                        text="")

root.mainloop()
