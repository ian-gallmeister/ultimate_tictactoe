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
  #Don't __init__ it so can use for ultimate tictac
  dividing_line = "-----------"
  play_line = " {} | {} | {} "
  values = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  current_player = 'X'
  winning_combos = [ [0,1,2], [3,4,5], [6,7,8], #Horizontal
                     [0,3,6], [1,4,7], [2,5,8], #Vertical
                     [0,4,8], [2,4,6] ]         #Diagonal
  winner = None

  #def __init__( self ):
  #  self.dividing_line = "-----------"
  #  self.play_line = " {} | {} | {} "
  #  self.values = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

  def play( self ):
    while True:
      self.draw()
      self.select()
      if self.is_winning():
        break
      self.swap_players()
      

  def one_turn( self ):
    self.draw()
    self.select()
    self.is_winning()
    self.swap_players()

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
        print( '{win} WINS!  Congrats!'.format(win=self.winner) )
        return True
    return False #Only gets here if no winners

  def select( self ):
    #Select spot 
    while True:
      #Prevent stupidity
      if sys.version_info[0] == 2: #For old python
        char = raw_input( 'Player: {}\nPlease select an open spot: '.format(self.current_player) )
      else: #For sensible python
        char = input( 'Player: {}\nPlease select an open spot: '.format(self.current_player) )
      if self.validate( char ):
        self.values[ int(char) - 1 ] = self.current_player #Uhhh ... keep track of this
        break

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
    #Elimintate digits < 1 and > 9
    char = int(char)
    if char < 1 or char > 9:
      print( 'Please enter an integer from 1 to 9\n', file=sys.stderr )
      return False
    #Eliminate already-chosen characters
    if self.values[ char - 1 ] in ['X', 'O']:
      print( 'That spot has already been taken.\n', file=sys.stderr )
      return False
  
    return True


def select_spot( values, char ):
  while True:
    spot = input( 'Please choose the spot to fill in (or press h for help): ' )
    if spot in ['h','H']:
      draw_board( ['1','2','3','4','5','6','7','8','9'])
      print( 'Please select the number that corresponds to the drawing above.\nIf the spot chosen has not been taken already, it will select it for {}.\nIf it has been chosen, it will complain and ask you to choose again.\n\n'.format(char) )
    elif valid_number( spot, values, char ):
      values[ int(spot) - 1 ] = char
      break

def valid_number( spot, values ):
  #All remaining are digits
  if not spot.isdigit():
    print( 'Invalid character.  Please select a valid integer', file=sys.stderr )
    return False
  
  spot = int( spot )
  #All remaining are in the right area
  if spot < 0 or spot > 10:
    print( 'Invalid number.  Please select a number from 1 to 9', file=sys.stderr )
    return False
  
  #All remaining aren't taken already
  if values[spot - 1] in ['X','O']:
    print( 'This spot has been taken', file=sys.stderr )
    return False
    
  values[ spot - 1 ] = char


if __name__ == '__main__':
  game = tictactoe()
  game.play()
