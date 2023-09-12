from typing import Any
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View
from pytube import Playlist,YouTube
from django.http import HttpResponse

def base(request):

    return render(request,"base.html")


def playlist(request):

        if request.POST.get('playlist-link'):
            global link
            link = request.POST.get('url')
            if 'www.youtube.com/playlist' in link:
                global yt
                yt = Playlist(link)
                platlist_title = yt.title
                playlist_owner = yt.owner
                playlist_thumbnail = YouTube(yt.video_urls[0]).thumbnail_url
                total_audio_size = 0
                qual,stream = [],[]
                for vid in YouTube(yt[0]).streams.filter(progressive=True):
                    qual.append(vid.resolution)
                    stream.append(vid)
                for vid in yt:
                    video = YouTube(vid)
                    total_audio_size += video.streams.get_audio_only().filesize_mb

                total_audio_size = round(total_audio_size)
                count = len(yt)

                data = {    'title' : platlist_title,
                            'thumbnail_url' : playlist_thumbnail,
                            'channel' : playlist_owner,
                            'qual' : qual,
                            'stream' : stream,
                            'count' : count,
                            'audio_size' : total_audio_size,
                        }

                global context
                context = {
                    'data' : data,
                }
                return render(request,'download.html',context)
            else:
                context = {
                    'message' : 'Invalid link. Please enter correct youtube playlist link'
                }
                return render(request,'message.html',context)
            
        elif request.POST.get('download'):
            try:
                if request.POST['download'] == 'audio':
                    for aud in Playlist(link):
                        try:
                            audio = YouTube(aud)
                            audio_dwn = audio.streams.get_audio_only()
                            audio_dwn.download(output_path='Downloads')
                        except Exception:
                            context = {
                                'message' : 'Sorry, something went wrong... please try again'
                            }
                            return render(request,'message.html',context)
                    return render(request,'download.html',context)
                
                else:
                    for i,vid in enumerate(Playlist(link)):
                        try:
                            video = YouTube(vid)
                            stream = [x for x in video.streams.filter(progressive=True)]
                            video_qual = video.streams[int(request.POST['download']) - 1]
                            title = video.title.replace('|','').replace('\\','').replace('?','').replace('/','').replace('>','').replace('<','').replace('"','').replace('*','').replace(':','')
                            video_qual.download(output_path='Downloads',filename=f'Video {i+1} {title} {video_qual.resolution}.mp4')
                        
                        except Exception:
                            pass

                    return render(request,'download.html',context)
                
            except Exception:
                context = {
                    'message' : 'Sorry, something went wrong... please try again'
                    }
                return render(request,'message.html',context)

        else:
            return render(request,"playlist_link.html")



def video(request):

        if request.POST.get('video-link'):
            global link
            link = request.POST['url']
            if 'www.youtube.com/watch' in link:
                yt = YouTube(link)
                thumbnail_url = yt.thumbnail_url
                title = yt.title
                channel = yt.author
                audio_size = yt.streams.get_audio_only().filesize_mb
                qual,stream,size = [],[],[]
                for vid in yt.streams.filter(progressive=True):
                    # qual.append(vid.resolution)
                    stream.append(vid)
                    # size.append(vid.filesize_mb)

                audio_size = round(audio_size)
                data = {    'title' : title,
                            'thumbnail_url' : thumbnail_url,
                            'channel' : channel,
                            # 'qual' : qual,
                            'stream' : stream,
                            # 'size' : size,
                            'audio_size' : audio_size,
                        }
                global context
                context = {
                            'data' : data,
                        }
                return render(request,'download.html',context)
            
            else:
                context = {
                    'message' : 'Invalid link. Please enter correct youtube video link'
                }
                return render(request,'message.html',context)
        
        elif request.POST.get('download'):

            try:
                if request.POST['download'] == 'audio':
                    try:
                        audio = YouTube(link)
                        audio_dwn = audio.streams.get_audio_only()
                        audio_dwn.download(output_path='Downloads')
                    except Exception:
                        context = {
                                'message' : 'Sorry, something went wrong... please try again'
                            }
                    return render(request,'download.html',context)
                
                else:
                    try:
                        video = YouTube(link)
                        # stream = [x for x in video.streams.filter(progressive=True)]
                        video_qual = video.streams[int(request.POST['download']) - 1]
                        video_qual.download(output_path='Downloads',filename=f'{video.title} {video_qual.resolution}.mp4')
                    except Exception:
                        context = {
                                'message' : 'Sorry, something went wrong... please try again'
                            }
                        return render(request,'message.html',context)

                    return render(request,'download.html',context)
                
            except Exception:
                context = {
                    'message' : 'Sorry, something went wrong... please try again'
                    }
                return render(request,'message.html',context)

        else:
            return render(request,'video_link.html',)
