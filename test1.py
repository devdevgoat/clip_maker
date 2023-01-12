#%%
from operator import indexOf
from moviepy.video.io.VideoFileClip import VideoFileClip
import pysrt
from datetime import datetime
import glob, os

title = 'dbzk51_test'
# absolute path to search all text files inside a specific folder
path = r'D:\Code\Youtube\clip_maker\source\*.mkv'
outPath = path.replace('source\*.mkv',f'clips\{title}\\')
files = glob.glob(path)

def tm2sec(timestring):
    pt = datetime.strptime(timestring,'%H:%M:%S,%f')
    total_seconds = pt.second + pt.minute*60 + pt.hour*3600
    return total_seconds

for f in files:
    fileName = os.path.basename(f)
    filenameNoExt = os.path.splitext(fileName)[0]
    fileDir = f.replace(f"\{fileName}",'')
    outDir = fileDir.replace('source','clips')
    subs = pysrt.open(f'{fileDir}\{filenameNoExt}.srt')
    videoIn = f
    for sub in subs:
        if "Edited at https://" in sub.text: continue
        wordCount = len(sub.text.split(' '))
        clipStart = tm2sec(str(sub.start))
        clipEnd = tm2sec(str(sub.end))
        if clipStart == clipEnd: continue
        videoOut = str(f"{outDir}\{title}\{title}_{clipStart}sec_{wordCount}words.mp4")
        print(f"Generating Clip->{clipStart}-{clipEnd}{videoOut}")
        with VideoFileClip(videoIn) as video:
            new = video.subclip(clipStart, clipEnd)
            new.write_videofile(videoOut)

#%%



#%%