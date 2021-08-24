import random
import pandas as pd
from csv import writer
import csv
def gamewin(comp, you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w' or you=='W':
            return False
        elif you=='g' or you=='G':
            return True
    elif comp=='w':
        if you=='s' or you=='S':
            return True
        elif you=='g' or you=='G':
            return False
    elif comp=='g':
        if you=='s' or you=='S':
            return False
        elif you=='w' or you=='W':
            return True

# driver code
player_name = input('Enter name: ')
comp_score = 0
player_score = 0
player = ''
count = 0
while player!='e':
    randNo = random.randint(1, 3)
    comp = ''
    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'w'
    elif randNo == 3:
        comp = 'g'
    player = input("Your Turn: Snake(s), Water(w), or Gun(g)? e for EXIT\n")
    if(player=='e' or player=='E'):
        break
    count = count + 1   #counting number of times played
    print(f"\nComputer chose {comp}\n")
    print(f"You chose {player}\n")
    a = gamewin(comp, player)
    if a==None:
        print("TIE\n")
    elif a:
        print("YOU WIN\n")
        player_score+=1
    else:
        print("YOU LOSE\n")
        comp_score+=1
print("\nComputer\tYou")
print(comp_score, "\t\t", player_score)
if comp_score < player_score:
    print("\nCongratulations! You win the game.\n")
elif comp_score > player_score:
    print("\nSorry, you lose the game! Better luck next time.\n")
else:
    print("\nGame Tied\n")

win_rate = (player_score/count)*100 #calculating win percentage
li = [player_name, win_rate, count] #new data for storing in the HighScores.csv file
flag = 0
#checking whether the current player's name is already present in HighScores.csv file or not
with open("HighScores.csv", 'r') as f:
    read = csv.reader(f, delimiter=",")
    for i in read:
        if player_name in i:
            flag = 1
    f.close()
#Condition for when current player's name is not present
if flag==0:
    with open("HighScores.csv", 'a') as f:
        w = writer(f)
        w.writerow(li)      #appending the current player's data to the file
        f.close()
    df = pd.read_csv("HighScores.csv")  #converting csv file to dataframe for sorting
    df.columns = ["Player Name", "Win Rate", "Times Played"]    #setting the column names
    df.set_index("Player Name", inplace=True)       #Setting index as name of player instead of 0, 1, 2 etc.
    df.sort_values(by=["Win Rate"], inplace=True, ascending=False)      #sorting the file by Win Rate in Descending Order
    print(df)
    df.to_csv("HighScores.csv")     #Converting the dataframe to csv file
else:
    df = pd.read_csv("HighScores.csv")
    df.columns = ["Player Name", "Win Rate", "Times Played"]
    df.set_index("Player Name", inplace=True)
    #checking whether the current player's score is higher than the one present in the file
    if df.loc[player_name, "Win Rate"] < win_rate:
        df.loc[player_name, "Win Rate"] = win_rate
        df.loc[player_name, "Times Played"] = count
    df.sort_values(by=["Win Rate"], inplace=True, ascending=False)
    print(df)
    df.to_csv("HighScores.csv")