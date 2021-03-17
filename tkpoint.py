theBoard = {'top-L':' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L':' ', 'mid-M': ' ', 'mid-R': ' ',
            'bot-L':' ', 'bot-M': ' ', 'bot-R': ' ',}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print('-+-+-')
    print("{0}|{1}|{2}".format(board['bot-L'], board['bot-M'], board['bot-R']))

def numToBoard(num):
    li = ['top-L', 'top-M', 'top-R',
          'mid-L', 'mid-M', 'mid-R',
          'bot-L', 'bot-M', 'bot-R',]
    return li[num - 1]

def validInput(input):
    try:
        temp = int(input)
        return True
    except:
        return False    

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print(f'Turn for {turn}. Move on which space?')
    move = input(">> ")
    
    while True:
        if not validInput(move):
            print(f'Turn for {turn}. Move on which space?')
            move = input(">> ")
            continue
        if int(move) > 0 and int(move) < 10:
            if theBoard[numToBoard(int(move))] == ' ':
                break
            else:
                print(f'Invalid movement.Turn for {turn}. Move on which space?')
                move = input(">> ")
        else:
            print(f'Invalid movement. Turn for {turn}. Move on which space?')
            move = input(">> ")       

    theBoard[numToBoard(int(move))] = turn
    if turn == 'X':
        turn = 'O'

    else:
        turn = 'X'    

printBoard(theBoard)    