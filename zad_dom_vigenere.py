# Napisz program do szyfrowania i deszyfrowania tekstu za pomocą szyfru Vigenère’a:
# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
# Obie funkcje przyjmuja text oraz klucz i zwracaja zmodyfikowany tekst.
# Tekst bedzie tylko w j. angielskim (znaki sa w tabeli 'alphabet')
# input tekst bedzie malymi literami i minimum jednym slowem, moze zawierac znaki interpunkcyjne, cyfry i spacje.
# key bedzie wielkimi literami (i bedzie najmniej jedna litera)
# mozesz napisac dodatkowe funkcje

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_vigenere(text, key):
    return ""

def decrypt_vigenere(text, key):
    return ""

# ---------------------
#        TESTY
# ---------------------

# Test 1:
test_input_text = 'to jest test szyfrowania'
test_input_key = 'ABCD'
test_output_text = 'tp lhsu vhsu ucygtrwbpla'
test_result = 'OK' if encrypt_vigenere(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test 1: ' + test_result)

# Test 2:
test_input_text = 'atak odbedzie sie jutro. dzis o 16 dalsze rozkazy. jesli brak kontaktu - nic nie robic.'
test_input_key = 'LEMON'
test_output_text = 'lxmy bofqrmti ewr uyffb. odug b 16 oexgmp vanxldk. xrdpu pelo wcaeewhh - ymo bvp vapvn.'
test_result = 'OK' if encrypt_vigenere(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test 2: ' + test_result)

# Test 3:
test_input_text = 'nic nie powinno sie zmienic'
test_input_key = 'A'
test_output_text = 'nic nie powinno sie zmienic'
test_result = 'OK' if encrypt_vigenere(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test 3: ' + test_result)

# Test 4:
test_input_text = 'tp lhsu vhsu fhsaairpydnjc'
test_input_key = 'ABCD'
test_output_text = 'to jest test deszyfrowania'
test_result = 'OK' if decrypt_vigenere(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test 4: ' + test_result)

# Test 5:
test_input_text = 'ycqxes wfqlnxam! tmidhap qs 16. uln fqfbvfl.'
test_input_key = 'HORNET'
test_output_text = 'rozkaz przyjety! czekamy do 16. bez odbioru.'
test_result = 'OK' if decrypt_vigenere(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test 5: ' + test_result)

# Test 6:
test_input_text = 'powinno wyjsc to samo'
test_input_key = 'AAAA'
test_output_text = 'powinno wyjsc to samo'
test_result = 'OK' if decrypt_vigenere(test_input_text, test_input_key) == test_output_text else 'NOT OK'
print('Test 6: ' + test_result)
