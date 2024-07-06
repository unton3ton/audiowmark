# conda activate AUDIOLIBROSA
# https://librosa.org/doc/main/generated/librosa.feature.mfcc.html

# pip install -u librosa

"""
Сравнение двух аудиосообщений с использованием библиотеки Librosa

Librosa — библиотека, которая обеспечивает анализ и обработку звука.
Сравнение производится путем вычисления характеристик MFCC (Mel Frequency Cepstral Coefficients),
описывающих звуковую сигнатуру каждого аудио.

Важные замечания:
— Для точного сравнения аудиозаписей они должны иметь одинаковую продолжительность
и аналогичные условия записи (громкость, уровень шума и т.д.).
— Возможно потребуется дополнительная предварительная обработка, например, нормализация громкости.
"""

import librosa
# >>> librosa.__version__
# >>> '0.10.1'

audiofile1 = "1wmbeforetelegram.mp3" # '611.wav'
audiofile2 = "1wmaftertelegram.mp3" # '611wm.wav'

y1, sr1 = librosa.load(audiofile1)
y2, sr2 = librosa.load(audiofile2)

# вычисление временной и частотной характеристик
mfcc1 = librosa.feature.mfcc(y=y1, sr=sr1)
mfcc2 = librosa.feature.mfcc(y=y2, sr=sr2)

# # вычисление расстояний между характеристиками
# distance = librosa.core.dtln(mfcc1, mfcc2)
# print(f'Distance between audios is {distance}') 
# # >>> AttributeError: No librosa.core attribute dtln

# print(mfcc1, '\n', mfcc2)
# >>> [[-480.07306   -480.07306   -477.90524   ... -480.07306   -480.07306   -480.07306  ]
#     [   0.           0.           2.9035292 ...    0.           0.     0.       ]
#     [   0.           0.           2.4379063 ...    0.           0.     0.       ]
#     ...
#     [   0.           0.           1.2641258 ...    0.           0.     0.       ]
#     [   0.           0.           1.9532175 ...    0.           0.     0.       ]
#     [   0.           0.           2.4714384 ...    0.           0.     0.       ]]

# print(type(mfcc2)) # <class 'numpy.ndarray'>

dist = mfcc1 - mfcc2

# print(dist := mfcc1 - mfcc2)
# >>> [[-3.0517578e-05 -3.0517578e-05 -1.8005371e-03 ... -3.0517578e-05  -3.0517578e-05 -3.0517578e-05]
#     [ 0.0000000e+00  0.0000000e+00 -1.6489029e-03 ...  0.0000000e+00   0.0000000e+00  0.0000000e+00]
#     [ 0.0000000e+00  0.0000000e+00  7.3051453e-04 ...  0.0000000e+00   0.0000000e+00  0.0000000e+00]
#     ...
#     [ 0.0000000e+00  0.0000000e+00  6.6807270e-03 ...  0.0000000e+00   0.0000000e+00  0.0000000e+00]
#     [ 0.0000000e+00  0.0000000e+00  5.4188967e-03 ...  0.0000000e+00   0.0000000e+00  0.0000000e+00]
#     [ 0.0000000e+00  0.0000000e+00  2.7470589e-03 ...  0.0000000e+00   0.0000000e+00  0.0000000e+00]]

# print((dist ** 2).sum(axis=0) ** 0.5)
# >>> [3.0517578e-05 3.0517578e-05 2.5206553e-02 ... 3.0517578e-05 3.0517578e-05  3.0517578e-05]
# print(f'lenght = {len((dist ** 2).sum(axis=0) ** 0.5)}') # 4529

print(f'Distance between audios {audiofile1} & {audiofile2} is {((dist ** 2).sum(axis=0) ** 0.5).sum()}') 
# Distance between audios 1.ogg & 1.wav is 74475.171875
# Distance between audios 1.mp3 & 1wmbeforetelegram.mp3 is 67688.578125
# Distance between audios 611.wav & 611wm.wav is 7894.84228515625
# Distance between audios 1wmbeforetelegram.mp3 & 1wmaftertelegram.mp3 is 0.0