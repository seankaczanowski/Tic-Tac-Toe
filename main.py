'''
Tic Tac Toe 1.0
'''

print('+-----------+')
print('| T | I | C |')
print('|---+---+---|')
print('| T | A | C |')
print('|---+---+---')
print('| T | O | E |')
print('+-----------+')
print('')
print('Main Menu')
print('=========')
print('1. One Player')
print('2. Two Player')
print('3. Quit')
print('')

i = 0 # Game Loop
while i == 0:
  
  # Variables for gameboard spaces
  one = ' '
  two = ' '
  three = ' '
  four = ' '
  five = ' '
  six = ' '
  seven = ' '
  eight = ' '
  nine = ' '

  gameboard = [[' ', one, ' | ', two, ' | ', three],['---', '+', '---', '+', '---'],[' ', four, ' | ', five, ' | ', six],['---', '+', '---', '+', '---'],[' ', seven, ' | ', eight, ' | ', nine]]
  
  
  game = input('Press # and Enter: ') # Variable for game mode or quit
  
  if game == '3': # Quit Option
    quit()

  elif game == '2': # 2 Player Mode
    for i in range(len(gameboard)): # Gameboard printing of previous turns plus current turn
      print(''.join(gameboard[i]))
    
  

