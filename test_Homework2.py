# Artur Kazukevich
# Date: 30/05/2023
# Description: Homework 2 Test Suit
# Grodno IT Academy Python 3.9.5

import unittest
from unittest.mock import patch
import Homework2 as Homework2


class TestHomework1_common_price(unittest.TestCase):
    # common_price
    def test_common_price_positive(self):
        self.assertEqual(Homework2.common_price(10, 10, 10, 10), "Общая цена составляет 10 рублей и 10 копеек за 10 товаров")
    def test_common_price_catch(self):
        self.assertEqual(Homework2.common_price(1, 30, 7, 3), "Общая цена составляет 0 рублей и 56 копеек за 3 товаров")
    def test_common_price_high_numbers(self):
        self.assertEqual(Homework2.common_price(0, 4, 4, 100000000000000000000000000), "Общая цена составляет 1000000000000000000000000 рублей и 0 копеек за 100000000000000000000000000 товаров")
        self.assertEqual(Homework2.common_price(0, 1, 100000000000000000000000, 10000000000000000000000000000000000000000000000), "Общая цена составляет 1000000000000000000000 рублей и 0 копеек за 10000000000000000000000000000000000000000000000 товаров")
    def test_common_price_zero_goods(self):
        self.assertEqual(Homework2.common_price(10, 10, 10, 0), "Общая цена составляет 0 рублей и 0 копеек за 0 товаров")
        self.assertEqual(Homework2.common_price(0, 1, 1, 0), "Общая цена составляет 0 рублей и 0 копеек за 0 товаров")
    def test_common_price_negative(self):
        self.assertEqual(Homework2.common_price(0, 0, 7, 3), False)
        self.assertEqual(Homework2.common_price(0, 30, 0, 3), False)
    def test_common_price_negative_goods(self):
        self.assertEqual(Homework2.common_price(0, 0, 7, -3), False)
        self.assertEqual(Homework2.common_price(0, 30, 0, -3), False)
        self.assertEqual(Homework2.common_price(0, 30, 1, -3), False)
    def test_common_price_type_error(self):
        self.assertEqual(Homework2.common_price(0, 30, 7, "3"), False)
        self.assertEqual(Homework2.common_price("0", 30, 7, 3), False)
        self.assertEqual(Homework2.common_price(0, "30", 7, 3), False)
        self.assertEqual(Homework2.common_price(0, 30, "7", 3), False)
        self.assertEqual(Homework2.common_price("0", "30", "7", "3"), False)

class TestHomework1_triangle(unittest.TestCase):
    # triangle
    def test_triangle_negative_values(self):
        # negative values
        self.assertEqual(Homework2.triangle(-1,2,2), False)
        self.assertEqual(Homework2.triangle(1,2,-2), False)
    def test_triangle_type_error(self):
        # type error
        self.assertEqual(Homework2.triangle(1,2,"3"), False)
        self.assertEqual(Homework2.triangle("1","2","3"), False)
    def test_triangle_impossible(self):
        # impossible
        self.assertEqual(Homework2.triangle(1,2,3), 0)
        self.assertEqual(Homework2.triangle(2,2,4), 0)
    def test_triangle_zero(self):
        # zero
        self.assertEqual(Homework2.triangle(0,0,0), False)
        self.assertEqual(Homework2.triangle(4,3,0), False)
    def test_triangle_positive(self):
        self.assertEqual(Homework2.triangle(1,1,1), 0.433)
        self.assertEqual(Homework2.triangle(1,2,2), 0.9682)
        self.assertEqual(Homework2.triangle(2,2,2), 1.7321)
        self.assertEqual(Homework2.triangle(4,6,9), 9.5623)
    def test_triangle_float(self):
        self.assertEqual(Homework2.triangle(0.5,0.5,0.5), 0.1083)
        self.assertEqual(Homework2.triangle(0.2,0.2,0.1), 0.0097)
        self.assertEqual(Homework2.triangle(526.63,524.35,645.35), 133829.7966)
        self.assertEqual(Homework2.triangle(19.2,23.5,18.7), 174.6526)

class TestHomework1_longest_word(unittest.TestCase):
    # longest_word
    def test_longest_word_negative(self):
        self.assertEqual(Homework2.longest_word(""), False)
        self.assertEqual(Homework2.longest_word(1), False)
    def test_longest_word_simple(self):
        self.assertEqual(Homework2.longest_word("This is a sample sentence where the longest word is in the middle!"), "sentence")
        self.assertEqual(Homework2.longest_word("Hello world, how are you?"), "world")
    def test_longerst_word_long(self):
        self.assertEqual(Homework2.longest_word("I am a very long sentence, but I am not the longest word in the sentence."), "sentence")
        self.assertEqual(Homework2.longest_word("I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest word in the sentence. I am a very long sentence, but I am not the longest"), "sentence")
    def test_longest_word_lorem(self):
        self.assertEqual(Homework2.longest_word("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur repredenderit sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."), "repredenderit")

class TestHomework1_uniques(unittest.TestCase):
    # uniques
    def test_uniques_incorrect_type(self):
        self.assertEqual(Homework2.uniques(10), False)
    def test_uniques_simple(self):
        self.assertEqual(Homework2.uniques("abc cde def"), "abcdef")
        self.assertEqual(Homework2.uniques("This is a sample sentence where the longest possible word is in the middle!"), "Thisamplentcwrogbd!")
        self.assertEqual(Homework2.uniques("Hello world, how are you?"), "Helowrd,hayu?")
    def test_uniques_long(self):
        self.assertEqual(Homework2.uniques("I am a very long sentence, but I am not the longest word in the sentence."), "Iamverylongstc,buhwdi.")
        self.assertEqual(Homework2.uniques("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur repredenderit sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."), "Loremipsudlta,cngbq.UvxDhfE")

class TestHomework1_count_string_capitalization(unittest.TestCase):
    # count_string_capitalization
    def test_count_string_capitalization_positive(self):
        self.assertEqual(Homework2.count_string_capitalization("HeWor"), "В строке 'HeWor' 2 большие и 3 маленькие буквы")
        self.assertEqual(Homework2.count_string_capitalization(""), "В строке '' 0 большие и 0 маленькие буквы")
        self.assertEqual(Homework2.count_string_capitalization("HELLO"), "В строке 'HELLO' 5 большие и 0 маленькие буквы")
        self.assertEqual(Homework2.count_string_capitalization("world"), "В строке 'world' 0 большие и 5 маленькие буквы")
    def test_count_string_capitalization_negative(self):
        self.assertEqual(Homework2.count_string_capitalization(25), False)
        self.assertEqual(Homework2.count_string_capitalization([]), False)
        self.assertEqual(Homework2.count_string_capitalization(["H", "e"]), False)
        self.assertEqual(Homework2.count_string_capitalization(True), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)
