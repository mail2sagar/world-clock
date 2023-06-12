from tkinter import *
from PIL import Image , ImageTk
from datetime import datetime
import pytz
import time

root = Tk()

root.title("World Clock")
root.geometry("600x450")

clock_img = ImageTk.PhotoImage(Image.open("clock.jpg"))


india_label = Label(root,text="India")

india_clock = Label(root)
india_clock['Image'] = clock_img

india_time = Label(root)


india_label.place(relx=0.2,rely=0.05,anchor=CENTER)

india_clock.place(relx=0.2,rely=0.35,anchor=CENTER)

india_time.place(relx=0.2,rely=0.65,anchor=CENTER)



usa_label = Label(root,text="USA")

usa_clock = Label(root)
usa_clock['Image'] = clock_img

usa_time = Label(root)


usa_label.place(relx=0.7,rely=0.05,anchor=CENTER)

usa_clock.place(relx=0.7,rely=0.35,anchor=CENTER)

usa_time.place(relx=0.7,rely=0.65,anchor=CENTER)

class India():
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time['text'] = "Time: "+current_time
        india_time.after(200,self.times)


class USA():
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        usa_time['text'] = "Time: "+current_time
        usa_time.after(200,self.times)

object_india = India()

object_usa = USA()


usa_btn = Button(root,text="Show Time",command=object_usa.times)

india_btn = Button(root,text="Show Time",command=object_india.times)


usa_btn.place(relx=0.7,rely=0.8,anchor=CENTER)

india_btn.place(relx=0.2,rely=0.8,anchor=CENTER)

root.mainloop()