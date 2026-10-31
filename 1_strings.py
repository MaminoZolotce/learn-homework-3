"""
Задание 1. Строки.

Реализуй функции. Исходная строка не должна изменяться.
В main() выведи результаты вызовов и добавь свои примеры.
"""


def normalize_name(name):
    """Удали пробелы по краям и сделай первую букву каждого слова заглавной.
    normalize_name("  аННА иВАНОВА  ") -> "Анна Иванова"
    normalize_name("") -> ""
    """
    return name.strip().title()

def count_words(text):
    """Верни количество слов, разделённых пробелами.
    count_words("  Python   это интересно  ") -> 3
    count_words("") -> 0
    """
    return len(text.split())


def make_slug(text):
    """Удали пробелы по краям, переведи буквы в нижний регистр.
    Раздели текст по пробелам и соедини слова дефисами.
    Пунктуацию сохраняй; транслитерация не нужна.
    make_slug("  Учим   Python  ") -> "учим-python"
    """
    return '-'.join(text.lower().split())


def main():
    print("Имя:", normalize_name("  аННА иВАНОВА  "))
    print("Пустое имя:", normalize_name(""))
    print("Количество слов:", count_words("  Python   это интересно  "))
    print("Пустой текст:", count_words(""))
    print("Slug:", make_slug("  Учим   Python  "))
    print("Пустой slug:", make_slug(""))



if __name__ == "__main__":
    main()
