import tkinter as tk
import os
import subprocess

#TODO if file exists we have a problem, works if file not downloaded
#TODO FILE ALREADY DOWNLOADED obsolete, because files get moved out of directory

class Interface:
    def __init__(self):
        #Path to current file
        self.current_directory = os.getcwd()
        self.music_destination = os.path.dirname(self.current_directory)
        print(self.music_destination)
        #Tkinter setup
        root = tk.Tk()
        root.title("Antons Music Man")

        #Textfield to copy the link into
        self.text_input = tk.Entry(root)
        self.text_input.pack()

        #Button to start the download
        submit_button = tk.Button(root, text="Submit", command=self.__process_input)
        submit_button.pack()

        root.mainloop()

    #Executed if the button is clicked
    #
    def __process_input(self):
        #downloads the youtube video as mp3 
        url = self.text_input.get()
        print("Anton wants to download: {}".format(url))
        output = subprocess.check_output(self.__download_audio(url), shell=True, text=True)
        #print(output)
        
        #find the name of the downloaded file
        filename = None
        for line in output.split("\n"):
            if line.startswith("[ExtractAudio]"):
                filename = self.__filename(line)
                print("===> "+ filename + "<===")
        
        #if the filename was found, open the finder
        if filename is not None:
            self.__move_file(filename)
            self.__show_in_finder(self.music_destination +"/"+filename)
        else:
            print("Filename not found in finder")

    #finds the filename in a given string
    def __filename(self, line):
        x = line.split()

        file_exists = None
        if line.find("[ExtractAudio] Not converting audio") != -1:
            print("*** FILE ALREADY DOWNLOADED ***")
            file_exists = True
        elif line.find("[ExtractAudio] Destination: ") != -1:
            print("*** FILE NOT DOWNLOADED YET ***")
            file_exists = False
        
        start = 4 if file_exists else 2
        end = None
        
        for i in range(0,len(x)):
            if x[i].find(".mp3") != -1:
                end = i+1
                break
            i += 1

        result_string = ""
        for i in x[start:end]:
            result_string += i+" "
            
        return result_string[:-1] if not file_exists else result_string[:-2]

    # gets the command to download the file
    def __download_audio(self, url):
        return "yt-dlp -x --audio-format mp3 --audio-quality 0 {}".format(url)

    #gets the command to show the 
    def __show_in_finder(self,path):
        subprocess.call(["open", "-R", path])

    def __move_file(self, filename):
        os.rename(self.current_directory+"/"+filename, self.music_destination+"/"+filename)
    
if __name__ == "__main__":
    Interface()
