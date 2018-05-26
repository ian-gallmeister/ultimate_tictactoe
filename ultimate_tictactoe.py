from __future__ import print_function
from tictactoe import tictactoe
import sys

"""
            |             |
 X | X | X  |  X | X | X  |  X | X | X 
----------- | ----------- | ----------- 
 X | X | X  |  X | X | X  |  X | X | X 
----------- | ----------- | ----------- 
 X | X | X  |  X | X | X  |  X | X | X 
            |             |
----------------------------------------
            |             |
 X | X | X  |  X | X | X  |  X | X | X 
----------- | ----------- | ----------- 
 X | X | X  |  X | X | X  |  X | X | X 
----------- | ----------- | ----------- 
 X | X | X  |  X | X | X  |  X | X | X 
            |             |
----------------------------------------
            |             |
 X | X | X  |  X | X | X  |  X | X | X 
----------- | ----------- | ----------- 
 X | X | X  |  X | X | X  |  X | X | X 
----------- | ----------- | ----------- 
 X | X | X  |  X | X | X  |  X | X | X 
            |             |

\   /
 \ /
  X
 / \
/   \

   _
  / \
 |   |
 |   |
  \_/

"""

#Turn
# Draw big board
# If prev choice leads to completed board
#  Find out which small_games are won, create small board with those selected in case it is needed
#  Ask user to choose a board
# Draw small board
# Run turn on small board, saving selection
# Check if has won small game - if so, break
# Change user and repeat

class ultimate_tictactoe():
  first_last = '            |             |'
  intermediate = '            |             |\n----------------------------------------\n            |             |'
  line = '{:11} | {:11} | {:11}'
  small_line = ' {} | {} | {}'
  smallseparator = '-----------'
  big_x = [ '   \   /', '    \ / ', '     X  ', '    / \ ', '   /   \\' ]
  big_o = [ '     _  ', '    / \ ', '   |   |', '   |   |', '    \_/ ' ]

  #Bottom left first, to the right and up
  current_player = 'X'
  small_game = None
  def __init__( self ):
    self.games = [ tictactoe() for i in range(9) ]

  def one_turn( self ):
    #Draw big board
    self.draw()
    #First turn.  Select small game then select a spot on small game
    if self.small_game == None:
      if sys.version_info[0] == 2:
        char = raw_input( 'No small game has been selected.  Please select one using the small board as a reference: ' )
      else:
        print( 'No small game has been selected.  Using the small board as a reference,' )
        char = input( 'please select a game to start from: ' )
    # If prev choice leads to completed board
    if self.games[self.small_game].winner != None:
      #Find which small_games are won, create small board to match 
      tmp = tictactoe()
      for _ in range(self.games):
        if self.games.winner == 'X':
          tmp.values[_] = 'X'
        elif self.games.winner == 'O':
          tmp.values[_] = 'O'
      tmp.draw()
      # Ask user to choose a board
      print( "Your next move would be in a completed board.  Please select the next board to move from." )
      self.small_game = tmp.select()
    # Draw small board
    self.games[self.small_game].draw()
    # Run turn on small board, saving selection
    self.small_game = self.games[self.small_game].one_turn()
    # Check if has won small game
    self.games[self.small_game].is_winning()
    # Check if has won big game
    self.is_winning()
    self.swap_players()
      
  def is_winning( self ):
    for combo in self.winning_combos:
      #If a combo has won, return True, congratulate winner
      if self.values[combo[0]] == self.values[combo[1]] == self.values[combo[2]]:
        self.winner = self.values[combo[0]]
        print( '{win} WINS!  Congrats!'.format(win=self.winner) )
        return True
    return False #Only gets here if no winners

  def draw( self ):
    pieces = []
    #Build lines to draw for each individual game
    #Left to right, down to up
    for game in self.games:
      if game.winner == 'X':
        pieces.append(self.big_x)
      elif game.winner == 'O':
        pieces.append(self.big_o)
      else:
        pieces.append([ self.small_line.format(game.values[6],game.values[7],game.values[8]),
          self.smallseparator,
          self.small_line.format(game.values[3],game.values[4],game.values[5]),
          self.smallseparator,
          self.small_line.format(game.values[0],game.values[1],game.values[2])
        ])

    #Build the big one
    bottom_row = [ self.line.format(pieces[0][0],pieces[1][0],pieces[2][0]),
      self.line.format(pieces[0][1],pieces[1][1],pieces[2][1]),
      self.line.format(pieces[0][2],pieces[1][2],pieces[2][2]),
      self.line.format(pieces[0][3],pieces[1][3],pieces[2][3]),
      self.line.format(pieces[0][4],pieces[1][4],pieces[2][4]),
    ]  
    middle_row = [ self.line.format(pieces[3][0],pieces[4][0],pieces[5][0]),
      self.line.format(pieces[3][1],pieces[4][1],pieces[5][1]),
      self.line.format(pieces[3][2],pieces[4][2],pieces[5][2]),
      self.line.format(pieces[3][3],pieces[4][3],pieces[5][3]),
      self.line.format(pieces[3][4],pieces[4][4],pieces[5][4]),
    ]
    top_row = [ self.line.format(pieces[6][0],pieces[7][0],pieces[8][0]),
      self.line.format(pieces[6][1],pieces[7][1],pieces[8][1]),
      self.line.format(pieces[6][2],pieces[7][2],pieces[8][2]),
      self.line.format(pieces[6][3],pieces[7][3],pieces[8][3]),
      self.line.format(pieces[6][4],pieces[7][4],pieces[8][4]),
    ]
    all_lines = [self.first_last] + top_row + [self.intermediate] + middle_row + [self.intermediate] + bottom_row + [self.first_last]
    print( '\n'.join(all_lines) )
    #5 lines for big X or big O

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


if __name__ == '__main__':
  game = ultimate_tictactoe()
  game.play()
