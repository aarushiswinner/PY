from pytube import YouTube

link=input('Enter the link of the video: ')

video=YouTube(link)

video.streams.get_by_itag(18).download()

print('done!')