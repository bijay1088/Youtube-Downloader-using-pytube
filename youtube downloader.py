import os
from pytube import YouTube


link = input("Enter your youtube link: ")



try:
    yt = YouTube(link)
except Exception as e:
    print("This video is unavailable.")

#location = input("Enter your download location: ")
location = os.getcwd()

AoV = input("\nWhat would you like to download?(1 or 2):\n1. Video\n2. Audio\n> ")

def video(yt):
    resolution = input("\nWhat resolution would you like to download in?\n1. 360p\n2. 720p\n3. 1080p\n> ")
    try:
        match resolution:
            case "1":
                print("Downloading.... Please Wait")
                yt.streams.get_by_itag(18).download()
                print("Download Complete.")
            case "2":
                print("Downloading.... Please Wait")
                yt.streams.get_by_itag(22).download()
                print("Download Complete.")
            case "3":
                print("Downloading.... Please Wait")
                yt.streams.get_by_itag(137).download()
                print("Download Complete.")
            case _:
                print("\nPlease select between 1 to 3 only.\n")
                video(yt)
    except AttributeError:
        print("\nThis quality is not available. Please choose another quality.")
        video(yt)

def audio(yt):
    ys = yt.streams.filter(only_audio=True)
    print("Downloading.... Please Wait")
    ys[0].download(location)
    print("Download Complete")



match AoV:
    case "1":
        video(yt)
    case "2":
        audio(yt)
    case _:
        print("Please select between 1 and 2 only.\n")

input()
