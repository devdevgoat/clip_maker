# %%
from operator import indexOf
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
videoIn = "D:\Anime\Dragonball Z Kai Season 1-4 [720p x264 AC3 Dual Audio ENG Subs]\Dragonball Z Kai 06 The End of Snake Way! King Kai's Bizarre Test!.mkv"
minStart = 8
codename = 'dbzk'
epNo = '06'
lengthSec = 30


clipStart = minStart*60
clipEnd = clipStart+lengthSec


fileName = os.path.basename(videoIn)
filenameNoExt = os.path.splitext(fileName)[0]
fileDir = videoIn.replace(f"\{fileName}",'')
outName = f"{codename + epNo}_{clipStart}sec_{lengthSec}sec.mp4"
outDir = f'E:\Clips\{codename}'

outDir2 = 'C:\\Users\\russe\\Creative Cloud Files\\Clips'
with VideoFileClip(videoIn) as video:
    new = video.subclip(clipStart, clipEnd)
    new.write_videofile(f'{outDir}\{outName}')
    new.write_videofile(f'{outDir2}\{outName}')


# %
# %%
