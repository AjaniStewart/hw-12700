TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10), (7,7))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

d = { ('a','e','i','o','l','n','r','s','t') : 1, 
      ('d','g') : 2,
      ('b','c','m','p') : 3,
      ('f','h','v','w','y') : 4,
      ('k') : 5,
      ('j','x') : 8,
      ('q','z') : 10
    }
    
def make_scrabble_board():
    board=[]
    for i in range(15):
        line=[]
        for i in range(15):
            line.append('_')
        board.append(line)
    
    
    for r,c in TRIPLE_WORD_SCORE:
        board[r][c] = 'T'

    for r,c in DOUBLE_WORD_SCORE:
        board[r][c] = 'D'

    for r,c in TRIPLE_LETTER_SCORE:
        board[r][c]='t'

    for r,c in DOUBLE_LETTER_SCORE:
        board[r][c] = 'd'
    return board


def print_board(b):
    for line in b:
        print ( ' '.join(line))

def score(l):
    for k,v in d.items():
        if l in k:
            return v


def add_word_across(board,word,r,c):
    #returns the score
    #go to board[r][c]
    #iterate over c (inner array)
    #[c]olumns are elements of outer array
    #[r]ows are elements of inner array
    sum = 0
    multiplier = 1
    for i in range(c,c+len(word)):
        if board[r][i] == 'T':
            multiplier *= 3
        elif board[r][i] == 'D':
            multiplier *= 2
        l = score(word[i-c])
            
        if board[r][i] == 't':
            l *= 3
        if board[r][i] == 'd':
            l *= 2
            
        sum += l
        board[r][i] = word[i-c]

    return  sum*multiplier

def add_word_down(board,word,r,c):
    sum = 0
    multiplier = 1
    for i in range(r,r+len(word)):
        
        if board[i][c] == 'T':
            multiplier *= 3
        elif board[i][c] == 'D':
            multiplier *= 2

        l = score(word[i-r])

        if board[i][c] == 't':
            l *= 3
        if board[i][c] == 'd':
            l *= 2
            
        sum += l
        board[i][c] = word[i-r]

    return  sum * multiplier

board = make_scrabble_board()
print(add_word_down(board,'hello',0,0))
print(add_word_across(board,'hello',0,0))
print_board(board)

