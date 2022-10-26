from pytube import YouTube, Search
import os
from youtubesearchpython import Search
from random import randint


def download_song(video_id, song_name):
    yt = YouTube(str(f'https://www.youtube.com/watch?v={video_id}'))
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download()

    base, ext = os.path.splitext(out_file)
    new_file = f'{song_name}.mp3'

    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")

    return str(new_file)


def find_video(name):

    allSearch = Search(f'песня {name}', limit = 3)
    allResults = allSearch.result().get('result')


    data = {}
    song_names = {}
    counter = 1

    for item in allResults:
        duration = item.get('duration')
        time = duration.replace(':', '.')
        
        try:
            if float(time) < 5.00:
                data[str(counter)] = item.get('id')
                song_names[str(counter)] = item.get('title')
                counter += 1
                # print(time)
            else:
                pass
        except:
            pass

    # for i in allResults:
    #     print(i.get('title'))

    # user_answer = int(input("enter number: "))
    # print(f'sond id: {data.get(user_answer)}')

    # start_download = download_song(video_id=data.get(user_answer))

    return data, song_names


def pring_song_message(list):
    nums = ['1', '2', '3']
    result_message = ''

    for song in nums:
        result_message += f'<b>{song}.</b> {list.get(song)}\n'

    return result_message
