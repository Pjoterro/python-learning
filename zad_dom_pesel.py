# Do napisania jest 7 funkcji, w dalszej czesci programu napisalem ulomne testy jednostkowe, nic nie zmieniaj w nich.
# Mozesz sobie zapuszczac program i sprawdzac czy dana funkcja dziala poprawnie
# https://www.gov.pl/web/gov/czym-jest-numer-pesel - to tak jakbys nie wiedziala xD (a tak serio to jest wytlumaczenie liczby kontrolnej)

# 1- funkcja do sprawdzania poprawnosci podanego nr pesel - sprawdzenie czy podany string zawiera tylko cyfry (zwraca boola):
def has_only_digits(pesel):
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for char in pesel:
        if not char in digits:
            return False
    return True


# 2- funkcja do sprawdzania poprawnosci podanego nr pesel - sprawdzenie czy podany string ma odpowiednia ilosc znakow (zwraca boola):
def has_correct_number_of_digits(pesel):
    return len(pesel) == 11

# 3- funkcja do sprawdzania poprawnosci podanego nr pesel - sprawdza czy podany string ma poprawna liczbe kontrolna (zwraca boola):
def has_correct_controll_number(pesel):
    multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    i = 0
    sum = 0
    if has_only_digits(pesel) and has_correct_number_of_digits(pesel):
        while (i < len(multipliers)):
            sum += (int(pesel[i]) * multipliers[i]) % 10
            i += 1
        return int(pesel[i]) == 10 - (sum%10)
    else:
        return False

# 4- funkcja do sprawdzania poprawnosci podanego nr pesel - sprawdza czy podany string jest poprawnym peselem (zwraca boola)
# ***(hint - uzyj tego co napisalas wyzej)***
def is_correct_pesel(pesel):
    return has_correct_controll_number(pesel)
# UWAGA - tak na prawde to ta funkcja jest zbedna, jej logika jest w funkcji has_correct_controll_number(pesel)

# 5- funkcja ktory wyciaga plec z poprawnego nr pesel (zwraca string "Male" lub "Female" lub "" dla niepoprawnego - nie wypisuje tylko zwraca!):
def get_sex(pesel):
    if is_correct_pesel(pesel):
        return "Male" if int(pesel[-2]) % 2 == 1 else "Female"
    else: 
        return ""

# 6- funkcja ktory zwraca date urodzin z nr pesel (zwraca stringa DD-MM-RRRR, np "31-01-1950") lub string "" dla niepoprawnego peselu
# wersja easy - zalozenie ze wszyscy sie urodzili miedzy 1900 a 1999
# wersja hard - uwzglednia pelen zakres 1800-2299
def get_birth_date(pesel):
    if is_correct_pesel(pesel):
        return pesel[4] + pesel[5] + "-" + pesel[2] + pesel [3] + "-19" + pesel[0] + pesel[1]
    else: 
        return ""

# 7- funkcja zwraca string z informacja o plc i dacie urodzenia np. "Female - 01-01-1900" jesli PESEL jest poprawny, lub pusty string "" jesli PESEL jest niepoprawny
# ***(hint - uzyj tego co napisalas wyzej)***
def return_sex_and_birth_date(pesel):
    if is_correct_pesel(pesel):
        return get_sex(pesel) + " - " + get_birth_date(pesel)
    else: 
        return ""

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
