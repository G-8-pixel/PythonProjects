# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 01:44:24 2021

@author: mehdiyeva

"""
# print even numbers in the range of first 20 numbers
i = 0
for i in range(20):
    if i%2==0:
     print('cüt ededler: ', i )
    i+=1

i = 0
while i<=20:
    print(i)
    i+=2 #i=i+2


num = 7
if num > 3:
    print('3')
    if num < 5:
        print('5')
        if num == 7: #bu if yuxardaki if'in icinde oldugu ucun, eger o if dogru olmasa bu altdaki oxunmur.
                     #Meselen num = 7 gotursen, bu if dogru olsa bele, yuxaridaki dogru olmadigi ucun oxunmayacaq bu.
            print('7')

#PROJECTS FOR JUNIOR PYTHON DEVELOPERS
"""Odd or even?
Welcome a user then ask them for a number between 1 and 1000.
When the user gives you the number, you check if it's odd or even and then you print a message letting them know."""

numb = int(input ('What number are you thinking? '))
#numb = int(num)
#for num in range(1,1000):
if (numb % 2)==0 and numb in range(1,1000):
     print('It is an even number')
elif numb not in range(1, 1000): #or numb < 1 or numb > 1000:
    print('Out of range! Choose a number between 1-1000: ')
else:
    print("That's an odd number! Have another?")

"""Word count:
Ask the user what's on their mind. Then after the user responds,
count the number of words in the sentence and print that as an output."""
#Count number of words in text file:
text = open('Data.txt') #use the existing text
data = text.read()
words = data.split()
print("oh nice, you just told me what's on your mind in " + str(len(words)), "words!")

#alternatively, ask user the text
strLine = input("what's on your mind? ")
count = len(strLine.split())
print("oh nice, you just told me what's on your mind in " + str(count), "words!")

#Count how many times a word occurred in given Text File; using count() method:
file = open('Data.txt')
line = file.read()
print("number of occurences of the word 'the': ", line.count('the'))


#Occurance of each word in the text file
file = open('Data.txt')
counts = {}
for line in file:
    words = line.split()
    #print(words) #List of words
#now we need to count those words in the List and print the count out.
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#print(counts)  #dictionary with words as keys and counts as values
lst = []
for keys, val in counts.items():
    lst.append((val, keys))
#print(lst)
lst = sorted(lst, reverse=True)
print(lst)
for val, keys in lst[:]:
    print(keys, val)

"""Mad libs game:
Ask the user for an input.
This could be anything such as a name, an adjective, a pronoun or even an action.
Once you get the input, you can rearrange it to build up your own story."""
# Loop back to this point once code finishes
#loop = 1

#while (loop < 10):

# All the questions that the program asks the user
noun = input("Choose a noun: ")
p_noun = input("Choose a plural noun: ")
noun2 = input("Choose a noun: ")
place = input("Name a place: ")
adjective = input("Choose an adjective (Describing word): ")
noun3 = input("Choose a noun: ")

# Displays the story based on the users input
print ("------------------------------------------")
print ("Be kind to your",noun,"- footed", p_noun)
print ("For a duck may be somebody's", noun2,",")
print ("Be kind to your",p_noun,"in",place)
print ("Where the weather is always",adjective,".")
print ()
print ("You may think that is this the",noun3,",")
print ("Well it is.")
print ("------------------------------------------")

    # Loop back to "loop = 1"
    #loop = loop + 1

"""Rock, Paper, Scissors
This is a popular game played between two people. Each player gets to form one of three shapes using their hand:"""
from random import randint
print('Welcome to the Rock, Paper, Scissors Game!')
choice = ['rock', 'paper', 'scissors'] #possible choices

def main() :
    player = input('Your choise? ').lower() #we take the lower case, in case user uses upper cases
    computer = choice[randint(0,2)] #computer takes random choices from the given list choices where rock is the 0th item, paper is the 1st and scissors is the 2nd,
    print('Computer chose: ', computer)
    if player == computer:
        print('Draw')
    elif player == 'rock' and computer =='paper':
        print ('Computer wins')
    elif player == 'paper' and computer == 'scissors':
        print('Computer wins')

    elif player == 'scissors' and computer== 'rock' :
        print('computer wins')
    elif player == 'scissors' and computer == 'paper':
        print ('Player wins')
    elif player == 'rock' and computer == 'scissors':
        print('Player wins')
    elif player == 'paper' and computer == 'rock':
        print('Player wins')
    #main()
main() #with this line together with the one above, the program loops

"""Biography info
Ask a user for their personal information one question at a time. Then check that the information they entered is valid.
Finally, print a summary of all the information they entered back to them.
Example: What is your name? If the user enters * you prompt them that the input is wrong, and ask them to enter a valid name."""

name = input("What's your name? ")
if name == '*':
  print = ('Please enter a valid name! ')

birthDate = input('Date of birth? ')
address = input('Your address? ')
goals = input('Your goals? ')

print ('\n- Name: ', name, '\n- Date of birth: ', birthDate, '\n- Address: ', address, '\n- Personal goals: ', goals)

"""Is a palindrome
Ask the user to give you five words. Then check if any of the five words is a palindrome.
A palindrome is a word that remains the same whether it's read forward or backward.
Example:
madam is a palindrome.
so is malayalam.
But not geeks."""

def convertInputString():
    rawInput = input("\nPlease enter a word, phrase, or a sentence \nto check if it is a palindrome: ")
    rawString = rawInput.lower()
    rawList = list(rawString)
    return rawList

def stripAnalphabetics(dirtyList):
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]
    for character in analphabeticList:
        if character in dirtyList:
            dirtyList.remove(character)
            return stripAnalphabetics(dirtyList)
    return dirtyList

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1]
    if reversedList == straightList:
        return "The text you have entered is a palindrome!"
    else:
        return "The text you have entered is not a palindrome."

def main():
    print("\nPalindrome checker")
    originalList = convertInputString()
    originalList = stripAnalphabetics(originalList)
    palindromeCheck = runPalindromeCheck(originalList)
    print(palindromeCheck)

main()
