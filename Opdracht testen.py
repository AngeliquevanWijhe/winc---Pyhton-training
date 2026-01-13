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
