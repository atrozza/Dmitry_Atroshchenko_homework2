# Dmitry Atroshchenko
# Date: 22/10/2023
# Description: Homework 2
# My version Python 3.11

# Объяснение работы с функциями:
# формат определения функции (то есть: мы ее создаем) - def func(arg1, arg2, arg3)
# arg1, arg2, arg3 - это аргументы, которые передаются в функцию при ее вызове (то есть, мы ее запускаем)

# оценивается: чистота кода, наличие комментариев (PEP8), прохождение всех тестов
# нельзя менять названия функций/файлов/входные данные

# пример названия репозитория для гитхаба: kazukevich_homework2
# добавьте в репозиторий с домашним задание файл readme с датой сдачи, фамилией и именем выполнившего и кратким
# описанием каждой задачи (коротко, что использовали, алгоритм функции), оформленным в стиле markdown

# Напишите программу, ĸоторая считает общую цену.
# Вводится m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара.
# Посчитайте общую цену в рублях и ĸопейĸах за l товаров.
# Уточнение:
# Используйте функцию return чтобы ответ был в рублях и копейках.
# Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"

# Для одного из тестов нужно применять библиотеку Decimal()

def common_price(m, n, s, l):
    # Проверка на то что в переменные m, n, s, l это простые числа
    # если введены числа то код продолжает свое выполнение если не только числа то выводится false
    
    # В принципе, проверка рабочая, но выглядит сложно =) По тестам мы видим, что передаются либо числа, либо строки. Так что тут достаточно будет проверки type(m) == int and ....
    # У тебя тут крашатся все тесты и пишут ошибку "int has no replace" - внимательнее к ошибкам питона, в них и есть ответ на их решение.
    # Если оставлять такой вариант, то нужно каждую переменную при проверке перегонять в str
    if not (m.replace(".", "", 1).isdigit() and n.replace(".", "", 1).isdigit() and s.replace(".", "", 1).isdigit() and l.replace(".", "", 1).isdigit()):
        return False
    else:
        m, n = float(m), float(n)
        s, l = int(s), int(l)
        # Тут очень правильная проверка.
        if l < 0 or (m == 0 and n == 0) or s == 0:
            return False
        else:
            # Логика решения верна.
            price_cop_1product = (m * 100 + n) / s
            price_cop_lproduct = price_cop_1product * l
            m = price_cop_lproduct // 100
            n = price_cop_lproduct % 100
            m = round(m)
            n = round(n)
            l = round(l)
            # Решение ок, но оно не прошло бы тест с огромными числами. Там будет ошибка питоновского переполнения - для такого теста я рекомендовал изучить Decimal
            # Для решения с ним и без него - см ответы.
            return "Общая цена составляет " + str(m) + " рублей и " + str(n) + " копеек за " + str(l) + " товаров"

# Если исправить ошибку с проверкой типов данных - то все тесты, кроме одного проходятся. Молодец!
# Не хватает комментариев


# Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь с точностью до четырёх десятичных.
# Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
# Если нет, вывести False.
# Бонусом - с правильным возвратом мы ещё получим обьяснение в консоль почему это не треугольник.


def triangle(a, b, c):
    # Проверка на то что в переменные a, b, c, это просытые числа
    # если введены числа то код продолжает свое выполнение если не только числа то выводится false

    # Тут снова крашатся все тесты по той же причине, что в предыдущей задачке.
    # Если исправить эту строку - все тесты проходятся. Не хватает комментариев.
    if not (a.replace(".", "", 1).isdigit() and b.replace(".", "", 1).isdigit() and c.replace(".", "", 1).isdigit()):
        return False
    else:
        a, b, c = float(a), float(b), float(c)
        if a + b >= c and a + c > b and b + c > a:
            s = (a + b + c) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            if area > 0:
                return round(area, 4)
            elif area == 0:
                return round(area)
        else:
            return False


# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении могут быть знаки препинания.
# Пример: если введено "This is a sample sentence where the longest word is in the middle!",
# то надо вернуть "sentence"
def longest_word(sentence):
    if not sentence:
        return False
    # Та же самая ошибка. Если исправить эту строку, то все тесты проходятся.
    # type(sentence) != str
    elif (sentence.replace(".", "").isdigit()):
        return False
    else:
        # Вариант ок, но рекомендую изучить регулярные выражения.
        punctuation = [',', '.', '!', '?']
        cleaned_sentence = sentence

        for char in punctuation:
            cleaned_sentence = cleaned_sentence.replace(char, '')
        words = cleaned_sentence.split()
        # Тут все верно и по логике, и по коду
        max_length = max(len(word) for word in words)
        longest_words = [word for word in words if len(word) == max_length]
        last_longest_word = longest_words[-1]
        return last_longest_word



# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".
def uniques(repeating_string):
    if not repeating_string:
        return False
    # Та же ошибка. Если ее исправить - все тесты проходятся.
    elif (repeating_string.replace(".", "").isdigit()):
        return False
    else:
        # Оч крутое решение.Все верно. Круто, что в одну строку
        no_space_string = repeating_string.replace(" ", "")
        result = "".join(sorted(set(no_space_string), key=no_space_string.index))
        return result


# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Проверка рассчитана только на английские буквы.
def count_string_capitalization(mixed_string):
    # Перемудрил - тут всего лишь достаточно проверить, что тип переменной это строка. Не нужно проверять каждый тип по отдельности.
    if ('[' in mixed_string and ']' in mixed_string) or mixed_string == 'True':
        return False
    elif mixed_string.replace(".", "").isdigit():
        return False
    else:
        count_upper_letter = 0
        count_lower_letter = 0
        for char in mixed_string:
            if char.isalpha():
                if char.isupper():
                    count_upper_letter += 1
                elif char.islower():
                    count_lower_letter += 1
        return "В строке '" + mixed_string + "' " + str(count_upper_letter) + " большие и " + str(count_lower_letter) + " маленькие буквы"
