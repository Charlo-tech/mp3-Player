from tkinter import*
import os
from tkinter import filedialog
from pygame import mixer
class MusicPlayer:
    def __init__(self, window):
        window.geometry("500x200");window.title("Charles Mp3 Player");window.resizable(0,0);window.configure(bg='#000000');window.wm_attributes('-alpha', 0.8);window.iconbitmap('icon.ico')
        
        Load = Button(window, text = "Load", width=10, command=self.load, bg='#0bec1b', fg='#000000', font=("Times",20))

        Play = Button(window, text = "Play", width=10, command=self.play, bg='#0bec1b', fg='#000000', font=("Times",20))

        Pause = Button(window, text = "Pause", width=10, command=self.pause, bg='#0bec1b', fg='#000000', font=("Times",20))

        Stop = Button(window, text = "Stop", width=10, command=self.stop, bg='#0bec1b', fg='#000000', font=("Times",20))

        Load.place(x=10,y=20);Play.place(x=330,y=20);Pause.place(x=330,y=130);Stop.place(x=10,y=130)
        self.music_file=False
        self.playing_state=False   
            
    def load(self):
        self.music_file=filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state=False
    def stop(self):
        mixer.music.stop()
root=Tk()
app=MusicPlayer(root)
root.mainloop()