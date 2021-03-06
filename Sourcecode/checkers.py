import random
import copy
#dict of starting board, with number and wether or not there is a piece

def makeboard():
    global board
    board = {57:' ',58:'o',59:' ',60:'o',61:' ',62:'o',63:' ',64:'o',
             49:'o',50:' ',51:'o',52:' ',53:'o',54:' ',55:'o',56:' ',
             41:' ',42:'o',43:' ',44:'o',45:' ',46:'o',47:' ',48:'o',
             33:' ',34:' ',35:' ',36:' ',37:' ',38:' ',39:' ',40:' ',
             25:' ',26:' ',27:' ',28:' ',29:' ',30:' ',31:' ',32:' ',
             17:'x',18:' ',19:'x',20:' ',21:'x',22:' ',23:'x',24:' ',
             9:' ',10:'x',11:' ',12:'x',13:' ',14:'x',15:' ',16:'x',
             1:'x',2:' ',3:'x',4:' ',5:'x',6:' ',7:'x',8:' '}

convert ={'a1':57,'a2':58,'a3':59,'a4':60,'a5':61,'a6':62,'a7':63,'a8':64,
          'b1':49,'b2':50,'b3':51,'b4':52,'b5':53,'b6':54,'b7':55,'b8':56,
          'c1':41,'c2':42,'c3':43,'c4':44,'c5':45,'c6':46,'c7':47,'c8':48,
          'd1':33,'d2':34,'d3':35,'d4':36,'d5':37,'d6':38,'d7':39,'d8':40,
          'e1':25,'e2':26,'e3':27,'e4':28,'e5':29,'e6':30,'e7':31,'e8':32,
          'f1':17,'f2':18,'f3':19,'f4':20,'f5':21,'f6':22,'f7':23,'f8':24,
          'g1':9,'g2':10,'g3':11,'g4':12,'g5':13,'g6':14,'g7':15,'g8':16,
          'h1':1,'h2':2,'h3':3,'h4':4,'h5':5,'h6':6,'h7':7,'h8':8}


#printing the current board
def show():
    print '    1   2   3   4   5   6   7   8  '
    print'  ---------------------------------'
    print 'A','|',board[57],'|',board[58],'|',board[59],'|',board[60],'|',board[61],'|',board[62],'|',board[63],'|',board[64],'|'
    print'  ---------------------------------'
    print 'B','|',board[49],'|',board[50],'|',board[51],'|',board[52],'|',board[53],'|',board[54],'|',board[55],'|',board[56],'|'
    print'  ---------------------------------'
    print 'C','|',board[41],'|',board[42],'|',board[43],'|',board[44],'|',board[45],'|',board[46],'|',board[47],'|',board[48],'|'
    print'  ---------------------------------'
    print 'D','|',board[33],'|',board[34],'|',board[35],'|',board[36],'|',board[37],'|',board[38],'|',board[39],'|',board[40],'|'
    print'  ---------------------------------'
    print 'E','|',board[25],'|',board[26],'|',board[27],'|',board[28],'|',board[29],'|',board[30],'|',board[31],'|',board[32],'|'
    print'  ---------------------------------'
    print 'F','|',board[17],'|',board[18],'|',board[19],'|',board[20],'|',board[21],'|',board[22],'|',board[23],'|',board[24],'|'
    print'  ---------------------------------'
    print 'G','|',board[9],'|',board[10],'|',board[11],'|',board[12],'|',board[13],'|',board[14],'|',board[15],'|',board[16],'|'
    print'  ---------------------------------'
    print 'H','|',board[1],'|',board[2],'|',board[3],'|',board[4],'|',board[5],'|',board[6],'|',board[7],'|',board[8],'|'
    print'  ---------------------------------'





def numofplayers():
    players = int(raw_input("Enter number of players: "))
    global nop
    if players == 1:
        nop = 1
    elif players == 2:
        nop = 2
    else:
        print "invalid entry"
        numofplayers()


    

def checkwin():
    os =[]
    xs=[]
    for key in board:
        if board[key] =="o" or board[key]=="O":
            os.append(key)
    for key in board:
        if board[key] =="x" or board[key]=="x":
            xs.append(key)
    if len(os)== 0:
        print "Player 1 wins"
        pa = raw_input("Play again?: ")
        if pa == "y":
            play()
        elif pa == "n":
            quit()
        else:
           print "invalid input"

    if len(xs) == 0:
        print "Player 2 Wins"
        pa = raw_input("Play again?: ")
        if pa == y:
            play()
        elif pa == n:
            quit()
        else:
            print"Invalid input"

