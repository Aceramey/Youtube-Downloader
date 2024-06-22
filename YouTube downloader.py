import os
import platform

vidFormats = ["mp4", "webm", "mov", "mkv"]
audFormats = ["mp3", "ogg", "wav"]
#remove these maybe? ^^^

try:
    import yt_dlp
except ImportError:
    if platform.system() == "Windows":
        print("yt-dlp not found, installing it for you :)")
        os.system("cmd /c pip install yt-dlp")
    elif platform.system() == "Linux":
        print("yt-dlp is not installed, either use a venv, or install it with pip using the --break-system-packages flag")

if os.path.exists(os.getcwd() + "\\" + "downloaded") == False and platform.system() == "Windows":
    os.system("cmd /c mkdir \"{0}\"".format(os.getcwd() + "\\downloaded"))
    os.system("cmd /c mkdir \"{0}\"".format(os.getcwd() + "\\downloaded\\Audio"))
    os.system("cmd /c mkdir \"{0}\"".format(os.getcwd() + "\\downloaded\\Video"))
elif os.path.exists(os.getcwd() + "/" + "downloaded") == False and platform.system() == "Linux":
    os.system("mkdir \"{0}\"".format(os.getcwd() + "/downloaded"))
    os.system("mkdir \"{0}\"".format(os.getcwd() + "/downloaded/Audio"))
    os.system("mkdir \"{0}\"".format(os.getcwd() + "/downloaded/Video"))


def download(format, playlist):
    vid = ""
    if platform.system() == "Windows":
        command = "cmd /c py -m yt_dlp"
    elif platform.system() == "Linux":
        command = "python3 -m yt_dlp"
    while vid == "":
        if playlist == True:
            vid = input("Enter link to playlist, or link to video in the playlist: ")
        else:
            vid = input("Enter link to {0}: ".format(format))
        if "youtube.com" in vid or "youtu.be" in vid:
            if playlist == False:
                match format:
                    case "video":
                        command += " --no-playlist -P \"{0}\\downloaded\\Video\" \"{1}\"".format(os.getcwd(), vid)
                    case "audio":
                        command += " --no-playlist --audio-format mp3 -x -P \"{0}\\downloaded\\Audio\" \"{1}\"".format(os.getcwd(), vid)
            else:
                match format:
                    case "video":
                        command += " --yes-playlist -P \"{0}\\downloaded\\Video\" \"{1}\"".format(os.getcwd(), vid)
                    case "audio":
                        command += " --yes-playlist --audio-format mp3 -x -P \"{0}\\downloaded\\Audio\" \"{1}\"".format(os.getcwd(), vid)
            if platform.system() == "Linux":
                command = command.replace("\\", "/")
            os.system(command)
            
        else:
            print("Invalid link, try again")
            vid = ""
    

def menu():
    choice = ""
    while choice not in ["1", "2", "3"]:
        print("Download options:")
        print("1. Video")
        print("2. Audio")
        print("3. Playlist")
        choice = input(": ")
        match choice:
            case "1":
                download("video", False)
            case "2":
                download("audio", False)
            case "3":
                format = ""
                while format == "":
                    format = input("Would you like to download audio or video? ")
                    if format.lower() not in ["a", "audio", "v", "video"]:
                        print("Invalid choice, try again")
                        format = ""
                if format.lower() == "a" or format.lower() == "audio":
                    download("audio", True)
                elif format.lower() == "v" or format.lower() == "video":
                    download("video", True)
            case _:
                print("Please choose one of the listed options\n")

menu()