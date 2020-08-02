#for item in list:
#    if conditional:
#        expression

# [expression FOR item IN list IF condition]

x = [i for i in range(0,9) if i % 2 == 0]

print("X: ", x)

# ------------------------------------------------------------------

listOfWord = ["EMILIANO", "GABRIELA", "CLAUDIA", "EMILIO", "KAREN"]

names = [names[::-1] for names in listOfWord]

print("Nombres: ", names)

# ------------------------------------------------------------------

listOfDigits = "EMILIANO GABRIELA 12345 EMILIANO GABRIELA 54321"

numbers = [x for x in listOfDigits if x.isdigit()]

print("Numeros: ", numbers)

# ------------------------------------------------------------------

By_7 = [x for x in range(1, 1000) if x % 7 == 0]

print("Divisible by 7: ", By_7)

# ------------------------------------------------------------------

Have_3 = [x for x in range(1, 1000) if '3' in str(x)]

print("Have a 3: ", Have_3)

# ------------------------------------------------------------------

MySpaces = "EMILIANO GABRIELA 12345 EMILIANO GABRIELA 54321"

int_spaces = [ e for e in MySpaces if e.isspace() ]

print("Espacios en una Cadena: ", len(int_spaces) )

# ------------------------------------------------------------------

MyVowels = "EMILIANO GABRIELA 12345 EMILIO GABRIELA 54321"

new_vowels = ''.join( c for c in MyVowels if c not in 'AEIOUaeiou' )

print("Vocales: ", new_vowels)

# ------------------------------------------------------------------

Less_Than_4 = "EMILIANO GABRIELA EMY CLAUDIA EMILIO KAREN"

int_less_4 = [c for c in Less_Than_4.split() if len(c) < 4]

print("Menor a 4 Letras: ", int_less_4)

# ------------------------------------------------------------------

#Use a dictionary comprehension to count the length of each word in a sentence.
sentence = 'Use a dictionary comprehension to count the length of each word in a sentence'
results = { word:len(word) for word in sentence.split() }
print(results)

#Use a nested list comprehension to find all of the numbers from 1-1000 that 
#are divisible by any single digit besides 1 (2-9)
# comprehension testing truth for divisibilty: [True for divisor in range(2,10) if number % divisor == 0]
results = [number for number in range(1,1001) if True in [True for divisor in range(2,10) if number % divisor == 0]]
print(results)

#For all the numbers 1-1000, use a nested list/dictionary comprehension to 
#find the highest single digit any of the numbers is divisible by.
# List comprehension for providing a list of all of the numbers a number is divisible by: divisor_list:
#       [divisor for divisor in range(1,1001) if number % divisor == 0]
results = {number:max([divisor for divisor in range(1,10) if number % divisor == 0]) for number in range(1,1001)}
print(results)