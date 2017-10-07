
#dict of starting board, with number and wether or not there is a piece
board = {57:' ',58:'o',59:' ',60:'o',61:' ',62:'o',63:' ',64:'o',
         49:'o',50:' ',51:'o',52:' ',53:'o',54:' ',55:'o',56:' ',
         41:' ',42:'o',43:' ',44:'o',45:' ',46:'o',47:' ',48:'o',
         33:' ',34:' ',35:' ',36:' ',37:' ',38:' ',39:' ',40:' ',
         25:' ',26:' ',27:' ',28:' ',29:' ',30:' ',31:' ',32:' ',
         17:'x',18:' ',19:'x',20:' ',21:'x',22:' ',23:'x',24:' ',
         9:' ',10:'x',11:' ',12:'x',13:' ',14:'x',15:' ',16:'x',
         1:'x',2:' ',3:'x',4:' ',5:'x',6:' ',7:'x',8:' '}

convert ={'a1':57,'a2':58,'a3':59,'a4':60,'a5':61,'a6':62,'a7':63,'a8':64,
          'b1':49,'b2':50,'b3':51,'b4':52,'b5':53,'b6':54,'b7':55,'b8':58,
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

show()



def p1turn():
    global end
    input = raw_input("Enter Move: ")
    start,end = input.split()
    start = convert[start]
    end = convert[end]
    
    
    
    if board[start] == "x" and board[end] == " ":
        if end - start == 7 or end - start == 9:
          board[start] = " "
          board[end] = "x"
          show()
          
        elif end-start==18 and board[start+9] == "o":
          board[start] = " "
          board[end] = "x"
          board[start+9]=" "
          show()
          p1jumpagain()
          
        elif end-start==14 and board[start+7] == "o":
          board[start] = " "
          board[end] = "x"
          board[start+7]=" "
          show()
          p1jumpagain()
        else:
          print "invalid"
    else:
        print "invalid move"
    

def p1jumpagain():
    if board[end+7]=="o" and board[end+14]==" ":
      board[end]=" "
      board[end+7]=" "
      board[end+14]="x"
      show()
      #end = end+14
      #p1jumpagain()


p1turn()
