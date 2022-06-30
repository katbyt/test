from typing import Dict


def count_sym(text: str) -> Dict[str, int]:
    """Функция для подсчета количества символов в тексте"""
    my_dict = dict()

    for sym in text:
        if sym in my_dict:
            my_dict[sym] += 1
        else:
            my_dict[sym] = 1

    return my_dict


with open('test.txt', encoding='utf-8') as file:
    result = count_sym(file.read())

print('Частота встречаемости символов в файле:')
length_text = sum(result.values())

for key in result:
    value = round(result[key] / length_text * 100, 2)
    print(f'{key} - {value}%')