def undo():
    print'undo'
    print pturn
    test=bstack.pop()
    test=bstack.pop()
    test=bstack.pop()
    
    for k,v in test.iteritems():
        for k2,v2 in board.iteritems():
            if k2 == k:
                board[k2]=test[k]
    show()
    if pturn == 1:
      p1turn()
    else:
      p2turn()

global bstack
bstack = []




def p1turn():
    global end
    global start
    global pturn
    pturn = 0
    
    
    print 'player 1'
    print pturn
    input = raw_input("P1 Enter Move: ")
    if input == "undo":
        pturn = 1
        undo()
    else:
        
        start,end = input.split()
        start = convert[start]
        end = convert[end]

        global ledge
        ledge=[1,9,17,25,33,41,49,57]
        global redge
        redge =[8,16,24,32,40,48,56,64]
        global iledge
        iledge = [2,10,18,26,34,42,50,58]
        global iredge
        iredge = [7,15,23,31,39,47,55,63]

        if (start in ledge or start in redge) and (end in ledge or end in redge):
            print "Invalid move"
            p1turn()
        elif (start in iledge or start in redge) and (end in redge or end in iledge):
            print "1nvalid move"
            p1turn()
        elif (start in iredge or start in ledge) and (end in ledge or end in iredge):
            print"Invalid move"
            p1turn()
        else:
            
            if board[start] == "x" and board[end] == " ":
                if end - start == 7 or end - start == 9:
                  moveup()
                elif end-start==18 and (board[start+9] == "o" or board[start+9] == "O"):
                  takeright(start,end)
                elif end-start==14 and (board[start+7] == "o" or board[start+7] == "O"):
                  takeleft(start,end)
                else:
                  print "invalid move"
                  p1turn()
            elif board[start]=="X" and board[end]==" ":
                if end-start== -7 or end-start == -9:
                    movedown()
                elif end - start == 7 or end - start == 9:
                    moveup()
                elif end-start==18 and (board[start+9] == "o" or board[start+9] == "O"):
                  takeright(start,end)
                elif end-start==14 and (board[start+7] == "o" or board[start+7] == "O"):
                  takeleft(start,end)
                elif end-start==-18 and (board[start-9]=="o" or board[start-9]=="O"):
                  takeleftdown(start,end)
                elif end-start==-14 and (board[start-7]=="o" or board[start-7]=="O"):
                  takerightdown(start,end)
            else:
              print "invalid move"
              p1turn()
        checkwin()
#maybe if it so same methods work for o's    
def moveup():
    if board[start] == "x":
      board[start] = " "
      board[end] = "x"
      if end >= 57 and end <=64:
        board[end] = "X"
      show()
    elif board[start] =="X":
      board[start] = " "
      board[end] = "X"
      show()
    elif board[start]=="O":
        board[start]=" "
        board[end]="O"
        show()
        
def movedown():
    if board[start]=="X":
      board[start]=" "
      board[end]="X"
      show()
    elif board[start]=="o":
        board[start]=" "
        board[end]="o"
        if end >=1 and end <=8:
            board[end]="O"
        show()
    elif board[start]=="O":
        board[start]=" "
        board[end]="O"
        show()

def takeright(start,end):
    s1=start
    e1=end
    if board[s1]=="x":
      board[start] = " "
      board[end] = "x"
      board[start+9]=" "
      if end >= 57 and end <=64:
        board[end] = "X"
      show()
    elif board[s1]=="X":
      board[start] = " "
      board[end] = "X"
      board[start+9]=" "
      show()
    elif board[s1]=="O":
        board[s1]=" "
        board[e1]="O"
        board[s1+9]=" "
        show()
    
    checkjump(e1)


def takeleft(start,end):
    s1=start
    e1=end
    if board[s1]=="x":
      board[s1] = " "
      board[e1] = "x"
      board[s1+7]=" "
      if end >= 57 and end <=64:
        board[end] = "X"
      show()
    elif board[s1]=="X":
      board[s1] = " "
      board[e1] = "X"
      board[s1+7]=" "
      show()
    elif board[s1]=="O":
        board[s1]=" "
        board[e1]="O"
        board[s1+7]=" "
        show()
    checkjump(e1)
      


def takeleftdown(start,end):
    s1 = start
    e1 = end
    if board[s1]=="X":
      board[s1]=" "
      board[e1]="X"
      board[s1-9]=" "
      show()
      checkjump(e1)
    elif board[s1]=="o":
        board[s1]=" "
        board[e1]="o"
        board[s1-9]=" "
        if end >=1 and end <=8:
            board[end]="O"
        show()
        checkjump(e1)
    elif board[s1]=="O":
        board[s1]=" "
        board[e1]="O"
        board[s1-9]=" "
        show()
        checkjump(e1)

