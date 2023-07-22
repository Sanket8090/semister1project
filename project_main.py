from pytube import YouTube
import instaloader
def instagram():
    ig=instaloader.Instaloader()
    db=input("Enter the instagram id:")
    ig.download_profile(db,profile_pic_only=True)



def Download(link):
    youtubeObject=YouTube(link)
    youtubeOBJECT=youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed succesfully")
link=input("Enter the youtube video URL: ")
Download(link)

choose=input("Enter 1 for instagram operators and 2 for youtube :")
if choose=="1":
    instagram()
else:
    link = input("Enter the youtube video URL: ")
    Download(link)