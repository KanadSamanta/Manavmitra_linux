import os
import sys

from browser_control import browser_control
from youtube_video_serach import video_search

with open(os.path.join(sys.path[0], "inquest_youtube.txt"), 'r') as inquest_read:
    inquest = inquest_read.read().replace("play", "")
    inquest_read.close()
print(inquest)
url = video_search(inquest)['url']
print(url)
if video_search(inquest)["duration"] is None:
    browser_control(url)
else:
    browser_control(url, time_to_run=video_search(inquest)["duration"])
