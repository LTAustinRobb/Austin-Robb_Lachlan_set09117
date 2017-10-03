board = {'a1':' ','a2':'o','a3':' ','a4':'o','a5':' ','a6':'o','a7':' ','a8':'o',
         'b1':'o','b2':' ','b3':'o','b4':' ','b5':'o','b6':' ','b7':'o','b8':' ',
         'c1':' ','c2':'o','c3':' ','c4':'o','c5':' ','c6':'o','c7':' ','c8':'o',
         'd1':' ','d2':' ','d3':' ','d4':' ','d5':' ','d6':' ','d7':' ','d8':' ',
         'e1':' ','e2':' ','e3':' ','e4':' ','e5':' ','e6':' ','e7':' ','e8':' ',
         'f1':'x','f2':' ','f3':'x','f4':' ','f5':'x','f6':' ','f7':'x','f8':' ',
         'g1':' ','g2':'x','g3':' ','g4':'x','g5':' ','g6':'x','g7':' ','g8':'x',
         'h1':'x','h2':' ','h3':'x','h4':' ','h5':'x','h6':' ','h7':'x','h8':' '}

def show():
    print'---------------------------------'
    print '|',board['a1'],'|',board['a2'],'|',board['a3'],'|',board['a4'],'|',board['a5'],'|',board['a6'],'|',board['a7'],'|',board['a8'],'|'
    print'---------------------------------'
    print '|',board['b1'],'|',board['b2'],'|',board['b3'],'|',board['b4'],'|',board['b5'],'|',board['b6'],'|',board['b7'],'|',board['b8'],'|'
    print'---------------------------------'
    print '|',board['c1'],'|',board['c2'],'|',board['c3'],'|',board['c4'],'|',board['c5'],'|',board['c6'],'|',board['c7'],'|',board['c8'],'|'
    print'---------------------------------'
    print '|',board['d1'],'|',board['d2'],'|',board['d3'],'|',board['d4'],'|',board['d5'],'|',board['d6'],'|',board['d7'],'|',board['d8'],'|'
    print'---------------------------------'
    print '|',board['e1'],'|',board['e2'],'|',board['e3'],'|',board['e4'],'|',board['e5'],'|',board['e6'],'|',board['e7'],'|',board['e8'],'|'
    print'---------------------------------'
    print '|',board['f1'],'|',board['f2'],'|',board['f3'],'|',board['f4'],'|',board['f5'],'|',board['f6'],'|',board['f7'],'|',board['f8'],'|'
    print'---------------------------------'
    print '|',board['g1'],'|',board['g2'],'|',board['g3'],'|',board['g4'],'|',board['g5'],'|',board['g6'],'|',board['g7'],'|',board['g8'],'|'
    print'---------------------------------'
    print '|',board['h1'],'|',board['h2'],'|',board['h3'],'|',board['h4'],'|',board['h5'],'|',board['h6'],'|',board['h7'],'|',board['h8'],'|'
    print'---------------------------------'

show()

def p1turn():
    input = raw_input("Enter Move: ")
    start,end = input.split()
    if board[start] == "x" and board[end] == " ":
        board[start] = " "
        board[end] = "x"
    else:
        print "invalid move"
    
    
p1turn()
show()
