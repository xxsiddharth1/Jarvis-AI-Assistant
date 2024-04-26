import tkinter as tk
import cv2
from PIL import Image, ImageTk
import jarvis
import threading

class JarvisGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Jarvis AI Assistant")
        self.master.geometry("800x600")

        self.video_label = tk.Label(self.master)
        self.video_label.pack()

        self.video_path = "Video.mp4"  # replace with your video file path
        self.video_cap = cv2.VideoCapture(self.video_path)
        self.video_playing = False

        self.start_button = tk.Button(self.master, text="Start Jarvis", command=self.start_jarvis)
        self.start_button.pack()

        self.play_video()

    def play_video(self):
        if self.video_cap.isOpened():
            ret, frame = self.video_cap.read()
            if ret:
                cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2_im)
                img_tk = ImageTk.PhotoImage(image=img)
                self.video_label.config(image=img_tk)
                self.video_label.image = img_tk
                self.master.after(1, self.play_video)
            else:
                self.video_cap.release()
        else:
            self.video_cap.release()

    def start_jarvis(self):
        threading.Thread(target=jarvis.main).start()

root = tk.Tk()
my_gui = JarvisGUI(root)
root.mainloop()