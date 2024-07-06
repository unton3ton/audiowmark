import os
from glob import glob

# fullcontainer = 'audiowatermark/armin-van-buuren-old-skool.mp3'

# # fullvideocontainer = 'nifracutout.mp4' # 'out.avi'

# os.system(f"audiowmark get {fullcontainer}")  
# print('\n\n')
# os.system(f"videowmark get {fullvideocontainer}")

# listcontainers = ['1after.mp3', '2after.mp3', '1after.ogg'] #['1before.mp3', '2before.mp3', '1ogg_before.ogg']

# for fullcontainer in listcontainers:
# 	print(f"{fullcontainer}:")
# 	os.system(f"audiowmark get {fullcontainer}")
# 	print('\n\n')

filenames = glob("audiowatermark/*.wav")
for container in filenames:
	os.system(f"audiowmark get {container}")