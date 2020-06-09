'''
Tic Tac Toe 1.0
Developed by Sean Kaczanowski
No Copyright
May 2020

Functional Tic Tac Toe Game
- Still in development!
- One or Two Player Mode 
- Gameboard Graphics with Xs and Os 
- Function to determine if win outcome is met 
- Computer Player Artificial Intelligence

Known Bugs
- Win does not terminate getatt
- Can replay space already played
- Wrong input accepted
'''

import random # For computer AI decision making

i = 0 # Game Loop
while i == 0:

  # Title Screen
  print('+-----------+')
  print('| T | I | C |')
  print('|---+---+---|')
  print('| T | A | C |')
  print('|---+---+---|')
  print('| T | O | E |')
  print('+-----------+')
  print('')
  print('Main Menu')
  print('=========')
  print('1. One Player')
  print('2. Two Player')
  print('3. Quit')
  print('')
  
  
  '''
  Lists And Functions Section
  '''

  # While Loop Variables
  j = 0
  k = 0

  # Gamespace List
  gamespace = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # List to record turns of each player throughout game

  # Win Conditions List
  win_outcomes = [[0, 0, 0], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]] # List of winning outcomes - [0, 0, 0] sublist used as null list for index[0]
 
  # Player Turn Function
  def player_turn(player, symbol): # Function for player's move
    for i in range(len(gamespace)):
        if i == int(player):
          gamespace[i] = symbol
  
  # Computer Turn Function
  def computer_turn(symbol):
    x = 0
    while x == 0:
      computer = random.randint(1, 9)
      if gamespace[computer] != 'X' or 'O':
        x = 1
        gamespace[computer] = symbol
      else:
        x = 0
  
  # Gameboard Function
  def gameboard(): # Function to display the gameboard for playing
    print(' ' + gamespace[1] + ' | ' + gamespace[2] + ' | ' + gamespace[3] + ' ')
    print('---+---+---')
    print(' ' + gamespace[4] + ' | ' + gamespace[5] + ' | ' + gamespace[6] + ' ')
    print('---+---+---')
    print(' ' + gamespace[7] + ' | ' + gamespace[8] + ' | ' + gamespace[9] + ' ')

  # Outcome Function
  def outcome(symbol): # Function to isolate the indices where X and O are and determine if the symbol has made a line of 3 to win
    symbol_space = [i for i, x in enumerate(gamespace) if x == symbol] # Determines where the index for where all the symbol is
    for l in range(len(win_outcomes)): # Loop to check if win condition is met
      if set(symbol_space) & set(win_outcomes[l]) == set(win_outcomes[l]):
        print('')
        print(symbol + ' Wins!')

  # Function for Player Input
  def player_input(number):
    k = 0
    while k == 0:
      player = input('Player ' + str(number) + ': ')
      if player == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
        k = 1
        return player
      else:
        print('Error. Try Again. Press # 1 - 9 and Enter')
      
  
  '''
  Main Menu Selection
  '''
  
  # Main Menu Selection
  game = input('Press # and Enter: ') # Variable for game mode or quit
  
  # Quit Option
  if game == '3': # Quit Option
    quit()

  '''
  Game Modes
  '''
  
  # Two Player Mode

  if game == '2':
  
    print('')
    print('Two Player Mode')
    print('')
    
    gameboard() # Displays to show the numbers for the spaces that can be played
    
    for i in range(len(gamespace)): # Resets the list to show only blanks until played 
      gamespace[i] = ' '   
    
    j = 0 # 2 Player Mode Game Loop
    while j == 0:

      print('')
      player1 = player_input(1)
      player_turn(player1, 'X') # Player 1's turn committed to gamespace

      print('')
      gameboard()
      outcome('X') # Checks if X wins

      print('')
      player2 = player_input(2)
      player_turn(player2, 'O') # Player 2's turn committed to gamespace
      
      print('')
      gameboard()
      outcome('Y') # Checks if O wins

  # One Player Mode
  if game == '1': # 1 Player Mode

    print('')
    print('One Player Mode')
    print('')
    
    gameboard() # Displays to show the numbers for the spaces that can be played

    for i in range(len(gamespace)): # Resets the list to show only blanks until played 
      gamespace[i] = ' '
  
    j = 0 # 2 Player Mode Game Loop
    while j == 0:

      print('')
      player1 = player_input(1)
      player_turn(player1, 'X') # Player 1's turn committed to gamespace

      print('')
      gameboard()
      outcome('X') # Checks if X wins

      print('')
      computer_turn('O')

      print('')
      gameboard()
      outcome('O')
