import random
while True:
    user_action = input("Enter a choice(rock,paper,scissor): ")

#making the computer choose randomly
    possible_actions = ["rock","paper","scissor"]
    comp_action = random.choice(possible_actions)

#printing the choises of the user and the comp
    print(f"\n You chose {user_action},Computer chose {comp_action}.\n")

    if user_action==comp_action:
        print(f"Both players selected{user_action}.You tie!")
    elif user_action== "rock":
        if comp_action=="paper":
            print("Paper covers rock! You lose")
        else:
            print("rock smashes scissor! You Win!")
    elif user_action== "paper":
        if comp_action=="rock":
            print("paper covers rock!You Win")
        else:
            print("scissor cuts paper! You lose")
    elif user_action== "scissor":
        if comp_action=="paper":
            print("scissor cuts paper! You lose")
        else:
            print("rock smashes scissor! You lose")

    play_again=input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break

