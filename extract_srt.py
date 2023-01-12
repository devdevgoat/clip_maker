#%%
from operator import index, indexOf
import os
import glob

# absolute path to search all text files inside a specific folder
path = r'D:\Code\Youtube\clip_maker\source\*.mkv'
files = glob.glob(path)
print(files)

for filename in files:
    filename = filename[:indexOf(filename,'.')]
    # should do a check for the codec type and not print when pgs
    cmd = f'ffmpeg -i "{filename}.mkv" -map 0:s:0 "{filename}.srt"'
    print(cmd)
    # os.system(f'cmd /c "{cmd}"')

# %%
