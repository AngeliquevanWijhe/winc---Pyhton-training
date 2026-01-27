from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
from helpers import get_countries

def shortest_names(names_countries):
    shortest=min(names_countries, key=len)
    country_list=[]
    for country_name in names_countries:
        if len(country_name)==len(shortest):
            country_list.append(country_name)
    return country_list

def most_vowels(names_countries):
    vowels='aeiouAEIOU'
    leaderboard=[("",0)]
    for country_name in names_countries:
        vowel_count=0
        for lowered_characters in country_name.lower():
            if lowered_characters in vowels:
                vowel_count +=1
        leaderboard.append((country_name, vowel_count))
    
    top_3 = []
    remaining = leaderboard[1:]
    
    for i in range(3):
        if not remaining:
            break
        max_country = remaining[0]
        for country in remaining:
            if country[1] > max_country[1]:
                max_country = country
        top_3.append(max_country[0])
        remaining.remove(max_country)
    
    return top_3
def alphabet_set(countries_abc):
    letters_alphabet=list('abcdefghijklmnopqrstuvwxyz')
    all_countries_used=[]
    for country_name in countries_abc:
        country_name = country_name.lower()
        for character in country_name:
            if character in letters_alphabet:
                letters_alphabet.remove(character)
                if country_name not in all_countries_used:
                    all_countries_used.append(country_name)
        if len(letters_alphabet)==0:
           return all_countries_used

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """


    print(shortest_names(countries))
    print(most_vowels(countries))
    print(alphabet_set(countries))






