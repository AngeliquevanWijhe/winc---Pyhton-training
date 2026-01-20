print ("Hi, my name is Mark!")
print ("Python can waltz!")
print ("one", "two", "three")

print (16)
print(1,2,3)
number = 3
name = "Adrie" 
vegetable = "carrot"
print (vegetable)
# volgende opdracht gaat over quatation marks
example_one = 'I\'m a string'
example_two = "I'm a string"
example_three = 'He said: "I\'m a string"'
print(example_one, ",", example_two, ",", example_three)
#using the escape character
print('I\'m a string\nI\'m a string\n')
#using the tab character
print('I\'m a string\tI\'m a string\n')

a = str(5)
print(a in 'We were lucky that they had a table for 5. ')

#also like this
b = '5'
print( b in 'We were lucky that they had a table for 5.')

#this will result in an error
x = "5"
print(x in 'We were lucky that they had a table for 5.')

#hieronder gaan we vergelijken
a = 'Me'
b = 'You'
print(a == b)
#returns False since the values are different
print(a != b)
#returns True since the values are different

x = 3
y = 3
print(x == y)
#returns True since the values are equal

#hieronder gaan we indexeren ofwel posities van letters in een string opvragen
letter_grades = 'ABCDEF'
print(letter_grades[0])
print(letter_grades[3])
#now with negatives
print(letter_grades[-1])
print(letter_grades[-3])
#This one evaluates to True, as they are the same
print(letter_grades[4] == letter_grades[-2])

# Hieronder gaan we de find functie gebruiken om de index van een letter of substring te vinden
full_name = 'John Doe'
#find the index of the space in the name
print(full_name.find(' '))

nonsense_string = 'ahehtreoieotoththahthtototohthththoaosmdbnxhjaoaoaoaoehbeotothbaoabaoasdorfohbaofb'
#where is the x?
print(nonsense_string.find('x'))

#hieronder gaan we slices maken van strings op basis van de posities
waltz = 'onetwothree'
print(waltz[0:3])
# We don't need to specify the 0 if we start at the beginning
print(waltz[:3])
print(waltz[3:6])
print(waltz[6:11])
# Same goes for the end -- we can leave it empty
print(waltz[6:])
# We can specify a step size if we don't want a continuous slice
print(waltz[0:11:2])
print(waltz[::2]) #this is almost the same
#use the find method to find the index
print(waltz[:waltz.find('t')])
#you can then move around that index
print(waltz[:waltz.find('t') + 1])

#hieronder gaan we de lengte van een string opvragen met de len() functie
sentence = 'The length of this string is:'
print(len(sentence))
print(sentence, len(sentence))
print('Wait.. You just made it longer!')

#hieronder gaan we f-strings gebruiken om variabelen in strings te plaatsen
answer = 42
naam = "Mark"
qa = f"The answer is... {answer} and my name is {naam}"
print(qa)

print (17//3)
print (17%3)
print (2 ** (3 + 3) - 2 * 11 )

one = 5 % (2 + 3) == 0
two = ("Piano"[0:0] == "" + "Guitar"[0:0])
three = 2 ** 3 + 3 - 2 * 11 == 42

print(one, two, three)

# les conditionals
def eligible_to_vote(age, nationality   ):
    if age >= 18 and nationality == 'Italian':
        print('Bene!')
        return True
    elif age >= 25 and nationality == 'Portuguese':
        print('Sim!')
        return True
    elif age >= 31 and nationality == 'Dutch':
        print('Top!')
        return True
    elif age >= 19  and nationality == 'Malawian':
        print('Iya!')
        return True
    else:
        return False
print(eligible_to_vote(20, 'Italian'))
print(eligible_to_vote(31, 'Dutch'))
print(eligible_to_vote(20, 'French'))

nice_weather = False
going_outside = True if nice_weather else False
print(going_outside)


#You are not limited to booleans.

nice_weather_odds = .4
party_location = 'inside' if nice_weather_odds < .6 else 'in the yard'
print(party_location)

def bouncer_bot(is_ladies_night, is_woman, is_full, is_drunk, age, is_wearing_cool_clothes):

    # Add your code below! #
    if age < 18:
        return "You're too young. Please come back when you're older."
    if is_drunk:
        return "Please come back when you're sober."
    if is_ladies_night and is_woman == False:
        return "It's ladies night. Come back another night."
    if is_full:
        return "No, too busy right now."
    if not is_wearing_cool_clothes:
        return "No, too busy right now."
    return "Welcome!"
print(bouncer_bot(False, False, False, False, 17, False))
print(bouncer_bot(False, False, False, True, 25, False))
print(bouncer_bot(True, False, False, False, 25, False))
print(bouncer_bot(False, False, True, False, 25, False))
print(bouncer_bot(False, False, False, False, 25, True))

#les data collections
#INDEXING AND SLICING
example_list = ['zeroth', 'first', 'second', 'third']
# Get the zeroth item.
print(example_list[0])
# Get the second item.
print(example_list[2])
# Get a slice of the list
print(example_list[0::2])

#COMPARISION AND ORDER
example_list_a = [1, 2, 3]
example_list_b = [3, 2, 1]
print(example_list_a == example_list_b) 
#evaluates to False

#CASTING
example_list_c = ['this', 'is', 'fun']
print(str(example_list_c))
print(list(str(example_list_c)))
#...and so on.

#COMMON OPERATIONS
print(len(example_list)) #4
print(min(example_list_a)) #1
print(example_list_a + example_list_b) #1,2,3,3,2,1
print('second' in example_list) #true

# This works fine
example_list = ['zeroth', 1, 2, 3]
example_list[0] = 0
print(example_list)
# Output: [0, 1, 2, 3]

example_string = ['Gi!']
# The next line results in an error
print(example_string)

set_a = set([1, 2, 3])
set_b = set([3, 4, 5])

# Union
# You can read this as 'set_a or set_b', so: 'any element that is in set a or set b'
print(set_a | set_b)

# Difference
print(set_a - set_b)

# Intersection
print(set_a.intersection(set_b))

# Checking if a set is a subset of another.
# In other words: if the other set includes all of its own elements.
small = set([2, 3])
big = set([1, 2, 3, 4])
print(small.issubset(big))

#Nested dictionaries
product = {
    "name": "tofu",
    "price": 2,
    "producer": {
        "name": "Tofu Company Limited",
        "country_of_origin": "France"
    }
}
print(product["producer"]["country_of_origin"])

students = [
  {
    "name":
    "Ali",
    "family_name":
    "Khan",
    "skills": {
      "Python": "beginner",
      "JavaScript": "expert",
    },
    "certificates": [
      {
        "name": "Back-end Development",
        "date_of_completion": "2022-01-17",
      },
      {
        "name": "Back-end Development",
        "date_of_completion": "2022-01-17",
      },
      {
        "name": "Data Analytics with Python",
        "date_of_completion": "",
      },
    ],
  },
  {
    "name":
    "Jessica",
    "family_name":
    "van Alphen",
    "skills": {
      "Python": "advanced beginner",
      "JavaScript": "beginner",
    },
    "certificates": [
      {
        "name": "Front-end Development",
        "date_of_completion": "",
      },
      {
        "name": "Back-end Development",
        "date_of_completion": "2022-01-17",
      },
      {
        "name": "Data Analytics with Python",
        "date_of_completion": "2020-01-17",
      },
    ],
  },
]

print(students[1]["skills"]["Python"])  # "advanced beginner"
print(students[0]["certificates"][1]["name"])  # "Back-end Development"
print(students[1]["name"] + " " + students[1]["family_name"])  # "Jessica van Alphen"
