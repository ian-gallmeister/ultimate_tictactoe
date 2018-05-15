from __future__ import print_function
from tictactoe import tictactoe

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
# Draw board
# Select number
# Check number for validity
# Set number in values list
# Check if has won - if so, break
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
  games = [ tictactoe() for i in range(9) ]

  def draw( self ):
    pieces = []
    #Build lines to draw for each individual game
    #Left to right, down to up
    for game in self.games:
      game.winner = 'O'
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
  


if __name__ == '__main__':
  game = ultimate_tictactoe()
  game.play()
