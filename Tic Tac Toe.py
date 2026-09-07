import random
def check_winners(board,YOU,COMP):
    if (#ROW
        board[0] == board[1] == board[2] == YOU or
        board[3] == board[4] == board[5] == YOU or
        board[6] == board[7] == board[8] == YOU or 
        #COLUMNS
        board[0] == board[3] == board[6] == YOU or
        board[1] == board[4] == board[7] == YOU or
        board[2] == board[5] == board[8] == YOU or 

        #DIAGONALS
        board[0] == board[4] == board[8] == YOU or
        board[2] == board[4] == board[6] == YOU ) :

        print("YOU WON !!")
        exit(0)

    elif (#ROW
        board[0] == board[1] == board[2] == COMP or
        board[3] == board[4] == board[5] == COMP or
        board[6] == board[7] == board[8] == COMP or 
            #COLUMNS
        board[0] == board[3] == board[6] == COMP or
        board[1] == board[4] == board[7] == COMP or
        board[2] == board[5] == board[8] == COMP or 
    
            #DIAGONALS
        board[0] == board[4] == board[8] == COMP or
        board[2] == board[4] == board[6] == COMP ):

            print("YOU LOSS !!")
            exit(0)

def start():
    print("Here is the board position for your reference")
    print(0, "|", 1, "|", 2)
    print("--+---+--")
    print(3, "|", 4, "|", 5)
    print("--+---+--")
    print(6, "|", 7, "|", 8)


    board = [" "," "," ",
            " "," "," ",
            " "," "," ",]
    
    while True:

        YOU = input("PICK YOUR TURN 'X' For FRIST & 'O' For SECOND:").upper()

        if YOU == "X":
            list1 = [0,1,2,3,4,5,6,7,8]      
            list2 = []
            while True:
                
                #Taking position input
                index = int(input("Chosse Your Position to mark :"))

                #checking Input here
                if index < 0 or index > 8 or index in list2:
                    print("Enter correct position !!")
                    continue

                #For taking track of position which are empty & fill
                list1.remove(index)
                list2.append(index)

                #Now Adding mark on board
                board[index] = YOU

                COMP = "O"
                comp_index = random.choice(list1) 

                #Computer Mark tracking
                list1.remove(comp_index)
                list2.append(comp_index)
                board[comp_index] = COMP

                print(board[0], "|", board[1], "|", board[2])
                print("--+---+--")
                print(board[3], "|", board[4], "|", board[5])
                print("--+---+--")
                print(board[6], "|", board[7], "|", board[8])

                check_winners(board,YOU,COMP)
    
                
        elif YOU == "O":

            list1 = [0,1,2,3,4,5,6,7,8]      
            list2 = []

            while " " in board :

                COMP = "X"
                comp_index = random.choice(list1)

                #Computer mark tracking
                list1.remove(comp_index)
                list2.append(comp_index)
                board[comp_index] = COMP

                #Board position reference 

                print(board[0], "|", board[1], "|", board[2])
                print("--+---+--")
                print(board[3], "|", board[4], "|", board[5])
                print("--+---+--")
                print(board[6], "|", board[7], "|", board[8])
                

                index = int(input("Chosse Your Position to mark :"))
                if index > 8 or index < 0 or index in list2 :
                    print("Enter correct position !!")

                list1.remove(index)
                list2.append(index)

                board[index] = YOU

                check_winners(board,YOU,COMP)

print("WELCOME TIC-TAC-TOE GAME !!")  

play = input("Want to start ? YES/NO :").upper()

if play == "YES" :
    start()

elif play == "NO":
    print("BEY BEY !!")

else:
    print("GIVE CORRECT INPUT")



        
                