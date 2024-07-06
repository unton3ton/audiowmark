```bash
sox 1.mp3 -r 44.1k -c 1 -b 16 2.wav
```

Сравнение двух аудиосообщений с использованием библиотеки Librosa.  

Librosa — библиотека, которая обеспечивает анализ и обработку звука. Сравнение производится путем вычисления характеристик MFCC (Mel Frequency Cepstral Coefficients), описывающих звуковую сигнатуру каждого аудио.  

Важные замечания:  
— Для точного сравнения аудиозаписей они должны иметь одинаковую продолжительность и аналогичные условия записи (громкость, уровень шума и т.д.).  
— Возможно потребуется дополнительная предварительная обработка, например, нормализация громкости.  

![](https://raw.githubusercontent.com/unton3ton/audiowmark/master/AudioAnal/photo_2023-06-21_10-22-16.jpg)


>>> librosa.version  
>>> '0.10.1'  
>>> AttributeError: No librosa.core attribute dtln  

Возможное решение:
``` python
dist = mfcc1 - mfcc2
print(f'Distance between audios is {((dist ** 2).sum(axis=0) ** 0.5).sum()}')
```

> Import them both into Audacity. Apply the “Invert” effect to one of the tracks. Select both tracks, then from the “Tracks menu > Mix and Render”. If the tracks were identical, the result will be silence. To check that it is absolute silence, select the full (mix) track, and open the “Amplify” effect. If the Amplify effect says that the “New Peak Amplitude” is “-infinity”, then the mix track is totally silent and the two imported files have identical audio.

![](https://raw.githubusercontent.com/unton3ton/audiowmark/master/AudioAnal/photo_2024-07-03_16-40-24%20(2).jpg)


![](https://raw.githubusercontent.com/unton3ton/audiowmark/master/AudioAnal/photo_2024-07-03_16-40-24.jpg)


![](https://raw.githubusercontent.com/unton3ton/audiowmark/master/AudioAnal/photo_2024-07-03_16-401-24.jpg)


![](https://raw.githubusercontent.com/unton3ton/audiowmark/master/AudioAnal/photo_2024-07-03_16-440-32.jpg)


![](https://raw.githubusercontent.com/unton3ton/audiowmark/master/AudioAnal/%D0%B1%D0%B5%D0%B7%20%D0%BE%D1%80%D0%B8%D0%B3%D0%B8%D0%BD%D0%B0%D0%BB%D0%B0%20%D0%BE%D0%B1%D0%BD%D0%B0%D1%80%D1%83%D0%B6%D0%B8%D1%82%D1%8C%20%D0%B2%D1%81%D1%82%D1%80%D0%B0%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B5%20%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D1%8F%D0%B5%D1%82%D1%81%D1%8F%20%D0%B2%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D1%8B%D0%BC.PNG)


## Sources

* [Comparing two supposedly identical tracks](https://forum.audacityteam.org/t/comparing-two-supposedly-identical-tracks/36424)
* [Audio Feature Extractions](https://pytorch.org/audio/stable/tutorials/audio_feature_extractions_tutorial.html)
* [Цифровое представление аналогового аудиосигнала. Краткий ликбез](https://habr.com/ru/articles/503786/)
* [Оцифровка аналоговой звуковой волны](https://foxford.ru/wiki/informatika/otsifrovka-analogovoy-zvukovoy-volny?utm_referrer=https%3A%2F%2Fya.ru%2F)
* [Spectrograms, MFCCs, and Inversion in Python](https://timsainb.github.io/spectrograms-mfccs-and-inversion-in-python.html)