def takerightdown(start,end):
    s1=start
    e1=end
    if board[s1]=="X":
      board[s1]=" "
      board[e1]="X"
      board[s1-7]=" "
      show()
      checkjump(e1)
    elif board[s1]=="o":
        board[s1]=" "
        board[e1]="o"
        board[s1-7]=" "
        if end >=1 and end <=8:
            board[end]="O"
        show()
        checkjump(e1)
    elif board[s1]=="O":
        board[s1]=" "
        board[e1]="O"
        board[s1-7]=" "
        show()
        checkjump()
   
    
def checkjump(e1):
    if e1+18 <= 64 and e1-18 >= 1:
      if board[e1]=="x" or board[e1]=="X":
          if (board[e1+9] == "o" or board[e1+9] == "O") and board[e1+18]==" ":
            s1=e1
            e1=e1+18
            takeright(s1,e1)
          elif (board[e1+7] == "o" or board[e1+7] == "O") and board[e1+14]==" ":
            s1=e1
            e1=e1+14
            takeleft(s1,e1)
          elif board[e1]=="X" and (board[e1-7] == "o" or board[e1-7] == "O") and board[e1-14]==" ":
            s1=e1
            e1=e1-14
            takerightdown(s1,e1)
          elif board[e1]=="X" and (board[e1-9] == "o" or board[e1-9] == "O") and board[e1-18]==" ":
            s1=e1
            e1=e1-18
            takeleftdown(s1,e1)
      elif board[e1]=="o" or board[e1]=="O":
          if board[e1]=="O" and (board[e1+9] == "x" or board[e1+9] == "X") and board[e1+18]==" ":
            s1=e1
            e1=e1+18
            takeright(s1,e1)
          elif board[e1]=="O" and (board[e1+7] == "x" or board[e1+7] == "X") and board[e1+14]==" ":
            s1=e1
            e1=e1+14
            takeleft(s1,e1)
          elif (board[e1-7] == "x" or board[e1-7] == "X") and board[e1-14]==" ":
            s1=e1
            e1=e1-14
            takerightdown(s1,e1)
          elif (board[e1-9] == "x" or board[e1-9] == "X") and board[e1-18]==" ":
            s1=e1
            e1=e1-18
            takeleftdown(s1,e1)
          

def p2turn():
    if nop == 1:
        pms = []
        pme = [-7,-9,+7,+9]
        for key in board:
            if board[key] =="o" or board[key]=="O":
                pms.append(key)  
        global end
        global start
        start = random.choice(pms)
        moves = random.choice(pme)
        end = start+moves


    elif nop == 2:
        input = raw_input("P2 Enter Move: ")
        if input == "undo":
            pturn = 2
            print pturn
            undo()
        else:
            start,end = input.split()
            start = convert[start]
            end = convert[end]
        
        
            if (start in ledge or start in redge) and (end in ledge or end in redge):
                p2turn()
            elif (start in iledge or start in redge) and (end in redge or end in iledge):
                print "1nvalid move"
                p2turn()
            elif (start in iredge or start in ledge) and (end in ledge or end in iredge):
                print"Invalid move"
                p2turn()
            else:
                if end >=1 and end<=64:
                    if board[start] == "o" and board[end] == " ":
                        if end - start == -7 or end - start == -9:
                          movedown()
                        elif end-start==-18 and (board[start-9] == "x" or board[start-9] == "X"):
                          takeleftdown(start,end)
                        elif end-start==14 and (board[start+7] == "x" or board[start+7] == "X"):
                          takeleft(start,end)
                        else:
                          p2turn()
                    elif board[start]=="O" and board[end]==" ":
                        if end-start== -7 or end-start == -9:
                            movedown()
                        elif end - start == 7 or end - start == 9:
                            moveup()
                        elif end-start==18 and (board[start+9] == "x" or board[start+9] == "X"):
                          takeright(start,end)
                        elif end-start==14 and (board[start+7] == "x" or board[start+7] == "X"):
                          takeleft(start,end)
                        elif end-start==-18 and (board[start-9]=="x"or board[start-9]=="X"):
                          takeleftdown(start,end)
                        elif end-start==-14 and (board[start-7]=="x" or board[start-7]=="X"):
                          takerightdown(start,end)
                    else:
                        p2turn()
                else:
                    
                    p2turn()
        checkwin()

def printai():
  pstrt = next(key for key, value in convert.items() if value == start)
  prend = next(key for key, value in convert.items() if value == end)
  print "AI moves "+pstrt+" to "+prend
def play():

  makeboard()
  numofplayers()
  show()
  while True:
    bstack.append(board.copy())
    p1turn()
    bstack.append(board.copy())
    p2turn()
    if nop ==1:
      printai()

play()
  
