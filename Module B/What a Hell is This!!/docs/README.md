# Название задания

What a Hell is This?!

# Описание задания

> Как карканье Ворона в ночи,  
> Как улыбка последняя, в ночь уходящего друга,  
> Как первый сон угасающего в полночи,  
> Как новорожденный, от первого испуга
>
> <div align="right">— Неизвестный</div>

# Краткое описание задачи

Участник получает в своё распоряжение текстовый файл в формате .txt со стихотворением Эдгара Алана По "Ворон" в переводе Михаила Александровича Зенкевича. Его задача - отыскать флаг, спрятанный в zero-width символах внутри текста.

Флаг кодируется сначала в XOR с ключом `nevermore`, затем в base64, затем в binary, затем в zero width (пара символов zero-width, один символ - 0, второй - 1). После этого он равномерно распределяется по тексту вместе с фальшивым флагом и шумом.

# Флаг

`flag{th3_r4v3n_c4w1ng_n3v3rm0r3_1s_p41nf6l}"`

# Оценка сложности

1. Участник должен быть знаком с любым языком программирования и должен иметь развитое системное мышление, позволяющее структурировать и упорядочивать внешне сложные задачи.
2. Участник должен иметь представление о существовании в пространстве Unicode символов с нулевой шириной, которые при обычном просмотре текста, никак не заметны глазом. И он должен иметь представление о том, как их обнаружить в тексте.
3. Также Участник должен иметь навыки в работе с XOR-шифрованием, шифрованием на основе base64, шифрованием на основе перевода исходных данных в бинарный вид.

Исходя из вышеупомянутых факторов, сложность задачи оценивается в 6,5 баллов из 10.

Если участник имеет опыт в программировании, он сможет решить задачу за 30-60 минут, создав короткий скрипт для извлечения флага. Для участников среднего уровня или новичков решение может занять несколько часов и потребовать дополнительных исследований по теме шифрования и Unicode.
