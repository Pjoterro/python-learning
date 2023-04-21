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

print("\nTEST has_only_digits(pesel):")
pesel_with_forbidden_chars = "111a2 7^719"
print("- INPUT: " + pesel_with_forbidden_chars)
has_only_digits_status = "Working" if has_only_digits(pesel_with_forbidden_chars) == False else "Not working"
print("- has_only_digits status: " + has_only_digits_status)
pesel_with_correct_chars = "11102576719"
print("- INPUT: " + pesel_with_correct_chars)
has_only_digits_status = "Working" if has_only_digits(pesel_with_correct_chars) == True else "Not working"
print("- has_only_digits status: " + has_only_digits_status)

print("\nTEST has_correct_number_of_digits(pesel):")
pesel_too_long = "950813119921"
print("- INPUT: " + pesel_too_long)
has_correct_number_of_digits_status = "Working" if has_correct_number_of_digits(pesel_too_long) == False else "Not working"
print("- has_correct_number_of_digits status: " + has_correct_number_of_digits_status)
pesel_too_short = "9508131199"
print("- INPUT: " + pesel_too_short)
has_correct_number_of_digits_status = "Working" if has_correct_number_of_digits(pesel_too_short) == False else "Not working"
print("- has_correct_number_of_digits status: " + has_correct_number_of_digits_status)
pesel_correct_length = "95081311992"
print("- INPUT: " + pesel_correct_length)
has_correct_number_of_digits_status = "Working" if has_correct_number_of_digits(pesel_correct_length) == True else "Not working"
print("- has_correct_number_of_digits status: " + has_correct_number_of_digits_status)

print("\nTEST has_correct_controll_number(pesel):")
pesel_with_incorrect_control_number = "89021766888"
print("- INPUT: " + pesel_with_incorrect_control_number)
has_correct_controll_number_status = "Working" if has_correct_controll_number(pesel_with_incorrect_control_number) == False else "Not working"
print("- has_correct_controll_number status: " + has_correct_controll_number_status)
pesel_with_correct_control_number = "89021766887"
print("- INPUT: " + pesel_with_correct_control_number)
has_correct_controll_number_status = "Working" if has_correct_controll_number(pesel_with_correct_control_number) == True else "Not working"
print("- has_correct_controll_number status: " + has_correct_controll_number_status)

print("\nTEST is_correct_pesel(pesel):")
incorrect_pesel = "89O21766887"
print("- INPUT: " + incorrect_pesel)
is_correct_pesel_status = "Working" if is_correct_pesel(incorrect_pesel) == False else "Not working"
print("- is_correct_pesel status: " + is_correct_pesel_status)
correct_pesel = "89021766887"
print("- INPUT: " + correct_pesel)
is_correct_pesel_status = "Working" if is_correct_pesel(correct_pesel) == True else "Not working"
print("- is_correct_pesel status: " + is_correct_pesel_status)

print("\nTEST get_sex(pesel):")
incorrect_sex_pesel = "06100999779"
print("- INPUT: " + incorrect_sex_pesel)
get_sex_status = "Working" if get_sex(incorrect_sex_pesel) == "" else "Not working"
print("- get_sex status: " + get_sex_status)
correct_male_pesel = "49120559317"
print("- INPUT: " + correct_male_pesel)
get_sex_status = "Working" if get_sex(correct_male_pesel) == "Male" else "Not working"
print("- get_sex status: " + get_sex_status)
correct_female_pesel = "26010253263"
print("- INPUT: " + correct_female_pesel)
get_sex_status = "Working" if get_sex(correct_female_pesel) == "Female" else "Not working"
print("- get_sex status: " + get_sex_status)


print("\nTEST get_birth_date(pesel):")
incorrect_birth_pesel = "42050138336"
print("- INPUT: " + incorrect_birth_pesel)
get_birth_date_status = "Working" if get_birth_date(incorrect_birth_pesel) == "" else "Not working"
print("- get_birth_date status: " + get_birth_date_status)
correct_birth_pesel = "91071558279"
print("- INPUT: " + correct_birth_pesel)
get_birth_date_status = "Working" if get_birth_date(correct_birth_pesel) == "15-07-1991" else "Not working"
print("- get_birth_date status: " + get_birth_date_status)

print("\nTEST return_sex_and_birth_date(pesel):")
incorrect_pesel = "56042O37692"
print("- INPUT: " + incorrect_pesel)
return_sex_and_birth_date_status = "Working" if return_sex_and_birth_date(incorrect_pesel) == "" else "Not working"
print("- return_sex_and_birth_date status: " + return_sex_and_birth_date_status)
correct_male_pesel = "56042037692"
print("- INPUT: " + correct_male_pesel)
return_sex_and_birth_date_status = "Working" if return_sex_and_birth_date(correct_male_pesel) == "Male - 20-04-1956" else "Not working"
print("- return_sex_and_birth_date status: " + return_sex_and_birth_date_status)
correct_female_pesel = "38040283442"
print("- INPUT: " + correct_female_pesel)
return_sex_and_birth_date_status = "Working" if return_sex_and_birth_date(correct_female_pesel) == "Female - 02-04-1938" else "Not working"
print("- return_sex_and_birth_date status: " + return_sex_and_birth_date_status)
