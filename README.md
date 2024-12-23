# cm_dz_4
4 дз по конф. упр., Малоенко Эдуард, ИКБО-40-23, вариант 14.

1) Общее описание

Разработать ассемблер и интерпретатор для учебной виртуальной машины 
(УВМ). Система команд УВМ представлена далее. 
Для ассемблера необходимо разработать читаемое представление команд 
УВМ. Ассемблер принимает на вход файл с текстом исходной программы, путь к 
которой задается из командной строки. Результатом работы ассемблера является 
бинарный файл в виде последовательности байт, путь к которому задается из 
командной строки. Дополнительный ключ командной строки задает путь к файлу
логу, в котором хранятся ассемблированные инструкции в духе списков 
“ключ=значение”, как в приведенных далее тестах. 
Интерпретатор принимает на вход бинарный файл, выполняет команды УВМ 
и сохраняет в файле-результате значения из диапазона памяти УВМ. Диапазон 
также указывается из командной строки. 
Форматом для файла-лога и файла-результата является json.

2) Описание всех функций и настроек

Загрузка константы 

A - Биты 0—7 - 164

B - Биты 8—15 - Константа

Размер команды: 2 байт. Операнд: поле B. Результат: регистр-аккумулятор. 

Тест (A=164, B=144):

0xA4, 0x90 

Чтение из памяти 

A - Биты 0—7 - 144 

B - Биты 8—18 - Смещение

Размер команды: 3 байт. Операнд: ячейка памяти по адресу, которым 
является сумма адреса (регистр-аккумулятор) и смещения (поле B). Результат: 
регистр-аккумулятор. 

Тест (A=144, B=392): 

0x90, 0x88, 0x01 

Запись в память 

A - Биты 0—7 - 29

B - Биты 8—23 - Адрес

Размер команды: 3 байт. Операнд: регистр-аккумулятор. Результат: ячейка 
памяти по адресу, которым является поле B. 

Тест (A=29, B=565):

0x1D, 0x35, 0x02 

Бинарная операция: побитовый циклический сдвиг влево 

A - Биты 0—7 - 74

B - Биты 8—23 - Адрес

Размер команды: 3 байт. Первый операнд: регистр-аккумулятор. Второй 
операнд: ячейка памяти по адресу, которым является поле B. Результат: регистр
аккумулятор. 

Тест (A=74, B=680):

0x4A, 0xA8, 0x02 

Тестовая программа:

Выполнить поэлементно операцию побитовый циклический сдвиг влево над 
двумя векторами длины 6. Результат записать в новый вектор. 

3) Примеры использования и результаты тестирования.

Протестируем каждую операцию:

![image](https://github.com/user-attachments/assets/c608aef8-d705-47f4-92bf-476b0233d8f7)

Загрузим константы 1, 1 и 1 в регистр-аккумулятор. Запишем значение с вершины регистра в память по адресу 1. Сделаем сдвиг на 1 для очередного верхнего значения в регистре. Запишем верхнее значение в регистре в память по адресу 2. Считаем значение из памяти по адресу 2 и запишем его в ячейку по адресу 3. Получим результат:

![image](https://github.com/user-attachments/assets/68d752a3-e453-4cc0-8593-0203d971d631)

Операции работают корректно.

Проведем тестирование на примере содержимого файла input_file.txt, реализующего тестовую программу. Инструмент
принимает файл со следующим содержимым:

![image](https://github.com/user-attachments/assets/7176fe6d-c8e1-4368-812b-71db08ae3157)

![image](https://github.com/user-attachments/assets/9516fad3-5ca9-4bc4-a169-69aee551e420)

Формируется бинарный файл:

![image](https://github.com/user-attachments/assets/a7ce699c-1ac3-427a-b207-f2ae9cb5303c)

Формируется файл-лог:

![image](https://github.com/user-attachments/assets/32474904-5374-4dc9-820e-5a448c99aaa3)

И получается результат: два вектора длиной 6, для одного из которых был произведен бинарный сдвиг влево на 1, а для второго - на 2.

![image](https://github.com/user-attachments/assets/a1a033e7-9263-40f0-a92c-94aa6d079191)

Таким образом, требуемая тестовая программа работает корректно.
