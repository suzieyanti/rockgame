from random import randint

#create a list of play options
print ("Permainan Batu , Kertas , Gunting\n")
t = ["Batu", "Kertas", "Gunting"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Batu , Kertas , Gunting?")
    if player == computer:
        print("Kunci!")
    elif player == "Batu":
        if computer == "Kertas":
            print("Anda Kalah!", computer, "Bantu", player)
        else:
            print("Anda Menang!", player, "Musnahkan", computer)
    elif player == "Kertas":
        if computer == "Gunting":
            print("Anda Kalah!", computer, "Potong", player)
        else:
            print("Anda Menang!", player, "Bantu", computer)
    elif player == "Gunting":
        if computer == "Batu":
            print("Anda Kalah!", computer, "Musnahkan", player)
        else:
            print("Anda Menang!", player, "potong", computer)
    else:
        print("TIDAK SAH.SEMAK EJAAN!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]