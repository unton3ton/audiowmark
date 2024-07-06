import os
from glob import glob

# container = '0a0b46ae_nohash_0.wav'

# fullcontainer = '0a0b46ae_nohash_0wm.wav'


# videocontainer = 'nifracut.mp4' # 'in.avi'

# fullvideocontainer = 'nifracutout.mp4' # 'out.avi'


watermark = '0123456789abcdef0011223344556677'


# os.system(f"audiowmark add {container} {fullcontainer} {watermark}")  
# # print('\n\n')
# # os.system(f"videowmark add {videocontainer} {fullvideocontainer} {watermark}")



filenames = glob("audiowm/*.wav")
for container in filenames:
	os.system(f"audiowmark add {container} audiowatermark/{container[8:]} {watermark}")