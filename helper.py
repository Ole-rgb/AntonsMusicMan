import tkinter as tk
import os



class Interface:
    def __init__(self):
        root = tk.Tk()
        root.title("Antons Music Man")

        self.text_input = tk.Entry(root)
        self.text_input.pack()

        submit_button = tk.Button(root, text="Submit", command=self.process_input)
        submit_button.pack()

        root.mainloop()

    
    def process_input(self):
        url = self.text_input.get()
        #TODO sent URL to downloader
        print("Anton wants to download: {}".format(url))
        os.system(self.get_command(url))

    
    def get_command(self, url):
        print("DOWNLOADING")
        return "yt-dlp -x --audio-format mp3 --audio-quality 0 {}".format(url)

