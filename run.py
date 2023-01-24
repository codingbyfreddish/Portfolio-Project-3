"""
Welcome to my adventure game.
Hope you will enjoy it!
To check out more visit www.github.com/codingbyfreddish
"""

# Introduction. User name and confirmation to start game
def start_game():
    print("Hey there! First things first, what is your name?")
    name = input("Name: ")
    print(f"{name}?? Well, i've heard worse i guess... who cares about names anyway, huh?\n")
    print(f"So {name} are you ready for an adventure? 'Yes' or 'No'")
    answer = input("Answer: ")
    if answer.lower().strip() == "yes":
        print(f"Buckle up {name}, you my friend are in for an epic adventure!\n")
        scene_one()
    else:
        print("Had a feeling you dident have what it takes. Welcome back when you do.")
        exit()


# Start of the adventure 
def scene_one():
    print("A little girl, named Petra, is wandering through the forest when she comes across a fork in the path.") 
    print("She must decide whether to take the path to the left or the path to the right.")
    answer = input("Will she go 'Left' or 'Right': ")
    if answer.lower().strip() == "left":
        print("Petra takes the left path. After walking for a while, she comes across a dark cave.")
        print("The cave looks scary and Petra gutfeeling says 'don't go in there.")
        print("But at the same time what if the cave contains a big, old tresure chest filled with gold and what not?")
        print("Petra stands infront of the cave not sure what to do, can you help her choose?")
        cave_or_not = input("'Go inside' or 'Continue': ")
        if cave_or_not.lower().strip() == "go inside":
            print("Petra goes inside the dark, scary cave... and is never seen again. ***Game Over***\n")
            game_over = input("Dont underestimate your gutfeeling. Want to play again? 'Yes or No': ")
            if game_over.lower().strip() == "yes":
                start_game()
            else:
                exit()
        else:
             print("Petra choose to trust her gut and wanders away from the cave.\n")
             scene_two()   

    else:
        print("Petra takes the right path. After walking for a while, she comes across a babbling brook.")
        print("She thinks for herself 'I am mighty thirsty, maybe i should drink alittle bit of water before continuing on my journey?'")
        drink_or_dont = input("'Drink' or 'Dont': ")
        if drink_or_dont.lower().strip() == "drink":
            print("Petra takes a couple sips of water and says to herself 'That sure was some quality H2O!'")
            print("Hydrated and feeling like a million bucks, she continues on her path.\n")
            scene_two()
        else:
            print("After a little while, Petra starts feeling weak and dizzy. She realize her adventure is coming to an end.")
            print("She hurrys home, and drinks close to a gallon of water. If only she had gotten some water in time... *** Game Over***\n")
            game_over = input("Stay hydrated friends.  Want to play again? 'Yes or No': ")
            if game_over.lower().strip() == "yes":
                start_game()
            else:
                exit()


# Start of scene two
def scene_two():
    print("After walking for a while, humming on Spice Girls 'Wannabe', she comes across a clearing with a large tree in the middle.")
    print("'Oh what a nice tree, i bet the view if great from up there! On the other hand, i am awfully tired, maybe its better to take a nap under it?' she says to herself.")
    print("What do you think Petra should do, 'Climb' or 'Nap'?")
    nap_or_die = input("Answer: ")
    if nap_or_die == "climb":
        print("Petra rushes to the tree and jumps up on the first branch she can see. With the speed of a skilled little monkey she flyes up branch after branch.")
        print("Well up at the highest point, she is mesmerized by the beautiful view. But when its time to climb down...")
        print("She freezes, only to remember how scared of heights she is. Who knows, maybe she's still up there? ***Game Over***\n")
        game_over = input("Never turn down a nap. Never. Want to play again? 'Yes or No': ")
        if game_over.lower().strip() == "yes":
            start_game()
        else:
            exit()
    else:
        print("Petra lays down under the tree. Within minutes, she falls asleep.")
        print("After twenty minutes or so, she wakes up... yawns once or twice, streaches abit and says to herself 'Thats what i call a perfect nap!'")
        print("She gets up, bruches of some grass and dirt and continues on her journey, filled with the magic powers a nap gives you.\n")
        scene_three()

# Start of scene three
def scene_three():
    print("After walking for a while, Petra comes across a berry bush. At this point of our adventure, her tummy was growling like a grizzly bear because she hadent eaten for hours.")
    print("She looked at the berries. Some of them she recognized, she remembered her kindergarden teacher showing them as berries you could eat.")
    print("But some of them she had never seen. 'What should i do now?' she asked herself")
    berries_or_be_burried = input("What do you think? Should she 'Eat all berries', 'None of them' or 'Only the ones she recognize'?: ")
    if berries_or_be_burried.lower().strip() == "only the ones she know":
        print("'Nomnomnom those berries were sooo yummy!' She shouted quietly for herself. With some newfound energy she felt ready to embark on her adventure.\n")
        scene_four()
    elif berries_or_be_burried.lower().strip() == "eat all berries":
        print("After eating every berries she could see, her tummy started aiking so much she had to run straight home. Guess she should have only eaten the ones she recognized. *** Game Over***")
        game_over = input("The berries got the best of you, dident they? Want to play again? 'Yes or No': ")
        if game_over.lower().strip() == "yes":
            start_game()
        else:
            exit()
    else: 
        print("Who does an adventure on a empty stomach? C'mon now, be serious for once. ***Game Over***\n")
        game_over = input("Want to play again? 'Yes or No': ")
        if game_over.lower().strip() == "yes":
            start_game()
        else:
            exit()

# Start of scene four
def scene_four():
    print(" ")


# Run all program functions
def main():
    start_game()
    scene_one()
    scene_two()
    scene_three()
    scene_four()


main()
