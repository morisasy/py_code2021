from pytube import YouTube
url = input("Enter your link").strip()
print("Downloading ... ")

try:
	if len(url):
	    YouTube(url).streams.first().download()
	    print(Video downloaded successfull)
    
except Exception as e:
  
   print("Exception occurred: {}".format(e))
