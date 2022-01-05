from youtubesearchpython import VideosSearch
from youtubesearchpython import *


def video_search(taburl, limit=1):
    try:
        videosSearch = VideosSearch(taburl, limit=limit)

        ttu = videosSearch.result()['result'][limit - 1]['id']
        ttu_time = videosSearch.result()['result'][limit - 1]['duration']
        print(videosSearch.result()['result'][limit - 1]['title'])

        if ttu_time is None:

            while True:

                videosSearch = VideosSearch(taburl, limit=limit)
                print(videosSearch.result()['result'][limit - 1]['title'])
                if videosSearch.result()['result'][limit - 1]['duration'] is None:

                    limit = limit + 1
                    continue
                else:
                    ttu = videosSearch.result()['result'][limit - 1]['id']
                    ttu_time = videosSearch.result()['result'][limit - 1]['duration']
                    if len(ttu_time.split(":")) > 2:

                        ttu_time = ttu_time.split(":")
                        ttu_time_seconds = int(ttu_time[0]) * 60 * 60 + int(ttu_time[1]) * 60 + int(ttu_time[2])

                    else:
                        ttu_time = ttu_time.split(":")

                        ttu_time_seconds = int(ttu_time[0]) * 60 + int(ttu_time[1])
                    break

        elif len(ttu_time.split(":")) > 2:

            ttu_time = ttu_time.split(":")
            ttu_time_seconds = int(ttu_time[0]) * 60 * 60 + int(ttu_time[1]) * 60 + int(ttu_time[2])


        else:
            ttu_time = ttu_time.split(":")

            ttu_time_seconds = int(ttu_time[0]) * 60 + int(ttu_time[1])

        print(ttu_time_seconds)
        return {"id": ttu,
                "duration": ttu_time_seconds,
                "time": ttu_time,
                "url": "https://www.youtube.com/watch?v=" + ttu}
    except:
        from fast_youtube_search import search_youtube
        for i in range(len(search_youtube(taburl.split()))):
            try:
                return {"url": "https://www.youtube.com/watch?v=" + search_youtube(taburl.split())[i]['id'],
                        "duration": None}
                break
            except Exception:
                continue
