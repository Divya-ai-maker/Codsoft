import random
print(" <--- WELCOME TO ROCK, PAPER and SCISSORS GAME !!--- >");
print(" <-- Let's go !!-- >");
user=input("Enter rock,paper or scissors:");
choices=["rock","paper","scissors"];
computer=random.choice(choices)
if(user == computer):
    print("Opss!Its a draw.");
elif((user == "rock" and computer == "scissor")or(user == "scissors"and computer
== "paper")or(user == "paper"and computer == "rock")):
    print("Congratulations !! You win");
else:
    print("Computer wins!");
