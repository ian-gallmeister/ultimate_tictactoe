from __future__ import print_function
import sys

"""
 X | X | X
-----------
 X | X | X
-----------
 X | X | X
"""

#Turn
# Draw board
# Select number
# Check number for validity
# Set number in values list
# Check if has won - if so, break
# Change user and repeat

class tictactoe():
  #Create play function to automate a single game
  dividing_line = "-----------"
  play_line = " {} | {} | {} "
  winning_combos = [ [0,1,2], [3,4,5], [6,7,8], #Horizontal
                     [0,3,6], [1,4,7], [2,5,8], #Vertical
                     [0,4,8], [2,4,6] ]         #Diagonal

  #This stays a class attribute - I want all nine to use the same value 
  current_player = 'X'

  def __init__( self ):
    #These need to be different for each instance
    self.values = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    self.winner = None

  def play( self ):
    while True:
      self.draw()
      self.select()
      if self.is_winning():
        break
      self.swap_players()
      
  def one_turn( self, cp ):
    self.draw()
    number = self.select( cp )
    self.is_winning()
    self.swap_players()
    return (number-1)

  def draw( self ):
    row1 = self.play_line.format( self.values[6], self.values[7], self.values[8] )
    row2 = self.play_line.format( self.values[3], self.values[4], self.values[5] )
    row3 = self.play_line.format( self.values[0], self.values[1], self.values[2] )
    board = '\n'.join([row1, self.dividing_line, row2, self.dividing_line, row3])
    print( board )

  def is_winning( self ):
    for combo in self.winning_combos:
      #If a combo has won, return True, congratulate winner
      if self.values[combo[0]] == self.values[combo[1]] == self.values[combo[2]]:
        self.winner = self.values[combo[0]]
        print( '{win} wins this small game!  Congrats!'.format(win=self.winner) )
        return True
    return False #Only gets here if no winners

  def select( self, cp ):
    #Select spot 
    while True:
      #Prevent stupidity
      if sys.version_info[0] == 2: #For old python
        char = raw_input( '\nPlayer: {}\nPlease select an open spot: '.format(cp) )
      else: #For sensible python
        char = input( '\nPlayer: {}\nPlease select an open spot: '.format(cp) )
      if self.validate( char ):
        self.values[ int(char) - 1 ] = cp #Uhhh ... keep track of this
        break
    return int(char)

  def swap_players( self ):
    if self.current_player == 'X':
      self.current_player = 'O'
    else:
      self.current_player = 'X'
  
  def validate( self, char ):
    #Eliminate non-digits
    if not char.isdigit():
      print( 'Please enter an integer\n', file=sys.stderr )
      return False
    #Elimintate igits < 1 and > 9
    char = int(char)
    if char < 1 or char > 9:
      print( 'Please enter an integer from 1 to 9\n', file=sys.stderr )
      return False
    #Eliminate already-chosen characters
    if self.values[ char - 1 ] in ['X', 'O']:
      print( 'That spot has already been taken.\n', file=sys.stderr )
      return False
  
    return True

if __name__ == '__main__':
  game = tictactoe()
  game.play()
