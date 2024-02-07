from pytube import YouTube, Search
from pytube.cli import on_progress

def searchfunc():
    prompt1 = input("What video would you like to search?: ")
    s = Search(prompt1)

    for v in s.results:
        print(f"{v.title}\n{v.watch_url}\n{v.publish_date}\n{str(int(v.length/60)) + 'm ' + str(v.length%60) + 's'}\n")

def linkfunc(directory):
    prompt2 = input("What video would you like to download?: ")
    yt = YouTube(prompt2, on_progress_callback=on_progress)
    yd = yt.streams.get_highest_resolution()
    file_size = yd.filesize

    og_directory = '/Users/lione/Downloads/TestFolder'

    if directory != "None":
        og_directory = directory

    yd.download(output_path=og_directory)
    print("Download complete!")

def changeDirectory():
    prompt3 = input("Would you like to change the directory of your file? (Y/N): ")

    if prompt3 == "Y" or prompt3 == "y":
        prompt4 = input("Please type your desired directory!: ")
        linkfunc(prompt4)
    elif prompt3 == "N" or prompt3 == "n":
        linkfunc("None")


intro = input("Would you like to search for a video or directly input a link? (S/L): ")
if intro == "S" or intro == "s":
    searchfunc()
    changeDirectory()
elif intro == "L" or intro == "l":
    changeDirectory()

#C:\Users\lione\Downloads\ytDownloader.py
#https://youtube.com/watch?v=9Zj0JOHJR-s