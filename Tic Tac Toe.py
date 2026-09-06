import random
def start():
    

    board = [" "," "," ",
            " "," "," ",
            " "," "," ",]
    
    while True:

        YOU = input("PICK YOUR TURN 'X' For FRIST & 'O' For SECOND:").upper()

        if YOU == "X":
            list1 = [0,1,2,3,4,5,6,7,8]      
            list2 = []
            while " " in board :
                #Taking position input
                index = int(input("Chosse Your Position to mark :"))
                #checking Input here
                if index < 0 or index > 8 or index in list2:
                    print("Enter correct position !!")
                    continue
                #For taking track of index which are empty & fill
                list1.remove(index)
                list2.append(index)
                #Now Adding mark on board
                board[index] = YOU

                COMP = "O"
                comp_index = random.choice(list1)
                #COMPuter index tracking
                list1.remove(comp_index)
                list2.append(comp_index)
                board[comp_index] = COMP

                print(board[0], "|", board[1], "|", board[2])
                print("--+---+--")
                print(board[3], "|", board[4], "|", board[5])
                print("--+---+--")
                print(board[6], "|", board[7], "|", board[8])


                if " " not in board:
                    break
        
        elif YOU == "O":

            list1 = [0,1,2,3,4,5,6,7,8]      
            list2 = []

            while " " in board :

                COMP = "X"
                comp_index = random.choice(list1)
                #COMPuter index tracking
                list1.remove(comp_index)
                list2.append(comp_index)
                board[comp_index] = COMP

                print(board[0], "|", board[1], "|", board[2])
                print("--+---+--")
                print(board[3], "|", board[4], "|", board[5])
                print("--+---+--")
                print(board[6], "|", board[7], "|", board[8])
                

                index = int(input("Chosse Your Position to mark :"))
                if index >= 8 and index in list2 :
                    print("Enter correct position !!")

                list1.remove(index)
                list2.append(index)

                board[index] = YOU

start()    
           
        
                