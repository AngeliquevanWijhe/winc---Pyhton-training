# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality
    }
    return dict(passport)

def add_stamp(passport, country):
    countries = get_countries()
    if country in countries:
        if country in (passport["place_of_birth"]):
            print("You cannot add a stamp for your country of birth.")
            return passport
        if "stamps" not in passport:
            passport["stamps"] = []
        #passport["stamps"].append(country)
        if country not in passport["stamps"]:
            passport["stamps"].append(country)
      
    return passport

def add_biometric_data(passport, name_bd, value_bd, date_bd):
    if "biometric" not in passport:
        passport["biometric"] = {}
    biometric_data = {
        "date": date_bd,
        "value": value_bd 
    }
    passport["biometric"][name_bd] = biometric_data
    return passport
    


# my_passport = create_passport("Angelique van Wijhe", "1970-06-02", "Netherlands", 1.68, "Dutch")
# print(my_passport)
# my_passport = add_stamp(my_passport, "France")
# print(my_passport)
# my_passport = add_stamp(my_passport, "France")
# print(my_passport)
# my_passport = add_stamp(my_passport, "Germany") 
# print(my_passport)
# my_passport = add_stamp(my_passport, "Netherlands")
# print(my_passport)
# my_passport = add_biometric_data(my_passport,"Haarkleur","Bruin","2026-01-20")
# print(my_passport)
# my_passport = add_biometric_data(my_passport,"Kleur ogen","Geel","2026-02-20")
# print(my_passport['biometric'])

omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_left", "brown", "2022-01-10")
print(omari)