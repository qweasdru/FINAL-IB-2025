# Writeup

Так как данный таск относится к категории `ppc`, то данный writeup будет поделён на две части — где в первой будет приведён код для решения, а во второй он будет подробно разобран.

# Код

```py
import os
import base64
import binascii
from typing import Generator
from xor_cipher import cyclic_xor
from itertools import permutations

root = os.path.realpath(f"{os.path.dirname(os.path.realpath(__file__))}/..")
dst = os.path.join(root, "dst", "nevermore.txt")

with open(dst, "r") as f:
    text = f.read()

    pairs = list(permutations(["\u200B", "\u200D", "\u2060", "\u200C", "\uFEFF"], 2))

    for pair in pairs:
        A, B  = pair
        print(f"trying pair {repr(A)} and {repr(B)}...")
        zero_width = "".join(x for x in text if x in pair)
        binary = zero_width.replace(A, "0").replace(B, "1")
        try:
            b64 = int(binary, 2).to_bytes((len(binary) + 7) // 8, byteorder='big').decode("utf-8")
            xor = base64.b64decode(b64)
            flag = cyclic_xor(xor, b"nevermore").decode("utf-8")
            print("flag:", flag)
            print()
        except:
            print(f"pair {repr(A)} and {repr(B)} invalid")
            print()
```

# Разбор

Не будем останавливаться на библиотеках — разберём только логику.

Логика для решения таска очень простая:

1. Мы читаем содержимое файла со стихотворением.
2. Создаём все возможные сочетания для пяти символов Unicode, обозначающих Zero-Width символы.
3. Для каждого сочетания:
   1. Вытаскиваем из текста все zero-width символы, соответствующие данному сочетанию
   2. Переводим извлечённые zero-width символы в бинарную строку с расчётом на то, что первый символ в паре — это 0, второй символ — 1
   3. Оборачиваем в try-except, чтобы отловить ошибки при декодировании:
      1. Переводим бинарную строку в байты, затем пытаемся декодировать в utf-8. Получаем строку base64
      2. Декодируем строку base64. Получаем XOR-строку
      3. Декодируем XOR-строку с ключом "nevermore" (есть в стихотворении, самый знаковый образ, точнее — слово). Получаем флаг

Ввиду того, что по всему тексту стихотворения равномерно размещено около 6 тысяч различных zero-width символов, нам представляется невозможным ручное решение данной задачи. Она требует именно что программного подхода.
