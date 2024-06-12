word_list = ['hello', 'world', 'government','important', 'icecream', 'school', 'colleage', 'programmer']

# 6 stage
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
GREEN = '\033[92m'
RESET = '\033[0m'
YELLOW = '\033[93m'

# random choose a word
import random
choosen_word = random.choice(word_list)
print(logo)
print(f"Shhh...Your choosen word is: {choosen_word}")
print('-'*50)
# create list of underscore match choosen word
blank_list = []
for i in range(len(choosen_word)):
    blank_list.append('_')

end_of_game = False 
current_state = 0
if_win = False

while not end_of_game and current_state < len(stages): 
    # check if the user won
    if not '_' in blank_list:
        end_of_game = True
        if_win = True
        print(blank_list)
        print("You won!!!")
    # guess a letter (user input)
    guess = input("Guess a letter: (just 1 letter)\n").lower()
    if guess in blank_list:
        print(f"{YELLOW}You've already guess {guess}.{RESET}")
        print(''.join(blank_list))
        continue

    # replace if guess letter exists
    count = 0
    for i in range(len(choosen_word)):
        if guess == choosen_word[i]:
            blank_list[i] = guess
            count += 1
    print(f"{GREEN}There are {count} letter in word.{RESET}")
    print(''.join(blank_list))
    
    # update state if letter doesnt exist
    if guess not in choosen_word:
        current_state += 1
    
    print(stages[6 - current_state])

# check if user lose
if not if_win:
    print("You lose!!!")
