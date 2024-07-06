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

