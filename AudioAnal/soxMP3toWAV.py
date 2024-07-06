import os
from glob import glob


filenames = glob("*.mp3") # audiowm


# i = 1
# for filename in filenames:
#         try:
#             os.rename(filename, str(i) + ".mp3")
#             i += 1 
#         except FileExistsError:
#             pass


for audio in filenames:
	os.system(f"sox {audio} -r 44.1k -c 1 -b 16 {audio[:-4]}.wav")
	os.remove(audio)

