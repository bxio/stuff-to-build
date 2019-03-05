from random import choice
def find(lst, a):
    result = []
    for i, x in enumerate(lst):
        if x == a:
            result.append(i)
    return result


words = ['rhythms', 'reddit', 'constant',
         'manager', 'training', 'hotel', 'destroy']
word = choice(words)
count = 0
chances = 4
letterlist = list(word)
dashlist = []
for l in letterlist:
    dashlist.append('-')
print('Welcome to Hangman\n\nGuess the: ' + str(len(letterlist)) + ' letter word.\n')
print (' '.join(dashlist) + '\n\n')
while count <= chances:
    chancesleft = chances - count
    let = input("Enter a letter: ")
    if let in letterlist:
        indexes = find(letterlist, let)
        for i in indexes:
            dashlist[i] = let
        print('\n' + ' '.join(dashlist) + '\n' + 'Good guess!\n')
    else:
        print('Wrong! Try again!')
        count += 1
        print('Chances left: ' + str(chancesleft) + '\n')
    combined = ''.join(dashlist)
    if combined == word:
        print(f'You win! The word was: {word}')
        break
    if count > chances:
        print(f'Game over. You lose! The word was: {word}')
        break
