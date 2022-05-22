# IMPORTING NECESSARY LIBARIES
from tkinter import *
import tkinter as tk
from pytube import YouTube
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog

#CREATING FUNCTIONS
def Browse():
    download_Directory = filedialog.askdirectory(
	initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_Directory)



def Download():
    youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(youtube_link)

    video = getVideo.streams.get_highest_resolution()
    video.download(download_Folder)
    
    # DISPLAYING THE MESSAGE
    messagebox.showinfo("SUCCESSFULLY",
						"DOWNLOADED AND SAVED IN\n"
						+ download_Folder)




# INITIALIZING WINDOW
window = Tk()
window.title("Youtube Video Downloader")
window.geometry("810x350")
window.resizable(False,False)
window.config(bg="#168ef0")

# CREATING LOGO
logo_img = Image.open("logo/logo.png")
resized = logo_img.resize((170, 91), Image.ANTIALIAS)
logo =ImageTk.PhotoImage(resized)

# CREATING LABELS
label1 = Label(window, image=logo, bg='#168ef0').place(x=20, y= 20)
label2 = Label(window, text='Youtube Video Downloader', font=("Koulen", 20, "bold"), bg= "#168ef0" ,fg= "white").place(x=210, y=40)
label3 = Label(window, text="YouTube link :", font=("open sans", 16),bg="#168ef0",fg= "white").place(x=45, y=180)
label4 = Label(window, text="Destination :", font=("open sans", 16),bg="#168ef0",fg= "white").place(x=45, y=233)

#CREATING VARIABLES
video_Link = StringVar()
download_Path = StringVar()

Link_text = Entry(window, textvariable= video_Link, width=45,).place(x=230, y= 183)
destination = Entry(window,textvariable=download_Path, width=35).place(x=265,y=235)


# CREATING BUTTONS
button1 = Button(window, text="Download Now",command=Download, width=11,).place(x=625, y=183)
button2 = Button(window, text="Safe At",command=Browse, width=11,).place(x=625, y=235)


window.mainloop()