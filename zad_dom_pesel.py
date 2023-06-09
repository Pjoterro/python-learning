# Do napisania jest 7 funkcji, w dalszej czesci programu napisalem ulomne testy jednostkowe, nic nie zmieniaj w nich.
# Mozesz sobie zapuszczac program i sprawdzac czy dana funkcja dziala poprawnie
# https://www.gov.pl/web/gov/czym-jest-numer-pesel - to tak jakbys nie wiedziala xD (a tak serio to jest wytlumaczenie liczby kontrolnej)

# 1- funkcja do sprawdzania poprawnosci podanego nr pesel - sprawdzenie czy podany string zawiera tylko cyfry (zwraca boola):
def has_only_digits(pesel):
    # tutaj kod (zmien ofc tego returna)
    return False


# 2- funkcja do sprawdzania poprawnosci podanego nr pesel - sprawdzenie czy podany string ma odpowiednia ilosc znakow (zwraca boola):
def has_correct_number_of_digits(pesel):
    # tutaj kod
    return False

# 3- funkcja do sprawdzania poprawnosci podanego nr pesel - sprawdza czy podany string ma poprawna liczbe kontrolna (zwraca boola):
def has_correct_controll_number(pesel):
    # tutaj kod
    return False

# 4- funkcja do sprawdzania poprawnosci podanego nr pesel - sprawdza czy podany string jest poprawnym peselem (zwraca boola)
# ***(hint - uzyj tego co napisalas wyzej)***
def is_correct_pesel(pesel):
    # tutaj kod
    return False

# 5- funkcja ktory wyciaga plec z poprawnego nr pesel (zwraca string "Male" lub "Female" lub "" dla niepoprawnego - nie wypisuje tylko zwraca!):
def get_sex(pesel):
    # tutaj kod
    return "Female"

# 6- funkcja ktory zwraca date urodzin z nr pesel (zwraca stringa DD-MM-RRRR, np "31-01-1950") lub string "" dla niepoprawnego peselu
# wersja easy - zalozenie ze wszyscy sie urodzili miedzy 1900 a 1999
# wersja hard - uwzglednia pelen zakres 1800-2299
def get_birth_date(pesel):
    # tutaj kod
    return "01-01-1900"

# 7- funkcja zwraca string z informacja o plc i dacie urodzenia np. "Female - 01-01-1900" jesli PESEL jest poprawny, lub pusty string "" jesli PESEL jest niepoprawny
# ***(hint - uzyj tego co napisalas wyzej)***
def get_sex_and_birth_date(pesel):
    # tutaj kod
    return "Female - 01-01-1900"

# Jesli wszystko poprawnie napisalas to wszystkie testy ponizej powinny miec status "Working"

#------------------------------------
# PONIZEJ NIC NIE RUSZAJ, TO SA TESTY
#------------------------------------

# Test has_only_digits():
input = "111a2 7^719" # wrong chars
output = False
test_result = "OK" if has_only_digits(input) == output else "NOT OK"
print("Test has_only_digits() 1: " + test_result)

input = "11102576719"
output = True
test_result = "OK" if has_only_digits(input) == output else "NOT OK"
print("Test has_only_digits() 2: " + test_result)

# Test has_correct_number_of_digits():
input = "950813119921" # too long
output = False
test_result = "OK" if has_correct_number_of_digits(input) == output else "NOT OK"
print("Test has_correct_number_of_digits() 1: " + test_result)

input = "9508131199" # too short
output = False
test_result = "OK" if has_correct_number_of_digits(input) == output else "NOT OK"
print("Test has_correct_number_of_digits() 2: " + test_result)

input = "95081311992"
output = True
test_result = "OK" if has_correct_number_of_digits(input) == output else "NOT OK"
print("Test has_correct_number_of_digits() 3: " + test_result)

# Test has_correct_controll_number():
input = "89021766888" # wrong controll number
output = False
test_result = "OK" if has_correct_controll_number(input) == output else "NOT OK"
print("Test has_correct_controll_number() 1: " + test_result)

input = "89021766887"
output = True
test_result = "OK" if has_correct_controll_number(input) == output else "NOT OK"
print("Test has_correct_controll_number() 2: " + test_result)

# Test is_correct_pesel():
input = "89O21766887" # has O (letter) instead of 0 (digit)
output = False
test_result = "OK" if is_correct_pesel(input) == output else "NOT OK"
print("Test is_correct_pesel() 1: " + test_result)

input = "89021766887"
output = True
test_result = "OK" if is_correct_pesel(input) == output else "NOT OK"
print("Test is_correct_pesel() 2: " + test_result)

# Test get_sex():
input = "06100999779" # incorrect sex
output = ""
test_result = "OK" if get_sex(input) == output else "NOT OK"
print("Test get_sex() 1: " + test_result)

input = "49120559317"
output = "Male"
test_result = "OK" if get_sex(input) == output else "NOT OK"
print("Test get_sex() 2: " + test_result)

input = "26010253263"
output = "Female"
test_result = "OK" if get_sex(input) == output else "NOT OK"
print("Test get_sex() 3: " + test_result)

# Test get_birth_date():
input = "42050138336" # incorrect birth date
output = ""
test_result = "OK" if get_birth_date(input) == output else "NOT OK"
print("Test get_birth_date() 1: " + test_result)

input = "91071558279"
output = "15-07-1991"
test_result = "OK" if get_birth_date(input) == output else "NOT OK"
print("Test get_birth_date() 2: " + test_result)

# Test return_sex_and_birth_date():
input = "56042O37692" # incorrect pesel
output = ""
test_result = "OK" if return_sex_and_birth_date(input) == output else "NOT OK"
print("Test return_sex_and_birth_date() 1: " + test_result)

input = "56042037692"
output = "Male - 20-04-1956"
test_result = "OK" if return_sex_and_birth_date(input) == output else "NOT OK"
print("Test return_sex_and_birth_date() 2: " + test_result)

input = "38040283442"
output = "Female - 02-04-1938"
test_result = "OK" if return_sex_and_birth_date(input) == output else "NOT OK"
print("Test return_sex_and_birth_date() 3: " + test_result)
