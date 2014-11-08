from __future__ import division
import random



class mine:
    def __init__(self):
        self.on_status=False
        self.blown_status=False

class locations:
    def __init__(self, column, row, max_col, max_row):
        self.row=None
        self.column=None
        self.loc_mine=mine()
        self.marked=False
        self.showing=False
        self.adj_cord=[]
        self.adj_col=[]
        self.adj_row=[]
        self.loc_value=0
        self.adj_col.append(column)
        self.adj_row.append(row)
        if column!=0:
            self.adj_col.append(column-1)
        if column!=max_col-1:
            self.adj_col.append(column+1)
        if row!=0:
            self.adj_row.append(row-1)
        if row!=max_row-1:
            self.adj_row.append(row+1)
        for i in self.adj_col:
            for j in self.adj_row:
                self.adj_cord.append((i,j))
            
        
            
class Game_Board:
    def __init__(self, columns=10, rows=10, num_bombs=10):
        self.rows=rows
        self.columns=columns
        self.total_space=rows*columns
        self.board={}
        self.keys=[]
        for i in range(columns):
            for k in range(rows):
                self.board[(i, k)]=locations(i, k, columns, rows)
                self.keys.append((i,k))
                
    def player_pick(self, row, column):
        if (row, column) in self.board and self.board[(row, column)].showing==False:
            if self.board[(row,column)].loc_mine.on_status==False:
                if all(self.board[adjacents].loc_mine.on_status==False for adjacents in self.board[(row,column)].adj_cord):
                    self.board[(row,column)].showing=True
                    self.board[(row,column)].loc_value='x'
                    for adj in self.board[(row,column)].adj_cord:
                       self.board[adj].showing=True
                       self.board[adj].loc_value='x'
                       
                else:
                    adj_bombs=0
                    for i in self.board[(row, column)].adj_cord:
                       if self.board[i].loc_mine.on_status==True:
                           adj_bombs=adj_bombs+1
                           self.board[(row,column)].loc_value=adj_bombs
                           self.board[(row,column)].showing=True
                return 1
            else:
                print "YOU LOSE!!"
                return 0
        else:
            return 2
            print "the coordinates you picked are not on the board"

            
    def place_bombs(self, numb_bombs):
        bombs_grid=random.sample(self.keys, numb_bombs)
        for bombs_locs in bombs_grid:
            self.board[bombs_locs].loc_mine.on_status=True
    def print_board(self):
        rows_to_print=[]
        current_row=[]
        for i in range(self.columns):
            for j in range(self.rows):
                current_row.append(self.board[(i,j)].loc_value)
            rows_to_print.append(current_row)
            current_row=[]
        for k in rows_to_print:
            print k
                
        
                       


def Game():
    print "Your Game will start now \n Pick a number of columns and rows each 2 or greater \n if your rows or columns is less than 2 we will use the default size of 10X10"
    try:
        rows=int(raw_input("Enter number rows \n"))
    except:
        print "you made some error entering the number of rows"
        rows=10
    try:
        columns=int(raw_input("Enter number of columns \n"))
    except:
        print "you made some error entering the number of columns"
        columns=10
        
    if rows<2 or columns<2:
        rows=10
        columns=10
    
        
    board_size=rows*columns
    print "Enter the number of mines. It must be less than %d" %board_size
    number_of_mines=int(raw_input())

    Board=Game_Board(columns, rows)
    Board.place_bombs(number_of_mines)
    playing_status=True
    
    while playing_status==True:
        Board.print_board()
        try:
            pick_row=int(raw_input("pick row"))
        except:
            print "ENTER A NUMBER"
            continue
            
        try:
            pick_column=int(raw_input("pick column"))
        except:
            print "ENTER A NUMBER"
            continue
            
        result=Board.player_pick(pick_row,pick_column)
        if result==0:
            break
        
        
Game()       
        
        
        
    
        
        

        
