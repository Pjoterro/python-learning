# Napisz program do szyfrowania i deszyfrowania tekstu za pomocą szyfru Vigenère’a:
# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
# Funkcja przyjmuje text oraz klucz i zwraca zmodyfikowany tekst.
# Tekst bedzie tylko w j. angielskim (znaki sa w tabeli 'alphabet')
# Input tekst bedzie malymi literami i minimum jednym slowem, moze zawierac znaki interpunkcyjne, cyfry i spacje.
# Key bedzie wielkimi literami (i bedzie najmniej jedna litera).
# Podanie klucza z minusem na poczatku wskazuje na "deszyfrowanie" tekstu!
# "LEMON" - klucz do zaszyforwania, "-LEMON" - klucz do rozszyfrowania
# Mozesz napisac dodatkowe funkcje

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def vigenere_encryption(text, key):
    result = ""
    return result

# ---------------------
#        TESTY
# ---------------------


# Test vigenere_encryption() 1:
test_input_text = 'to jest test szyfrowania'
test_input_key = 'ABCD'
test_output_text = 'tp lhsu vhsu ucygtrwbpla'
test_result = 'OK' if vigenere_encryption(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test vigenere_encryption() 1: ' + test_result)

# Test vigenere_encryption() 2:
test_input_text = 'atak odbedzie sie jutro. dzis o 16 dalsze rozkazy. jesli brak kontaktu - nic nie robic.'
test_input_key = 'LEMON'
test_output_text = 'lxmy bofqrmti ewr uyffb. odug b 16 oexgmp vanxldk. xrdpu pelo wcaeewhh - ymo bvp vapvn.'
test_result = 'OK' if vigenere_encryption(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test vigenere_encryption() 2: ' + test_result)

# Test vigenere_encryption() 3:
test_input_text = 'nic nie powinno sie zmienic'
test_input_key = 'A'
test_output_text = 'nic nie powinno sie zmienic'
test_result = 'OK' if vigenere_encryption(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test vigenere_encryption() 3: ' + test_result)

# Test vigenere_encryption() 4:
test_input_text = 'tp lhsu vhsu fhsaairpydnjc'
test_input_key = '-ABCD'
test_output_text = 'to jest test deszyfrowania'
test_result = 'OK' if vigenere_encryption(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test vigenere_encryption() 4: ' + test_result)

# Test vigenere_encryption() 5:
test_input_text = 'ycqxes wfqlnxam! tmidhap qs 16. uln fqfbvfl.'
test_input_key = '-HORNET'
test_output_text = 'rozkaz przyjety! czekamy do 16. bez odbioru.'
test_result = 'OK' if vigenere_encryption(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test vigenere_encryption() 5: ' + test_result)

# Test vigenere_encryption() 6:
test_input_text = 'powinno wyjsc to samo'
test_input_key = '-AAAA'
test_output_text = 'powinno wyjsc to samo'
test_result = 'OK' if vigenere_encryption(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test vigenere_encryption() 6: ' + test_result)

# Test vigenere_encryption() 7:
test_input_text = 'lrfwjwh dfuek'
test_input_key = '-BARDZODLUGIKLUCZ'
test_output_text = 'krotkie slowa'
test_result = 'OK' if vigenere_encryption(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test vigenere_encryption() 7: ' + test_result)
